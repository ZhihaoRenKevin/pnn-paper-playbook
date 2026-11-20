#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-figure-arrangement`: query T1/T2 VLM panel layouts and audit panel counts."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

def load_corpus():
    return [json.loads(l) for l in (REF_DIR / "t1t2_arrangement_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_blueprint(args):
    rows = load_corpus()
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.fig and int(r.get("fig_num", 0)) != args.fig: continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.flow and args.flow.lower() not in (r.get("flow") or "").lower(): continue
        out.append(r)
    flows = Counter(r.get("flow", "") for r in out if r.get("flow"))
    panels = [r["panels"] for r in out if isinstance(r.get("panels"), int) and r["panels"] > 0]
    med_p = sorted(panels)[len(panels)//2] if panels else 0
    print(f"Matched {len(out)} T1/T2 VLM-inspected figures | Median panels: {med_p} | Top flows: {flows.most_common(4)}")
    for r in out[:args.top]:
        print(f"  - [{r['tier']} {r['journal']} {r['year']} | Fig.{r['fig_num']} | {r['platform']}] panels={r.get('panels')} | grid={r.get('grid')} | flow={r.get('flow')} | hero={r.get('hero_pct')}% | 3D={r.get('has_3d')} | SEM/OM={r.get('has_sem_om')} | insets={r.get('insets')}")

def cmd_audit(args):
    ceilings = {1: (3, 5), 2: (4, 6), 3: (4, 6), 4: (3, 6), 5: (3, 5)}
    med, ceil = ceilings.get(args.fig, (4, 6))
    print(f"=== PNN {args.tier.upper()} Fig. {args.fig} Panel Arrangement Audit ===")
    print(f"Proposed panels: {args.panels} | T1/T2 median: {med} | T1/T2 soft ceiling: {ceil} | Hard outlier (>95th pct): 9+")
    if args.panels <= ceil:
        print("PASS: Panel count fits comfortably inside T1/T2 editorial whitespace bounds (64-66% whitespace).")
    elif args.panels <= 8:
        print("WARN: Dense figure. Ensure one clear hero panel (>=35% area), aligned axes, and move repetitive sweeps to Extended Data/SI.")
    else:
        print("FAIL (T4 overcrowding trap): >8 sub-panels causes text collisions and violates T1/T2 whitespace discipline.")
        print("Action: Keep 1 concept/hero + 3-4 decisive data/ablation panels in main Fig.; move per-port calibration, fabrication sweeps, and secondary confusion matrices to Extended Data Figs. / SI.")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Figure Arrangement CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pb = sub.add_parser("blueprint", help="Query real T1/T2 figure grid & flow blueprints")
    pb.add_argument("--fig", type=int, default=0); pb.add_argument("--tier", default="")
    pb.add_argument("--platform", default=""); pb.add_argument("--flow", default="")
    pb.add_argument("--top", type=int, default=8)
    pa = sub.add_parser("audit", help="Audit proposed sub-panel count for a figure")
    pa.add_argument("--fig", type=int, required=True); pa.add_argument("--panels", type=int, required=True)
    pa.add_argument("--tier", default="T1", choices=["T1", "T2"])
    args = ap.parse_args()
    if args.cmd == "blueprint": cmd_blueprint(args)
    else: cmd_audit(args)

if __name__ == "__main__":
    main()
