# PNN Visual Design & Color Palettes Playbook (`figure_archetypes.md`)

Distilled from **100% complete visual inspection of all 2,110 main figures across all 447 Tier 1 (`45` papers, `176` figures), Tier 2 (`126` papers, `503` figures), and Tier 3 (`276` papers, `1,431` figures) papers** (`2,026` rendered 150-dpi PNG pages in `_work/fig_png/*.png` inspected via PDF vector/bitmap scene-graph telemetry, pixel `#HEX` clustering, and local **RTX 5090 VLM/LLM `Qwen2.5-VL-7B` + `qwen2.5:14b`**) plus **published peer-review files**. Use this playbook whenever diagnosing a draft manuscript's novelty angle, planning figure panel counts, or assigning **exact `#HEX` / `RGB` color palettes**.

---

## 0A. Empirical Visual Census Across All 2,110 T1–T3 Main Figures (`447` Papers)

| Figure Number | Inspected Count (T1–T3) | Mean / Median Sub-Panels | Measured Row Topology (`1-row` / `2-row` / `3-row` / `4+-row`) | 3D / Hardware Schematic Presence | Mean Aspect Ratio (`W:H`) | Mean Whitespace Fraction |
|---|---|---|---|---|---|---|
| **Fig. 1** | **447** | **3.2** / **3** | `1-row`: 36.9%, `2-row`: 34.7%, `3-row`: 19.5%, `4+-row`: 8.9% | **92.2%** (412/447) | `1.39:1` | `72.7%` |
| **Fig. 2** | **416** | **4.7** / **4** | `1-row`: 35.1%, `2-row`: 27.2%, `3-row`: 25.7%, `4+-row`: 12.0% | **20.0%** (83/416) | `1.54:1` | `74.5%` |
| **Fig. 3** | **414** | **4.7** / **4** | `1-row`: 33.1%, `2-row`: 24.9%, `3-row`: 26.6%, `4+-row`: 15.5% | **18.4%** (76/414) | `1.51:1` | `75.9%` |
| **Fig. 4** | **392** | **4.3** / **4** | `1-row`: 30.9%, `2-row`: 28.6%, `3-row`: 24.7%, `4+-row`: 15.8% | **20.7%** (81/392) | `1.50:1` | `75.6%` |
| **Fig. 5** | **257** | **4.0** / **4** | `1-row`: 35.0%, `2-row`: 25.3%, `3-row`: 26.8%, `4+-row`: 12.8% | **21.8%** (56/257) | `1.62:1` | `74.0%` |
| **Fig. 6** | **111** | **3.4** / **3** | `1-row`: 45.0%, `2-row`: 24.3%, `3-row`: 19.8%, `4+-row`: 10.8% | **22.5%** (25/111) | `1.58:1` | `75.3%` |

- **Empirical Takeaway 1 (Panel Count Ceiling)**: Across all 2,110 T1–T3 figures, the median sub-panel count is **3 panels for Fig. 1** and **4 panels for Figs. 2–5** (mean `3.2–4.7`). Any draft figure with `>8` sub-panels (`a–m` or `a–o`) is a severe outlier (`>95th` percentile) and must be consolidated by moving repetitive per-port calibration panels to SI.
- **Empirical Takeaway 2 (Whitespace & Breathing Room)**: Published T1–T3 figures maintain **`72%–76%` background whitespace** across the bounding canvas (`aspect ratio ~1.4:1 to 1.6:1`), preventing cramped text collisions.
- **Empirical Takeaway 3 (Measured Chromatic Family Dominance across 2,110 T1–T3 Figures)**: **Cobalt-Blue** (`73.1%` of figures, e.g. `#0466A4`, `#0069B0`), **Sky-Blue** (`70.0%`, e.g. `#B3D1E3`, `#6EA9CB`), **Coral-Red** (`59.3%`, e.g. `#ED1C24`, `#C83E4D`), **Amber-Orange** (`37.3%`, e.g. `#EC7C30`, `#D85218`), **Cyan-Teal** (`32.0%`, e.g. `#498995`, `#2A9D8F`), and **Gold-Yellow** (`30.2%`, e.g. `#EBAF1F`, `#D99B26`) form the canonical scientific palette of T1–T3 PNN papers.

---

## 0. Novelty Discovery & T4 $\to$ T1 Story-Elevation Playbook (创新点发掘与立意拔高方法论)

When a draft reads like an incremental T3/T4 engineering report, apply the published T1/T2 story-elevation patterns below before touching the figures:

