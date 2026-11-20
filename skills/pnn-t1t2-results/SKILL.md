---
name: pnn-t1t2-results
description: Actionable T1/T2 PNN Results section drafting and revision playbook calibrated exclusively on 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 dilution). Use whenever writing or revising Results subheadings, figure-anchored paragraphs, operator-to-physics mappings, or ablation narratives.
---

# How to Write and Revise a T1/T2 PNN Results Section (`pnn-t1t2-results`)

Use this skill to structure Results as a **4-act experimental proof**, not a chronological lab diary. Every subheading maps 1:1 to a main figure, and every paragraph leads with its physical conclusion.

---

## 1. How to Write From Scratch (4-Act Results Architecture)

### Step 1: Lock 3-5 Noun-Phrase Subheadings Mapped 1:1 to Figs. 1-5
Write crisp `3-7` word noun phrases (never generic labels like `"Experimental Results"` or `"Simulations"`):
1. **Subheading 1 (Fig. 1)**: Architecture and physical operating principle (e.g., `Architecture of the programmable diffractive core`)
2. **Subheading 2 (Fig. 2)**: Device characterization, calibration, and primitive accuracy (e.g., `Phase calibration and matrix-multiplication fidelity`)
3. **Subheading 3 (Fig. 3)**: Core computing benchmark and physical ablations (e.g., `In-situ training and optical ablation controls`)
4. **Subheading 4 (Fig. 4)**: Multi-task scaling, robustness, or system-level throughput/energy (e.g., `System-level inference and noise resilience`)
5. **Optional Subheading 5 (Fig. 5)**: Real-signal end-to-end application or comparative scaling envelope.

### Step 2: Write Every Results Paragraph Using the 5-Beat Proof Loop
1. **Beat 1: Claim-First Topic Sentence**: Lead with what the measurement proves, NOT `"Fig. 2a shows a plot of..."` (put `(Fig. 2a)` inside or at the end of the claim sentence).
2. **Beat 2: Operator-to-Hardware Mapping**: Tie the mathematical equation directly to the physical knob (`"Applying voltage V_i to heater i imparts a phase shift Delta-phi_i across slot i, implementing the complex transmission matrix T(V)"`).
3. **Beat 3: Measured Number + Spread + Sample Size**: Report mean, uncertainty, and count inline (`"93.3% accuracy (mean +- s.d. = 92.8 +- 1.1%, n = 5 independent runs; Fig. 3b)"`).
4. **Beat 4: Sim-vs-Exp / Baseline Comparison + Residual Cause**: Compare directly against simulation or digital ground truth (`"on par with the 94.0% matched digital model"`) and assign any gap to an explicit physical source (`"the 0.7% residual is accounted for by 6-bit DAC quantization and thermal crosstalk"`).
5. **Beat 5: Discriminating Control / Design Takeaway**: Close with the ablation or physical takeaway that bridges to the next panel (`"Turning off heater phase diversity drops accuracy to 51.2%, confirming that the optical slab performs the discriminative projection rather than the electronic readout"`).

---

## 2. How to Revise an Existing Draft (4-Pass Surgery)

### Pass 1: Invert Plot-Tour Sentences into Claim-First Sentences
- Hunt down every sentence starting with `"Figure 2b presents..."`, `"As can be seen in Fig. 3a..."`, or `"Next, we measured..."`.
- Rewrite so the **physical result is the grammatical subject**, followed by the measured value and `(Fig. X)`.

### Pass 2: Enforce Measured-vs-Simulated Separation & Statistical Rigor
- Flag any accuracy or FOM missing `n`, uncertainty (`+- s.d.`), or held-out split definition.
- Tag every simulated or hardware-emulated curve explicitly in the sentence where it first appears (`"solid curves, FDTD simulation; symbols, measured data"`).
- Add the missing physical cause whenever experiment deviates from simulation.

### Pass 3: Native High-Register Precision & Concrete Before -> After
- Upgrade weak verbs (`give`, `make`, `change`, `cause`) -> `impart`, `decouple`, `dictate`, `yield`, `attain`, `account for`, `govern`.
- **Before (Lab-Diary / Weak Results Paragraph)**:
  > *"Figure 2b shows the measured transmission versus heater power. As can be seen, when we increase the power, the phase changes and we achieve a pi phase shift at 18 mW. Moreover, the error is small. Figure 2c shows the matrix multiplication result, which is very close to the ideal values. Notably, this proves our device works well."*
- **After (T1/T2 Claim-First Results Paragraph)**:
  > *"Each thermo-optic slot imparts a full pi phase shift at 18.2 +- 0.4 mW (n = 64 heaters; Fig. 2b), with thermal crosstalk between adjacent channels kept below -18 dB by deep isolation trenches. Across 100 random 4x4 weight matrices, hardware matrix-vector multiplication yields a normalized root-mean-square error of 2.1% (6.1-bit effective precision; Fig. 2c), on par with the 1.8% limit dictated by 12-bit DAC quantization and photodetector shot noise. Disabling heater modulation collapses output separability to chance level (Supplementary Fig. 4), confirming that linear mixing occurs in the optical domain."*

### Pass 4: Mandatory CLI Verification Gate
```bash
python3 scripts/pnn_results_tool.py lint path/to/results.txt
python3 scripts/pnn_results_tool.py query --tier T1 --native-only --top 3
```

---

## 3. Compact Pass/Fail Checklist
- [ ] `3-5` descriptive noun-phrase subheadings mapped 1:1 to main figures.
- [ ] Every paragraph opens with a physical claim (not a generic plot description).
- [ ] Every headline result includes uncertainty/sample size (`n`), matched baseline, and residual cause.
- [ ] Measured hardware, simulation, and emulation are never conflated.
- [ ] At least one explicit physics ablation proves optics is doing real computational work.

## 4. References & CLI
- Native-weighted exemplars: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_results_corpus.jsonl`](./references/t1t2_results_corpus.jsonl) (`49` native-primary `weight=2.0` sorted first).
