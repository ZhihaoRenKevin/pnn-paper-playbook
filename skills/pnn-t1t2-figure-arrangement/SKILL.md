---
name: pnn-t1t2-figure-arrangement
description: Actionable T1/T2 PNN Figure Arrangement, paper-level Fig. 1-5 storyboarding, panel-grid design, and Extended Data triage playbook calibrated from 478 visual M5 VLM inspections and 520 page-layout censuses across 113 Nature, Science, and Nature-subjournal research articles (reviews excluded; zero T3/T4 dilution). Use whenever planning a paper's multipanel figure sequence or fixing overcrowded slides/manuscript figures.
---

# How to Arrange and Revise T1/T2 PNN Figures (`pnn-t1t2-figure-arrangement`)

Use this skill to design clean, readable **Fig. 1-5 storyboards** and triage overflow panels into Extended Data or Supplementary Information so every main figure delivers **one unmistakable visual conclusion**.

---

## 1. How to Storyboard a Paper From Scratch (Canonical Fig. 1-5 Arc)

Assign exactly **one narrative job** per main figure (`4-5` main figures for *Nature*/*Science*, `4-6` for *Nature Photonics*/*Nature Electronics*):
- **Fig. 1 (Hero Architecture & Concept: `3-5` panels)**:
  - **Hero Panel `a` (`35-55%` of page area, top-left or full top row)**: Clean 3D physical architecture schematic showing exact optical flow and active knobs.
  - **Supporting Panels `b-d` (bottom row)**: Fabricated optical/SEM micrograph with scale bar + physical unit-cell mechanism + 1 preview performance comparison or conceptual scaling contrast.
- **Fig. 2 (Device Physics & Calibration: `4-6` panels)**:
  - Unit-cell transfer curve (measured vs simulated) -> uniformity/crosstalk map -> bit-precision/MAC error scatter -> bandwidth/switching speed.
- **Fig. 3 (Core Computing / Training Demo & Ablations: `4-6` panels)**:
  - Training/convergence curve -> confusion matrix or task accuracy bar chart -> **mandatory physics ablation panel** (untrained/linear/digital-readout-only control right inside the main figure!).
- **Fig. 4 (Multi-Task Scaling, Robustness, or Real-Signal System: `4-6` panels)**:
  - Harder real-world task / perturbation tolerance / drift recovery / multi-channel parallel scaling.
- **Fig. 5 (Optional System Benchmark & Scaling Envelope: `3-5` panels)**:
  - Measured vs projected Pareto frontier (TOPS/W vs latency or area density) alongside named electronic GPU/ASIC baselines and competing photonic platforms.

---

## 2. How to Lay Out Panels Cleanly (Grid & Reading-Flow Rules)
1. **Hard Panel Ceiling**: Keep main figures to **`4-6` panels** (absolute max `8` only for tightly paired small-multiples). If a figure reaches `9+` panels, immediately split or move secondary plots to Extended Data / SI!
2. **Hero Area Hierarchy**: Never make all 6 panels equal postage stamps. Give the hero panel (3D architecture in Fig. 1; headline accuracy/Pareto in Fig. 3-5) **`30-50%` of total figure area**, and align smaller quantitative panels on a clean `2x2` or `1x3` secondary grid.
3. **Strict Z-Pattern Reading Flow**: Place `a` at top-left, flowing left-to-right across Row 1 (`a -> b -> c`), then Row 2 (`d -> e -> f`). Never zigzag vertically in one column and horizontally in the next.
4. **Width & Font Discipline**: Build directly at journal print width (`180 mm` double-column, `89 mm` single-column) with `Arial` `7-8 pt` tick/axis labels and bold `9-10 pt` panel letters (`a`, `b`, `c`) aligned to identical horizontal/vertical baselines.

---

## 3. How to Revise an Overcrowded Figure (Extended Data / SI Triage)

When revising a crowded draft figure (`>=8` panels, tiny illegible fonts, or mixed stories), apply this exact triage table:

| Keep in Main Figure (Figs. 1-5) | Move to Extended Data (`Nature` max 10) | Move to Supplementary Information (SI) |
|---|---|---|
| Hero 3D physical architecture + real micrograph | Full optical/electronic bench photograph & PCB layout | Step-by-step fabrication process flow & GDS masks |
| Headline measured transfer curve + MAC fidelity | Individual device-to-device calibration histograms | Raw thermal/drift stability logs over hours |
| Primary task accuracy + mandatory physics ablation | Secondary datasets, hyperparameter sweeps, seed spreads | Derivations, FDTD mesh convergence, full SOTA tables |
| Headline Pareto / GPU comparison | Breakdown of 4-tier energy accounting sub-components | Extended multi-parameter sensitivity scans |

### Concrete Before -> After Arrangement Fix
- **Before**: Fig. 2 packs 11 sub-panels (`a-k`) combining fabrication flow, optical bench photo, 4 spectra, thermal map, crosstalk matrix, MAC scatter, and 2 confusion matrices at 4.5 pt font.
- **After**: Fig. 2 keeps `5` clean panels (`a` unit-cell schematic [top-left 35%], `b` phase-vs-power transfer curve, `c` crosstalk matrix, `d` 6.1-bit MAC scatter, `e` dynamic switching response) at crisp `8 pt` Arial; fabrication flow moves to Supplementary Fig. 1, bench photo moves to Extended Data Fig. 1, and confusion matrices move into Fig. 3 alongside the ablation control.

### Mandatory CLI Blueprint & Audit Gate
```bash
python3 scripts/pnn_arrangement_tool.py blueprint --fig 1 --tier T1 --top 3
python3 scripts/pnn_arrangement_tool.py audit --fig 2 --panels 9 --tier T1
```

---

## 4. Compact Pass/Fail Checklist
- [ ] `4-5` main figures (T1) or `4-6` (T2), each making exactly one headline claim.
- [ ] `4-6` panels per figure (`<=8` hard cap); hero panel takes `30-50%` of figure area.
- [ ] Clean Z-pattern reading order with aligned panel labels and `>=7 pt` print font size.
- [ ] Setup photos, raw calibration sweeps, and extra datasets triaged cleanly to Extended Data / SI.

## 4. References & CLI
- Layout blueprints & VLM corpus: [`references/t1t2_layout_blueprints.md`](./references/t1t2_layout_blueprints.md) and [`references/t1t2_arrangement_corpus.jsonl`](./references/t1t2_arrangement_corpus.jsonl).
