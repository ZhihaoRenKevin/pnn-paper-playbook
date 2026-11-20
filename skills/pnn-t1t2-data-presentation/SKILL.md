---
name: pnn-t1t2-data-presentation
description: Actionable T1/T2 PNN Data Presentation playbook calibrated from 113 published Nature, Science, and Nature-subjournal research articles and 478 visual VLM figure inspections (zero T3/T4 dilution). Use whenever choosing chart types for optical/ML quantities, overlaying simulated vs measured data, or designing mandatory physics ablation controls.
---

# How to Present and Revise PNN Experimental Data (`pnn-t1t2-data-presentation`)

Use this skill to choose the right visual encoding for every physical and ML quantity and to design the **5 physics ablation controls** that stop T1/T2 referees from claiming `"the electronics did all the work"`.

---

## 1. How to Choose the Right Plot for Every Physical Quantity

| Physical / ML Quantity | Mandatory T1/T2 Chart Type | Encoding Rules & Referee Traps to Avoid |
|---|---|---|
| **Measured vs Ideal MAC / Weight Accuracy** | Scatter (`y_meas` vs `y_ideal`) + `y = x` identity line + inset residual histogram | Report RMSE **and** effective bit precision (`ENOB`); never show only a cherry-picked 5-element vector |
| **Spectral / Phase Transfer Curves** | 1D line + discrete measured markers (`symbols = exp`, `dashed = sim`) | Show full sweep range; never smooth noisy spectra without showing raw points or stating filter width |
| **In-Situ Training Convergence** | Epoch curve with solid mean + translucent `+-1 s.d.` shaded band (`n >= 5` seeds) | Overlay **3 curves minimum**: Hardware, Matched Digital Baseline, and Offline/Untrained Control |
| **Classification Performance** | Normalized confusion matrix (sequential colormap, diagonal % printed cleanly) | State exact held-out sample count (`k/n`) right in the panel/caption; never plot training accuracy |
| **Thermal / Optical Crosstalk** | Symmetric heatmap (`dB` scale) with explicit diagonal & nearest-neighbor values | State exact channel pitch (`um`) and whether trenches or active compensation are on |
| **Throughput / Energy Scaling** | Log-log Pareto scatter (`TOPS/W` vs `TOPS/mm^2` or latency) | Use **filled markers = measured**, **open markers = projected**, and include at least 1 named GPU/ASIC |

---

## 2. The 5 Mandatory T1/T2 Physics Ablation Controls (Include >=2 in Main Figures!)

Before finalizing Figs. 2-4, verify which of these 5 controls neutralize your biggest referee attack (`C5`, `C6`, `C9`):
1. **Untrained / Static-Core Control** (proves programmable optical weights matter): Freeze or randomize chip weights while keeping the identical electronic readout classifier -> show a decisive accuracy drop.
2. **Linear-Only vs Nonlinear-Activation Control** (proves optical nonlinearity does real work): Disable optical nonlinearity and retrain the same linear optical core -> quantify the nonlinear accuracy gain on a non-linearly-separable task.
3. **Offline Digital-Twin vs In-Situ Hardware Training Control** (proves physical training overcomes mismatch): Download digital weights directly to chip without hardware-in-the-loop calibration -> show accuracy degradation vs in-situ recovery.
4. **Perturbation / Thermal-Drift Stress Test** (proves robustness): Perturb chip temperature, laser wavelength, or drive noise systematically -> plot accuracy vs perturbation amplitude.
5. **Electronic-Readout-Only Baseline** (kills the "backend MLP solved it" attack): Feed raw unmixed optical inputs directly into the backend digital classifier with the identical parameter budget -> prove the photonic core contributes measurable separation or FLOP reduction.

---

## 3. How to Revise Weak Data Figures (Concrete Before -> After)
- **Before**: Bar chart showing `"Our chip: 95%"` alone with truncated y-axis (`90-96%`), no error bars, no digital baseline, and no ablation control; simulated and measured curves plotted in separate panels with mismatched y-scales.
- **After**: Full-range paired comparison (`0-100%` or clearly broken axis) showing **Measured Hardware (`93.3 +- 1.1%`, `n=5`)**, **Matched Digital Model (`94.0%`)**, **Static-Core Control (`54.2%`)**, and **Readout-Only Baseline (`61.0%`)** in one unified panel, with simulated curves overlaid directly onto measured markers using identical axes.

### Mandatory CLI Chart Selector
```bash
python3 scripts/pnn_data_pres_tool.py recommend --quantity training_curve
python3 scripts/pnn_data_pres_tool.py recommend --quantity mac_fidelity
python3 scripts/pnn_data_pres_tool.py query --tier T1 --top 3
```

---

## 4. Compact Pass/Fail Checklist
- [ ] Every simulated-vs-measured comparison shares identical axes with explicit symbol/line distinction.
- [ ] Every training curve and accuracy bar reports mean, spread (`+- s.d.`), and `n` runs/samples.
- [ ] At least 2 of the 5 physics ablation controls appear directly in the main text (remaining in ED/SI).
- [ ] Measured vs projected data points are visually distinct (`filled` vs `open` markers) everywhere.

## 4. References & CLI
- Exemplar chart patterns: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_data_pres_corpus.jsonl`](./references/t1t2_data_pres_corpus.jsonl).
