# PNN Empirical Writing Templates (`writing_templates.md` — `v3`)

> Companion reference to `SKILL.md §§2–5, §8–9` and `08_Reading_Notes/Writing_patterns_v2.md` (`n = 1,447` cleaned papers across `T1–T4`). Use these structural blueprints to assemble section drafts; polish the final sentence-level wording in your own voice.

---

## 1. Title Blueprints by Claim Class & Target Tier

| Archetype | Target Tier | Structural Pattern | Verified In-Library Exemplars |
| :--- | :---: | :--- | :--- |
| **A. Category Coinage** | `T1` | `[Adjective/Domain] [New Computing Paradigm] [Models/Processors]` (`3–6` words) | *Optical generative models* (`Nature_25V644_903`); *Universal linear optics* (`Science_15V349_711`) |
| **B. Object + Enabling Mechanism** | `T1–T2` | `[Architecture/Network] trained with / enabled by [Physical Mechanism]` (`7–9` words) | *Deep physical neural networks trained with backpropagation* (`Nature_22V601_549`); *Fully forward mode training for optical neural networks* (`Nature_24V632_280`) |
| **C. Sentence Claim (Overturned Wisdom)** | `T1–T2` | `[Counter-intuitive Physical Property] [enhances/enables] [Computing Function]` (`6–9` words) | *Partial coherence enhances parallelized photonic computing* (`Nature_24V632_55`) |
| **D. Hardware + Capability** | `T1–T2` | `[Platform/Chip] for [High-Speed/Large-Scale Task]` (`7–10` words) | *All-analog photoelectronic chip for high-speed vision tasks* (`Nature_23V623_48`); *Large-scale photonic chiplet Taichi empowers 160-TOPS/W artificial general intelligence* (`Science_24V384_202`) |
| **E. Single Sharp Metric / Regime** | `T2–T3` | `[Architecture] using/achieving [Metric Defining New Physical Regime]` (`9–12` words) | *An optical neural network using less than 1 photon per multiplication* (`Nature Communications_22V13_123`) |

---

## 2. Seven-Sentence Abstract Blueprint (`T1–T3` Median = `7` Sentences, `165–178` Words)

1. **Sentence 1 (Domain Context):** State the computational bottleneck (`O(N^2)` matrix scaling, ADC/DAC wall-plug power, or latency in real-time sensing/communications) without generic AI hype.
2. **Sentence 2 (Specific Technical Gap):** `"However, existing photonic processors remain constrained by [specific physical bottleneck: e.g., volatile thermal weights / offline digital gradient computation / O-E-O conversion latency]."`
3. **Sentence 3 (`"Here we"` Anchor):** `"Here we demonstrate [SYSTEM/ARCHITECTURE], a [platform + core physical mechanism] that [primary capability]."`
4. **Sentence 4 (Physical Mechanism):** Explain how the optical field, material state, or multiplexing dimension performs the mathematical operation in hardware.
5. **Sentence 5 (Device/Primitive Metric + Baseline):** Report the measured hardware primitive figure of merit alongside its theoretical or digital reference (`"achieving [X]-bit effective precision ([Y] levels) at [Z] Gbaud"`).
6. **Sentence 6 (System Benchmark + Dual Operating Points):** Report task-level experimental performance with its comparator (`"On [Task], the processor reaches [A]% experimental accuracy ([B]% numerical model) at [C] TOPS and [D] pJ/MAC ([core_optical / wall_plug_system] boundary)"`).
7. **Sentence 7 (Hedged Significance):** State the concrete system regime or scaling horizon unlocked by the demonstration.

---

## 3. Four-Paragraph Introduction Funnels (`T1` Median = `4` Paragraphs, `538` Words)

### Funnel 1: Architectural / Energy Bottleneck (`40.0%` of `T1`)
- **¶1 (Compute Demand & Photonic Promise):** Contrast electronic data-movement energy (`~1–10 pJ/MAC` interconnect/memory) against passive optical propagation, citing landmark coherent (`MZI`), wavelength-multiplexed (`MRR`/`PCM`), and free-space (`diffractive`/`metasurface`) demonstrations.
- **¶2 (The Unsolved Bottleneck):** Pinpoint why prior demonstrations hit a scaling wall (e.g., `O(N^2)` insertion loss and footprint in deep meshes, ADC/DAC conversion dominating `>80%` of system power, or lack of non-volatile multi-bit memory).
- **¶3 (`"Here we"` & Physical Principle):** Introduce the proposed architecture, explicitly stating the dimensional mapping (wavelength, space, time, mode, or RF subcarrier) and how it bypasses the ¶2 bottleneck.
- **¶4 (Quantitative Verification Summary):** Summarize the experimental hardware scale, calibration/training protocol, benchmark tasks beyond toy MNIST, and measured throughput/energy across defined system boundaries.

### Funnel 2: Missing Physical Primitive / Training Paradigm (`28.9%` of `T1`)
- **¶1:** Frame the gap between inference-only optical accelerators and full neural execution (missing on-chip nonlinearity, in-situ gradient propagation, or hardware-native forward learning).
- **¶2:** Politely critique the `1–3` closest prior approaches (e.g., digital twin mismatch in offline training, slow coordinate-descent perturbation, or high threshold power in bulk optical nonlinearities).
- **¶3:** Present the physical primitive or in-situ training rule and prove its mathematical equivalence or convergence bound.
- **¶4:** Summarize hardware convergence, perturbation recovery, and multi-task benchmarks.

---

## 4. Results Section Opening & Ablation Blueprints

- **Subsection 1 (`Principle and device architecture`):** Open with the mathematical operator implemented by the physical system ($\mathbf{y} = \mathbf{U}\mathbf{x}$ or $\mathbf{y} = \sigma(\mathbf{W}\mathbf{x})$), map each matrix variable to a physical degree of freedom, and specify fabrication stack and footprint.
- **Subsection 2 (`Unit-cell / primitive characterization`):** Report measured transfer curves, insertion loss (`dB`), extinction ratio (`dB`), crosstalk (`dB`), programming speed (`ns`/`µs`/`GHz`), endurance cycles, and `N_eff` bit precision (`LSB`/`ENOB` from `N >= 100` random weight trials).
- **Subsection 3 (`Experimental task execution & physics ablations`):** Pair every hardware confusion matrix and accuracy with (i) the ideal floating-point baseline, (ii) the hardware-calibrated digital emulation, and (iii) the **physics ablation control** (optical core bypassed/randomized or pump off -> chance accuracy).
- **Subsection 4 (`System throughput, latency, and energy accounting`):** Decompose power and latency into optical core, laser source, DAC/ADC driver/readout, and total system wall-plug boundaries (`Table S1 Measured` vs `Table S2 Projected`).

---

## 5. Point-by-Point Referee Rebuttal Block (`R1–R10` Tactics)

```markdown
> **Referee #X, Comment Y (`[C-code]`):** "[Verbatim referee comment]"

**Response:** We thank the Referee for this insightful assessment. [1-sentence direct answer stating whether a new experiment (R1), numerical simulation (R2), comparison table (R3), or scope/limitation revision (R4/R5) was performed.]

1. **Physical / Quantitative Evidence:** [State the exact new measurement, derivation, or 4-tier energy breakdown with page/figure pointers.]
2. **Comparison with Prior Art / Baseline:** [Insert concise markdown comparison table matching wavelength, platform, scale, energy boundary, and experimental vs simulated status.]
3. **Manuscript Revisions:** We have updated **[Section X, Page Y, Lines Z]** and added **[Supplementary Note / Figure SX]** (`"verbatim added text"`).
```
