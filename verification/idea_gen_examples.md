# Grounded Idea Generation Verification Examples (v3.4 — R20)

本文件保存 `scripts/pnn_research_toolkit.py idea-gen` 三个固定验证查询的完整标准输出，全部数据均由工具从 `references/derived/` 与 `references/PNN_params/` 确定性读取生成。

## 1. 材料迁移查询（`--material Sb2Se3 --limit 3`）

```text
$ python scripts/pnn_research_toolkit.py idea-gen --material Sb2Se3 --limit 3
classes: A1, A2, A3, A4, A5, A6, B1, B2, C1, D1, D2, E1, E2, E3, F1, G1, H1, I1, J

## Card 1 [R3 · materials_atlas]
【1 空白】
- recipe: R3 | material_family: Sb2Se3 | code: A3 | param: levels (bits, direction: max) | papers_measured: 0 | best_measured:  ()
- contrast_row: material_family: GST (Ge2Sb2Te5 and doped GST) | code: A3 | param: levels (bits) | papers_measured: 1 | best_measured: 5 (exceeding 5 bits, A3-7dde1ba5bd9f)
【2 前作】
- A3-4dc4c3c54aa6 | Advanced Optical Materials_26V14_11_2502670_High‐Precision, Large‐Bandwidth, Multimode Nonvolatile Photonic Neural Network Based on Phase‐Change Metasurface | page: 2 | doi: 10.1002/adom.202502670
- A3-06eb1a743971 | Laser & Photonics Reviews_25V20_6_2501846_Back‐End‐Of‐Line Integrated Non‐Volatile Reconfigurable Devices for Programmable Photonic Integrated Circuits | page: 7 | doi: 10.1002/lpor.202501846
- A3-21437a377eab | Advanced Photonics_23V5_046004_Electrically programmable phase-change photonic memory for optical neural networks with nanoseconds in situ training capability | page: 4 | doi: 10.1117/1.ap.5.4.046004
- A3-5af30f0a7fac | Optica_26V13_2228_Nonvolatile photonic emulator based on phase-change coupled waveguide arrays | page: 1 | doi: 10.1364/optica.605248
- A3-60efdcd91d64 | Nature Nanotechnology_22V17_842_Ultra-low-energy programmable non-volatile silicon photonics based on phase-change materials with graphene heaters | page: 6 | doi: 10.1038/s41565-022-01153-w
【3 器件参数】
- GST (Ge2Sb2Te5 and doped GST) | A3 | pulse_width (μs, min) | papers_measured: 37 | median: 0.1 | best: 3.5e-08 (35 fs, A3-dd691bc45b63)
- GST (Ge2Sb2Te5 and doped GST) | A3 | switching_energy (pJ, min) | papers_measured: 28 | median: 502.5 | best: 0.224 (224 fJ to 3.8 pJ, A3-f0fd89de9b93)
- GST (Ge2Sb2Te5 and doped GST) | A3 | levels (levels, max) | papers_measured: 23 | median: 14.5 | best: 256 (more than 8 bits, A3-c5f062e64563)
- GST (Ge2Sb2Te5 and doped GST) | A3 | endurance (cycles, max) | papers_measured: 21 | median: 100 | best: 1e+07 (more than 107, A3-dcbf4d5b956b)
- GST (Ge2Sb2Te5 and doped GST) | A3 | contrast (%, max) | papers_measured: 20 | median: 30 | best: 300 (larger than 300%, A3-5de12d0ad935)
- GST (Ge2Sb2Te5 and doped GST) | A3 | contrast (dB, max) | papers_measured: 16 | median: 10.195 | best: 31.2 (31.2 dB, A3-a0b310aaee6f)
【4 审稿人会问】
- C11: Device physics, fabrication tolerance, material properties & packaging
- C1: Novelty, prior art & differentiation from existing optical/electronic architectures
- C4: Scalability, insertion/propagation loss, footprint & crosstalk
- C2: Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding)
【5 最小验证实验】
- task: MNIST | platform: PCM | papers_measured: 5 | papers_simulated: 8 | median: 91 | best: 99.37% (J-442eebe84ee2)
- task: object / scene / pattern / texture recognition (other datasets) | platform: PCM | papers_measured: 2 | papers_simulated: 1 | median: 95.2 | best: 96.4% (J-e39b9bb5d1cd)
- task: CIFAR-10 | platform: PCM | papers_measured: 1 | papers_simulated: 1 | median: 82 | best: 82% (J-fc3202029704)
【6 投稿档次】
- library_tiers: (none)
- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。
【7 库外查新】
- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：
- "Sb2Se3" "levels" photonic device experiment
- "Sb2Se3" integrated photonics optical computing

## Card 2 [R3 · materials_atlas]
【1 空白】
- recipe: R3 | material_family: Sb2Se3 | code: A5 | param: linewidth (nm, direction: min) | papers_measured: 0 | best_measured:  ()
- contrast_row: material_family: Si (SOI, doped, amorphous) | code: A5 | param: linewidth (nm) | papers_measured: 12 | best_measured: 0.019 (FWHM - 0.019 - nm, A5-1de64eff20b7)
【2 前作】
- A5-587c65ad6bfa | Laser & Photonics Reviews_25V20_6_2501846_Back‐End‐Of‐Line Integrated Non‐Volatile Reconfigurable Devices for Programmable Photonic Integrated Circuits | page: 4 | doi: 10.1002/lpor.202501846
【3 器件参数】
- Si (SOI, doped, amorphous) | A5 | channel_count (rings, max) | papers_measured: 44 | median: 10 | best: 256 (16 × 16, A5-79ae3890e698)
- Si (SOI, doped, amorphous) | A5 | extinction_ratio (dB, max) | papers_measured: 35 | median: 20 | best: 55 (55 dB, A5-660fad46d799)
- Si (SOI, doped, amorphous) | A5 | Q_factor (, max) | papers_measured: 28 | median: 11500 | best: 226000 (~226 K, A5-4ce7bf429fbd)
- Si (SOI, doped, amorphous) | A5 | weight_precision (bit, max) | papers_measured: 21 | median: 5.64 | best: 9.7 (approximately 9.7 bits, A5-6eec16ac21f0)
- Si (SOI, doped, amorphous) | A5 | linewidth (nm, min) | papers_measured: 12 | median: 0.173 | best: 0.019 (FWHM - 0.019 - nm, A5-1de64eff20b7)
- Si (SOI, doped, amorphous) | A5 | channel_count (channels, max) | papers_measured: 9 | median: 6 | best: 16 (16-channel, A5-b3a85d551b0e)
【4 审稿人会问】
- C11: Device physics, fabrication tolerance, material properties & packaging
- C1: Novelty, prior art & differentiation from existing optical/electronic architectures
- C4: Scalability, insertion/propagation loss, footprint & crosstalk
- C2: Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding)
【5 最小验证实验】
- task: MNIST | platform: MRR_WDM | papers_measured: 19 | papers_simulated: 18 | median: 94.8 | best: 98.2% (J-bc3d3ee1d709)
- task: RF / radar / wireless | platform: MRR_WDM | papers_measured: 5 | papers_simulated: 3 | median: 92.8 | best: 99.8% (J-16d17da670c8)
- task: medical imaging | platform: MRR_WDM | papers_measured: 4 | papers_simulated: 1 | median: 89.635 | best: 96% (J-49bf4ec4cb2b)
【6 投稿档次】
- library_tiers: (none)
- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。
【7 库外查新】
- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：
- "Sb2Se3" "linewidth" photonic device experiment
- "Sb2Se3" integrated photonics optical computing

## Card 3 [R3 · materials_atlas]
【1 空白】
- recipe: R3 | material_family: Sb2Se3 | code: E2 | param: bandwidth (nm, direction: max) | papers_measured: 0 | best_measured:  ()
- contrast_row: material_family: Si (SOI, doped, amorphous) | code: E2 | param: bandwidth (nm) | papers_measured: 12 | best_measured: 6000 (7.5- to 13.5-μm, E2-fef0c8056636)
【2 前作】
- E2-b9ba214e3fb0 | Light Science & Applications_25V14_182_Nonlocal phase-change metaoptics for reconfigurable nonvolatile image processing | page: 4 | doi: 10.1038/s41377-025-01841-x
【3 器件参数】
- Si (SOI, doped, amorphous) | E2 | bandwidth (nm, max) | papers_measured: 12 | median: 60 | best: 6000 (7.5- to 13.5-μm, E2-fef0c8056636)
- Si (SOI, doped, amorphous) | E2 | resolution (μm, min) | papers_measured: 12 | median: 5.695 | best: 2 (smallest width of approximately 2 μm, E2-eafaddf856fb)
- Si (SOI, doped, amorphous) | E2 | efficiency (%, max) | papers_measured: 9 | median: 44 | best: 81 (transmission ≈81%, E2-4ddc593904f6)
- Si (SOI, doped, amorphous) | E2 | NA (NA, max) | papers_measured: 8 | median: 0.27 | best: 0.35 (numerical apertures above 0.35, E2-ce33da1e547c)
- Si (SOI, doped, amorphous) | E2 | resolution (lp/mm, max) | papers_measured: 2 | median: 146 | best: 228 (up to 228.0 lp/mm (line width of 2.19 μm), E2-daaf30002b96)
- Si (SOI, doped, amorphous) | E2 | resolution (cy/mrad, max) | papers_measured: 1 | median: 0.0645 | best: 0.076 (0.076 cy/mrad, E2-56dec4434056)
【4 审稿人会问】
- C11: Device physics, fabrication tolerance, material properties & packaging
- C1: Novelty, prior art & differentiation from existing optical/electronic architectures
- C4: Scalability, insertion/propagation loss, footprint & crosstalk
- C2: Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding)
【5 最小验证实验】
- (no mapped benchmark_ledger platform for this class)
【6 投稿档次】
- library_tiers: (none)
- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。
【7 库外查新】
- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：
- "Sb2Se3" "bandwidth" photonic device experiment
- "Sb2Se3" integrated photonics optical computing
```

