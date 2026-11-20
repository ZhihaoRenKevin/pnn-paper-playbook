---
name: pnn-t1t2-si
description: Actionable T1/T2 PNN Supplementary Information (SI) and Extended Data (ED) architecture, drafting, and revision playbook calibrated exclusively on 100 full T1/T2 Research SI documents and 145 Extended Data captions (2.0x native-English-country weighting; zero T3/T4 dilution). Use whenever structuring, writing, or auditing a PNN Supplementary Information Word/LaTeX package.
---

# How to Architect and Revise T1/T2 Supplementary Information (`pnn-t1t2-si`)

Use this skill to turn SI from an unorganized dump of extra plots into a **referee-proof verification fortress** (`T1` typical `25-45` pages / `12-20` Supp Figs; `T2` typical `15-28` pages / `8-15` Supp Figs).

---

## 1. How to Structure SI From Scratch (Canonical Front-to-Back Blueprint)

1. **Page 1-2: Clickable Front Table of Contents**: List every `Supplementary Note`, `Supplementary Figure`, and `Supplementary Table` with exact page numbers.
2. **Supplementary Note 1: Device Physics, Mathematical Model & Mesh Convergence**: Governing transfer equations, eigenmode/FDTD grid & boundary convergence proof, fabrication tolerance sensitivity.
3. **Supplementary Note 2: Fabrication Flow & Hardware Characterization**: Wafer stack, process recipe, optical/SEM inspection across chips, insertion-loss breakdown.
4. **Supplementary Note 3: Calibration, Thermal/Optical Crosstalk & Drift Stability**: Individual channel phase-power curves, full crosstalk matrix, long-term drift logs, error-bar provenance.
5. **Supplementary Note 4: Complete 4-Tier Energy, Latency & Scaling Budget**: Full equations + `Supplementary Table 1` (Measured vs Projected breakdown) + `Supplementary Table 2` (Comprehensive All-Tier Competitor Comparison with exact boundaries and citations).
6. **Supplementary Note 5: ML Training Protocols, Hyperparameters & Ablation Controls**: Dataset splits, zero-leakage confirmation, multi-seed distributions, untrained-core / linear-only / readout-only ablation controls.
7. **Final Section: Numbered Supplementary References**: Always at the very end of the SI document.

---

## 2. How to Revise an Existing SI Package (4-Point Hygiene Surgery)
1. **Cross-Reference & Number Sync**: Verify every `Supplementary Note X`, `Supplementary Fig. Y`, and `Supplementary Table Z` cited in Main Text exists with the **exact same number, unit, and color palette** in SI.
2. **Purge Internal Artifacts**: Delete raw DOI tables, `.py`/`.csv`/`.fsp`/`.mph` filenames, unformatted terminal screenshots, and undefined internal acronyms.
3. **Word Formatting Compliance**: Bold collapsible `Heading 1`/`Heading 2` styles, justified body text, zero horizontal lines under equations, clickable TOC on page 1.
4. **Run the Automated SI Blueprint & Audit Gate**:
```bash
python3 scripts/pnn_si_tool.py plan --tier T1 --platform diffractive
python3 scripts/pnn_si_tool.py audit path/to/si_draft.md
python3 scripts/pnn_si_tool.py query --tier T1 --native-only --top 3
```

---

## 3. Compact Pass/Fail Checklist
- [ ] Clickable TOC upfront; numbered SI references at the very end.
- [ ] Dedicated notes for calibration/crosstalk, 4-tier energy/latency budget, and physics ablations.
- [ ] Measured and projected competitor numbers cleanly separated in `Supplementary Table`.
- [ ] Zero broken cross-references, zero internal filenames, 100% number/color sync with Main Text.

## 4. References & CLI
- Native-weighted SI blueprints: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_si_corpus.jsonl`](./references/t1t2_si_corpus.jsonl) (`41/100` native-primary `weight=2.0` sorted first).
