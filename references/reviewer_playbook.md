# Peer-Review Statistics (`Wave 1`, `Wave 2`, and `Combined` — Round-4 Calibrated `v2.4`)

> **Methodology, Deduplication & Calibration Disclosure (`R3` & `R9` Certified):**
> - **Kept Library Corpus (`05_Peer_Review_Files` after `PNN_moves.json` deduplication):** `194` peer-review PDFs (`191` active files containing referee reports — `58` Wave-1 files with human-assisted digests + `133` Wave-2 files segmented and coded with the Set-A calibrated coder — plus `3` 1-page *Nature Communications* transfer notice files [`25V16_4473`, `25V16_908`, `26V17_10241`] that state `"accepted without further review"` and contain `0` referee reports), yielding **`2234` verified unique referee comments** (`1159` in Wave 1; `1075` in Wave 2).
> - **Strict Non-Referee & Duplicate Filtering:**
>   1. **Zero Bibliography / Reference Entries (`0` items):** All reference citations (`et al.`, journal/volume/page strings, `[1]`, `R1.`) are stripped and verified (`0` remaining).
>   2. **Zero Author Replies / Manuscript Excerpts (`0` items):** All first-person author response paragraphs (`we`/`our` clauses) and line-numbered manuscript paste blocks are stripped and verified (`0` remaining).
>   3. **Zero Rebuttal-Repeat Duplicates (`0` duplicate groups):** Repeated referee quotes within the same `_PeerReview.pdf` are deduplicated so only the original referee report occurrence is counted.
> - **Held-Out Calibration & Confidence Limitations (`_work/pr_calibration.md`, `R9`):**
>   - **Concern Coding (`C1–C14`):** On unseen Held-Out `Set B` (`8` papers, `151` comments, zero tuning on `Set B`), strict primary-to-primary match is `107 / 151` (`70.86%`, unweighted Cohen's $\kappa = 0.6764$) and multi-label set inclusion (`pred_primary in gt_codes`) is `138 / 151` (`91.39%`). Because human Wave-1 digests listed multi-concern tags in numerical order (`[C1, C8]`), the blind coder selected the secondary tag in `20.53%` of Held-Out `Set B` comments; we report the exact zero-tuning $\kappa = 0.6764$ without post-hoc tag reordering.
>   - **Severity Coding (`major` / `minor` / `editorial`):** Calibrated against independent Wave-1 human-digest annotations (`R1` new experiment / `R2` new simulation / `R3` comparison table / `R4–R5` core claim concession / `Satisfied: no`), achieving `83.54%` exact agreement ($\kappa = 0.7053$) on Tuning `Set A` (`237` comments) and `73.51%` exact agreement ($\kappa = 0.5020$) on Held-Out `Set B` (`151` comments). **Confidence Limitation:** Because automated 3-class severity coding on unseen `Set B` reaches moderate agreement ($\kappa = 0.5020$, below the `0.70` target due to boundary ambiguity between substantive `minor` clarifications and `major` analytical requests), Wave-1 (`1159` human-assisted comments) and Wave-2 (`1075` rule-coded comments) are always reported side-by-side rather than pooled blindly.

---

## 1. Wave 1 Concern Distribution (`58` Files, `1159` Referee Comments — `wave1_human_assisted_digest`)

| Code | Concern Category | Primary Count | Primary Share (% of comments, sums to 100%) | Any-Mention Count | Any-Mention Share (% of comments) |
|---|---|---:|---:|---:|---:|
| `C1` | Novelty, prior art & differentiation from existing optical/electronic architectures | 99 | 8.5% | 153 | 13.2% |
| `C2` | Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding) | 69 | 6.0% | 119 | 10.3% |
| `C3` | Speed, throughput, latency & bandwidth bottlenecks | 68 | 5.9% | 130 | 11.2% |
| `C4` | Scalability, insertion/propagation loss, footprint & crosstalk | 104 | 9.0% | 181 | 15.6% |
| `C5` | Nonlinearity / 'all-optical' claims & O-E-O conversion | 40 | 3.5% | 68 | 5.9% |
| `C6` | Precision, noise, drift, stability & calibration | 94 | 8.1% | 169 | 14.6% |
| `C7` | Benchmarks, dataset scale & task difficulty (beyond toy XOR/Iris/MNIST) | 57 | 4.9% | 131 | 11.3% |
| `C8` | Fair comparison with electronic (GPU/ASIC) & photonic prior art | 75 | 6.5% | 197 | 17.0% |
| `C9` | Training method, in-situ vs offline optimization & layer ablation | 67 | 5.8% | 105 | 9.1% |
| `C10` | Experimental detail, hardware vs simulation boundary & reproducibility | 109 | 9.4% | 255 | 22.0% |
| `C11` | Device physics, fabrication tolerance, material properties & packaging | 49 | 4.2% | 120 | 10.4% |
| `C12` | Clarity, overclaim, terminology, figures & manuscript presentation | 218 | 18.8% | 415 | 35.8% |
| `C13` | Practicality, system integration, hybrid electronic overhead & deployment | 47 | 4.1% | 153 | 13.2% |
| `C14` | Theory, mathematical model rigour, equations & derivations | 63 | 5.4% | 179 | 15.4% |
| **Total** | **All referee comments** | **1159** | **100.0%** | **2375** | **204.9% (avg 2.05 codes/comment)** |

---

