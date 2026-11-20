---
name: pnn-paper-playbook
description: Use for photonic neural network and optical computing research, including planning, writing, illustrating or revising a paper, picking its journal tier, predicting and answering reviewers, and looking up measured device and system parameters, materials, benchmarks, coverage gaps, novelty, grant KPIs and new ideas from a 1,475-paper library.
---

# PNN Paper Playbook (Photonic Neural Networks & Optical Computing — v3.5.0)

> **About the data.** This skill carries no text from the papers or from peer-review files. Each parameter record gives value, unit, status, conditions, page and DOI (`references/citations.csv`), so every number can be checked against the paper. Paths such as `00_Index/`, `08_Reading_Notes/`, `_work/`, `Peer_review_statistics.md` and the audit files under `verification/` refer to the source library the data were compiled from, which is not distributed; sub-commands that need it say so (§19).

## Scope, Corpus & Honest Verification Status
Built from the PNN literature library (`<PNN_LIBRARY_ROOT>/`, see `08_Reading_Notes/README.md` for device paths): **1,475 kept paper cards** (`1475` cards: `1,308` / `1308` research papers + `167` reviews/perspectives, 100% aligned with the `1,475` deduplicated main PDFs across `01_T1`–`04_T4`), **1,109 kept Supplementary Information (`SI`) files** (`1109` SI files on disk: `858` PDF + `251` DOCX; `1,107` linked + `2` pending in `04_T4`), and **194 kept Peer-Review PDFs** (`191` active files containing **2,241** / `2241` verified referee comments [`1,159` Wave-1 + `1,082` Wave-2; **2,216** / `2216` leave-one-out comments excluding the 3 `R18` blind-test targets] + `3` 1-page transfer notices). Only published work in the library was used; unpublished manuscripts and confidential review files were excluded.

- **Folder-Based Tier Structure (`R4`, `[10]` Certified):**
  - **Tier 1 (`01_T1_Nature_Science`):** `44` kept cards (`32` research + `12` reviews) + `27` SI files (`100%` `llm_read_si`).
  - **Tier 2 (`02_T2_Nature_Subjournals`):** `126` kept cards (`83` research + `43` reviews) + `98` SI files (`100%` `llm_read_si`).
  - **Tier 3 (`03_T3_NatCommun_SciAdv`):** `271` kept cards (`268` research + `3` reviews) + `253` SI files.
  - **Tier 4 (`04_T4_IF_ranked`):** `1,034` kept cards (`925` research + `109` reviews) + `723` SI files.
- **Verification Ledgers (`08_Reading_Notes/verification/`):**
  - `verification/t1_pilot_semantic_audit.md` (`44` T1 papers), `verification/sota_77_cells_audit.md` (`77 / 77` SOTA cells verified word-for-word), `verification/factcheck_report_round4.md` (`35` sampled cards × `5` fields = `175` items + `30` sampled referee comments), and `verification/blind_test_predictions.md` (`R18` blind-test predictions on `3` unseen peer-review targets, `10` concrete `[C1]–[C14]` predictions each).

---

## 0. How to use this skill
- **Scope:** story, structure, figures, materials choice, novelty positioning, benchmarking, journal choice and reviewer strategy for PNN / optical-computing papers: integrated MZI/MRR/PCM/TFLN chips, diffractive and free-space optics, metasurface analog computing (differentiation, equation solving), meta-optic front ends, reservoir/spiking/physical-NN training, photonic tensor cores, Ising machines, in-sensor computing.
- **Paths:** every path in this file is relative to the skill folder, the folder that holds this `SKILL.md`. Run the toolkit by its path in that folder, for example `python3 <skill folder>/scripts/pnn_research_toolkit.py --help` (or `python` where that is Python 3). It needs Python 3.8 or later and only the standard library, and it finds its data next to itself whatever the working directory.
<!-- v3.5-t1t2-companion-skills begin -->
- **Dedicated T1/T2 How-to-Write & How-to-Revise Companion Skills (`v3.5.0`, under `skills/`):**
  - **Strict Separation Rule**: Information and factual SOTA lookups (`lit-search`, `atlas`, `materials`, `benchmark`, `sota-table`, `reviewer-finder`) use **all tiers (`T1-T4`, `1,475` papers)** here in the root playbook. Writing, visual, figure, benchmarking-narrative, SI, rebuttal, low-AIGC, and technology-naming craft live in **15 dedicated actionable companion skills** under `skills/`, calibrated strictly on **T1 & T2 research articles (`n = 113`, zero T3/T4 or review dilution, with `2.0x` native-English-country `US/GB/CA/AU` weighting on all writing skills)**:
    - Editorial & Pre-Submission Gatekeeper: `skills/pnn-t1t2-editorial-audit/SKILL.md`
    - Drafting & Revising Sections: `skills/pnn-t1t2-abstract/`, `pnn-t1t2-introduction/`, `pnn-t1t2-results/`, `pnn-t1t2-benchmarking/`, `pnn-t1t2-conclusion/`, `pnn-t1t2-methods/`, `pnn-t1t2-si/`, `pnn-t1t2-rebuttal/`
    - Figures & Data Visuals: `skills/pnn-t1t2-figure-color/`, `pnn-t1t2-figure-caption/`, `pnn-t1t2-figure-arrangement/`, `pnn-t1t2-data-presentation/`
    - Cross-Domain Writing Polish & Tech Naming: `skills/low-aigc-nondefensive-writing/`, `skills/sci-tech-naming/`
<!-- v3.5-t1t2-companion-skills end -->
- **Division of labour:** this skill decides *what* goes where and *why*; sentence-level voice, figure layout and grant or talk framing (§23) belong to your own writing, figure and proposal workflows.
- **Tier weights when rules conflict (`R4.2`):** **T1** (*Nature*, *Science*) `1.00` · **T2** (*Nature* subjournals) `0.70` · **T3** (*Nat. Commun.*, *Sci. Adv.*) `0.45` · **T4** (`04_T4_IF_ranked`) `0.25`. Rules are tagged **[T1]**, **[T1–T2]**, **[T1–T3]** (consensus) or **[T3]/[T4]**.
<!-- v3.4 begin §0 -->
- **Order of use:** idea generation & gap check -> §24 (`idea-gen`, `references/idea_playbook.md`) -> literature search -> §22 (`lit-search`, `related-work`) -> material & device parameter selection -> §20 (`materials`, `atlas`) -> novelty & coverage positioning -> §21 (`coverage`, `atlas`) -> §1 (claim class + tier fit) -> §§2–9 (`references/writing_templates.md`; benchmark selection -> §7.3 `benchmark`) -> platform & training protocols §§16–18 (`references/platform_physics_and_training.md`) -> reviewer pre-mortem §10.3 (`referee-simulator`) -> anti-pattern scan §13 (`draft-linter`) -> tier checklist §14. Answering reviewers -> §10.4 (`references/reviewer_playbook.md`).
<!-- v3.4 end §0 -->

---

## 1. Decide the claim class and the realistic tier first

