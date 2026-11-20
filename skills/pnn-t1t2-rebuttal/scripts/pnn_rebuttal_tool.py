#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-rebuttal`: T1/T2 winning rebuttal craft (12 Nature/NP/NN/NCS PR files) + ALL-TIER referee intelligence bridge."""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

AI_HYPE_WORDS = [
    "transformative", "groundbreaking", "pivotal", "pioneering", "unprecedented",
    "seamless", "seamlessly", "holistic", "compelling", "meticulous", "meticulously",
    "delve", "underscore", "underscores", "showcase", "showcasing", "elucidate",
    "orchestrate", "paradigm shift", "landscape", "cornerstone", "testament",
    "unlock", "unlocking", "revolutionize", "usher in", "not only", "but also",
    "rapidly evolving", "garnered increasing attention", "lays the groundwork",
    "opens new avenues", "broad application prospects", "poised to transform",
]

AI_BAD_OPENERS = [
    "Thus,", "Notably,", "Importantly,", "Interestingly,", "Remarkably,",
    "Strikingly,", "Specifically,", "More specifically,", "In particular,",
    "Subsequently,", "Obviously,", "Clearly,", "Collectively,", "Overall,",
    "Looking ahead,", "Looking forward,", "Moving forward,", "As such,", "Yet,",
]

def check_voice_hygiene(text: str) -> list[str]:
    issues = []
    if "\u2014" in text or "--" in text:
        cnt = text.count("\u2014")
        issues.append(f"Em-dash detected ({cnt}x): remove em-dashes for crisp T1/T2 clarity.")
    low = text.lower()
    hits = [w for w in AI_HYPE_WORDS if re.search(r"\b" + re.escape(w) + r"\b", low)]
    if hits:
        issues.append("AI/promotional vocabulary detected: " + ", ".join(hits[:8]))
    bad_op = [op for op in AI_BAD_OPENERS if re.search(r"(?:^|[\.\!\?]\s+)" + re.escape(op), text)]
    if bad_op:
        issues.append("Non-author / AI sentence openers detected: " + ", ".join(bad_op[:6]))
    return issues

def safe_read_text(arg: str) -> str:
    if len(arg) > 240 or "\n" in arg:
        return arg
    p = Path(arg)
    try:
        return p.read_text(encoding="utf-8", errors="replace") if p.exists() else arg
    except OSError:
        return arg


