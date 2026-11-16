# 新课题生成手册（Grounded Idea Playbook — v3.4 · R20）

本手册说明如何用 `scripts/pnn_research_toolkit.py idea-gen` 从已核验的十九类器件与系统参数表（`references/PNN_params/*_records.jsonl`）及确定性派生表（`references/derived/*.csv`）出发寻找立项切入点，并界定每一种配方的物理局限与人工核查义务。所有候选卡片仅依据命令行参数与本地静态表确定性生成，不调用任何生成式模型，也不包含任何未发表工作。

---

## 一、四种配方的定义、触发条件与局限

`idea-gen` 先依据 `--class` 与 `--function` 关键词子串求得目标类别集合（未给时取全部十九类；给了 `--function` 但未命中任何预设关键词时集合为空），再按四种配方生成排好序的候选表，并按 R1 → R2 → R3 → R4 顺序轮流取卡，直至达到 `--limit` 张数或候选耗尽。

1. **R1 实测覆盖稀薄（来源表：`device_coverage`；未指定 `--task` 时启用）**
   - **选行规则**：在 `device_coverage.csv` 中筛选类别属于目标集合、满足 `--platform` 或 `--material` 标签过滤条件且实测论文数在两篇及以下（`papers_with_measured <= 2`）的分支，按实测论文数、类别代号、标签字段名与标签字符串升序排列。
   - **物理与文献局限**：本库实测篇数稀少不等于学术界尚未实现。常见原因包括：① 相关工作因术语差异被归入同类的 `other` 标签或相邻类别（如光电突触归入 I1 而非 C1、激光器参数分记于 B2 与 G1）；② 商业化模块仅作输入加载或外围读出，按收录标准不计入本文自研器件实测；③ 该技术路线本身存在强物理制约（例如相位调制效率不足、自由载流子吸收过高或异质集成热预算冲突）。立项前必须先判别属于“真研究空白”还是“物理死胡同”。

2. **R2 仿真或预测显著领先实测（来源表：`device_parameter_atlas`；未指定 `--task` 时启用）**
   - **选行规则**：在 `device_parameter_atlas.csv` 中筛选具有明确优劣方向（`min` 或 `max`）且已有实测数值的行，要求 `best_simulated` 或 `best_predicted` 至少有一项为数值并显著优于实测极值——当单位为 `dB` 或 `dBm` 时领先幅度达到十个分贝单位及以上，其他单位下两者均为正数且比值达到十倍及以上；按实测论文数、类别代号、标签与参数升序排列。
   - **物理与文献局限**：全波或器件仿真常忽略光纤耦合损耗、波导侧壁粗糙度散射、电极寄生电容、热串扰与制造尺寸偏差，而 `predicted` 记录往往按器件本征带宽上限或理想单光子极限外推。必须回查实测与仿真记录各自的 `condition` 与 `note`，确认两者是否在相同波段、相同偏置及相同系统能量边界下比较，找到阻碍实验逼近理论值的真实工艺或电路瓶颈。

3. **R3 跨材料族迁移对照（来源表：`materials_atlas`；未指定 `--task` 且未指定 `--platform` 时启用）**
   - **选行规则**：在 `materials_atlas.csv` 中按（类别代号、参数、单位、优劣方向）分组，以组内已有实测记录中表现最优的材料族作为对照行（`contrast_row`），筛选同组内实测论文数在一篇及以下（`papers_measured <= 1`）且满足 `--material` 过滤条件的其他材料族作为迁移候选；按候选行的实测论文数、材料族名称、类别代号、参数与单位升序排列。
   - **物理与文献局限**：`materials_atlas.csv` 同时汇总了靠类别主标签归入与靠 `material_text` 文本匹配归入的记录（由 `papers_via_label` 区分，明细在 `materials_assignment.csv`）。若某条记录靠文本归入，该材料可能只是波导衬底、包层或片上探测器而非核心有源区；同时，将对照材料族的高指标迁移到新材料族时，必须核查目标波段吸收损耗、驱动电压或脉冲能量与现有光路及代工工艺的兼容性。

4. **R4 系统级 Benchmark 空白（来源表：`benchmark_ledger`；未指定 `--class`、`--function`、`--material` 时启用）**
   - **选行规则**：在 `benchmark_ledger.csv` 中排除汇总平台 `*`、`other` 以及未指明任务行，筛选实测论文数在一篇及以下（`papers_measured <= 1`）且满足 `--task`、`--platform` 过滤条件的（任务，平台）组合，按实测论文数、任务名与平台名升序排列。
   - **物理与文献局限**：`benchmark_ledger.csv` 仅统计 J 类准确率记录。衍射网络 E1 的分类准确率、储备池 F1 的时序预测误差、伊辛机 H1 的成功概率以及未进入 J 候选清单的传感内计算 I1 论文各自记录在本类表中；因此台账空白不代表该硬件路线从未演示过该任务。此外，单纯把旧硬件搬到新数据集若无架构或物理机制突破，难以支撑高档次期刊发表（见 `SKILL.md` §1 与 §14）。

---