### 1.1 Claim-Class Taxonomy & Empirical Distribution (`1,308` Research Papers across `A–G` + `167` Reviews; `n = 1,475` Kept Cards)
Every card and JSON record uses the exact `A–G` taxonomy below plus `is_review` (`true` for the `167` Reviews / Perspectives / News & Views):

| Claim class | Kept Cards (`n=1,475`) | Exemplars (Verified In-Library Stems) | Minimum evidence T1/T2 referees demand |
|---|:---:|---|---|
| **A. New computing primitive** | **467** (35.7%) | `Nature_19V569_208` (Feldmann PCM); `Science_15V349_711` (Carolan); `Nature_25V649_330` (McMahon); `Nature Photonics_21V15_541` (Sb2Se3) | Device physics + endurance/drift/levels + one network task on hardware + energy/OP with boundary |
| **B. Architecture / scale-up system** | **325** (24.8%) | `Nature_21V589_44` (Xu 11-TOPS); `Nature_21V589_52` (Feldmann PTC); `Nature_23V623_48` (ACCEL); `Science_24V384_202` (Taichi); `Nature_25V640_361` (PACE) | Measured throughput/latency/energy on real tasks vs named GPU/ASIC at matched accuracy; measured vs projected separated |
| **C. Training paradigm** | **63** (4.8%) | `Nature_22V601_549` (Wright PAT); `Science_23V380_398` (Pai BP); `Science_23V382_1297` (Momeni PhyLL); `Nature_24V632_280` (Xue FFM); `Nature_26V651_927` (Ashtiani) | Comparison vs in silico / PAT / DFA / EP; model-mismatch & drift tests; full training query/energy cost |
| **D. Free-space / diffractive / meta-optic** | **214** (16.4%) | `Science_18V361_1004` (Lin D2NN); `Nature_25V644_903` (Chen OGM); `Science_25V390_1259` (LightGen); `Nature_26V654_917` (MetaExtractor) | Fabrication evidence; experiment vs digital twin; optical operation fraction; misalignment/NA robustness |
| **E. Application-driven system** | **57** (4.4%) | `Nature_20V579_62` (Mennel); `Science_22V378_270` (Netcast); `Nature_24V627_80` (Wang radar); `Science_26V392_eady5344` (Huang Tb/s equaliser) | End-to-end application latency/energy on real signals vs incumbent electronic DSP |
| **F. Physics / limit & Ising** | **61** (4.7%) | `Science_16V354_603` (Inagaki CIM); `Science_23V379_41` (Miller bound); `Nature_24V632_55` (Dong partial coherence); `Nature_25V648_576` (Shastri Hopfield) | Counter-intuitive physical claim + analytical bound + experimental verification |
| **G. Analog math with waves** | **121** (9.3%) | `Science_14V343_160` (Silva); `Science_19V363_1333` (Estakhri IE); `Nature Nanotechnology_23V18_365` (Cordaro); `Nature Photonics_20V14_316` | Measured kernel transfer function vs ideal, NA/bandwidth/efficiency, quantitative image metric |
| **Review / Perspective / N&V** (`is_review = true`) | **167** (11.3% of 1,475) | `Nature_20V588_39` (Wetzstein); `Nature_25V645_53` (Momeni); `Nature Photonics_21V15_102` (Shastri) | Cross-platform taxonomy, honest energy/scaling wall synthesis, multi-decade roadmap |

### 1.2 Tier Fit & Story-Elevation Formulas (`references/figure_archetypes.md §0`)
- **Tier fit [T1–T2]:** a *Nature*/*Science* paper changes what the field believes is possible (system-level capability, or overturned wisdom: `"Partial coherence enhances parallelized photonic computing"`). *Nature Photonics*: decisive mechanism/platform advance plus one convincing system demo. *NC*/*SA*: one sharp capability or metric with clean benchmarking. If the honest headline is `"density only"` or `"simulation only"`, aim at T3/T4.
- **Story-Elevation Formulas:**
  1. **Bug-to-Feature Inversion:** Reframe partial coherence (`Nature_24V632_55`) or multimode disorder (`Nature Computational Science_24V4_429`) from parasitic non-idealities into high-dimensional computational resources.
  2. **Orthogonal Physical Synergy:** Decouple GHz electro-optic input modulation from non-volatile PCM weight storage (`Nature_21V589_52` Feldmann) within the same photonic core.
  3. **System Bottleneck Kill-Shot:** Target the true optoelectronic bottleneck — ADC power wall (`Nature_23V623_48` ACCEL) or deep MZI mesh insertion-loss/footprint scaling (`Science_24V384_202` Taichi).

---

## 2. Titles
Empirical distribution across **1,447** cleaned in-library papers (`Writing_patterns_v2.md` & `references/writing_templates.md`):
- **[T1]** **Median 8 words** (IQR 7–10, range 3–13), no numbers unless defining a new physical regime (`"160-TOPS/W"`, `"2000-node"`, `"200 GOPS"`), stating a system-level capability. Formulas: category coinage (*"Optical generative models"*); object + enabling method (*"Deep physical neural networks trained with backpropagation"*); device + for/with + capability (*"All-analog photoelectronic chip for high-speed vision tasks"*); sentence claim (*"Partial coherence enhances parallelized photonic computing"*).
- **[T2]** **Median 9 words** (IQR 8–11, range 3–17), mechanism explicit (*"Higher-dimensional processing using a photonic tensor core with continuous-time data"*; *"Nonlinear processing with linear optics"*).
- **[T3]** **Median 10 words** (IQR 9–12, ≤12 words), one capability or one sharp metric (*"An optical neural network using less than 1 photon per multiplication"*). **T4** median 11 words (IQR 9–13).
- Connectors: *with / for / using / enabled by*. No stacked adjectives. Never put an unmeasured or projected number in a title.

---

## 3. Abstract
Empirical distribution across **1,447** cleaned abstracts (`Writing_patterns_v2.md` & `references/writing_templates.md`):
- **Length:** **T1** median **7 sentences** (IQR 6–8), **169 words** (IQR 129–204); **T2** median **7 sentences**, **165 words** (IQR 143–195); **T3** median **7 sentences**, **178 words** (IQR 153–204); **T4** median **7 sentences**, **184 words** (IQR 155–211).
- **Moves [T1–T3]:** Context (1–2 S) -> Gap (`"However, ..."`, present in 53.3% of T1 and 60.5% of T3 abstracts) -> `"Here we [demonstrate/report] [NAME], a [one-line definition]"` (73.3% of T1 and 79.3% of T3) -> Mechanism (1 S) -> Results with numbers *and comparators* (80.0% of T1) -> hedged significance.
- Pair every headline number with its baseline (`"92.2% (92.7% theoretical)"`). Give two operating points when there is a trade-off (`Nature Communications_22V13_123` Wang: `99%` at `~3.1 photons/MAC`; `~90%` at `~0.66`). State the evidence type for emulations.

---

