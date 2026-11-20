---
name: low-aigc-nondefensive-writing
description: Dedicated Low-AIGC Humanization and Non-Defensive Scientific Writing skill for AI-assisted or AI-edited manuscripts, SI, cover letters, and rebuttals. Calibrated empirically against Pre-ChatGPT T1/T2 Nature/Science/Nature Photonics human prose (2010-2022, n=43) vs Post-LLM drift (2024-2026, n=52) and paired with author house-style guidelines. Eliminates both synthetic AIGC fingerprints (low burstiness, participial tails, em-dashes, AI hype, template wrap-ups) and defensive AI safety-hedging (repeated negative disclaimers, double-hedged weasel verbs, apologetic self-depreciation) while preserving 100% scientific honesty, numbers, and citations.
---

# Low-AIGC & Non-Defensive Scientific Writing Playbook (v1.0)

## 1. Empirical Pre-LLM Human Baseline vs Post-LLM Drift (`n=113` T1/T2 Research Articles)

Measured directly across all 113 published T1/T2 PNN Research Articles on local M5 (`references/human_vs_llm_t1t2_baseline.json`), strictly separating Pre-ChatGPT human-authored papers (`<=2022`) from Post-LLM era papers (`2024-2026`):

| Quantitative Prose Fingerprint | Pre-LLM Human T1/T2 (`<=2022`, `n=43`) | Post-LLM Era (`2024-2026`, `n=52`) | Unedited AI Draft (Typical) | Target For Your Manuscript |
|---|:---:|:---:|:---:|:---:|
| **Sentence-length burstiness (`std`, words)** | **`12.12`** | `11.87` | `4.0-6.5` (robotic uniform) | **`>= 9.0` words** (mix `<15w` & `25-35w` sentences) |
| **Participial tails / 1k words** (`, enabling / highlighting / thereby...`) | **`0.70`** | `1.57` (`2.24x` surge) | `5.0-12.0` | **`<= 1.2 / 1k`** (`<= 1` per 2 paragraphs) |
| **AI-hype vocabulary / 1k words** (`transformative`, `pivotal`, `seamless`, `underscore`...) | **`0.00`** | `0.48` | `4.0-10.0` | **`0.00 / 1k`** |
| **Em-dashes (`U+2014`) / 1k words** | `0.48` (human pre-LLM baseline: `<0.05`) | `0.30` | `2.0-8.0` | **`0.00 / 1k`** (strictly zero) |
| **`not only ... but also` / 1k words** | **`0.00`** | `0.00` | `0.8-2.5` | **`0.00 / 1k`** |
| **Defensive negative disclaimers / 1k words** (`does not constitute`, `we do not claim`, `merely`, `to some extent`...) | **`0.00`** | `0.00` | `2.0-6.0` (safety-hedged AI) | **`0.00 / 1k`** (state exact scope once positively!) |

