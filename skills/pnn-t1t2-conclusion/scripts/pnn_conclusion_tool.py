#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-conclusion`: query T1/T2 Discussion/Conclusions, journal headings, and lint drafts."""
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
    return [json.loads(l) for l in (REF_DIR / "t1t2_conclusion_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.journal and args.journal.lower() not in r["journal"].lower(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.limitation and not any(args.limitation.lower() in x.lower() for x in (r.get("conc_lims") or [])): continue
        out.append(r)
    print(f"Matched {len(out)} T1/T2 Conclusions/Discussions (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print("=" * 84)
        print(f"[{r['tier']} | {r.get('country_primary','?')} w={r.get('prose_weight',1.0):.1f} | {r['journal']} {r['year']} | Heading: {r['closing_heading']} | {r['closing_words']}w] {r['title']}")
        print(f"Moves: {' -> '.join(r.get('conc_moves') or [])} | Lab-vs-Physics split: {r.get('conc_lab_phys')}")
        print(f"Admitted limitations: {', '.join(r.get('conc_lims') or [])}")
        print(f"Future projection: {r.get('conc_proj','')}")
        if r.get("closing_verbatim"):
            print("Excerpt:", r["closing_verbatim"][:550], "..." if len(r["closing_verbatim"]) > 550 else "")

def cmd_heading(args):
    stats = json.loads((REF_DIR / "t1t2_conclusion_stats.json").read_text(encoding="utf-8"))
    by_j = stats["heading_by_journal"]
    print("=== Empirical T1/T2 Closing Section Heading Convention by Journal ===")
    for j, hc in sorted(by_j.items()):
        if args.journal and args.journal.lower() not in j.lower(): continue
        tot = sum(hc.values())
        top_str = ", ".join(f"{k}: {v}/{tot} ({100*v/tot:.0f}%)" for k, v in sorted(hc.items(), key=lambda x: -x[1]))
        print(f"  {j:30s} -> {top_str}")

def cmd_lint(args):
    txt = safe_read_text(args.file)
    paras = [p.strip() for p in re.split(r"\n\s*\n", txt.strip()) if len(p.strip().split()) >= 15]
    wc = len(txt.split())
    print(f"=== PNN T1/T2 Conclusion/Discussion Audit ({args.journal}) ===")
    print(f"Words: {wc} (T1/T2 target 250-550w) | Paragraphs: {len(paras)} (target 2-4)")
    flags = []
    if wc < 180 or wc > 750:
        flags.append(f"Word count {wc} outside T1/T2 closing window (250-550 words).")
    if not re.search(r"\b(?:limitation|limited\s+by|bottleneck|challenge|overhead|crosstalk|insertion\s+loss|drift|currently)\b", txt, re.I):
        flags.append("No explicit physical/engineering limitation disclosed (disarming referees requires naming the first scaling bottleneck).")
    if not re.search(r"\b(?:packaging|off[- ]chip|commercial|foundry|3D\s+integration|co[- ]packag|monolithic|projected|future|further)\b", txt, re.I):
        flags.append("Does not separate current lab-prototype constraints from fundamental physics or provide a concrete engineering roadmap.")
    if re.search(r"\b(?:in\s+conclusion|to\s+conclude|all\s+in\s+all|to\s+sum\s+up)\b", txt, re.I):
        flags.append("Avoid formulaic 'In conclusion / To conclude' openers; open directly with the physical significance synthesized.")
    flags.extend(check_voice_hygiene(txt))
    if not flags:
        print("PASS: Closing section follows T1/T2 authority, honesty, and roadmap discipline.")
    else:
        for i, fl in enumerate(flags, 1):
            print(f"  [{i}] {fl}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Conclusion & Discussion CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query T1/T2 closing sections")
    pq.add_argument("--tier", default=""); pq.add_argument("--journal", default="")
    pq.add_argument("--platform", default=""); pq.add_argument("--limitation", default="")
    pq.add_argument("--top", type=int, default=5)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    ph = sub.add_parser("heading", help="Show exact closing heading rules by journal")
    ph.add_argument("--journal", default="")
    pl = sub.add_parser("lint", help="Lint a draft Discussion/Conclusion")
    pl.add_argument("file"); pl.add_argument("--journal", default="Nature Photonics")
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    elif args.cmd == "heading": cmd_heading(args)
    else: cmd_lint(args)

if __name__ == "__main__":
    main()