## 2. 功能类别查询（`--function activation --limit 3`）

```text
$ python scripts/pnn_research_toolkit.py idea-gen --function activation --limit 3
classes: D1, D2

## Card 1 [R1 · device_coverage]
【1 空白】
- recipe: R1 | code: D2 (optoelectronic nonlinear activation) | platform: PD_amplifier | papers: 2 | papers_with_measured: 1 | sim_or_pred_only: 1 | records: 7
【2 前作】
- D2-285ae4bbfe44 | ACS Photonics_24_Neuromorphic Network with Photonic Weighting and Photoelectronic Nonlinear Activation Based on SOA and APD | page: 3 | doi: 10.1021/acsphotonics.4c01083
- D2-3e22cb27a47f | Photonics Research_23V12_85_Scalable orthogonal delay-division multiplexed OEO artificial neural network trained for TI-ADC equalization | page: 13 | doi: 10.1364/prj.493888
【3 器件参数】
- D2 | platform: PD_amplifier | bandwidth (GHz, max) | papers_measured: 1 | median: 8 | best: 8 (8 GHz, D2-8e5277d7c49c)
- D2 | *: * | bandwidth (GHz, max) | papers_measured: 8 | median: 1.7025 | best: 12 (more than 12 GHz, D2-b3d8f6181f43)
- D2 | *: * | energy_per_activation (fJ, min) | papers_measured: 3 | median: 100 | best: 3.2 (3.2 fJ bit–1, D2-ed5c7a553cf4)
【4 审稿人会问】
- C10: Experimental detail, hardware vs simulation boundary & reproducibility
- C11: Device physics, fabrication tolerance, material properties & packaging
- C6: Precision, noise, drift, stability & calibration
- C1: Novelty, prior art & differentiation from existing optical/electronic architectures
【5 最小验证实验】
- (no mapped benchmark_ledger platform for this class)
【6 投稿档次】
- library_tiers: T4:2
- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。
【7 库外查新】
- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：
- "PD_amplifier" "optoelectronic nonlinear activation" photonic computing experiment
- "PD_amplifier" optical neural network hardware demonstration

## Card 2 [R2 · device_parameter_atlas]
【1 空白】
- recipe: R2 | code: D1 (all-optical nonlinear elements) | material: thermo_optic_bistable | param: threshold (W/cm2, direction: min) | papers_measured: 1 | best_measured: 10000 (0.1 mW/ μm2, D1-a15fa97fb0aa) | best_simulated: 630 (D1-5c9665e9d123) | best_predicted:  ()
【2 前作】
- D1-a15fa97fb0aa | Nano Letters_26V26_1403_High-Resolution and Ultralow-Power Nonlinear Image Processing with Passive High-Quality Factor Metasurfaces | page: 6 | doi: 10.1021/acs.nanolett.5c05424
- D1-7b5b2e28e7a9 | Nature Nanotechnology_26V21_932_Optical multistability in a compact microcavity enabled by near-exceptional coupling | page: 6 | doi: 10.1038/s41565-026-02197-y
【3 器件参数】
- D1 | material: thermo_optic_bistable | threshold (W/cm2, min) | papers_measured: 1 | median: 52000 | best: 10000 (0.1 mW/ μm2, D1-a15fa97fb0aa)
- D1 | material: thermo_optic_bistable | threshold (mW, min) | papers_measured: 1 | median: 0.24 | best: 0.24 (240 μW, D1-7b5b2e28e7a9)
- D1 | *: * | threshold (mW, min) | papers_measured: 12 | median: 0.0049 | best: 2.4e-05 (24 nW, D1-98dbe23d2ff6)
- D1 | *: * | response_time (ps, min) | papers_measured: 11 | median: 4.625 | best: 0.018 (~18 fs, D1-e11b17c4633b)
- D1 | *: * | threshold (pJ, min) | papers_measured: 8 | median: 0.08 | best: 0.00042 (0.42 and 0.66 fJ, D1-4c41b56d9854)
- D1 | *: * | modulation_depth (%, max) | papers_measured: 6 | median: 31.35 | best: 80.9 (80.9%, D1-1303d8e23d7a)
【4 审稿人会问】
- C10: Experimental detail, hardware vs simulation boundary & reproducibility
- C6: Precision, noise, drift, stability & calibration
- C4: Scalability, insertion/propagation loss, footprint & crosstalk
- C12: Clarity, overclaim, terminology, figures & manuscript presentation
【5 最小验证实验】
- (no mapped benchmark_ledger platform for this class)
【6 投稿档次】
- library_tiers: T4:1
- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。
【7 库外查新】
- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：
- "thermo_optic_bistable" "threshold" photonic device measured
- "thermo_optic_bistable" "all-optical nonlinear elements" optical computing hardware

## Card 3 [R3 · materials_atlas]
【1 空白】
- recipe: R3 | material_family: 2D semiconductors (all: TMDs, BP, In2Se3, MXene …) | code: D2 | param: energy_per_activation (fJ, direction: min) | papers_measured: 0 | best_measured:  ()
- contrast_row: material_family: III-V (InP, GaAs, InGaAs, AlGaAs, GaN, AlN …) | code: D2 | param: energy_per_activation (fJ) | papers_measured: 2 | best_measured: 3.2 (3.2 fJ bit–1, D2-ed5c7a553cf4)
【2 前作】
- D2-a1409a8be6de | Nature Communications_24V15_2433_Broadband nonlinear modulation of incoherent light using a transparent optoelectronic neuron array | page: 8 | doi: 10.1038/s41467-024-46387-5
【3 器件参数】
- III-V (InP, GaAs, InGaAs, AlGaAs, GaN, AlN …) | D2 | bandwidth (GHz, max) | papers_measured: 2 | median: 5.65 | best: 8 (8 GHz, D2-8e5277d7c49c)
- III-V (InP, GaAs, InGaAs, AlGaAs, GaN, AlN …) | D2 | energy_per_activation (fJ, min) | papers_measured: 2 | median: 101.6 | best: 3.2 (3.2 fJ bit–1, D2-ed5c7a553cf4)
【4 审稿人会问】
- C11: Device physics, fabrication tolerance, material properties & packaging
- C1: Novelty, prior art & differentiation from existing optical/electronic architectures
- C4: Scalability, insertion/propagation loss, footprint & crosstalk
- C2: Energy accounting & wall-plug power boundary (lasers, DAC/ADC, TIA, thermal holding)
【5 最小验证实验】
- (no mapped benchmark_ledger platform for this class)
【6 投稿档次】
- library_tiers: (none)
- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。
【7 库外查新】
- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：
- "2D semiconductors" "energy_per_activation" photonic device experiment
- "2D semiconductors" integrated photonics optical computing
```

## 3. 任务与平台组合查询（`--task Fashion-MNIST --platform MZI --limit 3`）

```text
$ python scripts/pnn_research_toolkit.py idea-gen --task Fashion-MNIST --platform MZI --limit 3
classes: A1, A2, A3, A4, A5, A6, B1, B2, C1, D1, D2, E1, E2, E3, F1, G1, H1, I1, J
no idea card for these filters: no recipe applies, or every matching branch already has 2 or more measured papers (check `benchmark` / `coverage` / `atlas` for the measured state)
```
