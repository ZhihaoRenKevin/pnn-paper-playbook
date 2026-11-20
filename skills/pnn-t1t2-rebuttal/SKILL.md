---
name: pnn-t1t2-rebuttal
description: Actionable T1/T2 PNN Peer-Review Defense and Point-by-Point Rebuttal drafting and revision playbook calibrated on 12 full published T1/T2 Transparent Peer Review files (195k words, 132 T1/T2 comments, 2.0x native-English-country weighting) plus a live ALL-TIER referee-intelligence bridge (2,241 Nature-Portfolio comments & 146 named PNN referees). Use whenever planning revisions or writing point-by-point responses to Nature/Science referees.
---

# How to Plan and Write a Winning T1/T2 PNN Rebuttal (`pnn-t1t2-rebuttal`)

Use this skill to convert harsh T1/T2 referee reports into **Accept** decisions using concrete evidence rather than flattery or defensive arguments.
- **Rebuttal craft**: Strictly T1 & T2 Transparent Peer Reviews (`12` full files, `6/12` native-primary `US/GB/CA` `weight=2.0`).
- **Referee & attack intelligence**: ALL TIERS (`2,241` comments & `146` named referees) via `scripts/pnn_rebuttal_tool.py referee-intel`.

---

## 1. How to Write Every Point-by-Point Response (The 5-Beat T1/T2 Rebuttal Block)

Never answer a major technical objection with prose promises alone (`"we believe..."`, `"we will add..."`). Execute these 5 beats for every comment:
1. **Quote Verbatim**: Paste the exact `Reviewer X, Comment Y` verbatim (never paraphrase away the hard part).
2. **1-Line Direct Action Verdict**: State clearly what you did in present perfect (`"We thank the reviewer for raising this point. We have performed the requested untrained-core ablation experiment and added the full 4-tier energy accounting table."`). No grovelling (`"insightful"`, `"brilliant"`).
3. **Physical Explanation + Concrete New Evidence**: Provide the new measured data, ablation curve, equation derivation, or head-to-head GPU/competitor benchmark directly inside the response letter (inline mini-table or embedded figure).
4. **Honest Scope or Respectful Disagreement (When Needed)**: If a reviewer asks for something outside physical scope or misreads a prior paper, concede the valid premise concisely (`albeit`, `given that`), then present the quantitative physics showing why your regime is distinct: firm, polite, zero defensiveness.
5. **Exact Verbatim Diff + Page/Line Pointers**: Paste the revised manuscript text in quotes (highlighted/red) with exact locations (`Page 6, Lines 182-198; Fig. 3d; Supplementary Note 4, Table S2`).

---

## 2. How to Handle the Top 5 T1/T2 Kill-Shot Referee Attacks

| Referee Attack Code | Winning T1/T2 Evidence Move (Not Just Text!) |
|---|---|
| **`C5` Optics vs Electronics Doing the Work** | Run & plot the **Untrained-Core** and **Readout-Only** ablation controls side-by-side (`Fig. 3d`), plus count exact optical vs electronic FLOPs |
| **`C8` Unfair GPU/ASIC Comparison** | Add a matched-precision (`ENOB` = `INT4/INT8`), matched-batch benchmark against a named GPU (`A100/H100/Orin`) + derive crossover dimension `N*` |
| **`C2` Energy / Latency Boundary Cherry-Picking** | Add a **4-Tier Energy Table** (Optical Core -> Chip -> DAC/ADC I/O -> Wall-Plug) and full latency waterfall in Supplementary Note + Table S1 |
| **`C1` Missing Prior Art / Novelty Challenge** | Cite the reviewer's suggested papers fairly, add them into your comparative benchmark table, and demonstrate quantitative orthogonality on >=2 axes |
| **`C3/C4` Stability, Drift, Endurance, Yield** | Measure multi-hour drift, repeated cycling, or multi-chip variance (`n >= 3-5` devices) and quantify accuracy retention under perturbation |

---

## 3. Concrete Before -> After Rebuttal Rewrite
- **Before (Weak / Defensive / Unbacked Reply)**:
  > *"We thank the reviewer for this very insightful comment. We acknowledge that DAC/ADC power is important, and we do not claim our small prototype replaces a full GPU. We will address electrical overhead in future work, and we have briefly mentioned this limitation in the Discussion."*
- **After (Winning T1/T2 Native-Grade Reply)**:
  > *"We thank the reviewer for highlighting electrical I/O overhead. To quantify this contribution explicitly, we have measured the power draw of our 12-bit DAC array, TIA/ADC readout, laser wall-plug input, and thermo-optic heaters, and added a complete 4-tier energy accounting breakdown in Supplementary Note 4 (Supplementary Table 2). Within the optical core, matrix multiplication requires 0.34 pJ/MAC; including all off-chip electrical I/O yields 1.8 TOPS/W in the current N = 32 prototype, whereas scaling to N = 256 with 3D CMOS co-packaging amortizes I/O overhead to a projected 42 TOPS/W. We have updated the Main Text (Page 7, Lines 210-224) to report both boundaries explicitly: '[exact quoted revision]'."*

### Mandatory CLI Verification & All-Tier Intelligence Gate
```bash
python3 scripts/pnn_rebuttal_tool.py query-t1t2 --concern C8 --native-only --top 3
python3 scripts/pnn_rebuttal_tool.py referee-intel --topic diffractive --concern C5 --top 5
python3 scripts/pnn_rebuttal_tool.py lint path/to/rebuttal_draft.md
```

---

## 4. Compact Pass/Fail Checklist
- [ ] Every comment is quoted verbatim and answered in present perfect (`have added/measured`), zero future promises (`we will`).
- [ ] Every major technical attack is answered with new data, derivation, or table: never prose-only hand-waving.
- [ ] Exact Page/Line/Figure/Note pointers and verbatim revised quotes accompany every revision.
- [ ] Polite, calm, authoritative tone: zero flattery (`insightful`), zero defensive grovelling, zero em-dashes.

## 4. References & CLI
- T1/T2 winning defenses (`6/12` native-primary `weight=2.0` sorted first): [`references/t1t2_winning_rebuttals.md`](./references/t1t2_winning_rebuttals.md), [`references/t1t2_rebuttal_distill.jsonl`](./references/t1t2_rebuttal_distill.jsonl), and [`references/t1t2_pr_comments_132.jsonl`](./references/t1t2_pr_comments_132.jsonl).