## 二、卡片七个栏目的解读与使用者必补工作

每张候选卡固定输出七个栏目（机读模式 `--json` 输出对应的结构化字段）：

1. **`【1 空白】`（`row` 与 `contrast_row`）**：给出触发该卡片的派生表原行全部关键统计（R3 同时列出最优实测材料族对照行）。使用者应核查该行的单位组与记录数，确认不是单篇异常口径造成的假性空白。
2. **`【2 前作】`（`prior_work`）**：按实测极值、仿真极值、预测极值及同格其余记录的优先级列出最接近前作（同篇论文去重），附 `record_id`、文件名 `stem`、页码与 DOI。使用者必须回到 `references/PNN_params/<代号>_records.jsonl` 与原文核对完整段落、实验装置及 `condition`、`note` 字段，在引言与对比表中正面引用并具体区分这些最近似工作（C1）。
3. **`【3 器件参数】`（`target_params`）**：列出同类别同标签（不足时补全类 `*` 汇总行；R3 取对照材料族同类别行；R4 取 J 类对应平台行）的实测中位数（`measured_median`）与实测极值（`best_measured`，带 `record_id`）。立项定指标时，实测中位数代表领域常规基线，实测极值代表单项竞争前沿；严禁把不同器件在不同偏置或波段下测得的单项极值拼成不自洽的指标组合。
4. **`【4 审稿人会问】`（`reviewer`）——使用者须补充具体抗辩与实验设计**：
   - 工具仅按配方列出四项高频审稿关切编号及标题（R1 对应 C10、C11、C6、C1；R2 对应 C10、C6、C4、C12；R3 对应 C11、C1、C4、C2；R4 对应 C7、C8、C9、C10）。
   - **使用者必须补充三项内容**：① 打开 `references/reviewer_playbook.md` 查阅对应编号的真实审稿人批评原话与高解决率策略（优先采用补硬件实验 R1、补公平对比表 R3、诚实收缩声明边界 R5 与补解析误差推导 R6，避免无新证据的纯文字争辩 R8）；② 运行 `python scripts/pnn_research_toolkit.py referee-simulator` 逐项落实 `R18b` 首轮必查清单（新材料体系的能谱衍射拉曼与母相空白对照、热串扰随间距衰减与规模上限、全阵列电镜图与光纤到光纤插损分解及单元均匀性统计、与单篇最接近前作的机制对比）；③ 预先把物理消融对照（如去掉光学核心、关闭泵浦或注入扰动后的性能退化，见 `SKILL.md` §5）和四级能量边界表（`SKILL.md` §18）纳入实验计划。
5. **`【5 最小验证实验】`（`experiments`）**：给出 `benchmark_ledger.csv` 中对应平台实测篇数最多的代表任务，或 R4 任务的全平台汇总基线。若卡片属于纯器件或模拟运算类别而无台账映射平台，使用者须按 `SKILL.md` §1.1 补齐该类别的硬件级与网络级双重验证（不仅测单器件传递曲线、噪声等效位数与漂移，还须在至少一项非平凡任务上与同精度数字基线同划分对比）。
6. **`【6 投稿档次】`（`tiers`）**：显示库内同格论文所在的期刊分档计数（`papers_by_tier` 或 `measured_papers_by_tier`）。目标档次必须结合 `SKILL.md` §1 与 §14 独立判断：冲击高档次期刊须具备系统级硬件闭环或颠覆性物理机制、完整的端到端延时与能效实测对比及物理消融实验；若仅有仿真改进或单一静态器件表征，应下调预期档次。
7. **`【7 库外查新】`（`search_queries`）——使用者须在给出 idea 前完成联网查新**：
   - 工具仅生成包含当前行核心词的基础检索式，并提示必做库外检索。
   - **使用者必须补充四步查新**：① 在向合作者或文稿输出任何新课题建议前，联网检索 Google Scholar、Web of Science、arXiv、Optica、IEEE Xplore（含顶会论文）及专利数据库在本库下载截止日之后的最新进展；② 扩展材料化学式别名、器件结构全称与缩写、任务同义词进行组合检索；③ 用 `lit-search`、`atlas`、`coverage` 交叉检索本库相邻类别是否已有同类演示；④ 严格遵守保密与学术规范——用户本人未发表的研究内容绝不写入任何文件，未经完整联网核查严禁使用“首次”等排他性表述。

---

## 三、三个固定运行示例

### 示例一：按材料查询（`--material Sb2Se3 --limit 3`）

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

### 示例二：按功能查询（`--function activation --limit 3`）

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

### 示例三：按任务与平台查询（`--task Fashion-MNIST --platform MZI --limit 3`）

```text
$ python scripts/pnn_research_toolkit.py idea-gen --task Fashion-MNIST --platform MZI --limit 3
classes: A1, A2, A3, A4, A5, A6, B1, B2, C1, D1, D2, E1, E2, E3, F1, G1, H1, I1, J
no idea card for these filters: no recipe applies, or every matching branch already has 2 or more measured papers (check `benchmark` / `coverage` / `atlas` for the measured state)
```
