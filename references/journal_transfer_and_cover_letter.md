# PNN Journal Selection, Transfer Cascade, Cover Letter & Appeal Playbook (`journal_transfer_and_cover_letter.md`)

> **Empirical Basis**: Distilled from `1,471` published PNN papers across `T1` (`46`), `T2` (`126`), `T3` (`351`: *NC* `208`, *Sci. Adv.* `69`, *Adv. Mater.* `71`, *PNAS* `3`), and `T4a–T4d` (`948`), plus `191` Peer-Review files (`188` active + `3` *Nature* portfolio transfer notices).

---

## 1. Journal-by-Journal Editor & Referee Taste Matrix (`T1` to `T4b`)

| Tier & Journal | IF Bracket & Weight (`score / visual`) | What the Handling Editor Demands to Send Out for Review | Fatal Desk-Reject Triggers | Median Review Time (`Received → Accepted`) |
| :--- | :---: | :--- | :--- | :---: |
| ***Nature* / *Science*** (`T1`) | Top Flagship (`1.00 / 1.00`) | **A field-redefining conceptual surprise or system-scale milestone**: e.g., $>10,000$ components (`Nature_25V640_361`), commercial 3D CMOS-photonic tensor chip (`Nature_25V640_368`), model-free physical backpropagation (`Science_23V380_398`, `Nature_26V651_927`), or counter-intuitive wave physics (`Nature_24V632_55` partial coherence). | Incremental density/footprint improvement; single toy dataset (`MNIST`/`Iris` only); simulation-only or uncalibrated hardware emulation. | **278 days** (IQR `226–327 d`) |
| ***Nature Photonics*** (`T2`) | `IF ≈ 32–40` (`0.70 / 0.85`) | **Decisive optical physics / photonic integration mechanism + rigorous optical characterization**: novel wave-mixing operator, TFLN/PCM/microcomb material-device breakthrough, or first-of-its-kind on-chip optical processor with full spectrum/phase/loss calibration. | Pure ML wrapper around a standard foundry component without new optical physics; missing insertion loss / $Q$ / phase stability data. | **240 days** (IQR `181–283 d`) |
| ***Nature Electronics*** (`T2`) | `IF ≈ 34` (`0.70 / 0.85`) | **Complete optoelectronic system integration**: co-packaged or clearly accounted CMOS drivers/TIAs/ADCs, wall-plug energy/area efficiency (`TOPS/W`, `TOPS/mm²`), and real-world system workload (telecom equalization, radar, vision). | Ignoring electronic peripheral power (`DAC/ADC/TIA` wall) or reporting only passive optical core fJ/MAC. | **248 days** (IQR `195–290 d`) |
| ***Nature Machine Intelligence* / *Nature Computational Science*** (`T2`) | `IF ≈ 18–24` (`0.70 / 0.85`) | **Algorithmic / training paradigm innovation for physical hardware**: physics-aware training, in-situ gradient estimation, noise-exploiting Bayesian/probabilistic computing, or non-trivial operator learning with rigorous ML baselines. | Weak ML baselines (`Iris`/`MNIST` without modern digital comparison, missing train/val/test hygiene or error bars across random seeds). | **190–215 days** |
| ***Nature Communications* / *Science Advances*** (`T3`) | `IF ≈ 14–16` (`0.45 / 0.55`) | **One sharp architectural, material, or training capability backed by clean hardware experiments** + complete multi-column comparison table (`Table 1`) + honest limitations. | Simulation-only claims dressed as hardware (`0%` conversion rate when challenged by NC referees); missing ablation of the optical core. | **200 days** (IQR `152–260 d`) |
| ***Advanced Materials* / *PNAS*** (`T3`) | `IF ≈ 27.4` / NAS (`0.45 / 0.55`) | **For *Adv. Mater.***: Material/device innovation (ferroelectric, 2D van der Waals, perovskite, chalcogenide PCM, or reconfigurable metasurface) enabling in-sensor or neuromorphic photonic computing.<br>**For *PNAS***: Broad interdisciplinary physics + computing significance. | Lack of material/structural characterization (`TEM`/`XRD`/`XPS`/`SEM`/`Raman`) for *Adv. Mater.*; narrow specialist framing for *PNAS*. | **140–185 days** |
| ***Nano-Micro Letters* / *The Innovation*** (`T4a`) | `IF ≥ 30` (`0.40 / 0.45`) | High-impact nano-optoelectronic/photonic device + system application with exceptionally rich multi-panel figures (`Fig. 1` 3D architecture + 6–8 comprehensive characterization/benchmark panels) and a thorough SOTA benchmarking table. | Sparse figures ($<4$ panels per figure) or missing device-to-system application bridge. | **110–150 days** |
| ***Light: Science & Applications* / *eLight* / *Advanced Photonics* / *OEA* / *InfoMat*** (`T4b`) | `20 ≤ IF < 30` (`0.35 / 0.40`) | High-visibility optics/photonics engineering advance: high-density diffractive/metasurface processor, WDM/microcomb computing, or integrated photonic synapse with strong optical FOMs. | Unclear optical mechanism or poor visual presentation. | **145–175 days** (*LSA* median `168 d`) |

