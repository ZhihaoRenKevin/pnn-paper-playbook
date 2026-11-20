#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-figure-caption`: query 525 verbatim T1/T2 captions and lint drafts."""
from __future__ import annotations
import argparse, json, re
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


def load_corpus():
    return [json.loads(l) for l in (REF_DIR / "t1t2_captions_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.fig and int(r["fig_num"]) != args.fig: continue
        if args.journal and args.journal.lower() not in r["journal"].lower(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.keyword and args.keyword.lower() not in r["caption_verbatim"].lower(): continue
        out.append(r)
    print(f"Matched {len(out)} verbatim T1/T2 captions (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print("=" * 84)
        print(f"[{r['tier']} | {r.get('country_primary','?')} w={r.get('prose_weight',1.0):.1f} | {r['journal']} {r['year']} | Fig. {r['fig_num']} | {r['word_count']}w | panels={len(r['subpanels'])}] {r['title']}")
        print(f"Lead-in ({r['lead_in_words']}w): {r['lead_in_title']}")
        print("Verbatim:", r["caption_verbatim"])

def cmd_lint(args):
    txt = safe_read_text(args.file)
    txt = re.sub(r"\s+", " ", txt).strip()
    wc = len(txt.split())
    j = args.journal.lower()
    is_sci = "science" in j
    print(f"=== PNN T1/T2 Figure Caption Audit ({args.journal}) ===")
    flags = []
    if is_sci:
        if not re.match(r"^Fig\.\s*\d+\.", txt):
            flags.append("Science house style requires 'Fig. N.' (period separator, not pipe '|').")
        panels = sorted(set(re.findall(r"\(([A-N])\)", txt)))
        if not panels and wc > 80:
            flags.append("Science multi-panel captions use parenthesized uppercase '(A)', '(B)', '(C)'.")
    else:
        if not re.match(r"^Fig\.\s*\d+\s*\|", txt):
            flags.append("Nature family house style requires 'Fig. N |' (vertical bar separator).")
        panels = sorted(set(re.findall(r"(?:^|\.\s+|;\s+)([a-n]),\s+", txt)))
        if not panels and wc > 80:
            flags.append("Nature family multi-panel captions use bare bold lowercase + comma ('a, ... b, ...').")
    lead_m = re.match(r"^(?:Fig\.|Figure)\s*\d+\s*[\|\.:]\s*([^\.]+\.)", txt)
    lead = lead_m.group(1).strip() if lead_m else txt[:80]
    lw = len(lead.split())
    print(f"Words: {wc} (T1/T2 median 156-164w) | Lead-in: {lw}w (target 4-9w noun phrase) | Detected panels: {len(panels)} ({','.join(panels)})")
    if lw < 3 or lw > 12:
        flags.append(f"Lead-in title length {lw}w outside T1/T2 noun-phrase window (4-10 words).")
    if re.search(r"\b(?:demonstrates?|achieves?|outperforms?|proves?|reveals?)\b", lead, re.I):
        flags.append("Lead-in title contains a finite claim verb; 100% of T1/T2 PNN captions use concise noun-phrase titles.")
    if panels:
        wpp = wc / len(panels)
        print(f"Words per panel: {wpp:.1f}w (T1/T2 median ~43.5w/panel)")
        if wpp > 75:
            flags.append(f"Caption density {wpp:.1f}w/panel is bloated; trim verbose prose to ~35-55w/panel.")
    if re.search(r"\b(?:SEM|micrograph|microscope|optical image)\b", txt, re.I) and not re.search(r"\bscale\s+bar\b", txt, re.I):
        flags.append("Micrograph/SEM mentioned without explicit scale bar length in caption.")
    if re.search(r"\b(?:mean|average|accuracy|error)\b", txt, re.I) and not re.search(r"\b(?:s\.d\.|s\.e\.m\.|error\s+bar|shaded|n\s*=)\b", txt, re.I):
        flags.append("Summary metric mentioned without defining error bars/shaded bands or sample size n.")
    flags.extend(check_voice_hygiene(txt))
    if not flags:
        print("PASS: Caption adheres to T1/T2 house syntax and quantitative completeness.")
    else:
        for i, fl in enumerate(flags, 1):
            print(f"  [{i}] {fl}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Figure Caption CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query verbatim T1/T2 captions")
    pq.add_argument("--tier", default=""); pq.add_argument("--fig", type=int, default=0)
    pq.add_argument("--journal", default=""); pq.add_argument("--platform", default="")
    pq.add_argument("--keyword", default=""); pq.add_argument("--top", type=int, default=5)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pl = sub.add_parser("lint", help="Lint a figure caption draft")
    pl.add_argument("file"); pl.add_argument("--journal", default="Nature Photonics")
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    else: cmd_lint(args)

if __name__ == "__main__":
    main()