## 4. Introduction
Empirical distribution across **1,447** cleaned Introductions (`Writing_patterns_v2.md` & `references/writing_templates.md`):
- **Length:** **T1** median **4 paragraphs** (IQR 3–5), **538 words** (IQR 439–695); **T2** median **4 paragraphs**, **632 words**; **T3** median **5 paragraphs**, **688 words**; **T4** median **5 paragraphs**, **714 words**.
- **Funnels:** (1) compute crisis / CMOS bottleneck -> photonic promise -> *specific* architectural limitation -> `"Here we"` (40.0% of T1); (2) missing physical primitive — no in situ BP, no on-chip activation gradient, no non-volatile low-loss weight (28.9% of T1); (3) received wisdom overturned; (4) application bottleneck — Tb/s fiber nonlinearity, sub-ns RF blind source separation, 2D in-sensor vision (31.1% of T1); (5) formal DOF counting gap.
- **Prior-art etiquette [T1]:** cite whole families in grouped ranges; credit the 1–3 closest competitors individually and criticise them politely and specifically. Novelty and prior-art differentiation (**C1**) accounts for **172 primary referee comments (7.7% primary, 245 any-mention / 10.9% across all 2,241 verified referee comments)** — the competitor you omit is often your referee (§11).

---

## 5. Results architecture
- **[T1]** 3–5 noun-phrase headings (2–9 words), each <-> one main figure: principle/architecture -> characterisation of the primitive (precision, bits, error s.d.) -> tasks easy -> hard -> system benchmark (*"Computing speed and efficiency"*). **[T3]** short topic headings or run-in bold phrases.
- First sentence of each section carries the claim; every chip number sits beside its simulated/digital baseline in the same sentence.
- Statistics: $n$, repeats, $\text{mean} \pm \text{s.d.}$ (or $2\sigma$), fixed test subsets (*"first 1,000 test images, no selection"*), confusion matrices with $n$, LSB/ENOB.
- **Ablations that prove the physics does the work [T1]:**
  - Photonic layer replaced by identity gives chance accuracy (`Nature_22V601_549` Wright PAT);
  - With vs without the optical convolution / metasurface front-end (`Nature_24V632_55` Dong; `Nature_26V654_917` Hu);
  - Optics-only vs electronics-only vs fused optoelectronic execution (`Nature_23V623_48` ACCEL);
  - Laser off / pump off -> no convergence (`Nature_25V640_361` Hua PACE);
  - On-chip backpropagation vs digital offline training over 5 random initialisations (`Nature_26V651_927` Ashtiani);
  - In-situ thermal/mechanical perturbation injection followed by autonomous recovery (`Science_23V380_398` Pai; `Nature_24V632_280` Xue FFM).

---

## 6. Figures
Full figure statistics, color palettes, and layout archetypes across **4,015 figures inspected by `Qwen2.5-VL-7B`** live in `Figure_patterns_v2.md` and `references/figure_archetypes.md`:
- **Hard specifications:** *Nature* family: `89 mm` (1-col) / `183 mm` (2-col) widths, $\le 170\text{ mm}$ height; `5–7 pt` text at print size; **bold lowercase `8 pt` panel letters (`a, b, c`), top-left**; sans-serif (`Arial` / `Helvetica`); RGB; vector line art + `600 dpi` PNG/SVG. *Science*: bold **uppercase** (`A, B, C`). Wiley: `(a)`. Median T1 panel count is **5 panels per figure** (IQR 4–6).
- **Seven Fig. 1 Archetypes (`references/figure_archetypes.md`):**
  - **A. Hero render + pipelines (38% of T1):** `Nature_21V589_44` (Xu); `Nature_21V589_52` (Feldmann); `Nature_23V623_48` (ACCEL); `Science_24V384_202` (Taichi); `Nature_25V644_903` (Chen OGM).
  - **B. Hardware tour -> applications (19% of T1):** `Nature_25V640_361` (Hua PACE); `Nature_25V640_368` (Ahmed Lightmatter); `Nature_25V645_354` (Kalinin AOC).
  - **C. Algorithm-first (19% of T1):** `Nature_22V601_549` (Wright PAT); `Science_23V380_398` (Pai); `Nature_24V632_280` (Xue FFM); `Nature_26V651_927` (Ashtiani).
  - **D. Building block -> architectures (12% of T1):** `Nature_19V569_208` (Feldmann); `Nature Photonics_17V11_441` (Shen); `Nature Photonics_21V15_367` (Zhou DPU).
  - **E. Conventional vs proposed (12% of T1):** `Nature_23V623_48` (ACCEL); `Nature_24V632_55` (Dong); `Science_26V394_212` (Marsh).
  - **F. Math-to-physics strip:** `Science_14V343_160` (Silva); `Science_19V363_1333` (Estakhri); `Nature Communications_22V13_123` (Wang).
  - **G. Positioning + concept [T3]:** `Nature Communications_22V13_1044` (Zhu); `Nature_25V640_361` (Hua Fig. 1g).
- **Canonical Sequences:** **T1** 4–6 dense main figures + 6–10 ED figures, no main-text tables; **T2** 4–5 + SI; **T3** 4–6, comparison table allowed in main text. Every figure = one claim.

---

## 7. Metrics and benchmarking ledger (PNN must-haves)

### 7.1 Headline Measured SOTA Anchors (`references/metrics_sota.md` & `references/Metrics_SOTA_table.xlsx`)
The full **11-Platform × 7-Core-Metric SOTA Summary Table (`77 / 77` verified cells across `56` `llm_read` landmarks)**, the `248`-row `Measured_SOTA` ledger, and the `75`-row `Projected_Simulated_SOTA` ledger live in `references/metrics_sota.md` and `references/Metrics_SOTA_table.xlsx`:
- `MZI`: **40 aJ/MAC** (`core-only`, `Science_22V378_270` p.1); **65.5 TOPS** & **200 ps** ToF (`Nature_25V640_368` p.1, SI p.10); **16 bits** (`Nature Photonics_17V11_441` p.4).
- `MRR`: **345 fJ/OP**, **3.5 TOPS/mm²**, **570 ps** (`Nature_22V606_501` p.7–9); **11.321 TOPS**, **90 wavelengths**, **62.9 GBaud** (`Nature_21V589_44` p.1–9); **8 bits** (`Nature Electronics_21V4_837` p.4).
- `PCM`: **1.2; 162 TOPS/mm²**, **8.1 µs/image**, **5 bits**, **16 wavelengths**, **2 / 13.5 GHz** (`Nature_21V589_52` p.6–10, SI p.19); **0.108 TOPS** (`Nature_24V632_55` p.4–5).
- `TFLN`: **212 GOPS**, **3.3 bits**, **106 GBaud** (`Nature_25V648_576` p.4); **17.5 GOPS/mm²** (`Science Advances_25V11_eadu0228` p.8–9); **244 ns** (`Nature_24V627_80` p.6).
- `diffractive`: **7.48 × 10^4 TOPS/W**, **4.55 × 10^3 TOPS**, **72 ns/frame**, **500 MHz** (`Nature_23V623_48` p.8–9); **447.7 TOPS/mm²** (`Nature Communications_24V15_6189` p.1, p.8); **8 / 16 bits**, **2.20 million neurons** (`Nature Photonics_21V15_367` p.5, p.8).
- `metasurface`: **6.64 × 10^2 TOPS/W**, **3.57 × 10^4 / 2.49 × 10^2 TOPS**, **2.62 × 10^2 TOPS/mm²** (`Science_25V390_1259` SI p.10–11); **41 million meta-atom parameters** (`Nature_26V654_917` p.1).
- `reservoir`: **67.5 fJ/bit**, **1.6 Tbit/s**, **55 ps**, **112 GBaud** (`Science_26V392_eady5344` p.1–10); **8 / 12 bits**, **1,024 spatial macromodes** (`Nature_26V657_377` p.2–10).
- `spiking` / `Ising` / `in-sensor` / `other`: **430 pJ / 710 pJ**, **200 ns**, **15 WDM channels** (`Nature_19V569_208` p.3–8); **2048 DOPO spins** (`Science_16V354_603` p.1); **20 ns**, **9 bits** (`Nature_25V645_354` p.1–5); **2.24 pJ/MAC**, **32 TOPS/mm²** (`Nature Communications_26V17_Single-device in-sensor computing for multi-channel multiply-accumulate operations` p.2, p.6); **0.25 aJ/MAC** (`Nature Communications_22V13_123` p.1).

