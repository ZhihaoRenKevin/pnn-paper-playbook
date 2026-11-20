---
name: pnn-t1t2-benchmarking
description: Actionable T1/T2 PNN Benchmarking drafting and revision playbook calibrated on 113 Nature, Science, and Nature-subjournal research articles (+ 26 separated major reviews; 2.0x native-English-country prose weighting) with a live ALL-TIER (1,475 papers) factual SOTA bridge. Use whenever building a PNN energy/latency budget, GPU comparison, scaling crossover analysis, or competitor table.
---

# How to Build and Revise T1/T2 PNN Benchmarks (`pnn-t1t2-benchmarking`)

Use this skill to build **referee-proof energy, latency, precision, and GPU/ASIC benchmarks** that survive *Nature*/*Science* `C2` (energy boundary) and `C8` (fair electronic comparison) audits.
- **Benchmarking craft & prose**: Strictly T1 & T2 (`49` native-primary papers `weight=2.0`).
- **Factual competitor SOTA numbers**: ALL TIERS (`T1-T4`, `1,475` papers) via `scripts/pnn_benchmark_tool.py all-tier-sota`.

---

## 1. How to Build a Referee-Proof Benchmark From Scratch (5-Step Protocol)

### Step 1: Report All 4 Tiers of the Energy Accounting Boundary (Never Cherry-Pick Tier 1 Alone!)
Always build a small breakdown table (Main or SI Table) separating:
1. **Tier 1: Optical Core Only (`E_opt`)**: Laser optical power entering the chip / optical switching energy per MAC (`fJ-pJ/MAC`).
2. **Tier 2: Active Photonic Chip (`E_chip`)**: Tier 1 + laser wall-plug efficiency (`10-30%`) + on-chip heater/EO/PCM driver power + photodetector/TIA bias.
3. **Tier 3: Electrical I/O Boundary (`E_io`)**: Tier 2 + high-speed DAC + ADC + SerDes energy at matched bit precision (`ENOB`) and sampling rate.
4. **Tier 4: Full Wall-Plug System (`E_sys`)**: Tier 3 + control FPGA/MCU, memory access (SRAM/DRAM), and TEC thermal stabilization.

### Step 2: Decompose End-to-End Latency Honestly
Never quote optical time-of-flight (`10 ps`) as system latency! State:
`t_total = t_DAC/encode + t_modulator/settle + t_optical_TOF + t_PD/TIA + t_ADC + t_digital_readout/comm`
Explicitly separate **single-inference latency** from **steady-state pipelined throughput (`TOPS`)** and **weight-reconfiguration time** (crucial for thermo-optic `us` vs EO `ps` vs PCM `ns-us`!).

### Step 3: Compare Against a Named Electronic GPU/ASIC at Matched Precision & Task
- Name the exact chip (`NVIDIA A100`, `H100`, `RTX 4090`, `Jetson Orin`, or `Google TPU v4`), exact numerical precision (`INT4`/`INT8`/`FP16` matched to your measured optical `ENOB`), exact batch size (`batch=1` for low-latency edge vs batched for throughput), and exact benchmark dataset.
- Show the **Crossover Dimension `N*`**: Derive the minimum matrix size `N*` at which optical `O(N)` fan-out energy/latency beats electronic `O(N^2)` data movement, and state honestly whether your fabricated prototype is below or above `N*`.

### Step 4: Build a Two-Zone Competitor Table (Measured vs Projected Strictly Split)
Never mix a competitor's projected `1,000 TOPS/W` with another paper's measured `2.1 TOPS/W` in the same column! Use explicit columns: `Platform` | `Year` | `Measured Precision (ENOB)` | `Measured Core Energy` | `Measured System Energy (Boundary)` | `Measured Task & Accuracy (vs Digital)` | `Projected Scaling (Assumptions)`.

### Step 5: Pull Verified All-Tier Competitor Numbers Before Writing
```bash
python3 scripts/pnn_benchmark_tool.py all-tier-sota --task MNIST --top 8
python3 scripts/pnn_benchmark_tool.py all-tier-sota --platform MZI --param energy --top 8
```

---

## 2. How to Revise Weak Benchmarking Prose (Concrete Before -> After)
- **Before (Guaranteed `C2`/`C8` Rejection)**:
  > *"Our photonic chip achieves an ultra-low energy consumption of 0.25 pJ/MAC and 50 ps latency, which is dramatically faster and 100x more energy-efficient than commercial GPUs, proving its versatile superiority for AI."*
- **After (Authoritative T1/T2 Native-Grade Benchmark)**:
  > *"Within the optical core, matrix multiplication consumes 0.25 pJ per MAC at 50 ps time-of-flight latency (Tier 1). Accounting for laser wall-plug efficiency (20%), thermo-optic holding power (18 mW per channel), and 8-bit DAC/ADC conversion overhead yields a measured prototype system efficiency of 1.8 TOPS/W at 6.1-bit effective precision on held-out Fashion-MNIST (91.4%, on par with the 92.1% 6-bit digital baseline; Supplementary Table 2). For matrix widths N <= 32, prototype efficiency remains limited by off-chip electrical I/O rather than photonic propagation; scaling to N = 256 with 3D CMOS co-packaging amortizes DAC/ADC overhead to a projected 42 TOPS/W, surpassing an NVIDIA A100 operating at matched INT8 precision for batch-1 low-latency inference."*

### Mandatory CLI Audit Gate
```bash
python3 scripts/pnn_benchmark_tool.py audit path/to/benchmark_section.txt
python3 scripts/pnn_benchmark_tool.py table-schema --tier T1
python3 scripts/pnn_benchmark_tool.py query --tier T1 --native-only --top 3
```

---

## 3. Compact Pass/Fail Checklist
- [ ] Every energy figure specifies its exact boundary (Tier 1 Optical Core vs Tier 2-4 Chip/System).
- [ ] Latency separates optical propagation, weight reconfiguration, and electrical I/O.
- [ ] Named GPU/ASIC comparator runs at matched bit precision, batch size, and task.
- [ ] Measured prototype values and projected scaled values are separated in both prose and tables.
- [ ] Competitor numbers verified against the all-tier (`1,475`-paper) SOTA ledger.

## 4. References & CLI
- T1/T2 craft exemplars (`weight=2.0` native-first): [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md), [`references/t1t2_benchmark_corpus.jsonl`](./references/t1t2_benchmark_corpus.jsonl), and separated review taxonomy [`references/t1t2_review_benchmark_taxonomy.jsonl`](./references/t1t2_review_benchmark_taxonomy.jsonl).
