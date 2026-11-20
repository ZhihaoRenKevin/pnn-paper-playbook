---
name: pnn-t1t2-abstract
description: Actionable T1/T2 PNN Title and Abstract drafting and revision playbook calibrated exclusively on 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 or review dilution). Use whenever drafting a PNN title/abstract from scratch or revising a weak draft to Nature/Science standard.
---

# How to Write and Revise a T1/T2 PNN Title and Abstract (`pnn-t1t2-abstract`)

Use this skill as an active **drafting and revision coach**, not a statistics summary. Craft rules come strictly from `113` published T1/T2 research articles (`49` native-English-country primary papers weighted `2.0x`; `0` T3/T4).

---

## 1. How to Write From Scratch (5-Minute Blueprint)

### Step 1: Collect 6 Mandatory Inputs Before Writing Sentence 1
1. **Target Claim Class** (`A` new primitive, `B` scale-up architecture, `C` training paradigm, `D` diffractive/metasurface, `E` application system, `F` physical bound/Ising, `G` analog wave math).
2. **Single Sharp Physical Bottleneck** (e.g., `O(N^2)` MZI cascade loss, O-E-O ADC/DAC energy wall, volatile thermal holding power, offline model mismatch).
3. **Platform + Core Mechanism** (1 line: material/chip + physical degree of freedom that breaks the bottleneck).
4. **Device/Primitive Measured FOM** (number + unit + speed/precision + reference target).
5. **System Task Result + Matched Baseline** (measured task accuracy/latency/throughput paired with its digital or electronic baseline).
6. **Exact Accounting Boundary & Evidence Tag** (`optical core` vs `chip electrical I/O` vs `wall-plug system`; `measured hardware` vs `hardware-calibrated numerical emulation`).

### Step 2: Draft the Title (Target 7-10 Words, Zero Colons)
- **Rule**: Never use `Name: Subtitle` (`0.0%` colon rate in T1/T2). Reveal your coined short name in Abstract S3 instead.
- **Pick 1 of 4 Proven Title Patterns**:
  1. **Capability + Platform**: `[System/Chip] for [Concrete High-Impact Capability]` (e.g., `All-analog photoelectronic chip for high-speed vision tasks`)
  2. **Platform + Enabling Method**: `[Photonic Architecture] trained with [Physical Method]` (e.g., `Integrated photonic neural network with on-chip backpropagation training`)
  3. **Physical Claim**: `[Physical Property] enhances/enables [Photonic Computing Capability]` (e.g., `Partial coherence enhances parallelized photonic computing`)
  4. **Regime Number + Architecture** (only if the number defines a new measured physical regime): `[Measured Regime Number] [Platform] for [Task]` (e.g., `11 TOPS photonic convolutional accelerator for optical neural networks`)

### Step 3: Draft the 7-Sentence Abstract (Target 150-195 Words)
Write strictly in this sequence:
1. **S1 (14-20w) Domain Context**: State the computing or physical task and why optics matters. Never open with `"In today's rapidly evolving AI era..."` or `"ChatGPT"`.
2. **S2 (16-24w) Physical Bottleneck**: Pivot with `However,` and state the exact physical law limiting prior optical hardware (`limited by`, `bound by`, `at the expense of`, not `suffer from`).
3. **S3 (16-24w) Breakthrough Anchor**: `"Here we demonstrate/propose [Full Technology Name] ([SHORT]), a [platform] that [circumvents/breaks S2 bottleneck]."`
4. **S4 (18-26w) Physical Mechanism**: Explain in concrete physics how the hardware executes the linear operator, weight storage, or nonlinear/training step (`imparts`, `decouples`, `harnesses`, `encodes`).
5. **S5 (15-22w) Measured Primitive Metric**: State the chip-level FOM with units inline in parentheses next to the noun (`bit precision`, `loss`, `bandwidth`, `switching energy`).
6. **S6 (18-28w) System Benchmark + Baseline + Boundary**: Report measured task accuracy next to its digital baseline (`93.3% compared with 94.0% digital`) AND state the exact energy/latency accounting boundary (`optical core` vs `wall-plug`). If any larger task uses emulation, explicitly tag it `"hardware-calibrated numerical emulation"`.
7. **S7 (14-20w) Grounded Horizon Closer**: State one concrete scaling or application regime unlocked by the demonstrated physics. Zero hype adjectives.