## 2. Wave 2 Concern Distribution (`133` Files, `1075` Referee Comments — `llm_calibrated_v2`)

| Code | Concern Category | Primary Count | Primary Share (% of comments, sums to 100%) | Any-Mention Count | Any-Mention Share (% of comments) |
|---|---|---:|---:|---:|---:|
| `C1` | Novelty, prior art & differentiation from existing optical/electronic architectures | 71 | 6.6% | 88 | 8.2% |
| `C2` | Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding) | 44 | 4.1% | 51 | 4.7% |
| `C3` | Speed, throughput, latency & bandwidth bottlenecks | 36 | 3.3% | 63 | 5.9% |
| `C4` | Scalability, insertion/propagation loss, footprint & crosstalk | 42 | 3.9% | 68 | 6.3% |
| `C5` | Nonlinearity / 'all-optical' claims & O-E-O conversion | 46 | 4.3% | 52 | 4.8% |
| `C6` | Precision, noise, drift, stability & calibration | 136 | 12.7% | 170 | 15.8% |
| `C7` | Benchmarks, dataset scale & task difficulty (beyond toy XOR/Iris/MNIST) | 74 | 6.9% | 85 | 7.9% |
| `C8` | Fair comparison with electronic (GPU/ASIC) & photonic prior art | 65 | 6.0% | 92 | 8.6% |
| `C9` | Training method, in-situ vs offline optimization & layer ablation | 35 | 3.3% | 52 | 4.8% |
| `C10` | Experimental detail, hardware vs simulation boundary & reproducibility | 111 | 10.3% | 139 | 12.9% |
| `C11` | Device physics, fabrication tolerance, material properties & packaging | 115 | 10.7% | 181 | 16.8% |
| `C12` | Clarity, overclaim, terminology, figures & manuscript presentation | 191 | 17.8% | 196 | 18.2% |
| `C13` | Practicality, system integration, hybrid electronic overhead & deployment | 15 | 1.4% | 24 | 2.2% |
| `C14` | Theory, mathematical model rigour, equations & derivations | 94 | 8.7% | 133 | 12.4% |
| **Total** | **All referee comments** | **1075** | **100.0%** | **1394** | **129.7% (avg 1.30 codes/comment)** |

---

## 3. Combined Corpus Concern Distribution (`191` Active Files / `194` Kept PR Files, `2234` Referee Comments)

| Code | Concern Category | Primary Count | Primary Share (% of comments, sums to 100%) | Any-Mention Count | Any-Mention Share (% of comments) |
|---|---|---:|---:|---:|---:|
| `C1` | Novelty, prior art & differentiation from existing optical/electronic architectures | 170 | 7.6% | 241 | 10.8% |
| `C2` | Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding) | 113 | 5.1% | 170 | 7.6% |
| `C3` | Speed, throughput, latency & bandwidth bottlenecks | 104 | 4.7% | 193 | 8.6% |
| `C4` | Scalability, insertion/propagation loss, footprint & crosstalk | 146 | 6.5% | 249 | 11.1% |
| `C5` | Nonlinearity / 'all-optical' claims & O-E-O conversion | 86 | 3.8% | 120 | 5.4% |
| `C6` | Precision, noise, drift, stability & calibration | 230 | 10.3% | 339 | 15.2% |
| `C7` | Benchmarks, dataset scale & task difficulty (beyond toy XOR/Iris/MNIST) | 131 | 5.9% | 216 | 9.7% |
| `C8` | Fair comparison with electronic (GPU/ASIC) & photonic prior art | 140 | 6.3% | 289 | 12.9% |
| `C9` | Training method, in-situ vs offline optimization & layer ablation | 102 | 4.6% | 157 | 7.0% |
| `C10` | Experimental detail, hardware vs simulation boundary & reproducibility | 220 | 9.8% | 394 | 17.6% |
| `C11` | Device physics, fabrication tolerance, material properties & packaging | 164 | 7.3% | 301 | 13.5% |
| `C12` | Clarity, overclaim, terminology, figures & manuscript presentation | 409 | 18.3% | 611 | 27.4% |
| `C13` | Practicality, system integration, hybrid electronic overhead & deployment | 62 | 2.8% | 177 | 7.9% |
| `C14` | Theory, mathematical model rigour, equations & derivations | 157 | 7.0% | 312 | 14.0% |
| **Total** | **All referee comments** | **2234** | **100.0%** | **3769** | **168.7% (avg 1.69 codes/comment)** |

---

## 4. Severity & Multi-Round Referee Outcome Breakdown

### 4.1 Severity Distribution (`major` / `minor` / `editorial`)

> **Confidence Caveat (`R9`):** Tuning `Set A` $\kappa = 0.7053$, Held-Out `Set B` $\kappa = 0.5020$ (`73.51%` exact match). Use Wave-1 human-curated shares (`58` files) as the primary benchmark and treat Wave-2 automated severity shares as an approximate extension.

| Subset | Total Comments | `major` | `minor` | `editorial` |
|---|---:|---:|---:|---:|
| **Wave 1 (`58` files)** | 1159 | 588 (50.7%) | 536 (46.2%) | 35 (3.0%) |
| **Wave 2 (`133` files)** | 1075 | 509 (47.3%) | 549 (51.1%) | 17 (1.6%) |
| **Combined (`191` active / `194` kept files)** | 2234 | 1097 (49.1%) | 1085 (48.6%) | 52 (2.3%) |
