# PNN Pre-Submission Checklists, 12-Point Pre-Mortem & Anti-Pattern Audit

Run this audit on any PNN / optical computing draft before submission or revision delivery.

---

## 1. The 12-Point Referee Pre-Mortem (Answer in the Manuscript, Not in the Rebuttal)

Check that the draft explicitly answers all 12 questions in the main text, Methods, or SI before submission:

- [ ] **1. Energy & Throughput Ledger:** What exact components are counted in every TOPS, TOPS/W, J/OP, and $\text{TOPS/mm}^2$ number (laser wall-plug, DAC/ADC, TIA, thermal holding power $P_\pi$, memory/refresh, FPGA/CPU)? Are **Measured** and **Projected** values separated into distinct rows/tables?
- [ ] **2. Optical vs Electronic Share:** Which exact mathematical operations happen optically and which happen electronically? Where is the O-E-O conversion? What percentage of total MACs/FLOPs is executed optically?
- [ ] **3. Speed & Latency Consistency:** At what clock/baud rate were the task accuracy and bit precision actually measured? Is the claimed latency physically compatible with the slowest component in the loop (sensor response, DAC update, thermal time constant $\tau$, TIA bandwidth, ADC averaging)?
- [ ] **4. Fair Digital & Ablation Baselines:** Is there a digital baseline of the *exact same model capacity, input features, train/test split, and bit precision* plotted alongside the photonic result? Is there a **physics ablation** (e.g., frozen/untrained optical core, bias-only readout, or identity replacement) proving the optical reconfiguration does the work?
- [ ] **5. Precision, Drift & Reproducibility:** Are effective bits/levels, RMS programming error, multi-hour/multi-day stability, thermal crosstalk, and repeated-readout variance reported with $n$ and error bars?
- [ ] **6. Scaling Law & First Bottleneck:** How do insertion loss ($\text{dB}$), footprint ($\text{mm}^2$), electrical I/O pad count, and thermal power scale with port count $N$? What is the first physical bottleneck (SNR, combining loss $1/N$, FSR, thermal crosstalk) and at what $N$ does it hit?
- [ ] **7. Prior-Art Etiquette:** Are the 1–3 closest competing papers cited and compared fairly in both the Introduction and the comparison table (remember: omitted competitors are frequently chosen as referees)?
- [ ] **8. Dataset Rigour & No Data Leakage:** Are preprocessing transforms (PCA, normalization, feature selection) fitted **strictly on the training split**? Are checkpoint selections done on the validation split rather than the test split? Are test sample counts $n$ stated as exact integer ratios (e.g. `25/30 = 83.3%`)?
- [ ] **9. Training Cost & Method:** If claiming in-situ / hardware-in-the-loop training, how many forward queries per update step are required (e.g. $2 \times N_\text{heaters}$ for paired finite differences), what is the total wall-clock training time and energy, and how does it compare with offline digital-twin training?
- [ ] **10. Claim-Word Audit:** Every high-risk word (`"all-optical"`, `"deep"`, `"nonlinear"`, `"real-time"`, `"non-volatile"`, `"scalable"`, `"held-out"`, `"distillation"`, `"perfect"`, `"first"`) is either backed by a direct quantitative proof or replaced by the referee-safe term.
- [ ] **11. Cross-Document Number & Unit Audit:** Every number (wavelength, $Q$, ER, transmission $\%$, accuracy $\%$, sample count $n$, voltage range, heater count, dimensions) is 100% identical across Abstract, Introduction, Results, Discussion, Methods, Figure panels, Captions, and SI.
- [ ] **12. Reproducibility & Ethics Statements:** Data and code availability point to a public repository/DOI (or structured source data); wearable/human-subject measurements include an explicit ethics/self-collection declaration.

---

## 2. Anti-Pattern Scan (Seen in T4 Papers & Past Drafts — Fix Immediately)

