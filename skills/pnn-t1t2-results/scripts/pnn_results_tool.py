#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-results`: query T1/T2 Results subheading & proof arcs and lint Results drafts."""
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
    return [json.loads(l) for l in (REF_DIR / "t1t2_results_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.claim_class and r["claim_class"].upper() != args.claim_class.upper(): continue
        out.append(r)
    print(f"Matched {len(out)} T1/T2 Research Results architectures (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print(f"  - [{r['tier']} {r['journal']} {r['year']} | Class {r['claim_class']} | {r['platform']}] {r['title']}")
        print(f"    Subheadings: {' | '.join(r.get('true_results_headings') or [])}")
        print(f"    Opening: {r.get('results_opening_style')} | Eq style: {r.get('eq_integration')} | Fig refs: {r.get('fig_refs_total')}")

def cmd_lint(args):
    txt = safe_read_text(args.file)
    wc = len(txt.split())
    fig_refs = len(re.findall(r"\bFig(?:ure)?\.?\s*\d+[a-nA-N]?", txt))
    has_baseline = bool(re.search(r"\b(?:simulat|theor|digital|baseline|ideal|compared\s+with|agrees\s+well)\b", txt, re.I))
    has_stats = bool(re.search(r"(?:±|\+/-|\bs\.d\.|\bn\s*=|RMS|ENOB)", txt))
    print(f"=== PNN T1/T2 Results Narrative Audit ===")
    print(f"Words: {wc} | Figure panel refs: {fig_refs} | Paired sim/digital baseline: {has_baseline} | Stats/uncertainty: {has_stats}")
    flags = []
    if fig_refs < 3:
        flags.append("Very low panel-anchoring density; weave 'As shown in Fig. Xa,' / '(Fig. Xb)' directly into every claim paragraph.")
    if not has_baseline:
        flags.append("No simulated/theoretical or digital baseline paired beside chip numbers.")
    if not has_stats:
        flags.append("No uncertainty/sample-size tokens (+-s.d., n=, RMS, ENOB) detected in Results.")
    if re.search(r"\b(?:we\s+first\s+tried|we\s+then\s+attempted|failed\s+attempt)\b", txt, re.I):
        flags.append("Chronological lab-notebook narration detected; organize Results by physical claim -> mechanism -> proof.")
    flags.extend(check_voice_hygiene(txt))
    if not flags:
        print("PASS: Results section matches T1/T2 claim-first narrative and statistical pairing.")
    else:
        for i, fl in enumerate(flags, 1):
            print(f"  [{i}] {fl}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Results Craft CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query T1/T2 Results subheading progressions")
    pq.add_argument("--tier", default=""); pq.add_argument("--platform", default="")
    pq.add_argument("--claim-class", default=""); pq.add_argument("--top", type=int, default=8)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pl = sub.add_parser("lint", help="Lint a Results draft")
    pl.add_argument("file")
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    else: cmd_lint(args)

if __name__ == "__main__":
    main()
