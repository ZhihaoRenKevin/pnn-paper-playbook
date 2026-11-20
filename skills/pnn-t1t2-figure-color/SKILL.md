---
name: pnn-t1t2-figure-color
description: Actionable T1/T2 PNN Figure Color selection, palette assignment, and colorblind-safety revision playbook calibrated via pixel-level CIELAB K-means clustering across 520 published Nature, Science, and Nature-subjournal research figure pages (reviews separated; zero T3/T4 dilution). Use whenever choosing HEX palettes, separating 3D material colors from data-curve colors and 2D colormaps, or fixing garish/unsafe figure colors.
---

# How to Choose and Revise T1/T2 PNN Figure Colors (`pnn-t1t2-figure-color`)

Use this skill to pick cohesive, publication-grade `#HEX` palettes and fix cluttered or colorblind-unsafe figures before rendering in Matplotlib, Origin, or Blender. Calibrated pixel-by-pixel across `520` published T1/T2 research figure pages (`0` T3/T4).

---

## 1. How to Assign Colors From Scratch (3-Layer Color Architecture)

Never let 3D device schematics, 1D data curves, and 2D optical field maps share the same rainbow palette. Assign colors in 3 strict layers:

### Layer 1: 3D Device & Material Palette (Low-Chroma Architectural Neutrals)
Keep hardware materials muted (`C* <= 30`) so optical beams and data curves pop effortlessly:
- **Silicon waveguide / slab**: `#5C6F84` (slate blue-grey) or `#6E7B8B`
- **SiO2 cladding / BOX**: `#E8EEF2` (cool pale grey-blue, semi-transparent)
- **Silicon nitride (`Si3N4`) / AlN / ScAlN**: `#8DA7BE` (soft steel) or `#96B8A8` (muted sage)
- **TiN / Au electrodes & heaters**: `#D4A359` (matte warm gold) or `#C88D48`
- **PCM (`GST`/`GSST`/`Sb2Se3`) active patch**: `#8F4B6E` (muted plum-berry)
- **Canvas background**: Strictly pure white `#FFFFFF` (maintain `60-68%` open whitespace across the figure page).

### Layer 2: 1D Data-Curve Semantic Palette (Refined T1/T2 Empirical Medoids)
Use **3-5 high-contrast, colorblind-safe ink colors** (`C* ~ 40-58`, never neon `#FF0000` / `#00FF00` / `#0000FF`) and lock **one color = one physical quantity/wavelength** across the entire manuscript + SI:
- **Primary Proposed Hardware / Measured Data**: `#3C6CB5` (T1 Cobalt) or `#B83C35` (T1 Crimson)
- **Matched Digital / Theoretical Reference**: `#2B2F36` (Charcoal dashed) or `#7C8594` (Neutral slate)
- **Secondary Channel / Wavelength 2 / Baseline B**: `#DF9159` (Warm Amber) or `#2E8B7D` (Teal)
- **Tertiary Channel / Ablation Control**: `#6946A3` (Plum) or `#7BC170` (Sage)
- **Shaded Confidence Band (`+-1 s.d.`)**: Same hue as its parent curve at `alpha = 0.16-0.22`.

### Layer 3: 2D Field, Confusion-Matrix & Heatmap Colormaps
- **Intensity / Optical Power / Confusion Matrix (Sequential)**: `viridis`, `cividis`, `magma`, or white-to-cobalt (`#FFFFFF -> #9DB9DE -> #214B8C`). Never use `jet` or `rainbow`.
- **Signed Optical Field (`E_z`, phase `-pi..+pi`, error residuals: Diverging)**: `RdBu_r` or `#2C5AA0 -> #F7F7F7 -> #B83C35` centered strictly at `0`.

---

## 2. How to Revise Existing Weak Figures (4-Step Color Rescue)
1. **Kill Rainbow & Neon Curves**: Replace pure RGB (`#FF0000`, `#00FF00`, `#0000FF`, `#FFFF00`) and `jet` colormaps with the Layer 2/3 HEX sets above.
2. **Enforce Global Wavelength/Class Consistency**: Audit Fig. 1 through Fig. 5 + SI so `1550 nm` (or `Hardware` vs `Digital`) keeps the exact same `#HEX` in every panel.
3. **Double-Encode Curves for Greyscale & CVD Readers**: Pair color differences with marker/linestyle differences (e.g., solid line + filled circles for measured hardware; dashed line for simulation/digital baseline; open triangles for ablation control).
4. **Run the Automated Machado Colorblind Delta-E Audit**:
```bash
python3 scripts/pnn_color_tool.py palette --tier T1
python3 scripts/pnn_color_tool.py palette --journal "Nature Photonics"
python3 scripts/pnn_color_tool.py check-cvd "#B83C35,#3C6CB5,#DF9159,#6946A3"
```
Every curve pair must achieve **Machado Deuteranopia & Protanopia `Delta-E >= 15`** (fix any flagged pair by shifting lightness `L*` or swapping one hue before exporting 600 dpi PNG + SVG!).

### Concrete Before -> After Color Fix
- **Before**: Bright green (`#00FF00`) measured curve + red (`#FF0000`) simulated curve on a grey grid background + `jet` confusion matrix -> fails deuteranopia (`Delta-E < 8`), looks like default MATLAB/Excel.
- **After**: T1 Crimson (`#B83C35`, filled circles) measured data + Charcoal (`#2B2F36`, dashed line) simulation on pure white `#FFFFFF` with inward ticks, 4-sided clean box, no gridlines + white-to-cobalt sequential confusion matrix -> passes Machado CVD (`Delta-E > 28`) and matches *Nature Photonics* print standards.

---

## 3. Compact Pass/Fail Checklist
- [ ] `<=5` distinct curve colors per panel; zero neon primaries; zero `jet`/`rainbow` colormaps.
- [ ] 3D materials muted (`C* <= 30`) so optical signals and curves stay visually foregrounded.
- [ ] Same physical quantity/wavelength uses identical `#HEX` across all Main + SI figures.
- [ ] `check-cvd` reports `Delta-E >= 15` for every curve pair under Deuteranopia and Protanopia.

## 4. References & CLI
- Journal palettes & HEX sheets: [`references/t1t2_journal_palettes_and_exemplars.md`](./references/t1t2_journal_palettes_and_exemplars.md) and [`references/t1t2_color_corpus.jsonl`](./references/t1t2_color_corpus.jsonl).
