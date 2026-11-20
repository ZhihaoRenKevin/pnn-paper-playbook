#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-figure-color`: empirical T1/T2 CIELAB HEX palettes + Machado CVD checker."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

def _s2l(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def _l2s(c: float) -> float:
    c = max(0.0, min(1.0, c))
    return c * 12.92 if c <= 0.0031308 else 1.055 * (c ** (1.0 / 2.4)) - 0.055

def hex_to_lab(hx: str) -> tuple[float, float, float, float, float]:
    h = hx.lstrip("#")
    r, g, b = int(h[0:2], 16) / 255.0, int(h[2:4], 16) / 255.0, int(h[4:6], 16) / 255.0
    lr, lg, lb = _s2l(r), _s2l(g), _s2l(b)
    x = (0.4124564 * lr + 0.3575761 * lg + 0.1804375 * lb) / 0.95047
    y = (0.2126729 * lr + 0.7151522 * lg + 0.0721750 * lb) / 1.00000
    z = (0.0193339 * lr + 0.1191920 * lg + 0.9503041 * lb) / 1.08883
    eps, kap = 216.0 / 24389.0, 24389.0 / 27.0
    fx = x ** (1/3) if x > eps else (kap * x + 16.0) / 116.0
    fy = y ** (1/3) if y > eps else (kap * y + 16.0) / 116.0
    fz = z ** (1/3) if z > eps else (kap * z + 16.0) / 116.0
    L = 116.0 * fy - 16.0
    a = 500.0 * (fx - fy)
    bb = 200.0 * (fy - fz)
    C = math.hypot(a, bb)
    H = math.degrees(math.atan2(bb, a)) % 360.0
    return (L, a, bb, C, H)

def sim_cvd_hex(hx: str, mode: str) -> str:
    h = hx.lstrip("#")
    lr, lg, lb = _s2l(int(h[0:2], 16)/255.0), _s2l(int(h[2:4], 16)/255.0), _s2l(int(h[4:6], 16)/255.0)
    if mode == "deut":
        sr = 0.367322*lr + 0.860646*lg - 0.227968*lb
        sg = 0.280085*lr + 0.672501*lg + 0.047413*lb
        sb = -0.011820*lr + 0.042940*lg + 0.968881*lb
    else:
        sr = 0.152286*lr + 1.052583*lg - 0.204868*lb
        sg = 0.114503*lr + 0.786281*lg + 0.099216*lb
        sb = -0.003882*lr - 0.048116*lg + 1.051998*lb
    R, G, B = int(round(_l2s(sr)*255)), int(round(_l2s(sg)*255)), int(round(_l2s(sb)*255))
    return f"#{R:02X}{G:02X}{B:02X}"

def cmd_palette(args):
    stats = json.loads((REF_DIR / "t1t2_color_stats.json").read_text(encoding="utf-8"))
    key = "research_T1" if args.tier.upper() == "T1" else ("research_T2" if args.tier.upper() == "T2" else "research_all_t1t2")
    grp = stats["pixel_color_census"].get(key, stats["pixel_color_census"]["research_all_t1t2"])
    if args.journal:
        for jk, jv in stats["pixel_color_census"].get("by_journal_research", {}).items():
            if args.journal.lower() in jk.lower():
                grp = jv; key = jk; break
    print(f"=== Empirical T1/T2 CIELAB Palette [{key}] (n={grp['n_pages']} figure pages) ===")
    print(f"Median whitespace: {grp['whitespace_frac']['median']*100:.1f}% | Median C*: {grp['chroma_med_Cstar']['median']} (P90={grp['chroma_p90_Cstar']['median']}) | Median L*: {grp['lightness_med_Lstar']['median']}")
    print("| Hue Family | Presence | Empirical Medoid | Crisp Accent Line (C*>34) | Soft Fill/Band (C*<=34) | L* | C* |")
    print("|---|---:|:---:|:---:|:---:|---:|---:|")
    accents = []
    for fam, v in grp["canonical_hex_by_family"].items():
        if fam == "neutral_slate_grey": continue
        print(f"| {fam} | {v['presence_pct']}% | `{v['empirical_medoid_hex']}` | `{v['accent_line_hex']}` | `{v['soft_fill_hex']}` | {v['L_med']} | {v['C_med']} |")
        accents.append(v["accent_line_hex"])
    print("\nMatplotlib prop_cycle snippet:")
    print(f"plt.rcParams['axes.prop_cycle'] = plt.cycler(color={accents[:6]!r})")

def cmd_check_cvd(args):
    hexes = [h.strip() for h in args.hexes.split(",") if h.strip()]
    print("=== CIELAB Restraint & Colorblind Safety Audit (vs T1/T2 Median C*=27-29, P90=51-52) ===")
    labs = {}
    for hx in hexes:
        L, a, b, C, H = hex_to_lab(hx)
        labs[hx] = (L, a, b, C, H)
        warn = " [OVERSATURATED >68: tone down for Nature/Science!]" if C > 68 else " [OK T1/T2 range]"
        print(f"  {hx}: L*={L:5.1f}, C*={C:5.1f}, H={H:5.1f} deg{warn}")
    for mode, label in (("deut", "Deuteranopia"), ("prot", "Protanopia")):
        min_de, worst_pair = 999.0, ("", "")
        sim_labs = {hx: hex_to_lab(sim_cvd_hex(hx, mode))[:3] for hx in hexes}
        for i in range(len(hexes)):
            for j in range(i + 1, len(hexes)):
                l1, l2 = sim_labs[hexes[i]], sim_labs[hexes[j]]
                de = math.sqrt(sum((u - v) ** 2 for u, v in zip(l1, l2)))
                if de < min_de:
                    min_de, worst_pair = de, (hexes[i], hexes[j])
        status = "PASS" if min_de >= 14.0 else "WARN (too close for CVD readers; pair with linestyle/marker!)"
        print(f"  {label} min pairwise Delta-E: {min_de:.1f} between {worst_pair[0]} & {worst_pair[1]} -> {status}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Figure Color CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pp = sub.add_parser("palette", help="Print empirical T1/T2 CIELAB HEX palettes")
    pp.add_argument("--tier", default="all", choices=["all", "T1", "T2"])
    pp.add_argument("--journal", default="")
    pc = sub.add_parser("check-cvd", help="Check chroma restraint and Deuteranopia/Protanopia Delta-E")
    pc.add_argument("hexes", help="Comma-separated HEX list e.g. #4C6FB0,#BF4843,#DF9159,#7BC170")
    args = ap.parse_args()
    if args.cmd == "palette": cmd_palette(args)
    else: cmd_check_cvd(args)

if __name__ == "__main__":
    main()
