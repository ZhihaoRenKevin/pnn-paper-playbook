#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-data-presentation`: query T1/T2 chart modalities, ablations, and proof arcs."""
from __future__ import annotations
import argparse, json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

QUANTITY_MAP = {
    "transfer_curve": ("line_markers + curve_fit", "Overlay measured points (filled markers) with analytical/FDTD fit (solid/dashed line) on identical axes; report R^2 or RMS residual."),
    "weight_precision": ("hist_err + scatter_target_vs_meas", "Plot target vs measured weight scatter (y=x diagonal) + inset residual error histogram with exact RMS error and ENOB = -log2(RMS)."),
    "training_curve": ("train_errband", "Plot hardware-in-the-loop curve (crimson/cobalt) with shaded +-1 s.d. band across seeds alongside untrained-core & digital-matched-precision controls."),
    "classification": ("conf_mat + bar_err", "Single-hue sequential Blues confusion matrix printing exact integer counts k/n and row-normalized %, paired with digital baseline bar/star."),
    "field_mode": ("heatmap_field", "Use perceptually uniform inferno/magma for |E|^2, YlOrRd for Delta-T, and symmetric RdBu_r for signed weights/phase. Never use jet."),
    "high_speed": ("eye_wave + spectrum", "Show time-domain eye diagram or modulated waveform with exact Gbaud/ns scale bar alongside SNR/BER or spectrum plot."),
    "stability_drift": ("line_markers", "Plot multi-minute/multi-hour frozen-checkpoint readout or endurance cycle trace with +-s.d. band and zero-hold-power tag if non-volatile."),
    "scaling_benchmark": ("loglog_pareto", "Use log-log axes with diagonal iso-FOM contours, filled markers for Measured vs hollow for Projected, and highlight 'This work' with a distinct crimson star."),
}

def load_corpus():
    return [json.loads(l) for l in (REF_DIR / "t1t2_data_pres_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.ablation and not any(args.ablation.lower() in a.lower() for a in (r.get("ablations") or [])): continue
        out.append(r)
    print(f"Matched {len(out)} T1/T2 Data Presentation records (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print(f"  - [{r['tier']} {r['journal']} {r['year']} | {r['platform']}] {r['title']}")
        print(f"    Arc: {' -> '.join(r.get('data_arc') or [])}")
        print(f"    Ablations: {', '.join(r.get('ablations') or [])} | Sim/Exp: {r.get('sim_exp')} | Rigor: {', '.join(r.get('stat_rigor') or [])}")

def cmd_recommend(args):
    q = args.quantity.lower()
    matched = [(k, v) for k, v in QUANTITY_MAP.items() if q in k or q in v[0].lower() or q in v[1].lower()]
    if not matched:
        print("Available quantities:", ", ".join(QUANTITY_MAP.keys()))
        return
    for k, (mod, rule) in matched:
        print(f"[{k}] Recommended modality: {mod}")
        print(f"  T1/T2 Standard: {rule}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Data Presentation CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query T1/T2 proof arcs & ablation controls")
    pq.add_argument("--tier", default=""); pq.add_argument("--platform", default="")
    pq.add_argument("--ablation", default=""); pq.add_argument("--top", type=int, default=8)
    pr = sub.add_parser("recommend", help="Recommend T1/T2 chart modality for a physical quantity")
    pr.add_argument("--quantity", required=True)
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    else: cmd_recommend(args)

if __name__ == "__main__":
    main()
