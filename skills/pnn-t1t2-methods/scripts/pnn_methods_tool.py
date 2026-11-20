#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-methods`: query T1/T2 Methods subsection structures and audit reproducibility."""
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
    return [json.loads(l) for l in (REF_DIR / "t1t2_methods_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = [r for r in rows if (not args.tier or r["tier"].upper() == args.tier.upper()) and (not args.platform or args.platform.lower() in (r.get("platform") or "").lower())]
    print(f"Matched {len(out)} T1/T2 Methods blueprints (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print(f"  - [{r['tier']} {r['journal']} {r['year']} | {r['methods_words']}w | {r['platform']}] {r['title']}")
        print(f"    Core order: {' -> '.join(r.get('methods_core_order') or [])} | DataAvail:{r.get('has_data_avail')} CodeAvail:{r.get('has_code_avail')} RepoDOI:{r.get('has_github_zenodo')}")

def cmd_audit(args):
    txt = safe_read_text(args.file)
    print("=== PNN T1/T2 Methods & Reproducibility Gatekeeper ===")
    checks = [
        ("1. Fabrication & foundry stack (materials, layer thicknesses, node/etch)", bool(re.search(r"\b(?:fabricat|foundry|wafer|SOI|Si3N4|TFLN|etch|lithograph|nm|um|µm)\b", txt, re.I))),
        ("2. Optical bench specs (laser wavelength/dBm, modulator/PD bandwidth, coupling)", bool(re.search(r"\b(?:laser|dBm|mW|photodetector|grating|edge\s+coupler|GHz|MHz|nm)\b", txt, re.I))),
        ("3. Electrical I/O specs (DAC/ADC bits & MSa/s-GSa/s, TIA, sourcemeter/AWG)", bool(re.search(r"\b(?:DAC|ADC|AWG|oscilloscope|TIA|sourcemeter|FPGA|PCB|GSa|MSa|bit)\b", txt, re.I))),
        ("4. Calibration & training protocol (optimizer, lr, epochs, batch, in-situ step)", bool(re.search(r"\b(?:calibrat|training|optimizer|Adam|SGD|SPSA|backpropagation|epoch|learning\s+rate)\b", txt, re.I))),
        ("5. Speed & 4-tier energy accounting equations", bool(re.search(r"\b(?:TOPS|GOPS|energy|power\s+consumption|latency|wall[- ]plug|MAC)\b", txt, re.I))),
        ("6. Digital baseline & leak-free dataset splits (train/val/test, train-only PCA)", bool(re.search(r"\b(?:dataset|train(?:ing)?\s+set|test\s+set|validation|baseline|PyTorch|split)\b", txt, re.I))),
        ("7. Data & Code Availability + public repository/DOI", bool(re.search(r"\b(?:Data\s+availability|Code\s+availability|GitHub|Zenodo|10\.5281|repository)\b", txt, re.I))),
        ("8. Competing Interests / Ethics declaration", bool(re.search(r"\b(?:Competing\s+interests|no\s+competing|patent|ethics|IRB|consent)\b", txt, re.I))),
    ]
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'MISS'}] {label}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Methods Craft CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query T1/T2 Methods structures")
    pq.add_argument("--tier", default=""); pq.add_argument("--platform", default=""); pq.add_argument("--top", type=int, default=8)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pa = sub.add_parser("audit", help="Audit a Methods draft")
    pa.add_argument("file")
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    else: cmd_audit(args)

if __name__ == "__main__":
    main()
