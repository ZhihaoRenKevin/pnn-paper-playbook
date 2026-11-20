---
name: pnn-t1t2-methods
description: Actionable T1/T2 PNN Methods and Reproducibility Disclosures drafting and revision playbook calibrated exclusively on 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 dilution). Use whenever writing or auditing Methods subsections, instrumentation specs, training protocols, energy equations, or Data/Code availability statements.
---

# How to Write and Revise a T1/T2 PNN Methods Section (`pnn-t1t2-methods`)

Use this skill to write a crisp, fully reproducible Methods section that passes *Nature*/*Science* technical and editorial compliance checks on the first pass (`T1` target `1,600-3,000w`, `T2` target `900-1,800w`).

---

## 1. How to Write From Scratch (Canonical 7-Subsection Order)

Write Methods in this exact logical sequence (omitting only subsections that genuinely do not apply):
1. **Device Design & Electromagnetic/Multiphysics Modeling**: Specify exact solver name/version (e.g., Ansys Lumerical FDTD/MODE, COMSOL), wafer stack dimensions (`220 nm` SOI, `2 um` BOX), material refractive indices with citations, mesh convergence grid, and boundary/PML settings.
2. **Chip Fabrication & Packaging**: State foundry/cleanroom (`commercial silicon foundry, EBL/DUV lithography), etch steps, cladding/CMP, heater/electrode metallurgy, wire-bonding, and fiber-array/edge-coupling packaging (with measured fiber-to-chip insertion loss).
3. **Experimental Optical & Electronic Testbed**: List **exact make, model, and operating spec** of every key instrument: tunable laser (wavelength, output power, linewidth), polarization controller, AWG/DAC (sampling rate, bit resolution, voltage swing), photodetector/TIA (bandwidth, responsivity, noise floor), oscilloscope/ADC, and TEC temperature stability (`+-0.01 C`).
4. **Calibration, Crosstalk & Hardware Training Protocol**: State exact initialization, phase-voltage lookup or matrix calibration routine, crosstalk measurement/compensation, optimizer (`Adam`, coordinate descent, PAT, FFM), learning rate, batch size, epoch count, and wall-clock training time.
5. **Datasets, Preprocessing & Split Hygiene**: Name every dataset, sample count, train/validation/test split rule, and confirm **zero data leakage** (PCA/normalization fitted strictly on training data; held-out subjects/sessions/trials never seen during hyperparameter selection).
6. **Speed, Throughput & Energy Accounting Equations**: Define `1 MAC = 2 OP` explicitly, write the exact equations for all 4 energy tiers (Optical Core -> Chip -> Electrical I/O -> Wall-Plug) and end-to-end latency, and state exact specs of any GPU/ASIC baseline used for comparison.
7. **Mandatory Editorial Declarations**: `Data availability` (Zenodo/Figshare/GitHub + source data), `Code availability` (GitHub/Zenodo commit/release), `Author contributions`, and `Competing interests`.

---

## 2. How to Revise an Existing Methods Draft (3-Pass Surgery)
1. **Replace Vague Equipment Phrases with Exact Specs**: Turn `"a laser and high-speed photodetector were used"` -> `"a continuous-wave tunable laser (Santec TSL-570, 1550 nm, 10 dBm) coupled via a 12-channel fiber array (3.2 dB per facet loss) into a 10 GHz InGaAs photodetector (Thorlabs RXM10AF)"`.
2. **Tighten Wordy Lab Grammar**: Strip `"in order to"` -> `"to"`, `"due to the fact that"` -> `"because"`, and repetitive passive boilerplate; use clean active/passive balance tied to equations via `such that` and `given that`.
3. **Run the Automated Reproducibility Audit**:
```bash
python3 scripts/pnn_methods_tool.py audit path/to/methods.txt
python3 scripts/pnn_methods_tool.py query --tier T1 --native-only --top 3
```
Fix every missing disclosure flagged (`wafer/fab`, `laser/DAC/PD models`, `optimizer/epochs`, `MAC=2 OP equation`, `no-leakage split`, `Data/Code availability`).

---

## 3. Compact Pass/Fail Checklist
- [ ] All 7 canonical subsections covered with exact geometry, material sources, and instrument models.
- [ ] Dataset split explicitly guarantees zero train/test leakage (preprocessing fitted on train split only).
- [ ] Energy (`Tier 1-4`) and latency equations match Main Text numbers to the last digit.
- [ ] `Data availability`, `Code availability`, and `Competing interests` statements present and concrete.

## 4. References & CLI
- Native-weighted exemplars: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_methods_corpus.jsonl`](./references/t1t2_methods_corpus.jsonl) (`49` native-primary `weight=2.0` sorted first).