- **Division of Labour**: Pair this skill with [`author house-style guidelines`](../author house-style guidelines/SKILL.md) (for author's authentic 2019-2023 connectors `Therefore,`, `However,`, `Thanks to X,`, `Additionally,`, `we propose`) and the 13 `pnn-t1t2-*` skills (for section-specific T1/T2 structure). **Rewriting MUST NEVER alter any measured number, unit, statistical count `k/n`, citation, or scientific conclusion.**

---

## 2. Part A: Six Quantitative Levers to Lower AIGC Detection Rate

AI detectors (Turnitin/iThenticate AIGC, GPTZero, ZeroGPT, CNKI-AIGC) primarily detect **statistical predictability and syntactic symmetry**, not just individual buzzwords. Apply all six levers in order:

1. **Restore Sentence-Length Burstiness (`std >= 9 words`)**:
   - AI prose defaults to uniform 19-24 word sentences. Break rhythmic uniformity deliberately: put a **crisp 8-14 word declarative result sentence** right next to a **26-34 word physical mechanism sentence**.
   - Avoid 3+ consecutive sentences in the 18-24 word band.
2. **Cut Participial Tails (`<= 1.2 / 1k words`)**:
   - Every `, enabling ...`, `, thereby ...`, `, highlighting ...`, `, underscoring ...`, `, demonstrating ...`, `, paving the way for ...` tacked onto the end of a main clause is a bright AIGC beacon.
   - **Fix**: Split into a crisp second sentence (`Therefore, ...` / `This reduces ...`) or convert to a plain `which` clause (`..., which agrees well with the FDTD prediction`).
3. **Eliminate Synthetic Punctuation & Symmetry Patterns**:
   - **Zero em-dashes (`U+2014`)**: replace with commas, parentheses, or a full stop.
   - **Zero mid-paragraph colon reveals** (`"This solves a key challenge: thermal crosstalk."` -> `"This reduces thermal crosstalk."`).
   - **Zero `not only ... but also`** and **zero mechanical 3-noun abstract triads** (`"high speed, low power, and superior scalability"` -> give concrete measured metrics instead).
   - **Zero `both X and Y` filler rhythm pairs** when plain `X and Y` reads cleaner.
4. **Strip AI-Era Openers & Lexicon (`0.00 / 1k`)**:
   - Delete sentence-opening crutches: `Notably,`, `Importantly,`, `Remarkably,`, `Strikingly,`, `Specifically,`, `More specifically,`, `In particular,`, `Subsequently,`, `Collectively,`, `Overall,`, `Looking ahead,`, `Moving forward,`, `Thus,`, `Hence,`, `Yet,`, `As such,`.
   - Swap LLM-favored verbs/adjectives back to plain scientist English: `utilize/employ` -> `use`; `leverage/harness` -> `use` (or physical verb); `elucidate` -> `explain/analyze`; `showcase` -> `show`; `underscore` -> `confirm/show`; `facilitate` -> `enable/allow`; `exhibits a limitation` -> `is limited by`; `by a factor of 4.5` -> `4.5 times`.
5. **Delete Paragraph Wrap-Up Cliché Tails**:
   - LLMs love ending every body paragraph with `"Taken together, these results demonstrate the robustness and versatility of our platform."` Published pre-2023 *Nature*/*Science* paragraphs end directly on the last physical observation or equation, then move straight to the next paragraph.
6. **Anchor Claims in Concrete Physical Mechanisms & Parenthetical Numbers**:
   - Replace abstract filler (`"significant performance enhancement"`) with bare physical nouns and numbers in parentheses (`"13.5 times signal improvement"`, `"insertion loss (2.1 dB)"`, `"thermal decay time (12 us)"`).

---

## 3. Part B: Six Laws of Non-Defensive Scientific Authority

When an AI edits a manuscript under strict scientific-integrity rules, it often over-corrects into **defensive, self-undermining, legalistic hedging** (`"We do not claim..."`, `"This does not constitute..."`, `"only a small-scale preliminary proof-of-concept..."`). In real *Nature* / *Science* / *Nature Photonics* papers, **defensive disclaimers are 0.00 / 1k words** because **exact positive scope IS honesty**: apologizing repeatedly signals weakness to editors and invites rejection.

### Law 1: Positive Scope Framing (State What It IS, Never Define by What It Is NOT)
- **Defensive AI**: *"Our power estimate does not represent a full wall-plug system benchmark and should not be compared directly against commercial GPUs; it only captures the optical modulator energy."*
- **Non-Defensive T1/T2**: *"At 10 Gbaud, the electro-optic modulator consumes 0.34 pJ per MAC (modulator-only boundary); complete system power including laser, DAC, TIA, and ADC contributions is itemized in Supplementary Note 4 (Table S2)."*

### Law 2: The One-Place Scope Rule (Zero Echo Disclaimers)
- State any methodological boundary (`within-session split`, `hardware-calibrated numerical emulation`, `train-only 4-component PCA`, `core-optical boundary`) **ONCE**, cleanly and accurately, where the result is introduced (and in Methods/SI).
- **Never** repeat `"this is not claimed as..."` or `"note that this is only an emulation..."` across Abstract, Intro, Fig. 3, Fig. 4, and Discussion. Repeating a caveat 4 times turns transparent reporting into self-sabotage.

### Law 3: Engineering-Roadmap Limitation Framing (No Self-Depreciation)
- **Defensive AI**: *"Admittedly, a major weakness of our current prototype is its high 6 dB grating-coupler loss and slow 12 us thermo-optic heaters, which severely hinder real-world deployment."*
- **Non-Defensive T1/T2**: *"In the current prototype, fiber-to-chip grating coupling (6 dB per facet) and thermo-optic reconfiguration time (12 us) set the primary loss and weight-update ceilings. Replacing grating couplers with inverse-taper edge couplers (<1 dB) and integrating heterogeneous TFLN or non-volatile PCM phase shifters directly removes both ceilings without modifying the core topology."*

### Law 4: Assertive Plain Verbs + Exact Conditions (Zero Double-Hedging)
- **Defensive AI**: *"These preliminary observations may potentially suggest that closed-loop tuning could possibly mitigate thermal drift to some extent."*
- **Non-Defensive T1/T2**: *"Closed-loop feedback holds the classification accuracy within 93.3 +- 0.8% over 4 hours of continuous operation (Fig. 3d)."*
- Ban stacked hedges: `may potentially`, `could possibly`, `might tentatively`, `appears to suggest`, `seems to indicate`, `to some extent`, `relatively`, `somewhat`, `plausibly`.

### Law 5: Clean Positive Attribution for Emulations & Compact Hardware
- **Defensive AI**: *"Because our chip has only 4 input ports, we could not test full images directly on hardware and instead relied on a simplified PCA proxy that should not be viewed as a full-scale vision benchmark."*
- **Non-Defensive T1/T2**: *"To process 28 x 28 images on the 4-input photonic core, we evaluate two complementary schemes: 2 x 2 spatial patch tiling directly on hardware and 4-component PCA fit strictly on the training split (Methods). Across 1,000 test images, the chip reaches 91.4% accuracy, compared with 92.1% for the matched 4-bit digital model."*

### Law 6: Firm Technical Authority in Rebuttals & Cover Letters
- Never grovel (`"We sincerely apologize for this huge oversight"`, `"We completely agree our work is very preliminary"`).
- State the factual resolution calmly and directly: *"We have added the requested untrained-core ablation experiment (Page 7, Fig. 3d) and complete 4-tier power breakdown (Supplementary Note 4, Table S1)."* When disagreeing with a referee on scope, stay concise and factual (*"We agree that X was shown in Ref. 12; however, our device targets Y, which is orthogonal to X."*).

---

## 4. Quick-Check Transformation Table (More in `references/rewrite_patterns_and_examples.md`)

| Section | High-AIGC + Defensive AI Draft (Reject) | Low-AIGC + Non-Defensive T1/T2 Rewrite (Adopt) |
|---|---|---|
| **Abstract** | *"In today's rapidly evolving AI landscape, photonic chips--leveraging light--offer a transformative paradigm, thereby enabling low-power computing. Admittedly, our prototype is only a small-scale proof-of-concept and does not constitute a full GPU replacement."* | *"Electronic data movement limits the energy efficiency of matrix-heavy neural inference. However, cascaded Mach-Zehnder meshes suffer from quadratic footprint and insertion-loss scaling. Here we propose a 64-heater programmable silicon diffractive chip operating at 1550 nm. The chip reaches 93.3% accuracy (28/30) on held-out test samples, compared with 94.0% for the matched digital model, with an optical-core energy of 0.34 pJ per MAC."* |
| **Results** | *"Notably, as can be observed, the curve appears to suggest reasonable agreement with simulation, underscoring the validity of our model, although it should be noted that measurement noise remains present."* | *"As shown in Fig. 2b, the measured transmission spectrum agrees well with the 3D FDTD simulation (RMS residual = 0.032 across 1530-1565 nm). Residual deviations stem from +-4 nm waveguide-width variations observed in CDSEM metrology (Extended Data Fig. 1)."* |
| **Discussion** | *"Taken together, these preliminary findings may potentially pave a transformative pathway, though we do not claim immediate superiority over commercial A100 GPUs due to severe off-chip electronics overhead."* | *"Two engineering factors bound the current prototype: off-chip DAC/ADC power and grating-coupler insertion loss (6 dB). Moving to 3D CMOS-photonic co-packaging and edge couplers (<1 dB) raises the projected system efficiency above 50 TOPS/W (Supplementary Note 4), opening a practical route for compact near-sensor vision processors."* |

---

## 5. Automated Audit Workflow (Run Before Every Submission / Revision)
1. Run the standalone zero-dependency auditor on any `.md`, `.txt`, `.tex`, or `.docx` draft:
```bash
python3 scripts/aigc_nondefensive_auditor.py audit path/to/manuscript.docx
python3 scripts/aigc_nondefensive_auditor.py audit path/to/draft.md --verbose
```
2. Target **`AIGC Risk < 20/100`** and **`Defensiveness Risk < 15/100`** (`0` em-dashes, `0` AI-hype words, `<=1.2/1k` participial tails, `sent_std >= 9.0`, `0` negative self-policing disclaimers).
3. Verify zero numeric/citation drift after rewriting, then run final similarity check on NUS iThenticate (`nus-ith.turnitin.com`) per [`05_Manuscript_Revision_SOP.md`](../manuscript-rebuttal-playbook/references/05_Manuscript_Revision_SOP.md).

---

## 6. References & Tools
- **Empirical Baseline**: [`references/human_vs_llm_t1t2_baseline.json`](./references/human_vs_llm_t1t2_baseline.json)
- **20+ Side-by-Side Rewrite Patterns**: [`references/rewrite_patterns_and_examples.md`](./references/rewrite_patterns_and_examples.md)
- **Standalone Auditor CLI (supports `.docx`/`.md`/`.txt`/`.tex`)**: [`scripts/aigc_nondefensive_auditor.py`](./scripts/aigc_nondefensive_auditor.py)

<!-- native-english-register begin -->

---

## 6. Native-English-Country (`US/UK/CA/AU`, `2.0x` Weight) High-Register Vocabulary & Grammar Elevation
Eliminating AI fingerprints and defensive caveats is step 1; elevating prose to idiomatic *Nature*/*Science* precision is step 2. Empirically calibrated from **`49` native-primary T1/T2 papers (`US/GB/CA/AU`, `243,610` words, weight `2.0x`) vs `51` non-native T1/T2 papers (`278,262` words, weight `1.0x`)** (`0` T3/T4; full bank in [`references/native_high_register_guide.md`](./references/native_high_register_guide.md)):
- **Precision Verbs Enriched `1.8x-3.9x` in Native T1/T2 Prose**: `impart` (`3.87x`), `harness` (`3.70x`), `account for` (`3.04x`), `necessitate` (`2.63x`), `entail` (`2.54x`), `render` (`2.21x`), `decouple` (`2.17x`), `dictate` (`2.14x`), `attain` (`2.09x`), `yield` (`1.78x`), `eliminate` (`1.55x`), `circumvent` (`1.45x`). Use these cleanly for physical precision while avoiding pompous AI hype (`delve`, `underscore`, `showcase`, `orchestrate`, `transformative`).
- **Idiomatic Collocations & Grammar Frames (`1.5x-3.2x` Native Lift)**:
  - **Objective physical limits** (`limited by` `2.03x`, `bound by` `2.46x`, `governed by`) instead of melodramatic `suffer from` (`0.56x`).
  - **Compact inline concession** (`albeit` `3.16x`, `nonetheless`) instead of apologetic disclaimer paragraphs.
  - **Honest scope & scaling** (`in principle` `2.63x`, `viable` `2.41x`, `proof of concept` `2.25x`, `on par with` `2.10x`, `at the expense of` `1.45x`, `such that` `1.90x`, `given that` `2.01x`).
  - **Quantitative density & clause balance**: `6.97` inline parenthetical numbers per 1k words (`1.76x` higher than non-native) and balanced semicolons (`0.93/1k`) instead of `Moreover`/`Furthermore`/`Accordingly` chains.
- **Top Non-Native Overused Clichés to Replace**: `versatile` (`0.37x` -> name exact modes), `accordingly` (`0.45x` -> `in turn` / direct causality), `dramatically` (`0.53x` -> exact `Nx` factor), `suffer from` (`0.56x` -> `limited by` / `bound by`), `propose` spam (`0.60x` -> vary with `introduce`/`demonstrate`/`present`/`formulate`), `specifically`/`in particular` filler (`0.57-0.63x`), `empower`, `pave the way`, `play a vital role`.
- **New CLI Commands (`scripts/aigc_nondefensive_auditor.py`, v2.0)**:
  - `python3 scripts/aigc_nondefensive_auditor.py vocab-upgrade <file.docx|draft.md|text>` (scores Native Register Readiness `0-100` and outputs verbatim US/UK/CA/AU *Nature*/*Science* upgrades)
  - `python3 scripts/aigc_nondefensive_auditor.py native-lexicon --category {verbs|collocations|cliches|syntax} --top 15`
<!-- native-english-register end -->