---

## 2. How to Revise an Existing Draft (4-Pass Surgery)

### Pass 1: Structural & Credibility Surgery
- **Cut title colons and filler adjectives** (`Novel`, `High-Performance`, `Smart`, `Versatile`).
- **Move the physical bottleneck to S2**: If the draft delays the gap until S4 or the Introduction, pull it into S2 right after S1.
- **Pair every naked number**: Add the matched digital/electronic comparator and energy boundary to every accuracy, TOPS, and pJ/MAC figure.
- **Separate measured vs emulated claims**: Never write `"our chip classifies ImageNet"` if ImageNet ran in a hardware-calibrated simulator.

### Pass 2: Native High-Register Vocabulary & Grammar Upgrade
Apply these direct substitutions (calibrated from `49` US/UK/CA/AU T1/T2 papers weighted `2.0x`):
- Replace `suffer from [problem]` -> `are limited by` / `are bound by` / `incur [penalty]`.
- Replace repeated `achieve` / `propose` / `realize` -> `attain`, `yield`, `afford`, `impart`, `circumvent`, `demonstrate`.
- Replace `dramatically` / `hugely` / `versatile` -> exact factor (`by 14x`, `by two orders of magnitude`) or explicit operating modes.
- Tuck a real prototype constraint inline using `albeit` or `while` instead of adding a defensive disclaimer sentence (`"We do not claim..."`).
- Place quantitative specs inline in parentheses right next to the noun (`"64 thermo-optic phase shifters (1550 nm)"`).

### Pass 3: Concrete Before -> After Rewrites
- **Before (Weak T3 / AI-Flavored Title & S1-S3)**:
  > *"OMDNN: A Novel Versatile On-Chip Programmable Diffractive Deep Neural Network for AI. In recent years, rapidly growing AI models have attracted tremendous attention. However, current photonic chips suffer from huge footprint and dramatic loss. To this end, we propose a transformative OMDNN chip that empowers ultra-low-power computing with 0.3 pJ/MAC."*
- **After (Crisp T1/T2 Native-Grade Title & S1-S3)**:
  > *"Programmable silicon slab-diffractive processor for integrated optical inference. Photonic integrated circuits offer sub-nanosecond latency for matrix-heavy neural inference. However, cascaded Mach-Zehnder meshes are limited by quadratic footprint and insertion-loss scaling as network width grows. Here we demonstrate a programmable silicon diffractive core (SlabCore) that imparts reconfigurable phase modulation across 64 thermo-optic elements within a single planar slab. The chip attains 93.3% held-out classification accuracy, on par with the 94.0% matched digital model, while operating at 0.34 pJ per MAC within the optical core."*

### Pass 4: Mandatory CLI Verification Gate
Run the local zero-dependency linter before returning any drafted or revised abstract:
```bash
python3 scripts/pnn_abstract_tool.py lint path/to/abstract.txt --tier T1
python3 scripts/pnn_abstract_tool.py query --tier T1 --native-only --top 3
```
Pair with `low-aigc-nondefensive-writing/scripts/aigc_nondefensive_auditor.py audit` and `vocab-upgrade` to guarantee `AIGC Risk < 20`, `Defensiveness < 15`, and `0` em-dashes.

---

## 3. Compact Pass/Fail Checklist
- [ ] Title is `<=10` words (T1) or `<=12` words (T2), zero colons, zero unmeasured numbers.
- [ ] Abstract is `145-195` words (T1) or `150-210` words (T2) in `6-8` sentences.
- [ ] S2 names the exact physical bottleneck; S3 anchors the chip/method cleanly.
- [ ] Every metric has units, a comparator/baseline, and an explicit energy/evidence boundary.
- [ ] Zero em-dashes, zero AI hype (`transformative`, `seamless`, `empower`), zero defensive self-policing.

## 4. References & CLI
- Native-weighted exemplars: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_abstract_corpus.jsonl`](./references/t1t2_abstract_corpus.jsonl) (`49` native-primary `US/GB/CA/AU` `weight=2.0` sorted first).