def cmd_query_t1t2(args):
    rows = [json.loads(l) for l in (REF_DIR / "t1t2_rebuttal_distill.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    comments = [json.loads(l) for l in (REF_DIR / "t1t2_pr_comments_132.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    if args.concern:
        c_hits = [c for c in comments if args.concern.upper() in str(c.get("primary_concern", "") + " " + str(c.get("concerns", ""))).upper()]
        print(f"=== T1/T2 Primary Peer Review Comments for Concern {args.concern.upper()} ({len(c_hits)}/132 T1+T2 comments) ===")
        for c in c_hits[:args.top]:
            print(f"  - [{c['tier']} {c['journal']} | R{c.get('round')} {c.get('referee')} | {c.get('severity')} | Tactics:{c.get('tactics')}]")
            print(f"    Attack: {str(c.get('referee_quote',''))[:220]}")
    else:
        print(f"=== T1/T2 Full Transparent Peer Review Case Studies ({len(rows)} papers) ===")
        for r in rows[:args.top]:
            d = r.get("data") or {}
            print("=" * 84)
            print(f"[{r['tier']} | {r.get('country_primary','?')} w={r.get('prose_weight',1.0):.1f} | {r['journal']}] {r['stem']}")
            print(f"Rounds: {d.get('rounds_total')} | Referees: {d.get('referee_count')} | R1 Skeptic: {d.get('r1_skeptic_summary')}")
            for atk in (d.get("top_attacks") or [])[:3]:
                print(f"  * [{atk.get('code')} -> {atk.get('tactic')}] Attack: {atk.get('attack')} | Winning Fix: {atk.get('winning_response')}")
            if d.get("gold_response_phrase"):
                print(f"  Gold phrase: \"{d['gold_response_phrase']}\"")

def cmd_referee_intel(args):
    """Information-layer bridge: ALL-TIER (T1-T4) 2,241-comment attack statistics + 146 named PNN referees from sibling pnn-paper-playbook."""
    pnn_ref = (SKILL_DIR.parent.parent / "references" if (SKILL_DIR.parent.parent / "references").exists() else SKILL_DIR.parent / "pnn-paper-playbook" / "references")
    nr_p = pnn_ref / "named_reviewers.md"
    pr_p = pnn_ref / "pr_comments_v2.jsonl"
    if args.topic and nr_p.exists():
        print(f"=== ALL-TIER Named PNN Referees matching '{args.topic}' (from 146-referee bank) ===")
        hits = []
        for ln in nr_p.read_text(encoding="utf-8", errors="replace").splitlines():
            if args.topic.lower() in ln.lower() and ("|" in ln or "**" in ln):
                hits.append(ln.strip())
        for h in hits[:args.top]:
            print(" ", h[:180])
    if not pr_p.exists() and not nr_p.exists():
        rb_p = pnn_ref / "reviewer_playbook.md"
        print("=== ALL-TIER Reviewer Concern Playbook Bridge (Public Metadata Mode) ===")
        print("Raw peer-review files and named referee tables are not distributed publicly (see LICENSE-DATA.md).")
        if rb_p.exists():
            q = (args.concern or args.topic or "").lower()
            hits = [ln.strip() for ln in rb_p.read_text(encoding="utf-8", errors="replace").splitlines() if q and q in ln.lower()]
            for h in hits[:max(args.top, 4)]:
                print(" ", h[:180])
        return
    if args.concern and pr_p.exists():
        prs = [json.loads(l) for l in pr_p.read_text(encoding="utf-8").splitlines() if l.strip()]
        hits = [d for d in prs if args.concern.upper() == str(d.get("primary_concern", "")).upper()]
        tacts = Counter(c for d in hits for c in re.findall(r"R\d+", str(d.get("tactics", ""))))
        print(f"=== ALL-TIER Nature-Portfolio Statistics for {args.concern.upper()} ({len(hits)}/{len(prs)} primary comments) ===")
        print("  Top tactics used:", tacts.most_common(6))

def cmd_lint(args):
    txt = safe_read_text(args.file)
    print("=== PNN T1/T2 Rebuttal Craft & Editorial Clarity Audit ===")
    flags = []
    if re.search(r"\binsightful\b", txt, re.I):
        flags.append("Avoid cliché 'insightful comment/question' (flagged in author house-style guidelines).")
    if re.search(r"\bwe\s+will\s+(?:add|include|revise|perform|update)\b", txt, re.I):
        flags.append("Future-tense promise ('we will add/revise') detected: state completed revisions in present perfect ('we have added/revised') with exact Page/Line/Note Sx.")
    if not re.search(r"\b(?:Page\s+\d+|Line\s+\d+|Note\s+S\d+|Supplementary\s+(?:Note|Fig|Table)|Extended\s+Data|Fig\.\s*\d+)\b", txt, re.I):
        flags.append("Missing exact revision location pointers (Page, Line, Fig. X, Note SX, Table SX).")
    if not re.search(r"\b(?:experiment|measurement|simulation|table|derivation|limitation|revised|clarified)\b", txt, re.I):
        flags.append("Looks like pure verbal arguing (R8 has lowest resolution rate 68.2%); anchor response in new data (R1/R2), table (R3), SI derivation (R6), or honest scope concession (R4/R5).")
    flags.extend(check_voice_hygiene(txt))
    if not flags:
        print("PASS: Rebuttal adheres to T1/T2 evidence-first conversion tactics and author house-style guidelines.")
    else:
        for i, fl in enumerate(flags, 1):
            print(f"  [{i}] {fl}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Rebuttal Craft CLI (+ All-Tier Referee Intelligence Bridge)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query-t1t2", help="Query T1/T2 Transparent Peer Review winning defenses")
    pq.add_argument("--concern", default=""); pq.add_argument("--top", type=int, default=6)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pi = sub.add_parser("referee-intel", help="Query ALL-TIER 2,241-comment stats & 146 named PNN referees")
    pi.add_argument("--topic", default=""); pi.add_argument("--concern", default=""); pi.add_argument("--top", type=int, default=8)
    pl = sub.add_parser("lint", help="Audit a point-by-point rebuttal draft")
    pl.add_argument("file")
    args = ap.parse_args()
    if args.cmd == "query-t1t2": cmd_query_t1t2(args)
    elif args.cmd == "referee-intel": cmd_referee_intel(args)
    else: cmd_lint(args)

if __name__ == "__main__":
    main()