### 7.2 Mandatory Accounting Rules
1. **Throughput (`OPS`):** define $1\text{ MAC} = 2\text{ OPs}$, call peaks `"peak"`, show exact arithmetic derivation, and report whole-pipeline timing beside the optical-core figure.
2. **Energy (`TOPS/W`, `J/OP`, `photons/MAC`):** state the exact boundary (`core_optical`, `laser_plus_core`, `chip_electrical_io`, or `wall_plug_system`; see §18).
3. **Latency:** per inference, per loop, and end-to-end time-to-solution vs a named processor on the same algorithm.
4. **Precision:** levels -> bits; noise-equivalent bits $= -\log_2(\text{RMS error})$; ENOB/LSB *at the operating speed*.
5. **Measured vs projected:** never mix measured and projected values in the same column (`Table S1 Measured`, `Table S2 Projected`).

### 7.3 怎么选 benchmark (`R13`)
<!-- v3.4 begin §7.3 -->
用 `benchmark --task <任务名> [--platform <平台>]` 查询 `references/derived/benchmark_ledger.csv`（汇总 J 类准确率记录；E1 衍射网络、F1 储备池与 H1 伊辛机的任务指标另存各自类别表），查看各任务在不同平台与期刊分档（`papers_by_tier`）下的实测篇数（`papers_measured`）、仿真篇数（`papers_simulated`）、实测中位数（`measured_median`）及实测极值（`best_measured_text`，带 `best_measured_record_id`）。严禁跨不同任务、不同类别数、不同输入降采样或不同测试子集直接横向比高低；引用任何极值前必须核对 `best_measured_condition` 与原记录中的硬件层数、校准方式及论文自报的同划分数字基线，并在正文中把芯片实测结果与同精度数字基线并列报告。

```text
$ python scripts/pnn_research_toolkit.py benchmark --task Fashion-MNIST --platform MZI
| task | platform | papers | papers_measured | papers_simulated | measured_median | best_measured | best_measured_text | best_measured_record_id | best_measured_stem | best_measured_tier | best_measured_condition | best_measured_calc | papers_by_tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fashion-MNIST | MZI | 3 | 2 | 1 | 90.055 | 95.2 | 95.2% | J-e7770b65f656 | Optica_26V13_1423_Distillation-guided optical neural networks with reinforcement learning-assisted calibration | T4 | Fashion-MNIST on the chip under induced weight misalignment, after PPO online calibration (69.2% without) |  | T3:2;T4:1 |
```
<!-- v3.4 end §7.3 -->

---

## 8. Discussion
- Structure (`Writing_patterns_v2.md` & `references/writing_templates.md`): 1-paragraph summary without repeating abstract numbers -> **honest physical limitations & first scaling bottleneck** (insertion loss dB/stage, ADC/DAC wall, thermal crosstalk, alignment tolerance) -> concrete engineering path to scale (TFLN/BTO electro-optic modulators, non-volatile PCM weights, 3D CMOS co-packaging, WDM comb parallelism) with quantitative projections clearly labeled `[Projected]`.
- Never end with generic hype; end with the concrete system regime unlocked once the stated bottleneck is solved.

---

## 9. Methods, SI and statements
- **Methods subsections:** Device fabrication & foundry stack -> Optical & electrical experimental setup (laser power dBm, modulator/AWG bandwidth, TIA/oscilloscope sampling rate, temperature controller) -> Calibration & training protocol -> Speed and energy accounting ledger (explicit equations for all 4 boundaries) -> Digital baseline implementation & dataset splits.
- **Statements:** Data Availability & Code Availability with public repository DOIs (`Zenodo` / `GitHub` / `CodeOcean`), Ethics/IRB declaration for any human sensor data, Competing Interests (declare startup/patent links).

---

## 10. Reviewer playbook (`194` Kept Peer-Review PDFs / `191` Active Files, `2,241` Referee Comments; `Peer_review_statistics.md` & `references/reviewer_playbook.md`)

### 10.1 What referees attack (`C1`–`C14` across Wave-1 `1,159` + Wave-2 `1,082` = `2,241` Comments; Leave-One-Out `2,216`)
Full tables live in `Peer_review_statistics.md` and `references/reviewer_playbook.md`:
- **Top Primary Concerns (`n = 2,241`):** **C12 Clarity, overclaim & figures** (`17.1%` primary / `26.3%` any) · **C6 Precision, noise, drift & calibration** (`10.5%` / `15.4%`) · **C10 Experimental detail & hw/sim boundary** (`9.9%` / `17.8%`) · **C1 Novelty & prior art** (`7.7%` / `10.9%`) · **C11 Device physics & fab tolerance** (`7.5%` / `13.8%`) · **C14 Theory & derivations** (`7.0%` / `14.1%`) · **C4 Scalability, loss & crosstalk** (`6.6%` / `11.3%`) · **C8 Fair GPU/ASIC comparison** (`6.4%` / `13.1%`) · **C7 Benchmarks** (`5.9%` / `9.7%`) · **C2 Energy boundary** (`5.1%` / `7.7%`) · **C3 Speed/latency** (`4.8%` / `8.8%`) · **C9 Training & ablation** (`4.6%` / `7.1%`) · **C5 Nonlinearity** (`3.9%` / `5.4%`) · **C13 Electronic overhead** (`2.9%` / `8.1%`).
- **Held-Out Calibration & Severity Caveat (`_work/pr_calibration.md`, `R9`):** On unseen `Set B` (`151` comments), concern coding hits `70.86%` exact ($\kappa = 0.6764$) and `91.39%` multi-label inclusion. Automated 3-class severity hits $\kappa = 0.7053$ on `Set A` (`237`) and moderate $\kappa = 0.5020$ on unseen `Set B`; thus **Wave-1 human severity (`major = 50.7%`, `minor = 46.2%`, `editorial = 3.0%`) is the primary reference**, while Wave-2 automated severity (`Combined major = 49.7%`) is an approximate indicator.

