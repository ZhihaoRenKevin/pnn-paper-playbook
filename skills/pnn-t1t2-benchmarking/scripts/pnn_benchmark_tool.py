#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-benchmarking`: query T1/T2 benchmarks, audit claims, and emit table schemas."""
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
    return [json.loads(l) for l in (REF_DIR / "t1t2_benchmark_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.baseline and not any(args.baseline.lower() in b.lower() for b in (r.get("elec_base") or [])): continue
        if args.task and not any(args.task.lower() in t.lower() for t in (r.get("tasks") or [])): continue
        out.append(r)
    print(f"Matched {len(out)} T1/T2 Benchmarking records (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print(f"  - [{r['tier']} {r['journal']} {r['year']} | {r['platform']}] {r['title']}")
        print(f"    Electronic baselines: {', '.join(r.get('elec_base') or ['none'])} | Optical SOTA: {r.get('opt_sota')} | Bench Fig: {r.get('b_fig')}")
        print(f"    Energy bounds: {', '.join(r.get('e_bounds') or [])} | Meas/Proj split: {r.get('meas_proj')} | Latency decomp: {r.get('lat_decomp')}")
        print(f"    Formats: {', '.join(r.get('b_formats') or [])} | Tasks: {', '.join((r.get('tasks') or [])[:4])}")
        print(f"    Fairness defenses: {', '.join(r.get('fairness') or [])}")

def cmd_audit(args):
    txt = safe_read_text(args.file)
    print("=== PNN T1/T2 Benchmarking Rigour Audit ===")
    checks = [
        ("1. Energy accounting boundary stated (core/laser/chip-IO/wall-plug)", bool(re.search(r"\b(?:core[- ]optical|laser\s+power|wall[- ]plug|DAC|ADC|TIA|electrical\s+overhead)\b", txt, re.I))),
        ("2. Throughput arithmetic & MAC=2 OP defined", bool(re.search(r"\b(?:TOPS|GOPS|MAC|OPs?/s)\b", txt))),
        ("3. Named electronic baseline (GPU/TPU/FPGA/ASIC/DSP)", bool(re.search(r"\b(?:NVIDIA|A100|H100|V100|RTX|TPU|FPGA|ASIC|CMOS|CPU|DSP)\b", txt))),
        ("4. Measured vs Projected explicitly separated", bool(re.search(r"\b(?:projected|estimated|extrapolat|scaled)\b", txt, re.I) and re.search(r"\b(?:measured|experimental|demonstrated)\b", txt, re.I))),
        ("5. Precision / ENOB / bit depth at operating speed", bool(re.search(r"\b(?:ENOB|\d+(?:\.\d+)?[- ]bit|bit\s+precision|RMS\s+error)\b", txt, re.I))),
        ("6. Real-signal or beyond-toy task present", bool(re.search(r"\b(?:Fashion[- ]MNIST|CIFAR|ImageNet|speech|audio|radar|fiber|fibre|Ising|PDE|in[- ]sensor|generative|medical|ECG)\b", txt, re.I))),
        ("7. End-to-end latency breakdown (not optical ToF alone)", bool(re.search(r"\b(?:latency|end[- ]to[- ]end|time[- ]to[- ]solution|readout|DAC|ADC)\b", txt, re.I))),
    ]
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'MISS'}] {label}")

def cmd_schema(args):
    print(f"=== T1/T2 Recommended Benchmark Table Schema ({args.tier.upper()}) ===")
    print("Note: T1 (Nature/Science) puts full comparison tables in Extended Data / SI Table S1 (Measured) & Table S2 (Projected), keeping a visual log-log Pareto scatter in Main Fig. 4/5.")
    print("| Reference | Platform / Material | Wavelength / Mux | Scale (N x M) | Precision (ENOB/bits) | Clock / Baud | Throughput (TOPS, Measured) | Latency (Optical / E2E) | Energy/OP [Boundary] | Insertion Loss (dB) | Task & Acc (Chip vs Digital) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")

def cmd_all_tier_sota(args):
    """Information-layer bridge: queries ALL-TIER (T1-T4, 1,475 papers) factual SOTA/benchmark numbers from sibling pnn-paper-playbook."""
    import csv
    pnn_ref = (SKILL_DIR.parent.parent / "references" if (SKILL_DIR.parent.parent / "references").exists() else SKILL_DIR.parent / "pnn-paper-playbook" / "references")
    bl_p = pnn_ref / "derived" / "benchmark_ledger.csv"
    at_p = pnn_ref / "derived" / "device_parameter_atlas.csv"
    if args.task and bl_p.exists():
        rows = list(csv.DictReader(open(bl_p, encoding="utf-8-sig")))
        hits = [r for r in rows if args.task.lower() in r.get("task", "").lower() and (not args.platform or args.platform.lower() in r.get("platform", "").lower())]
        print(f"=== ALL-TIER (T1-T4, 1,475 papers) Benchmark Ledger for task='{args.task}' ({len(hits)} rows) ===")
        for r in hits[:args.top]:
            print(f"  - {r.get('task')} | {r.get('platform')} | meas={r.get('papers_measured')} | med={r.get('measured_median')} | best={r.get('best_measured_text')} ({r.get('best_measured_tier')}, {r.get('best_measured_stem','')[:45]}) | tiers={r.get('papers_by_tier')}")
    elif at_p.exists():
        rows = list(csv.DictReader(open(at_p, encoding="utf-8-sig")))
        hits = [r for r in rows if (not args.platform or args.platform.lower() in (r.get("label", "") + " " + r.get("code", "")).lower()) and (not args.param or args.param.lower() in r.get("param", "").lower())]
        print(f"=== ALL-TIER (T1-T4, 1,475 papers) Device Parameter Atlas ({len(hits)} rows, showing top {min(len(hits), args.top)}) ===")
        for r in hits[:args.top]:
            print(f"  - [{r.get('code')}] {r.get('label')} | {r.get('param')} ({r.get('unit')}) | meas={r.get('papers_measured')} | med={r.get('measured_median')} | best={r.get('best_measured_text')} ({r.get('best_measured_tier')}, calc={r.get('best_measured_calc')})")
    else:
        print("Sibling pnn-paper-playbook references not found at:", pnn_ref)

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Benchmarking Craft CLI (+ All-Tier Factual SOTA Bridge)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query T1/T2 benchmarking strategies (craft = T1/T2 only)")
    pq.add_argument("--tier", default=""); pq.add_argument("--platform", default="")
    pq.add_argument("--baseline", default=""); pq.add_argument("--task", default="")
    pq.add_argument("--top", type=int, default=8)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pa = sub.add_parser("audit", help="Audit a manuscript/section for T1/T2 benchmarking completeness")
    pa.add_argument("file")
    ps = sub.add_parser("table-schema", help="Print T1/T2 Measured-vs-Projected comparison table schema")
    ps.add_argument("--tier", default="T1", choices=["T1", "T2"])
    pall = sub.add_parser("all-tier-sota", help="Query ALL-TIER (T1-T4, 1,475 papers) factual SOTA/benchmark competitor numbers")
    pall.add_argument("--task", default=""); pall.add_argument("--platform", default="")
    pall.add_argument("--param", default=""); pall.add_argument("--top", type=int, default=10)
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    elif args.cmd == "audit": cmd_audit(args)
    elif args.cmd == "all-tier-sota": cmd_all_tier_sota(args)
    else: cmd_schema(args)

if __name__ == "__main__":
    main()
