---
name: pnn-t1t2-editorial-audit
description: Actionable T1/T2 PNN Editorial Story-Elevation, Realistic Tier-Fit, and 16-Point Pre-Submission Full-Manuscript Gatekeeper calibrated exclusively on 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 dilution). Use BOTH before drafting (to elevate framing and pick the realistic journal tier) and before submission (to audit the complete Main + SI package).
---

# How to Elevate Story Framing & Run a T1/T2 Pre-Submission Audit (`pnn-t1t2-editorial-audit`)

Use this skill at **two critical checkpoints**: (1) **Before drafting**, to stress-test your realistic journal tier and sharpen the headline physical story; and (2) **Before submission**, to catch desk-reject flaws across Main Text, Figures, Methods, and SI.

---

## 1. Checkpoint A (Before Drafting): Pick Your Realistic Tier & Elevate the Story

### Step 1: Run the Objective Tier-Fit Test First
```bash
python3 scripts/pnn_editorial_audit_tool.py tier-fit \
  --claim-class B --measured-e2e --ablation --real-task --gpu-bench --novel-mechanism
```
- **Target T1 (*Nature* / *Science*)** ONLY if you have: (a) a genuine physical paradigm inversion or new scaling regime, (b) end-to-end measured hardware on a non-trivial task, (c) explicit physics ablations proving optics does real work, AND (d) honest 4-tier energy/latency comparison vs a named GPU/ASIC.
- **Target T2 (*Nature Photonics* / *Nature Electronics* / *Nature Nanotechnology* / *Nature Computational Science*)** if you have a decisive device/platform/training breakthrough with clean hardware benchmarks and honest scaling boundaries.
- **Target T3 (*Nature Communications* / *Science Advances*)** if the core advance is a strong metric improvement, compact integration, or clean single-chip demonstration without full system-level GPU beat.

### Step 2: Apply 1 of 3 Proven T1/T2 Story-Elevation Moves (Without Overclaiming!)
1. **Bug-to-Feature Inversion**: Turn a conventional nuisance (e.g., partial coherence, multimode interference, thermal coupling, slab diffraction) into the exact degree of freedom that unlocks parallelism or footprint compression.
2. **Bottleneck Kill-Shot**: Frame your chip not as `"another photonic NN"`, but as the direct physical solution to one specific scaling wall (e.g., eliminating deep MZI cascade loss, breaking O-E-O ADC overhead, or removing static heater power).
3. **Orthogonal Synergy**: Show two independent physical controls cleanly decoupled on the same chip (e.g., fast EO encoding + non-volatile/TO weighting) with quantitative proof of zero mutual degradation.

---

## 2. Checkpoint B (Before Submission): 16-Point Desk-Reject Gatekeeper

Run the automated full-manuscript audit first, then clear every red flag manually:
```bash
python3 scripts/pnn_editorial_audit_tool.py full-audit path/to/manuscript.md --tier T1
```

### The 16 Pass/Fail Gates (Fix Every Failure Before Submitting!)
1. **Colon-Free Concise Title**: `<=10` words (T1) or `<=12` words (T2), zero colons, zero unmeasured numbers.
2. **7-Sentence Abstract Discipline**: `145-210` words; S2 physical gap; S3 `"Here we"` anchor; S5-S6 metrics paired with baselines & boundaries.
3. **Lean Introduction (`420-680w`)**: Zero `"In recent years"` filler, zero TOC roadmap paragraph, diplomatic prior-art credit to likely referees.
4. **Claim-First Results Subheadings**: `3-5` noun-phrase subheadings mapped 1:1 to main figures.
5. **Measured vs Emulated Separation**: Zero conflation of hardware-calibrated simulation with physical chip execution.
6. **Physics Ablations in Main Text**: `>=2` controls (Untrained-Core, Linear-Only, Offline-vs-In-Situ, Readout-Only) proving optical contribution.
7. **4-Tier Energy & Full Latency Accounting**: Optical Core, Chip, Electrical I/O, and Wall-Plug boundaries stated cleanly.
8. **Fair Electronic Comparator**: Named GPU/ASIC at matched precision (`ENOB`), batch size, and task + crossover `N*`.
9. **Visual Color & CVD Safety**: Muted 3D materials, refined T1/T2 curves, consistent `#HEX` across Main + SI, Machado `Delta-E >= 15`.
10. **Exact Journal Caption Syntax**: `Fig. N |` + `a,` (Nature) or `Fig. N.` + `(A)` (Science), noun-phrase title, scale bars, error-bar `n`.
11. **Clean Panel Arrangement**: `4-6` panels per figure (`<=8` max), clear hero panel (`30-50%` area), Z-pattern order.
12. **Journal-Exact Closing Heading & Limitations**: Separates laboratory packaging from fundamental physics; links every limit to a labeled projected fix.
13. **Reproducible Methods**: Exact wafer/fab, instrument models, zero-leakage train/test split, equations, Data/Code availability.
14. **Synchronized SI Package**: Clickable TOC, zero internal filenames, 100% number/color/reference alignment with Main Text.
15. **Low-AIGC, Non-Defensive Native Prose**: Run `low-aigc-nondefensive-writing` `audit` (`AIGC < 20`, `Defensiveness < 15`) and `vocab-upgrade` (`Native Register >= 80`, zero em-dashes).
16. **Clean Technology Naming**: Pronounceable 1-2 syllable short form, collision-checked across `6,490` papers (`sci-tech-naming`), one canonical spelling everywhere.

---

## 3. References & CLI
- Desk-accept framing models (`49` native-primary `weight=2.0` sorted first): [`references/t1t2_desk_accept_exemplars.md`](./references/t1t2_desk_accept_exemplars.md) and [`references/t1t2_editorial_hooks.jsonl`](./references/t1t2_editorial_hooks.jsonl).