### 10.2 Who the referees are and how they move
- **Archetypes:** energy/circuit auditor ~30% (DAC/ADC, memory, latency feasibility, TOPS definitions) · device/integrated-photonics physicist ~30% (loss, $Q$, drift, fabrication) · ML/algorithm referee ~25% (baselines, datasets, training) · free-space/metasurface optics ~15% · reservoir/dynamical ~10% · theory/physics rigour ~10%.
- **What converted rejecting referees:** comparison table + new experiments (`R1` + `R3`); system-energy numbers across all 4 boundaries; honest scope concessions (`R4` + `R5`); title/claim reframing (`"all-optical"` -> `"optoelectronic"`, `"real-time"` -> measured latency).

### 10.3 Pre-submission pre-mortem (12-point core check + 4 `R18b` blind-test checks; see `references/checklists.md`)
Audit all 12 core items before submission: (1) 4-tier energy/TOPS boundary tables (measured vs projected separated); (2) optical vs electronic operation split & O-E-O location; (3) speed at which accuracy/ENOB were measured; (4) matched-precision digital baseline on the identical split; (5) bit precision, drift, and chip-to-chip variation; (6) loss/footprint/crosstalk scaling vs $N$; (7) closest prior art cited & differentiated; (8) task beyond toy MNIST/XOR + ablation controls; (9) in-situ vs offline training cost & query count; (10) trigger words (`"all-optical"`, `"real-time"`, `"scalable"`, `"deep"`, `"nonlinear"`) backed by numbers or removed; (11) cross-document number/unit/integer-ratio consistency; (12) code/data DOIs.
- **Four First-Round Referee Checks Added from `R18b` Blind-Test Calibration (`scripts/pnn_research_toolkit.py referee-simulator`):**
  1. **Material-centric completeness (`[C11]/[C10]`, `R18b-1`):** For 2D materials, MXene, perovskites, oxide memristors, ferroelectrics, or new PCM compositions, include XPS peak deconvolution, indexed XRD (checking residual parent/MAX/impurity phases), Raman mode assignment, and parent/control sample measurements.
  2. **Thermal crosstalk & large-scale integration (`[C4]`, `R18b-2`):** Whenever thermo-optic heaters or photothermal antennas are used, quantify inter-channel thermal crosstalk vs pitch, thermal decay constant $\tau_{\text{th}}$, and architectural scaling ceiling $N_{\max}$.
  3. **Foundational hardware display (`[C10]/[C11]`, `R18b-3`):** Provide full-device/array SEM micrographs with scale bars and critical dimensions, fiber-to-fiber + on-chip insertion loss breakdown, and unit-to-unit uniformity ($\mu \pm \sigma$); keep secondary deep analytical sub-checks as internal self-audits after foundational display items are complete.
  4. **Explicit differentiation vs single closest reference (`[C1]/[C8]`, `R18b-4`):** Contrast directly against the single closest landmark paper in Intro ¶3 and SI Table S1.

### 10.4 Response tactics (`R1–R10`; `references/reviewer_playbook.md`)
- **Highest resolution rates:** **R6 New SI derivation/section** (`95.2%` R2+ resolution) · **R7 Clarified methods/text** (`94.8%`) · **R5 Limitations/Discussion paragraph** (`94.1%` — resolves 93% of energy/comparison objections vs 65% when arguing) · **R2 New simulation/analysis** (`93.9%`) · **R1 New hardware experiment** (`92.0%`) · **R3 Comparison table** (`91.4%`) · **R8 Pure rebuttal/arguing** (`68.2%` — weakest; never argue without new data, a table, or a scope concession).

---

## 11. Likely referees
Plan for the referee archetypes in §10.2 and the concern codes `C1`–`C14` in `references/reviewer_playbook.md`; `reviewer-finder` lists the leading groups for a platform.

---

## 12. House styles of leading groups & recomputed 4-tier global rankings
Full **140-group recomputed score table** (`00_Index/PNN_groups_on_map.json`, `version: 2026-10-28`, excluding self; including 14 Singapore Hub PIs across NUS, NTU, SUTD, A*STAR IME, and AMF) lives in `references/global_groups.md` (`_work/group_scores_recomputed.csv`); Top-20 narrative house styles live in `references/house_styles.md`.
- **4-Tier Score Formula (`R4.2`):** $\text{Score} = 1.00 N_{\text{T1}} + 0.70 N_{\text{T2}} + 0.45 N_{\text{T3}} + 0.25 N_{\text{T4}}$ (`T1–T4` strictly match folders `01–04`).
- **Top-15 Global Groups (`references/global_groups.md`):** 1. **Aydogan Ozcan** (`18.45`) · 2. **Harish Bhaskaran** (`16.85`) · 3. **Wolfram H. P. Pernice** (`16.45`) · 4. **Dirk Englund** (`12.50`) · 5. **Xinliang Zhang** (`12.15`) · 6. **C. David Wright** (`12.10`) · 7. **Chaoran Huang** (`11.55`) · 8. **Lu Fang** (`10.95`) · 9. **Jianji Dong** (`10.85`) · 10. **Peter L. McMahon** (`10.80`) · 11. **Qionghai Dai** (`10.50`) · 12. **Mona Jarrahi** (`9.30`) · 13. **Yang Chai** (`8.70`) · 14. **Min Gu** (`8.50`) · 15. **Bhavin J. Shastri** (`8.45`).

---

## 13. Anti-patterns (seen in T4 papers and past drafts — fix immediately; see `references/checklists.md`)
1. **Fig. 1 with ~12 sub-panels** mixing system render, conventional-vs-ours, mechanism and a table -> restrict to **4–5 panels** (`T3`) or **5–8 panels** (`T1`).
2. **Gap stated only in Intro ¶6–7 and absent from the abstract** -> state the specific technical gap in **Abstract sentence 2** and **Intro ¶2–3**.
3. **Undefined headline metrics** (`"<0.34 pJ"`, `"<10 ns"`) without unit operation or boundary -> apply §7 & §18 4-boundary ledger.
4. **Emulations with measured device statistics presented like hardware results** -> label evidence type explicitly (`"Hardware-calibrated numerical emulation"`).
5. **Test-set accuracy that is not an integer fraction of $n$** or mismatched numbers across text/figures/SI -> run `python scripts/pnn_research_toolkit.py draft-linter <file>` (number consistency, integer ratios, trigger words, boundaries).
6. **Only the best operating point reported** -> report both accuracy/energy or precision/speed operating points.
7. **No limitations or projection paragraph; no numeric comparison table** -> apply §8 and §6.5.
8. **Promotional vocabulary & AI-style em-dashes** (`seamless`, `leverage`, `transformative`, `groundbreaking`, `—`) -> rewrite in plain, specific language.
9. **>15-word titles with nested qualifiers** -> shorten to $\le 12$ words (`T3`) or 7–8 words (`T1/T2`).
10. **Frames around every panel, two levels of lettering (`a-i, a-ii`), raster text, rainbow/`jet` colormaps, `"4*1"`** -> four-sided closed axes, bold `a, b, c`, vector `Arial`, `"4 × 1"`.
11. **Missing data/code DOIs and ethics/consent statements.**

