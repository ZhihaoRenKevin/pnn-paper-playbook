#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-si`: query 100 T1/T2 SI architectures, generate SI/ED plans, and audit SI drafts."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

def safe_read_text(arg: str) -> str:
    if len(arg) > 240 or "\n" in arg:
        return arg
    p = Path(arg)
    try:
        return p.read_text(encoding="utf-8", errors="replace") if p.exists() else arg
    except OSError:
        return arg

def load_corpus():
    return [json.loads(l) for l in (REF_DIR / "t1t2_si_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = [r for r in rows if (not args.tier or r["tier"].upper() == args.tier.upper()) and (not args.platform or args.platform.lower() in (r.get("platform") or "").lower())]
    print(f"Matched {len(out)} T1/T2 SI architectures (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print(f"  - [{r['tier']} {r['journal']} {r['year']} | {r['si_pages']}p | {r['supp_fig_count']} SFigs | {r['supp_table_count']} STabs | ED={r['ed_fig_count']}] {r['title']}")
        print(f"    Org: {r.get('org_pattern')} | Modules: {', '.join(r.get('core_modules') or [])}")
        if r.get("offloaded_from_main"):
            print(f"    Offloaded: {r['offloaded_from_main']}")

def cmd_plan(args):
    t = args.tier.upper()
    print(f"=== Recommended {t} PNN Supplementary Information & Extended Data Plan ({args.platform or 'Integrated PIC'}) ===")
    if t == "T1":
        print("Extended Data (main submission, 4-8 ED Figs + 1-2 ED Tables):")
        print("  - ED Fig. 1: Full chip layout, wafer/die micrograph, and fabrication cross-section SEM")
        print("  - ED Fig. 2: Complete experimental optical + electrical testbed schematic & instrumentation")
        print("  - ED Fig. 3: Unit-cell uniformity, per-channel calibration curves, and thermal/optical crosstalk matrix")
        print("  - ED Fig. 4: Multi-seed training convergence, drift stability over time, and full ablation breakdowns")
        print("  - ED Table 1: Comprehensive Measured Hardware SOTA Comparison (separate from Projected Table S2)")
    print("Supplementary Information Document (Front-Matter TOC -> Numbered Supplementary Notes -> References at End):")
    print("  - Table of Contents (mandatory for >15p SI; zero internal filenames or raw DOI tables)")
    print("  - Supplementary Note 1: Theoretical formulation, coupled-mode / wave-transfer derivations & scaling bounds")
    print("  - Supplementary Note 2: Fabrication run-sheet, foundry stack, CDSEM/TEM metrology & insertion-loss budget")
    print("  - Supplementary Note 3: Per-port calibration, crosstalk inversion matrix & noise-limited ENOB derivation")
    print("  - Supplementary Note 4: 4-Tier Speed, Latency & Energy Accounting Ledger (core / laser+core / chip I/O / wall-plug)")
    print("  - Supplementary Note 5: Dataset splits, leak-free preprocessing (train-only PCA), digital baselines & ablation controls")
    print("  - Supplementary Table S1 (Measured Hardware Benchmarks) & Supplementary Table S2 (Projected / Scaled Benchmarks)")

def cmd_audit(args):
    txt = safe_read_text(args.file)
    print("=== PNN T1/T2 Supplementary Information Audit ===")
    checks = [
        ("1. Front Table of Contents present", bool(re.search(r"\b(?:Table\s+of\s+Contents|Contents)\b", txt[:5000], re.I))),
        ("2. Numbered Supplementary Notes / Sections", bool(re.search(r"\b(?:Supplementary\s+(?:Note|Section)|Note\s+S)\s*\d+", txt, re.I))),
        ("3. Numbered Supplementary Figures (Fig. S1 / Supplementary Fig. 1)", bool(re.search(r"\b(?:Supplementary\s+Fig|Fig(?:ure)?\.?\s*S)\s*\d+", txt, re.I))),
        ("4. Measured vs Projected comparison tables separated", bool(re.search(r"\b(?:Table\s+S|Supplementary\s+Table)\s*\d+", txt, re.I))),
        ("5. Calibration / crosstalk / noise-sensitivity analysis included", bool(re.search(r"\b(?:calibrat|crosstalk|noise|drift|tolerance)\b", txt, re.I))),
        ("6. Energy & latency breakdown equations included", bool(re.search(r"\b(?:energy|power\s+budget|wall[- ]plug|DAC|ADC|TOPS/W|latency)\b", txt, re.I))),
        ("7. Zero internal file names / raw script paths leaked", not bool(re.search(r"\b(?:\.py|\.csv|\.fsp|\.mph|C:\\Users|/Users/)\b", txt))),
    ]
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'MISS'}] {label}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Supplementary Information Craft CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query 100 T1/T2 SI structures")
    pq.add_argument("--tier", default=""); pq.add_argument("--platform", default=""); pq.add_argument("--top", type=int, default=8)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pp = sub.add_parser("plan", help="Generate T1/T2 SI + Extended Data blueprint")
    pp.add_argument("--tier", default="T1", choices=["T1", "T2"]); pp.add_argument("--platform", default="")
    pa = sub.add_parser("audit", help="Audit an SI draft")
    pa.add_argument("file")
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    elif args.cmd == "plan": cmd_plan(args)
    else: cmd_audit(args)

if __name__ == "__main__":
    main()