| Formula | From Incremental T4 Framing (Avoid) | To T1/T2 *Nature* / *Nat. Photon.* Framing (Adopt) | In-Library T1/T2 Exemplars | Decisive Figure / Control Required |
|---|---|---|---|---|
| **1. Bug-to-Feature Inversion (逆转物理非理想性为计算机制)** | *"Partial coherence or multimode speckle degrades isolated channel weights, so we calibrate around it."* | *"Collective physical mode coupling enables parallel optical computation across partially coherent or disordered modes without $O(N^2)$ discrete waveguide wiring."* | `Nature_24V632_55` (Dong partial coherence); `Nature Computational Science_24V4_429` (Gigan disordered media); `Optica_23V10_339` (spatiotemporal chaos) | **Physics Ablation Panel**: Compare collective mode coupling vs full coherence or frozen random projection (`R1`/`R2`). |
| **2. Orthogonal Timescale / Mechanism Synergy (快慢多物理场解耦协同)** | *"Our photonic circuit combines fast modulation and non-volatile memory."* | *"Decoupling **GHz input modulation** from **non-volatile phase-change or ferroelectric weight storage** eliminates O-E-O weight-reload latency."* | `Nature_21V589_52` (Feldmann WDM $\times$ PCM); `Nature_26V657_377` (Pierangeli DOP); `Nature Communications_25V16_8329` (ferroelectric Pockels memory) | **Timescale Separation Plot**: Eye diagram / GHz RF modulation trace paired with multi-hour weight stability trace. |
| **3. System Bottleneck Kill-Shot (直击 ADC/DAC 墙与 $O(N^2)$ 级联损耗墙)** | *"Our chip has compact footprint and low insertion loss."* | *"Bypassing the **cascade loss and $O(N^2)$ phase-shifter wiring wall** of deep MZI meshes via a shallow distributed chiplet or all-analog front end."* | `Nature_23V623_48` (ACCEL ADC bypass); `Science_24V384_202` (Taichi shallow distributed path); `Nature_25V640_361` (Hua PACE latency wall) | **Scaling Comparison Scatter (Fig. 1 or Fig. 5)**: Footprint ($\text{mm}^2$), insertion loss (dB), and energy per OP vs matrix dimension $N\times K$. |
| **4. Naming Discipline (精准概念命名与避坑)** | Calling a 1-stage chip *"Deep Neural Network"* or claiming *"WDM parallelism"* when experiments use a single CW laser. | Use accurate architectural terms aligned with the measured hardware, and never depict unmeasured hardware (e.g., WDM DEMUX arrays) in Fig. 1. | `Nature Communications_22V13_1044` (IDNN); `Nature Communications_24V15_6189` (TDONN) | **Terminology Audit (`C12`)**: 100% alignment between Fig. 1 schematic components and Figs. 2–4 measured hardware. |

### Three-Question Diagnostic Workflow (改稿改图前必问三题)
1. **What is the physical bottleneck broken?** (Why did conventional architectures require $O(N^2)$ discrete elements or frequent O-E-O conversions, and how does the measured physical mechanism overcome that scaling?)
2. **What is the unassailable control experiment?** (Every hardware learning curve in Fig. 4 must sit next to: ① **Untrained optical core + trained digital readout**, ② **Input-bypass digital readout without optical core**, and ③ **Calibrated digital baseline** on the exact same train/val/test split.)
3. **Does every element drawn in Fig. 1 appear in the experimental Results?** (If an element in Fig. 1 was not physically measured in Figs. 2–4, **delete it from Fig. 1 immediately**.)

---

## 1. Exact `#HEX` / `RGB` Color Palettes for *Nature* / *Nature Photonics* Figures

Never mix device-material colors with optical-field or data-curve colors. Fix one palette in Fig. 1 and enforce it across Figs. 1–5 and SI:

### 1.1 3D Device & Layer Material Palette (器件与三维叠层标准色卡)
| Physical Layer / Component | Role in 3D Render & Cross-Section | Primary `#HEX` (`RGB`) | Edge / Highlight `#HEX` | Opacity (`alpha`) & Material Finish |
|---|---|:---:|:---:|:---:|
| **Silicon Core / Waveguide (`Si`)** | Waveguides, MZI arms, microrings & directional couplers | **`#1F5A82`** (`31, 90, 130` Deep Slate Blue) | `#3A86B7` | `1.00` (Matte satin, crisp bevel `0.5 px`) |
| **Upper Oxide Cladding (`SiO2` / `TOX`)** | Semi-transparent upper oxide cladding | **`#D9ECF7`** (`217, 236, 247` Ice Glass Blue) | `#9BC4E2` | **`0.18–0.25`** (Translucent glass) |
| **Buried Oxide (`BOX`)** | Insulating oxide layer beneath Si | **`#B8C7D4`** (`184, 199, 212` Cool Ash Blue-Grey) | `#8FA3B5` | `0.85` (Smooth matte) |
| **Silicon Substrate (`Si Sub`)** | Bottom mechanical base (`300 K` heat sink) | **`#6C757D`** (`108, 117, 125` Dark Neutral Slate) | `#495057` | `1.00` (Dark matte base) |
| **Thermo-Optic Microheaters (`TiN` / `Au`)** | Top-layer heater strips & routing pads | **`#D99B26`** (`217, 155, 38` Warm Champagne Gold) | `#F2C14E` | `1.00` (Metallic specular highlight) |
| **Electro-Optic Layer (`TFLN` / `BTO`)** | Electro-optic modulator waveguide | **`#2A9D8F`** (`42, 157, 143` Deep Teal) | `#52B788` | `0.90` (Semi-gloss crystal) |
| **Phase-Change Material (`PCM`: GST / Sb2Se3 / Sb2S3)** | Non-volatile weight patch (Crystalline vs Amorphous) | Crystalline: **`#9B2226`** (Ruby)<br>Amorphous: **`#EE9B00`** (Amber) | `#CA6702` | `1.00` (High-contrast patch) |

### 1.2 Data Curves, Benchmarks & Control Baselines Palette (数据曲线与对照基线色卡)
| Semantic Curve / Bar Role | Primary `#HEX` (`RGB`) | Shaded Error Band `#HEX` (`alpha=0.20`) | Line / Marker Style | Where Used |
|---|---|:---:|:---:|---|
| **1. This Work — Hardware Measured (实测硬件/在环训练)** | **`#C83E4D`** (`200, 62, 77` *Nature* Crimson Red) **or** **`#0072B2`** (`0, 114, 178` Deep Cobalt) | `#F2B8BE` or `#A6CEE3` | Solid line (`1.5 pt`), filled circles (`●`, `4.5 pt`) | Training accuracy/loss, port spectra, benchmark star (`★`) |
| **2. Physical Digital Twin / Full-Wave Simulation (物理模型/FDTD/MODE)** | **`#E07A5F`** (`224, 122, 95` Terracotta Coral) **or** **`#2A9D8F`** (`42, 157, 143` Teal) | `#F4CBC0` or `#B2E2DC` | Solid or long-dash line (`1.3 pt`), open diamonds (`◇`) | Mode dispersion, simulated vs measured transmission |
| **3. Untrained-Core Control (未训练核对照 + trained readout)** | **`#3D5A80`** (`61, 90, 128` Slate Navy) | `#B8C7D9` | Dashed line (`--`, `1.2 pt`), open squares (`□`) | Fig. 4 ablation proving active hardware optimization beats static core |
| **4. Input-Bypass / No-Optics Control (仅数字读出/无光核基线)** | **`#7F8C8D`** (`127, 140, 141` Neutral Grey) | `#D5DBDB` | Dotted line (`:`, `1.1 pt`), triangles (`△`) | Fig. 4 lower-bound baseline |
| **5. Secondary State / Comparison Channel (状态 B / 负向通道)** | **`#D97724`** (`217, 119, 36` Ochre Orange) vs **`#1F6F8B`** (`31, 111, 139` Cerulean) | `#F5D0A9` | Solid line (`1.3 pt`), filled squares (`■`) | Complementary channel or state comparison |

### 1.3 Physical Field Colormaps (二维物理场与矩阵专用色标 — 严禁混用)
- **Optical Intensity Field $|E(x,y)|^2$ or Transmission (dB)**: Use **`magma`** or **`inferno`** (black $\to$ deep purple $\to$ crimson $\to$ bright yellow-white) or single-hue **`Purples`/`Blues`** on white background. Never use `jet`.
- **Temperature Distribution $\Delta T(x,y,z)$ & Thermal Plumes**: Use **`YlOrRd`** or **`afmhot_r`** (pale cream $\to$ amber $\to$ deep red `#99000D`). **Never use the same colormap for both $|E|^2$ and $\Delta T$ in the same paper!**
- **Signed Differential Response $\Delta S$ or Signed Weights $W_{ij}$**: Use diverging **`RdBu_r`** (deep blue `#2166AC` = negative $\to$ pure white `#FFFFFF` = zero $\to$ deep red `#B2182B` = positive), with symmetric colorbar limits `[-max, +max]`.
- **Confusion Matrices**: Use sequential single-hue **`Blues`** (`#F7FBFF` $\to$ `#08306B`), printing integer sample counts in bold white on dark cells (`>50%` max) and dark navy `#1B263B` on light cells.