---

## 14. Tier checklists (pass all before submitting; see `references/checklists.md`)
- **T1/T2 (*Nature*, *Science*, *NP*, *NE*, *NNano*, *NCS*, *NMI*):** field-level claim in $\le 7\text{–}8$-word title · system-level hardware result on a real task with measured latency *and* energy · benchmark figure vs named GPU/ASIC at matched accuracy · physics ablation · $\le 6$ main figures + ED · measured/projected split · enumerated limitations · repository DOIs.
- **T3 (*Nat. Commun.*, *Sci. Adv.*):** one sharp capability or metric in $\le 12$-word title · Fig. 1 with log–log positioning scatter · main-text Table 1 comparison with losses shown · hardware evidence for the headline · harder task than toy MNIST/XOR (or full hardware-in-the-loop ablation controls) · two operating points · limitations + projection paragraphs.
- **T4 (`04_T4_IF_ranked`: *Adv. Mater.*, *PNAS*, *Light Sci. Appl.*, *Optica*, *Laser Photonics Rev.*, *PhotoniX*, *ACS Photonics*, *Nanophotonics*, etc.):** clean single contribution · defined metrics · vector figures (`Arial`) · comparison table · honest scope; avoid the §13 anti-patterns.

---

## 15. Library map & `references/` inventory
Master library structure (`<PNN_LIBRARY_ROOT>/`, see `08_Reading_Notes/README.md` for machine root paths):
- `00_Index/`: Read-only index (`PNN_Catalogue.xlsx`, `library_manifest.json`, `PNN_moves.json`, `PNN_groups_on_map.json`, `PNN_roadmap_trends.md`, `PNN_SI_added_since_v2.json`, `PNN_lit_search_tests.json`, `PNN_blind_test_targets.json`, `audit_v6_records.py`, `audit_final_pnn.py`).
- `01_T1_Nature_Science/` (`44`), `02_T2_Nature_Subjournals/` (`126`), `03_T3_NatCommun_SciAdv/` (`271`), `04_T4_IF_ranked/` (`1,034`), `05_Peer_Review_Files/` (`194`), `07_PI_Photos/`, `09_World_Map_PPT/`.
- `08_Reading_Notes/`: `paper_cards/*.md` & `_work/cards_index.csv` (**`1,475` / `1475` cards**: `1,308` / `1308` research + `167` reviews; **`1,109` / `1109` SI files**); `Peer_review_statistics.md` & `_work/pr_comments_v2.jsonl` (**`2,241` / `2241` comments**; `2,216` leave-one-out); `verification/` (`t1_pilot_semantic_audit.md`, `sota_77_cells_audit.md`, `factcheck_report_round4.md`, `blind_test_predictions.md`).
- **Reference Playbooks in `references/`:**
<!-- v3.4 begin §15 -->
  1. `references/PNN_params/` — 十九类逐篇原文核验的器件与系统参数记录表（`<代号>_records.jsonl`，每条含页码、字符偏移与 `record_id`）及规范说明 `README_PNN_params.md`。
  2. `references/derived/device_parameter_atlas.csv` & `.md` — 类别 × 标签 × 参数图谱（实测 / 仿真 / 预测篇数、实测中位数与极值及 `record_id`），以及规则与哈希清单 `PNN_atlas_spec.json`、`derived_manifest.json`。
  3. `references/derived/materials_atlas.csv` & `.md`、`materials_assignment.csv` — 材料族参数图谱与归属明细（`R11`）。
  4. `references/derived/device_coverage.csv` & `.md` — 各类各标签实测与纯仿真覆盖统计（`R12` 覆盖部分；论文功能标签与功能×平台矩阵留待 v3.5）。
  5. `references/derived/benchmark_ledger.csv` & `.md`、`benchmark_task_assignment.csv` — 按任务与平台分组的准确率台账（`R13`）；新课题生成手册见 `references/idea_playbook.md` 与 `verification/idea_gen_examples.md`（`R20`）。
<!-- v3.4 end §15 -->
  6. `references/metrics_sota.md` & `references/Metrics_SOTA_table.xlsx` — 11-Platform × 7-Metric SOTA table (`77/77` verified cells) + `248` Measured & `75` Projected rows.
  7. `references/reviewer_playbook.md`, `references/global_groups.md`, `references/house_styles.md`, `references/figure_archetypes.md`, `references/checklists.md`, `references/platform_physics_and_training.md`, `references/experimental_ml_benchmarks.md`, `references/mathematical_models_and_scaling.md`, `references/writing_templates.md`, `references/journal_transfer_and_cover_letter.md`, `references/library_index.csv`（注：`materials`、`functions` 两列未经验收）.
  8. `references/citations.csv` — 1,475 篇的 DOI、期刊、年、卷、文章号、题目、第一 / 末位 / 通讯作者与末位作者单位（取自 `00_Index/PNN_Catalogue.xlsx`；单位来自 OpenAlex，未逐篇核实）。

---

## 16. Platform-Specific Physics & Experimental Verification Protocols
See [`references/platform_physics_and_training.md §1`](./references/platform_physics_and_training.md) for the complete 11-platform non-ideality, calibration, and physics-ablation matrix (`MZI`, `MRR`, `PCM`, `diffractive`, `metasurface`, `microcomb/WDM`, `reservoir`, `TFLN`, `spiking`, `Ising`, `in-sensor`/`2D-optoelectronic`).

## 17. Hardware-in-the-Loop & On-Chip Training Playbook
See [`references/platform_physics_and_training.md §2`](./references/platform_physics_and_training.md) for the quantitative comparison of In-Situ Optical Backpropagation (`Science_23V380_398`, `Nature_26V651_927`), Physics-Aware Training (`Nature_22V601_549`), Fully Forward Mode / Physical Forward-Forward (`Science_23V382_1297`, `Nature_24V632_280`), and Perturbation/SPSA Optimization (`Nature Photonics_17V11_441`, `Nature Communications_22V13_1044`).

## 18. End-to-End Energy, Latency & System Boundary Accounting Protocol
See [`references/platform_physics_and_training.md §3`](./references/platform_physics_and_training.md) and [`references/mathematical_models_and_scaling.md`](./references/mathematical_models_and_scaling.md) for the four canonical energy boundaries (`core_optical`, `laser_plus_core`, `chip_electrical_io`, `wall_plug_system`), end-to-end latency decomposition, and DAC/ADC amortization crossover $N^*$.