---

## 2. Cascade & Transfer Playbook (When Desk-Rejected or Post-Review Transferred)

Across the `191` Peer-Review files, **31%** of *Nature Communications* and *Nature Photonics* papers originated as transfers from *Nature*, *Science*, *Nature Photonics*, or *Nature Electronics*. Follow these rules when transferring:

1. **Never Transfer Blindly After a Desk Reject Without Reframing the Opening 3 Paragraphs**:
   - **Moving *Nature* $\to$ *Nature Photonics***: Shift the Abstract and Introduction opening from broad AI scaling clichés to the **specific optical wave-mixing / light–matter interaction mechanism** in Sentence 1–2. Move detailed ML task extensions to `Fig. 4–5` and elevate the optical transfer matrix, phase/thermal mechanism, and loss/bandwidth characterization into `Fig. 2–3`.
   - **Moving *Nature Photonics* / *Nature Electronics* $\to$ *Nature Communications* / *Science Advances***: Add an explicit **6–8 column positioning table (`Table 1`)** in the main text or Discussion (`R3`), tone down universalist adjectives into exact quantitative regimes (`R4`), and ensure all **5 Mandatory Hardware Ablation Controls** (`experimental_ml_benchmarks.md §1`) are visible.
   - **Moving *Nature* Portfolio $\to$ *Advanced Materials* / *Light: Science & Applications* / *Nano-Micro Letters***: Expand the material/fabrication characterization (`SEM`, layer stack, switching/thermal physics) and include a `Fig. 1` quantitative positioning chart (`radar` or `log–log scatter`) alongside the 3D schematic.

2. **How to Win an Appeal on a Split-Decision Reject (`18%` Published Over a Final Referee Reject)**:
   - Editors at *Nature Photonics*, *Nature Electronics*, and *Nature Communications* **never** grant an appeal based on rhetorical disagreement (`R8` has the lowest success rate in the corpus: `68.2%`).
   - Successful appeals always follow the **3-Part Empirical Appeal Formula**:
     1. **Immediate Concession on Scope (`R4` + `R5`)**: Accept the rejecting referee's terminology boundary (e.g., replace `"all-optical"` with `"optoelectronic"`, replace `"held-out generalization"` with `"fixed-partition in-situ optimization"`, or scope energy claims to `"core optical vs. wall-plug"`).
     2. **One Decisive New Physical Control / Ablation (`R1` / `R2`)**: Provide the actual plot or table requested by the referee right inside the appeal letter (e.g., `cold-core vs. trained-core` ablation, `slot vs. slab` thermal-optical comparison, or `4-level energy breakdown table`).
     3. **Point-by-Point Consensus Map**: Show that Referees #1 and #2 are fully satisfied and that Referee #3's remaining technical question has now been answered with concrete data rather than argument.

---

## 3. High-Conversion Cover Letter Structure (5-Paragraph Discipline, $\le 450$ Words)

Write it naturally and directly (no AI clichés, no em-dashes):
1. **Paragraph 1 (Submission & Quantitative Headline, 2–3 sentences)**: State manuscript title, target journal, article type, and the single sharpest physical capability with its core numbers.
2. **Paragraph 2 (The Concrete Bottleneck in Prior Art, 3–4 sentences)**: Name the exact trade-off in existing photonic/electronic processors (citing 3–4 recent T1/T2 landmarks by author/year/venue) that remained unresolved.
3. **Paragraph 3 (How This Work Solves It + Hardware Proof, 4–5 sentences)**: Summarize the physical mechanism, fabricated chip scale, calibration fidelity, and hardware benchmark results (explicitly pairing hardware scores with digital/untrained controls).
4. **Paragraph 4 (Why This Specific Journal Now, 2–3 sentences)**: Connect directly to the journal's readership and recent conversations in that venue.
5. **Paragraph 5 (Ethics, Originality & Suggested/Excluded Reviewers)**: Standard declarations + **4–6 non-conflicting Suggested Reviewers** selected via `python scripts/pnn_research_toolkit.py reviewer-finder`.