| # | Anti-Pattern to Eliminate | Referee / Editor Reaction | Concrete Fix |
|---|---|---|---|
| 1 | **Fig. 1 with 10–15 sub-panels** mixing system render, conventional-vs-ours, device physics, and a table | Visual overload; flagged as T4 styling | Restrict Fig. 1 to **4–5 panels** carrying one clear message; move device curves to Fig. 2 and tables to Table 1 / SI. |
| 2 | **Generic "AI / LLM compute crisis" opener** with the actual technical gap buried in Intro ¶6 | Referees complain the motivation is disconnected from the device demo | State the specific physical/architectural gap in **Abstract sentence 2** and **Intro ¶2–3**. |
| 3 | **Undefined headline metrics** (`"<0.34 pJ"`, `"<10 ns"`) without operation definition or boundary | Immediate C2/C3 audit in Round 1 (3 rounds of energy grilling in NC) | Add a dedicated Methods subsection (*Speed and Energy Accounting Ledger*) and state the boundary inline (`"0.34 pJ per optical MAC (modulator only)"`). |
| 4 | **Emulations with measured device statistics presented like hardware runs** | Rejecting objection if unflagged (`"projections/simulations, not hardware"`) | Label headings and figure titles explicitly (`"Hardware-calibrated numerical emulation"`) and include at least one end-to-end hardware task. |
| 5 | **Test accuracy that is not an integer ratio of $n$**, or `"100%"` confusion matrix without $n$ or variance | ML referee flags statistical invalidity or data leakage | Always write `k/n (XX.X%)` in text and print `n = ...` on every confusion matrix. |
| 6 | **Reporting only the best quantized/compensated operating point** while hiding raw analog performance | Referees suspect post-processing does all the work | Report **both operating points** in the abstract and main text (e.g. raw analog vs 4-bit, or frozen core vs trained core). |
| 7 | **No limitations paragraph in Discussion** | Forces referees to write the limitations as rejection reasons | Add an explicit paragraph: `"Two limitations remain in the current prototype. First, ... Second, ..."` each paired with a concrete physical remedy. |
| 8 | **Qualitative comparison table** (`"High / Low / Not addressed"`) or omitting losing metrics | Read as evasive; triggers mandatory major revision | Use sourced numbers in every cell, separate `[Measured]` and `[Projected]`, and include columns where your platform trades off performance. |
| 9 | **AI-polished promotional vocabulary & em-dashes** (`transformative`, `seamless`, `leverage`, `delve`, `pivotal`, `—`) | Sounds synthetic and inflates claims (triggers C12 overclaim in 100% of papers) | Rewrite in plain language: zero em-dashes, plain connectors (`Therefore,`, `However,`, `Thanks to`), $\le 1$ promotional word per paper. |
| 10 | **15–18 word titles with stacked adjectives** or **$>80$ references** in a research article | Reads like a T4 incremental paper or a review article | Shorten title to **7–8 words (T1/T2)** or **$\le 12$ words (T3)**; trim main-text references to **50–70**. |
| 11 | **Rounded boxes around every panel, two-level labels (`a-i, a-ii`), raster text, `jet` colormap, `4*1`** | Instant visual downgrade | Open/four-sided axes, single-level bold `a, b, c`, vector text (`Arial`), `inferno`/`viridis`/`RdBu`, proper `4 × 1`. |

---

## 3. Tier-Specific Submission Checklists

### Tier 1 / Tier 2 (*Nature*, *Science*, *Nature Photonics*, *Nature Electronics*, *Nature Nanotechnology*, *Nature Computational Science*)
- [ ] **Title:** $\le 7\text{–}8$ words, no numbers, states a field-changing capability or mechanism.
- [ ] **Abstract:** 150–230 words; every headline number paired with its digital/theoretical comparator and boundary.
- [ ] **Hardware Evidence:** End-to-end hardware demonstration on real tasks with measured speed, latency, and energy.
- [ ] **Physics Ablation:** Explicit control experiment proving the optical physics (not electronic pre/post-processing) drives task performance.
- [ ] **System Benchmark Figure:** Main-text closing figure comparing accuracy/latency/energy against named GPU/ASIC on log axes; detailed Measured vs Projected tables in Extended Data / SI.
- [ ] **Artwork:** 4–6 dense main figures (vector PDF/SVG + 600 dpi PNG), unified semantic colour code, 6–10 Extended Data figures (for *Nature*).
- [ ] **Discussion:** Enumerated limitations + quantitative scaling roadmap with loss/footprint bounds.
- [ ] **Timeline & Process:** Expect 3 referees (circuit/energy auditor + device physicist + ML specialist), 2–3 rounds, ~8–9 months.

### Tier 3 (*Nature Communications*, *Science Advances*)
- [ ] **Title:** $\le 12$ words, one sharp capability or verified metric.
- [ ] **Fig. 1:** 4–5 panels including a **log–log benchmark positioning scatter plot** (`"This work"` in red).
- [ ] **Main-Text Table 1:** Sourced multi-metric comparison table showing both winning and losing columns, with `[Measured]` and `[Projected]` rows separated.
- [ ] **Task Complexity:** At least one task beyond basic MNIST/Iris (or multi-task hardware-in-the-loop demonstration with full ablation controls).
- [ ] **Public Peer Review Ready:** *Nat. Commun.* publishes peer-review files for ~37% of PNN papers — write every Methods disclosure and referee response for public readers.

### Tier 4 (*Light: Science & Applications*, *eLight*, *Adv. Photon.*, *Adv. Mater.*, *Adv. Funct. Mater.*, *Adv. Opt. Mater.*, *Laser & Photonics Reviews*, *ACS Photonics*, *Photonics Research*)
- [ ] **Single Clean Story:** Well-defined device or algorithmic contribution with complete characterization (insertion loss, $Q$/ER, tuning power, speed).
- [ ] **Honest Evidence Labels:** Clearly distinguish 2.5D/3D simulations, hardware measurements, and device-calibrated emulations.
- [ ] **Zero T4 Visual Traps:** Vector typography (`Arial`), no panel frames, no `jet` rainbow sweeps, consistent numbers across text and figures.