## 19. Executable Scientific Research CLI Toolkit (`scripts/pnn_research_toolkit.py`)
<!-- v3.4 begin §19 -->
Run `python scripts/pnn_research_toolkit.py <subcommand>` — 文献与写作审稿子命令：`lit-search`, `related-work`, `sota-table`, `energy-latency-audit`, `referee-simulator`, `reviewer-finder`, `figure-blueprint`, `draft-linter`；器件参数、台账与新课题确定性查询子命令：`atlas`, `materials`, `coverage`, `benchmark`（均支持 `--tsv` 机读输出）与 `idea-gen`（支持 `--json` 机读输出），直接查询文库卡片、审稿意见、SOTA 台账及 `references/PNN_params/`、`references/derived/` 参数图谱。
<!-- v3.4 end §19 -->

**v3.4.1 用法要点（2026-11-10）**
- **标签匹配：** `atlas`、`coverage`、`benchmark`、`idea-gen` 的 `--label` / `--platform` 先按不区分大小写的精确标签匹配，再查别名表（如 `MRR` → `MRR_WDM`、`microring`；`TFLN` → `LNOI`；`SiN` ↔ `Si3N4`）。仍无匹配时打印该类可用的标签。`no measured record in library` 只表示标签有效但没有符合条件的行，不等于领域空白。
- **计算值标记：** `atlas`、`materials` 默认输出含 `best_measured_calc`（`yes` = 论文按公式算出或估计的值）和 `best_measured_condition`。能效、吞吐等系统量的极值常是只算光功率或按公式外推的数，引用前看条件和能量边界，优先用直接测量值或 `measured_median`。
- **需要文库文件夹的子命令：** `figure-blueprint`（缺 `08_Reading_Notes/_work` 时退出码 3）和 `referee-simulator`（缺文件时只打印通用清单并在 stderr 警告）。文库不随 skill 分发；有文库时，可设环境变量 `PNN_LIBRARY_ROOT` 指向它。`reviewer-finder` 按 `references/global_groups.md` 列各平台的主要课题组。其余子命令只读 skill 自带的 `references/`。
- **其他：** `lit-search` 的 `--author` / `--group` / `--year` 与输出里的 DOI 来自 `references/citations.csv`；`sota-table` 把实测与预测 / 仿真分成两张表；`draft-linter` 检查破折号、宣传用语、不带数字的触发词、题目长度、同一指标的不同数值、准确率整数比、能量与吞吐的单位运算和边界、`4*1` 写法和数据 / 代码可用性声明。

---

## 20. 材料怎么选 (How to Choose Materials — `R11`)
<!-- v3.4 begin §20 -->
按器件类别抓核心权衡参数组合，不单挑孤立指标：相变器件（A3）比 `loss_per_pi`、`delta_n`、`switching_energy`、`endurance`、`levels`；热光移相器（A1）比 `P_pi`、`response_time`、`thermal_crosstalk`；电光调制器（A2）比 `VpiL`、`eo_bandwidth`、`insertion_loss`、`energy_per_bit`；其他非易失元件（A4）比 `write_voltage`、`write_energy`、`retention`、`endurance`；微环与干涉网格（A5、A6）比 `Q_factor`、`extinction_ratio`、`loss_per_stage`；光电探测与突触（C1、I1）比 `responsivity`、`bandwidth`、`dark_current`、`energy_per_event`、`retention`。先用 `materials --family <材料族> [--class <代号>] [--param <参数>]` 查跨类别表现，再用 `atlas --class <代号> --param <参数> --top <N>` 按同单位组对比各材料或器件类型的实测排名。注意核对 `papers_via_label`：差值部分的论文系由 `material_text` 文本匹配归入（可查 `materials_assignment.csv` 与原记录 `material_text`），该材料在文中可能只是衬底或探测器而非有源调制材料，引用前须核实。`best_measured_calc` 为 `yes` 时，该极值是论文按公式算出或估计的，不是直接测量，写入正文前回到原记录核对条件与边界。

```text
$ python scripts/pnn_research_toolkit.py materials --family Sb2Se3 --class A3 --param loss_per_pi
# Materials Atlas (note: papers_via_label counts papers assigned by class label; remaining papers come from material_text)
| material_family | code | param | unit | direction | papers_measured | papers_via_label | measured_median | best_measured | best_measured_text | best_measured_record_id | best_measured_tier | best_measured_calc | best_measured_condition | best_simulated | best_simulated_record_id | best_predicted | best_predicted_record_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sb2Se3 | A3 | loss_per_pi | dB/π | min | 5 | 5 | 0.3 | 0.037 | 0.037 dB/π | A3-79639186030b | T3 |  | crystalline-phase loss from ring Q fits | 0.03 | A3-11c808de9252 |  |  |
```
<!-- v3.4 end §20 -->

---

## 21. 怎么定位新颖性 (How to Position Novelty — `R12`)
<!-- v3.4 begin §21 -->
先运行 `coverage --class <代号> [--label <标签>]` 查看目标类别下各平台或材料分支的总论文数、含实测论文数（`papers_with_measured`）、仅仿真或预测论文数、期刊分档与年份分布及稀薄标记 `thin`（实测论文在两篇及以下）；再运行 `atlas --class <代号> --param <参数>`（配合 `--top`）将本文实测值与库内 `measured_median`、`best_measured` 对照，核查 `best_measured_record_id` 的测量条件与系统边界，明确新颖性属于“填补稀薄实测分支”“把高指标仿真推进为硬件实测”还是“在同边界下协同提升多项核心优值”（功能×平台矩阵待 v3.5 补充）。注意：本库覆盖度仅反映截至入库日的已收文献，“首次”（`first`）或“未见报道”等表述前必须联网检索最新期刊、会议与预印本。

```text
$ python scripts/pnn_research_toolkit.py coverage --class D2
| code | class | label_field | label | papers | papers_with_measured | papers_simulation_or_prediction_only | records | papers_by_tier | papers_by_year | params_with_measured_data | thin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2 | optoelectronic nonlinear activation | platform | PD_amplifier | 2 | 1 | 1 | 7 | T4:2 | 2023:1;2024:1 | bandwidth;function_shape;wavelength | thin |
| D2 | optoelectronic nonlinear activation | platform | PD_modulator | 11 | 10 | 1 | 35 | T1:2;T2:2;T3:4;T4:3 | 2019:1;2022:1;2023:1;2024:2;2025:5;2026:1 | bandwidth;energy_per_activation;function_shape;programmable;wavelength |  |
| D2 | optoelectronic nonlinear activation | platform | other | 6 | 6 | 0 | 23 | T1:1;T3:1;T4:4 | 2022:1;2025:1;2026:4 | bandwidth;energy_per_activation;function_shape;programmable;wavelength |  |
```
<!-- v3.4 end §21 -->

---

## 22. 找文献与写相关工作 (Literature Search & Related Work — `R15`)
Use `scripts/pnn_research_toolkit.py` (`references/library_index.csv`［注：`materials`、`functions` 两列未经验收］ + `references/citations.csv`) to retrieve exact in-library citations and draft structured Related Work paragraphs without missing competitors:
1. **Multi-filter literature search (`lit-search`):**
   - `python scripts/pnn_research_toolkit.py lit-search --platform TFLN --tier T1,T2 --top 20`
   - Supports `--platform`, `--material`, `--function`, `--task`, `--claim-class`, `--tier`, `--year` / `--year-min` / `--year-max`, `--title-word`, `--author`, `--group`, `--keyword`, `--exclude-reviews`, `--only-measured` and `--top`（`--material`、`--function` 对应列未经验收）. Outputs a Markdown table (`tier | year | class | platform | materials | functions | headline_measured | first / last author | DOI | stem & card path`); author, group and DOI come from `references/citations.csv`.
2. **Citation-ready Related Work drafter (`related-work`):**
   - `python scripts/pnn_research_toolkit.py related-work --topic "on-chip training of MZI meshes" --max-refs 15`
   - Ranks T1/T2/T3 papers by topic words in the title, then platform / material / function; groups the candidates by platform with DOIs and lists the 1–3 closest with headline value, page and DOI. It returns candidates, not finished prose: read the papers before citing.

---

## 23. 基金、报告与讲座 (Grants, Reports & Talks — `R16`)
When drafting grant proposals, progress reports, or invited talks, anchor quantitative claims strictly on `00_Index/PNN_roadmap_trends.md`, `00_Index/PNN_groups_on_map.json`, `references/metrics_sota.md`, and `references/global_groups.md`（功能×平台矩阵留待 v3.5）:
- **Field Evolution & Quantitative Trend Data (`00_Index/PNN_roadmap_trends.md`):**
  - Across `1,289` dated research articles (`<=2019` · `2020–22` · `2023–24` · `2025–26`), annual output expanded from `8` (`2014`) -> `57` (`2020`) -> `187` (`2024`) -> `247` (`2025`) -> `369` (`2026`), spanning 6 major directions: `Diffractive & metasurface` (`419`), `In-sensor & synapses` (`300`), `WDM, microcomb & TFLN` (`170`), `Integrated matrix processors` (`146`), `Reservoir, spiking & Ising` (`119`), and `Non-volatile in-memory` (`88`).
  - Highlight the 2025–26 structural inflections in grant Motivation slides: hardware-in-the-loop training surged (`3 -> 18 -> 24 -> 45` papers across the 4 periods), monolithic `TFLN` computing jumped (`1 -> 3 -> 3 -> 22`), ferroelectric `BTO/HZO` weights emerged (`0 -> 3 -> 3 -> 15`), while `1,181` papers still omit decomposed system energy vs only `35` reporting peripheral/wall-plug energy (`core-only: 50`, `both: 3`).
- **Grant Whitepapers, KPIs & Talk Positioning:**
<!-- v3.4 begin §23 -->
  - *Gap Analysis & Device/Material KPIs:* 立项书与答辩报告的差距分析先用 `coverage` 定位实测稀薄分支或仅有仿真的技术环节，再用 `atlas` 读取同单位组下的实测中位数（`measured_median`，作为起评基线或中期里程碑）与实测极值（`best_measured`，作为结题竞争锚点），所有引用的基线值与极值一律由工具查询得出并保留对应 `record_id` 及测试条件说明；系统级算力与能效锚点可按四级能量边界结合 `references/metrics_sota.md` 与 `benchmark` 台账核定，国际竞争格局可参照 `references/global_groups.md`。

```text
$ python scripts/pnn_research_toolkit.py atlas --class A1 --param P_pi --top 3
| code | label_field | label | param | unit | direction | papers_measured | measured_median | best_measured | best_measured_text | best_measured_record_id | best_measured_tier | best_measured_calc | best_measured_condition | best_simulated | best_simulated_record_id | best_predicted | best_predicted_record_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | material | doped_Si | P_pi | V | min | 1 | 1.75 | 1.75 | 1.75 V | A1-35076b43d725 | T4 |  | half-wave voltage of one thermo-optic phase shifter within an MRR |  |  |  |  |
| A1 | material | not_stated | P_pi | V | min | 1 | 3 | 3 | Vπ switching voltage of 3 V | A1-e40ef024e770 | T4 | yes |  |  |  |  |  |
| A1 | material | TiN | P_pi | V | min | 1 | 5.4 | 5.2 | Vπ = 5.2 V | A1-8fcae0d631b2 | T4 |  | MZI used for in-situ weight update (voltage scan 0–7.5 V) |  |  |  |  |
| A1 | material | TiN | P_pi | mA | min | 2 | 9.305 | 9.2 | 9.2 mA | A1-9b8247fb3eff | T4 |  | π phase shift of a TOMZI |  |  |  |  |
| A1 | material | TiN | P_pi | mW | min | 19 | 20 | 1.26 | 1.26 mW/ π | A1-1443331c2ea9 | T4 |  | suspended waveguide with trenches |  |  |  |  |
| A1 | material | not_stated | P_pi | mW | min | 14 | 20 | 1.3 | 1.3 mW/π | A1-386db2bf900e | T3 |  | characterised across many chips and two wafers |  |  |  |  |
| A1 | material | graphene | P_pi | mW | min | 1 | 10.2 | 10.2 | Pπ = 10.2 mW | A1-ba70492c7134 | T4 |  | test interference structure (Vπ = 2.11 V) |  |  |  |  |
```
<!-- v3.4 end §23 -->

---

## 24. 出新 idea (Grounded Idea Generation — `R20`)
<!-- v3.4 begin §24 -->
用 `idea-gen [--function <文字>] [--platform <P>] [--material <M>] [--task <T>] [--class <C>] [--limit <N>] [--json]` 从派生表与原记录确定性生成候选卡片（详解与固定示例见 `references/idea_playbook.md` 及 `verification/idea_gen_examples.md`）：
- **四种配方**：R1 实测稀薄分支（`device_coverage`）、R2 仿真或预测领先实测十倍或十个分贝单位以上（`device_parameter_atlas`）、R3 同参数跨材料族迁移对照（`materials_atlas`）、R4 具体平台与任务的准确率台账空白（`benchmark_ledger`），按顺序轮流取卡。
- **卡片七栏**：`【1 空白】`、`【2 前作】`（含 `record_id`、页码与 DOI）、`【3 器件参数】`（实测中位数与极值锚点）、`【4 审稿人会问】`（映射高频关切，使用者须结合 `references/reviewer_playbook.md` 与 `referee-simulator` 补齐消融与对策）、`【5 最小验证实验】`、`【6 投稿档次】`（对照 §1 与 §14）、`【7 库外查新】`。
- **边界**：用户未发表的工作绝不写入任何文件；文库有截止日期与筛选范围，给出任何 idea 前必须联网查新。

```text
$ python scripts/pnn_research_toolkit.py idea-gen --task Fashion-MNIST --platform MZI --limit 3
classes: A1, A2, A3, A4, A5, A6, B1, B2, C1, D1, D2, E1, E2, E3, F1, G1, H1, I1, J
no idea card for these filters: no recipe applies, or every matching branch already has 2 or more measured papers (check `benchmark` / `coverage` / `atlas` for the measured state)
```
<!-- v3.4 end §24 -->

