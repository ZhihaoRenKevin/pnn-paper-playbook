# PNN 器件参数表（PNN_params）

> **说明**：记录表不含论文原句。核对数值时，按 `page`（`src` 为 `s` 时是 SI 页码）和 `references/citations.csv` 里的 DOI 查原文。`record_id` 是抽取时用含原句的完整记录算出的，这里只作编号用，不能复算。文中提到的 `00_Index\`、`fulltext\`、`check\` 等文件夹和各个脚本压缩包属于原始文库，不随数据分发。

写入：2026-10-29 / 10-30（新加坡时间；10-30 下午做了最后合并，晚上按独立抽查和标题 / 摘要补查的结果修订，见第 26 节）　写入者：下载 agent（逐篇人工阅读，不经本地模型）

这个文件夹放的是从库里全文逐篇抽出来的器件参数和系统级指标。十九类已全部完成：

- **A3 相变材料器件**：1636 条记录，87 篇论文（10-29）
- **E1 衍射网络**：1875 条记录，203 篇论文（10-30）
- **A1 热光移相器 / 加热器**：247 条记录，102 篇论文（10-30）
- **A5 微环权重库 / 滤波器**：467 条记录，120 篇论文（10-30）
- **A2 电光调制器 / 移相器**：203 条记录，52 篇论文（10-30）
- **A4 其他非易失 / 可编程元件**（铁电、MEMS、磁光、电荷俘获、光学忆阻器等）：108 条记录，18 篇论文（10-30）
- **A6 MZI 网格 / 酉矩阵处理器**：398 条记录，76 篇论文（10-30）
- **B1 微梳 / 多波长光源**：111 条记录，31 篇论文（10-30）
- **B2 激光器 / VCSEL 阵列（作光源或神经元）**：102 条记录，39 篇论文（10-30）
- **G1 光子脉冲神经元**：76 条记录，33 篇论文（10-30）
- **C1 光电探测器**：181 条记录，62 篇论文（10-30）
- **D1 全光非线性元件**（可饱和吸收、Kerr、SOA、量子点、原子蒸气、热光双稳、相变材料等）：192 条记录，55 篇论文（10-30）
- **D2 光电非线性激活单元**（探测器 + 调制器 / 放大器）：65 条记录，18 篇论文（10-30）
- **E2 计算超表面 / 模拟空间微分器**（微分、边缘检测、卷积核）：509 条记录，100 篇论文（10-30）
- **E3 SLM / DMD 硬件**（像素数、帧率、位深、像素间距、波长）：551 条记录，116 篇论文（10-30）
- **F1 延时 / 物理储备池计算**（节点数、延时、速率、任务指标、波长）：391 条记录，57 篇论文（10-30）
- **H1 光子伊辛机 / 组合优化硬件**（自旋数、连接方式、求解时间、成功概率、波长）：276 条记录，51 篇论文（10-30）
- **I1 传感内计算 / 光电突触器件**（波长、响应度、PPF、电导态数、非线性因子、保持时间、每次事件能量、动态范围、耐久、阵列规模）：1112 条记录，250 篇论文（10-30）
- **J 系统级指标**（吞吐量、能效、计算密度、延时、精度、矩阵规模、准确率、时钟 / 符号率）：1587 条记录，345 篇论文（10-30）

十九类合计 10087 条记录，涉及 1133 篇论文（按文件名计；同一篇论文常在几类里都有记录：器件参数在 A–I 各类，系统指标在 J）。

最后合并（10-30）做了三件事：做别的类时顺带记的 A1（18 条）、A2（4 条）记录并进了 A1、A2 的表；做 J 时发现 I1 漏记的 2 条每脉冲能量补进了 I1；新增 `PNN_all_scripts.zip` 和 `run_all_PNN.py`，可以把 A3、E1 以外的 17 类一次从头重跑（见第 25 节）。

10-30 晚又做了两件事（第 26 节）：一是独立抽查，没参与抽取的 agent 对照全文逐条判，两轮抽样之外又把 A1、D1、D2 三类逐条复核，报出的错误都核对原文后改了脚本、全部重跑；二是按标题 / 摘要补查关键词清单之外的论文，补了 59 篇（54 篇有记录）。

## 1. 文件

| 文件 | 内容 |
|---|---|
| `A3_records.jsonl` / `A3_records.csv` | A3 全部参数记录，一行一条（1636 条，87 篇论文） |
| `A3_papers.csv` | A3 每篇论文一行：记录数、实测/仿真/预测条数、材料、器件类型、各参数条数 |
| `A3_screening.csv` | A3 候选论文 155 篇的筛选结果和理由 |
| `A3_scripts.zip` | A3 逐篇抽取脚本（`pNNN.py`）、没有脚本写的 66 条筛选结论 `screen_A3.json`、汇总程序 `build_A3.py`、重跑程序 `run_all_A3.py`（见第 25 节） |
| `E1_records.jsonl` / `E1_records.csv` | E1 全部参数记录（1875 条，203 篇论文） |
| `E1_papers.csv` | E1 每篇论文一行：记录数、实测/仿真/预测条数、平台、实际加工的层数、实测波长/频率、各参数条数 |
| `E1_screening.csv` | E1 候选论文 254 篇（另加 1 个重复文件名）和标题 / 摘要补查的 12 篇的筛选结果、理由，以及 v3.3 原来的判断（`v33_own_device`、`v33_review`；补查的 12 篇没有） |
| `E1_scripts.zip` | E1 逐篇抽取脚本（`eNNN.py`）、汇总程序 `build_E1.py`、重跑程序 `run_all_E1.py` |
| `A1_records.jsonl` / `A1_records.csv` | A1 全部参数记录（247 条，102 篇论文） |
| `A1_papers.csv` | A1 每篇论文一行：记录数、实测/仿真/预测条数、加热器材料，以及 Pπ、调谐功率、调谐效率、电阻、长度、响应时间、热串扰的取值摘要 |
| `A1_screening.csv` | A1 的筛选结果和理由：关键词候选 127 篇，另加 21 篇从 A5 候选里顺带抽的、15 篇由 A2/A4/A6 脚本顺带记的（`candidate` 列都为 `no (extra)`；后 15 篇的 `keyword_hits_A1` 记 0） |
| `A5_records.jsonl` / `A5_records.csv` | A5 全部参数记录（467 条，120 篇论文） |
| `A5_papers.csv` | A5 每篇论文一行：记录数、平台，以及 Q、FSR、半径/直径、环数/通道数、通道间隔、消光比、调谐效率、权重精度的取值摘要 |
| `A5_screening.csv` | A5 候选论文 227 篇的筛选结果和理由 |
| `A1A5_scripts.zip` | A1/A5 逐篇脚本（`fNNN.py`，个别补充脚本为 `fNNNx.py`）、工具 `ex.py` `exv4.py` `classes_v4.py`、候选清单 `worklist_A1A5.json`、汇总程序 `build_A1A5.py`、重跑程序 `run_all_A1A5.py`（单独重跑得到的 A1 表少 A2/A4/A6 脚本写的 21 条，见第 25 节） |
| `A2_records.jsonl` / `A2_records.csv` | A2 全部参数记录（203 条，52 篇论文） |
| `A2_papers.csv` | A2 每篇论文一行：记录数、实测/仿真/预测条数、材料，以及 VπL、Vπ、电光带宽、速率、消光比、插入损耗、每比特能量、长度的取值摘要 |
| `A2_screening.csv` | A2 的筛选结果和理由：关键词候选 320 篇，另加 1 篇由 B1/B2/G1 脚本顺带记的、1 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`，`keyword_hits_A2` 记 0） |
| `A4_records.jsonl` / `A4_records.csv` | A4 全部参数记录（108 条，18 篇论文） |
| `A4_papers.csv` | A4 每篇论文一行：记录数、材料，以及电平数、保持时间、耐久、写入时间、写入电压、写入能量、静态功耗、相移、插入损耗、消光比的取值摘要 |
| `A4_screening.csv` | A4 的筛选结果和理由：关键词候选 291 篇，另加 1 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `A6_records.jsonl` / `A6_records.csv` | A6 全部参数记录（398 条，76 篇论文） |
| `A6_papers.csv` | A6 每篇论文一行：记录数、平台，以及网格规模、MZI 数、架构、保真度、每级损耗、总插入损耗、消光比、串扰、校准方法、总功耗的取值摘要 |
| `A6_screening.csv` | A6 的筛选结果和理由：关键词候选 237 篇，另加 1 篇从 A2 候选里顺带抽的（`candidate` 列为 `no (extra)`） |
| `A246_scripts.zip` | A2/A4/A6 逐篇脚本（每篇一个 `gNNN.py`，同一篇另有补充筛选的为 `gsNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_A246.json`、汇总程序 `build_A246.py`、重跑程序 `run_all_A246.py`（单独重跑得到的 A2 表少 B1/B2/G1 脚本写的 4 条，见第 25 节） |
| `B1_records.jsonl` / `B1_records.csv` | B1 全部参数记录（111 条，31 篇论文） |
| `B1_papers.csv` | B1 每篇论文一行：记录数、平台，以及梳间隔、线数、单线功率、泵浦功率、波长的取值摘要 |
| `B1_screening.csv` | B1 的筛选结果和理由：关键词候选 47 篇，另加 2 篇顺带抽的（`candidate` 列为 `no (extra)`） |
| `B2_records.jsonl` / `B2_records.csv` | B2 全部参数记录（102 条，39 篇论文） |
| `B2_papers.csv` | B2 每篇论文一行：记录数、平台，以及激光器数、阈值电流、输出功率、调制带宽、能量、波长的取值摘要 |
| `B2_screening.csv` | B2 的筛选结果和理由：关键词候选 54 篇，另加 8 篇从 G1 候选里顺带抽的（`candidate` 列为 `no (extra)`） |
| `G1_records.jsonl` / `G1_records.csv` | G1 全部参数记录（76 条，33 篇论文） |
| `G1_papers.csv` | G1 每篇论文一行：记录数、平台，以及脉宽、不应期、阈值、每脉冲能量、发放率、波长的取值摘要 |
| `G1_screening.csv` | G1 候选论文 164 篇的筛选结果和理由 |
| `B1B2G1_scripts.zip` | B1/B2/G1 逐篇脚本（每篇一个 `hNNN.py`，补充筛选为 `hsNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_B1B2G1.json`、汇总程序 `build_B1B2G1.py`、重跑程序 `run_all_B1B2G1.py` |
| `C1_records.jsonl` / `C1_records.csv` | C1 全部参数记录（181 条，62 篇论文） |
| `C1_papers.csv` | C1 每篇论文一行：记录数、实测/仿真/预测条数、材料，以及响应度、带宽、暗电流、NEP、波长的取值摘要 |
| `C1_screening.csv` | C1 的筛选结果和理由：关键词候选 251 篇，另加 1 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `D1_records.jsonl` / `D1_records.csv` | D1 全部参数记录（192 条，55 篇论文） |
| `D1_papers.csv` | D1 每篇论文一行：记录数、实测/仿真/预测条数、非线性机理（`materials` 列），以及阈值、响应时间、调制深度、函数形状、增益、波长的取值摘要 |
| `D1_screening.csv` | D1 的筛选结果和理由：关键词候选 217 篇，另加 4 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `D2_records.jsonl` / `D2_records.csv` | D2 全部参数记录（65 条，18 篇论文） |
| `D2_papers.csv` | D2 每篇论文一行：记录数、平台，以及带宽、每次激活能量、可编程方式、函数形状、波长的取值摘要 |
| `D2_screening.csv` | D2 的筛选结果和理由：关键词候选 27 篇，另加 12 篇从 C1、D1 候选里顺带抽的、1 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `C1D1D2_scripts.zip` | C1/D1/D2 逐篇脚本（每篇一个 `iNNN.py`，补充筛选为 `isNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_C1D1D2.json`、汇总程序 `build_C1D1D2.py`、重跑程序 `run_all_C1D1D2.py` |
| `E2_records.jsonl` / `E2_records.csv` | E2 全部参数记录（509 条，100 篇论文） |
| `E2_papers.csv` | E2 每篇论文一行：记录数、实测/仿真/预测条数、平台，以及运算、NA、带宽、效率、分辨率、偏振、波长的取值摘要 |
| `E2_screening.csv` | E2 的筛选结果和理由：关键词候选 139 篇，另加 19 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `E3_records.jsonl` / `E3_records.csv` | E3 全部参数记录（551 条，116 篇论文） |
| `E3_papers.csv` | E3 每篇论文一行：记录数、平台，以及像素数、帧率、位深、像素间距、波长的取值摘要 |
| `E3_screening.csv` | E3 候选论文 191 篇的筛选结果和理由 |
| `E2E3_scripts.zip` | E2/E3 逐篇脚本（每篇一个 `kNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_E2E3.json`、汇总程序 `build_E2E3.py`、重跑程序 `run_all_E2E3.py` |
| `F1_records.jsonl` / `F1_records.csv` | F1 全部参数记录（391 条，57 篇论文） |
| `F1_papers.csv` | F1 每篇论文一行：记录数、实测/仿真/预测条数、平台，以及节点数、延时、速率、任务指标、波长的取值摘要 |
| `F1_screening.csv` | F1 的筛选结果和理由：关键词候选 109 篇，另加 10 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `H1_records.jsonl` / `H1_records.csv` | H1 全部参数记录（276 条，51 篇论文） |
| `H1_papers.csv` | H1 每篇论文一行：记录数、实测/仿真/预测条数、平台，以及自旋数、连接方式、求解时间、成功概率、波长的取值摘要 |
| `H1_screening.csv` | H1 的筛选结果和理由：关键词候选 196 篇，另加 1 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`） |
| `F1H1_scripts.zip` | F1/H1 逐篇脚本（每篇一个 `mNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_F1H1.json`、汇总程序 `build_F1H1.py`、重跑程序 `run_all_F1H1.py` |
| `I1_records.jsonl` / `I1_records.csv` | I1 全部参数记录（1112 条，250 篇论文） |
| `I1_papers.csv` | I1 每篇论文一行：记录数、实测/仿真/预测条数、材料，以及波长、响应度、PPF、电导态数、保持时间、每次事件能量、动态范围、耐久、阵列规模、非线性因子的取值摘要 |
| `I1_screening.csv` | I1 的筛选结果和理由：关键词候选 375 篇，另加 19 篇按标题补的、3 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`；它们的 `keyword_hits_I1` 记 0，前 19 篇实际命中 0–7 次） |
| `I1_scripts.zip` | I1 逐篇脚本（每篇一个 `nNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_I1.json`、汇总程序 `build_I1.py`、重跑程序 `run_all_I1.py` |
| `J_records.jsonl` / `J_records.csv` | J 全部参数记录（1587 条，345 篇论文） |
| `J_papers.csv` | J 每篇论文一行：记录数、实测/仿真/预测条数、平台，以及吞吐量、能效、计算密度、延时、精度、矩阵规模、准确率、时钟 / 符号率的取值摘要 |
| `J_screening.csv` | J 的筛选结果和理由：关键词候选 536 篇，另加 2 篇 I1 留给 J 的、11 篇标题 / 摘要补查的（`candidate` 列为 `no (extra)`，`keyword_hits_J` 记 0） |
| `J_scripts.zip` | J 逐篇脚本（每篇一个 `jNNN.py`）、工具 `ex.py` `exv4.py` `classes_v4.py` `mkscreen.py` `chk.py`、候选清单 `worklist_J.json`、汇总程序 `build_J.py`、重跑程序 `run_all_J.py` |
| `PNN_all_scripts.zip` | A1/A5、A2/A4/A6、B1/B2/G1、C1/D1/D2、E2/E3、F1/H1、I1、J 八批的全部逐篇脚本（3265 个）、工具、八个候选清单和汇总程序、各批的重跑程序，以及一次重跑这 17 类的 `run_all_PNN.py`（A3、E1 仍用各自的 zip） |
| `verify_params.py` | 核对程序：逐条检查引文是否原样出现在全文里、数值是否在引文里、record_id 是否对得上（各类通用） |
| `README_PNN_params.md` | 本说明 |
| `check\` | 独立抽查的材料（第 26 节）：抽样、每个核对 agent 的判定 `judgments.jsonl` 和报告、改动清单 `PNN_params_check_fixes.md`、补查后仍未收的文件清单 `PNN_unscreened_2026-10-30.md` |
| `derived\` | 由这 19 张记录表算出的派生表（参数图谱、材料图谱、覆盖表、准确率台账），程序 `build_derived.py`，说明见其中的 `README_derived.md` |

CSV 都是 UTF-8 带 BOM，Excel 可直接打开。

## 2. 怎么做的（各类相同）

1. 候选：A3、E1 用 v3.3 运行结果里归到该类的论文（A3 155 篇，E1 254 篇）；A1、A5 用 v4 关键词清单（`classes_v4.py`，同一篇论文的关键词命中 ≥ 8 次算候选；两类合并成 283 篇的 `worklist_A1A5.json`，其中 A1 候选 127 篇、A5 候选 227 篇）；A2、A4、A6 同样用 v4 关键词清单（A2、A6 命中 ≥ 10 次，A4 ≥ 8 次；三类合并成 668 篇的 `worklist_A246.json`，其中 A2 候选 320 篇、A4 291 篇、A6 237 篇）；B1、B2、G1 也用 v4 关键词清单（B1 命中 ≥ 6 次，B2、G1 ≥ 8 次；先去掉文件名带审稿意见的文件，三类合并成 234 篇的 `worklist_B1B2G1.json`，其中 B1 候选 47 篇、B2 54 篇、G1 164 篇）；C1、D1、D2 也用 v4 关键词清单（C1 命中 ≥ 8 次，D1 ≥ 6 次，D2 ≥ 4 次；三类合并成 446 篇的 `worklist_C1D1D2.json`，其中 C1 候选 251 篇、D1 217 篇、D2 27 篇；审稿意见文件留在清单里，登记为不属于该类）；E2、E3 也用 v4 关键词清单（两类都是命中 ≥ 8 次；去掉 4 个审稿意见文件后合并成 323 篇的 `worklist_E2E3.json`，其中 E2 候选 139 篇、E3 191 篇）；F1、H1 也用 v4 关键词清单（F1 命中 ≥ 6 次，H1 ≥ 8 次；去掉 4 个文件名带审稿意见的文件后合并成 295 篇的 `worklist_F1H1.json`，其中 F1 候选 109 篇、H1 196 篇；H1 的关键词会把 promising、rising 等词里的 "ising" 也算进去，误报的逐篇核对后登记为不属于 H1）；I1 也用 v4 关键词清单（命中 ≥ 8 次的 379 篇去掉 4 个审稿意见文件，剩 375 篇；另按标题补了 19 篇关键词命中不到 8 次、但明显属于 I1 的论文，放在清单末尾，合并成 394 篇的 `worklist_I1.json`）；J 也用 v4 关键词清单（命中 ≥ 4 次的 539 篇去掉 3 个审稿意见文件，剩 536 篇；另补了 2 篇 I1 写明留给 J、但不在关键词候选里的论文，合并成 538 篇的 `worklist_J.json`）。10-30 晚又按标题 / 摘要补查，在各清单末尾补了 59 篇（见第 6 项和第 26 节）。全文都在 `08_Reading_Notes\fulltext\`。
2. 筛选：逐篇看摘要和正文。综述（含展望、评论、News & Views）只登记不抽；不属于该类的登记为 `not_A3` / `not_E1` / `not_A1` / `not_A5` / `not_A2` / `not_A4` / `not_A6` / `not_B1` / `not_B2` / `not_G1` / `not_C1` / `not_D1` / `not_D2` / `not_E2` / `not_E3` / `not_F1` / `not_H1` / `not_I1` / `not_J` 并写明理由；重复文件（含 145 字符截断的文件名、只有 SI 的文件）登记为 `duplicate`；审稿意见文件（Peer Review File）登记为不属于该类。
3. 抽取：每篇读正文和 SI，所有数值都配一句原文（`quote_text`）。原文取自 v3.3 用的同一套规范化文本（去参考文献、合并空白、展开连字），所以可以用程序原样查到。
4. 机器核对（每条都过）：
   - 引文必须在正文或 SI 的规范化文本里原样出现，并记下位置（`src`、`char_offset`、`page`、`section`）；
   - `value_text` 里的每个数字都必须出现在引文里；
   - 标签只能取固定取值（见第 4–22 节）；
   - `record_id = 类别代码-` + SHA-256(stem | param | value_text | quote | 材料或平台标签 | state | condition | device) 的前 12 位。
5. 全部记录已用 `verify_params.py` 重新核对：A3 1636 条、E1 1875 条、A1 247 条、A5 467 条、A2 203 条、A4 108 条、A6 398 条、B1 111 条、B2 102 条、G1 76 条、C1 181 条、D1 192 条、D2 65 条、E2 509 条、E3 551 条、F1 391 条、H1 276 条、I1 1112 条、J 1587 条，均为 0 条有问题。这些表是 10-30 晚改完之后从头重跑的结果：`run_all_PNN.py` 把八批 3265 个脚本放进同一个输出文件夹一起跑（A1、A2 两类的完整表只能这样重跑得到），`run_all_A3.py`、`run_all_E1.py` 各跑 A3、E1，没有一个脚本失败（用法见第 25 节）。发布版（10-30 下午）也照同样的办法在干净目录里重跑核对过，结果与当时交付的表逐字相同。
6. 标题 / 摘要补查：上面的候选清单都按全文里的关键词计数选，用词不同的论文会漏掉（例如 "photonic reservoir"、"extreme learning machine"、"metasurface … edge-enhanced imaging"）。10-30 晚逐篇看了所有类都没筛过的论文的标题和摘要，补了 59 篇，加在各清单末尾（筛选表 `candidate` 列为 `no (extra)`，关键词计数记 0），其中 54 篇有记录；其余没筛过的 77 个文件和原因列在 `check\PNN_unscreened_2026-10-30.md`（第 26 节）。

## 3. 通用字段

| 字段 | 含义 |
|---|---|
| `record_id` | 记录编号（由内容算出，内容变了编号就变） |
| `stem` | 论文文件名（不含扩展名），与 `fulltext\` 下的文件对应 |
| `param` | 参数名（第 4–22 节） |
| `value_text` | 原文写法（单位和限定词照抄；PDF 转文字时丢失的符号见第 24 节） |
| `value_num` / `value_num_hi` | 数值；区间时 `value_num_hi` 为上限，列举几个值时为最大值 |
| `qualifier` | `~`（约）、`>`、`<`、`≥`、`≤`、`±`、`up to`、`max`、`min`（文中给的最大 / 最小值）、`range`（区间）、`list`（列举几个值：`value_num` 取最小、`value_num_hi` 取最大）或空；原文给 "0 到 X" 一类的扫描范围时只记上限 X，qualifier 记 `max` |
| `unit` | 单位 |
| `status` | `measured` 实测 / `simulated` 仿真 / `predicted` 估算或外推 |
| `material_text` / `device` | 材料或实现方式原文描述 / 器件描述 |
| `condition` / `note` | 测量条件 / 备注（文中自相矛盾、符号丢失、换算方法等都写在 note） |
| `src` / `page` / `section` / `char_offset` | 引文出处：`m` 正文、`s` SI；页码、章节、在规范化文本中的位置 |
| `quote_text` | 原文引句（抽取时用于核对，不随数据分发） |
| `code` | 类别代码（A3、E1、A1、A5、A2、A4、A6、B1、B2、G1、C1、D1、D2、E2、E3、F1、H1、I1、J） |

A3 另有 `material`、`device_type`、`state`、`role`；E1 另有 `platform`、`layer_type`；A1 另有 `material`（加热器材料）；A5 另有 `platform`；A2、A4、C1、I1 另有 `material`；D1 另有 `material`（这一列放的是非线性机理）；A6、B1、B2、G1、D2、E2、E3、F1、H1、J 另有 `platform`。

## 4. A3（相变材料器件）约定

- **参数名**：delta_n, delta_k, n_value, k_value, n_eff, delta_neff, levels, level_step, switching_energy, energy_density, pulse_width, pulse_amplitude, switching_time, endurance, retention, insertion_loss, propagation_loss, contrast, crosstalk, loss_per_pi, phase_efficiency, L_pi, cell_length, film_thickness, wavelength, drive。
- **材料**：GST、N-GST、Ge-rich GST、GSST（Ge2Sb2Se4Te1）、GSSe（Ge2Sb2Se5）、GSSST、Sb2Se3、Sb2S3、GeTe、Sb2Te3、SbTe（SbTe9）、AIST、Sb、Se、Te、other（如 Sc0.2Sb2Te3、Ge3Sb2Te15）。
- **器件类型**：waveguide_cell、microring、mzi、coupler_or_switch、metasurface_or_free_space、thin_film、fiber、other。
- **只记本文的数据**。引用别人的材料常数（n、k、Δn 等）不单独成条，只在 `material_text` 里注明出处。
- 消光比（dB、%、dB/µm）记在 `contrast`；dB/µm 的损耗记在 `propagation_loss`；dB/π 记在 `loss_per_pi`。
- `phase_efficiency` 只放"每单位长度或每伏"的量（π/µm、rad/µm、nm/µm、VπL）。只给总共振移动（pm、nm）的，写进相关记录的 `condition`，不单独成条。
- `levels` 只记文中明确给出的可区分状态数；"n-bit" 换算为 2^n 写进 `value_num`。
- 能量按原文：光脉冲多数是波导内或物镜前的能量，原文怎么说就在 `condition`/`note` 里怎么写。
- 文中前后不一致的数值（比如 25 nm 和 27 nm、86 nJ 和 83 nJ）分别成条，在 `note` 里说明。
- 纯仿真论文：所有记录都是 `simulated`，并在筛选表里注明。
- `state` 一律按物理过程填写（晶化 / 非晶化），原文把哪个叫 "write"、哪个叫 "erase" 写在 `condition`。

## 5. E1（衍射网络）约定

**纳入标准**：论文自己训练或设计的衍射网络 / 衍射处理器——一层或多层衍射面（3D 打印、双光子打印、光刻、超表面、PCB 微波、SLM/DMD、液晶、片上衍射区），其特征经训练或设计，由自由空间或平板内的衍射完成计算、分类、成像或信号处理。实验做的和纯数值设计的都收。

**不收（登记为 `not_E1`，理由见筛选表）**：
- 单个未经训练的计算超表面（只做微分 / 边缘检测）；
- 声学衍射网络（非光、非电磁）；
- 衍射不是被训练的那一步的自由空间乘加（DOE 只做分束、光栅只做路由、透镜傅里叶光学做矩阵乘法、OLED-SLM 成像乘法器等）；
- 逆向设计的自由形状纳米光子散射介质（不是分层衍射网络）；
- 用耦合器网格"等效"衍射的导波电路（SSPP 耦合器、微带分支线耦合器、集总元件芯片）；
- 衍射网络只在引言或对比表里出现的论文。

**参数名**：wavelength, frequency, pixel_pitch, layer_count, layer_spacing, input_distance, output_distance, neurons_per_layer, layer_size, efficiency, phase_levels, accuracy, fabrication。

**平台（`platform`）**：3d_printed_polymer、two_photon_polymer、metasurface_dielectric、metasurface_metallic、pcb_microwave、slm_dmd、liquid_crystal、on_chip、other_material、numerical_only。归类做法：
- 刻蚀石英 / 熔融石英 / 光刻胶 DOE、钙钛矿量子点膜 → other_material；
- 微波 F4B/PTFE 介质柱 → metasurface_dielectric；PCB 铜贴片、可编程 PIN 管超表面、SSPP 微波结构 → pcb_microwave；
- 太赫兹光刻 SSPP、硅光片上衍射区（metaline、刻槽） → on_chip；
- 液晶 RIS / 光写入液晶 → liquid_crystal；
- 只做数值设计的 → numerical_only，设想的实现方式写在 `material_text`。

**状态**：
- 实际做出来（含用 SLM 显示）的几何参数 → `measured`；
- 对实物设计算出来的精度、效率 → `simulated`，平台仍按实物填；
- 纯数值论文 → `numerical_only` + `simulated`。唯一例外：LPR 2026 鬼成像分类（解码器是计算出来的"虚拟衍射层"，但精度来自真实光学测量），平台记 numerical_only、精度记 measured，`note` 里说明。

**其他约定**：
- `layer_type` 只用于 `layer_count`：`fabricated`（实际做出 / SLM 实现的层）或 `design`（仅数值设计或扫描）。SLM 上实现的层算 fabricated。
- `neurons_per_layer`：`value_num` 存乘积（"200 × 200" 存 40000），单位 `features`。
- `fabrication` 记录没有数值（`value_num` 为空），做法写在 `value_text`，细节写在 `condition`。
- 效率可以用 dB：单位记 `dB`，损耗存负值（如插入损耗 15 dB 存 −15）。
- 原文给小数（0.76）的效率换算成百分数（76%），`note` 里注明。
- 换算或推出来的数值（几个距离相加、厚度乘折射率、70/72 算出的正确率、16 级由 4 次刻蚀得到等）都在 `note` 里写清算法。
- 原文没给的参数不补、不猜，宁可缺。
- 只研究激活材料、附带一个数值衍射网络的论文：只抽少量记录，并在筛选表里注明。
- `accuracy` 的 `condition` 写数据集和条件；Ozcan 组常用的"实验与数值结果的一致率"（例如对 50 个数值上已分对的样本，实验 88% 一致）按 measured 记，`condition` 里写明含义。
- 量子门的保真度、成像的 PSNR/SSIM 等不算 accuracy，不单独成条。

## 6. A1（热光移相器 / 加热器）约定

**纳入标准**：论文自己器件上的热光调谐元件（金属、TiN、掺杂硅、石墨烯、ITO 等加热器）的数据——用来移相、调 MZI、调微环 / 微盘谐振的都收。由控制光加热的也收：Nat Commun 2025 17:989（PHIL）的钛纳米天线吸收控制光发热，它的调谐效率是按光功率算的，`condition` 写明。

**不收（登记为 `not_A1`）**：
- 加热器只用来切换相变材料（这些数据在 A3）；
- 不是热光的调谐：电光（LN、BTO、PZT）、MEMS、磁光、载流子注入的推挽 MZI；
- 寄生的热效应：电磁铁线圈发热、光吸收发热、光热非线性（不是加热器）；
- 加热器只在引言或对比表里出现、全文没有本器件数值的论文。

**参数名**：P_pi, tuning_power, tuning_efficiency, heater_resistance, heater_length, response_time, thermal_crosstalk, insertion_loss, wavelength。

**材料（`material`）**：TiN、metal_other（TiW、W、Pt、Ti、Cr、NiCr、Al、只写"金属"的）、doped_Si、graphene、ITO、other、not_stated（没写材料，或文中前后矛盾）。

**约定**：
- `P_pi` 单位 mW。只给 Vπ 的记 V，只给 Iπ 的记 mA，`note` 写明；能用文中的电阻换算的，近似功率写在 `note`，不改 `value_num`。
- 只给 2π 功率的不折半：记为 `tuning_power`，`condition` 写 "2π"。
- `tuning_power`：其他调谐范围的功率（2π、一个 FSR、某个波长移动、偏置点、满量程、最大值）。范围写在 `condition`。只给电流或电压的照记（mA、V）。系统级的合计（一条路由路径、整个网络的全部加热器）也记，`condition` 写明是合计。
- `tuning_efficiency` 按原文单位（nm/mW、pm/mW、GHz/mW、π/mW、rad/mW、mW/nm、nm/V）。微环 / 微盘加热器的谐振移动效率，A1 和 A5 各记一条（同一引句）。
- `response_time`：原文给时间就记时间（ns、µs、ms）；只给速率（"10 kHz"、3-dB 带宽 311 kHz）就记 kHz，`condition` 写明是速率。
- `thermal_crosstalk` 按原文量纲：%（串扰系数、相对变化）、K（多为仿真温升）、nm/mW（加热一个器件时相邻器件的漂移率）、µm / mm（为避免串扰而取的间距）。
- `heater_resistance` 统一用 Ω；原文 kΩ 的在 `value_num` 换算，`note` 注明。
- 同一篇里有几种加热器（测试结构和主芯片、补偿阵列和输入调制器、悬空和普通移相器）时按器件分开记；文中只给其中一种写了材料的，另一种记 not_stated。
- 偏置的 MZI 各输出口从 0 V 到开关点的功率不是 Pπ，记 `tuning_power`，`condition` 写明是哪个口。
- 功耗估算表里假设的值记 `predicted`；仿真设计记 `simulated`。
- 引用别人的数值（"典型 1–10 mW/π"等）不记。
- A5 候选论文里顺带出现的加热器数据也抽了（21 篇，其中 1 篇是重复文件），筛选表 `candidate` 列为 `no (extra)`。
- A2/A4/A6 的脚本处理 MZI 网格等芯片时顺带记的加热器数据（15 篇 21 条）也在 A1 表里。这些论文不在 A1 关键词候选里，筛选表 `candidate` 列为 `no (extra)`，`keyword_hits_A1` 记 0。

## 7. A5（微环权重库 / 滤波器）约定

**纳入标准**：论文自己做的（或数值设计的）微环、微盘、跑道环、椭圆环、光纤结 / 微球等谐振器，用作权重、滤波、波分复用、调制、非线性单元，或在可编程网格里合成的环；加载相变材料的微环；只用来测传输损耗的测试环也记（`device` 写明）。

**不收（登记为 `not_A5`）**：
- 只作光梳源的微环（Kerr / 孤子梳，属于光源类 B1）、自注入锁定激光的反馈环、微环激光器（光源）；
- 环只在引言、对比表或功耗估算里出现；
- 纯理论里假设的环参数（文中给的 Q、FSR 只是模型假设或引用值）。

**参数名**：Q_factor, linewidth, FSR, extinction_ratio, channel_spacing, tuning_efficiency, channel_count, weight_precision, crosstalk, radius, wavelength。

**平台（`platform`）**：SOI、SiN、LNOI、polymer、III_V、other（PZT、AlN、BTO-on-Si、光纤结、光纤微球等）。

**约定**：
- `Q_factor` 无单位；原文写了 loaded / intrinsic 的写在 `condition`。上标丢失的（"104"）在 `value_num` 改正，`note` 注明。
- `radius`：半径或直径都记在这里，直径在 `condition` 写 "diameter"；跑道环记弯曲半径；椭圆环记半轴。
- `channel_count`：单位 `rings`（环的个数）或 `channels`（波长通道数）。"6 × 32 阵列"这类在 `value_num` 存乘积，`note` 注明。
- `weight_precision`：单位 `bit`、`levels`，或 `avg error`（原文只给平均误差的）。系统级的计算精度（MVM 的等效位数等）也记在这里，`condition` 写明。
- `extinction_ratio`：谐振的消光比；调制 / 开关 / 逻辑输出的消光比也记，`condition` 写明是哪一种。原文写成负数（"−13.12 dB"）的存正值，`note` 注明。
- "达到 6 bit 需要的 Q"、容量估算 → `predicted`；仿真设计 → `simulated`；设计尺寸（半径等）随实际做出的器件记 `measured`。
- 微环加热器的调谐效率同时记在 A1（见第 6 节）。

## 8. A2（电光调制器 / 移相器）约定

**纳入标准**：论文自己芯片上的电驱动、易失的调制器 / 移相器：薄膜铌酸锂（TFLN / LNOI，含晶圆代工的 TFLN）、硅载流子（PN 耗尽、PIN 注入、MOSCAP）、SiGe / GeSi 电吸收调制器、PZT 和 BTO 的易失 Pockels 模式、石墨烯、等离子体、注入锁定的 VCSEL、AlN 压电光机移相器、二维材料等。代工 PDK 里的调制器做在作者自己的芯片上、数据是作者测的，也算。

**不收（登记为 `not_A2`）**：
- 商用或台式调制器（iXblue、Thorlabs、HyperLight 提供的 TFLN 调制器、商用 IC-TROSA 和八通道发射模块等），只用来加载输入；
- 热光调制（属于 A1；有加热器数据的已记入 A1）；
- 非易失器件（BTO / PZT 的非易失态、铁电掺杂石墨烯、磁光存储等记在 A4，相变材料在 A3）；
- 自由空间 SLM / DMD / 液晶 / 超表面、全光开关（χ2、Kerr、光热）、微波或声学器件；
- 只有静态谐振移动（pm/V）、没有调制指标的微环（谐振数据在 A5）；
- 器件只在引言、对比表或功耗估算里出现的。

**参数名**：VpiL, Vpi, eo_bandwidth, data_rate, insertion_loss, extinction_ratio, energy_per_bit, length, wavelength。

**材料（`material`）**：TFLN、BTO、Si_carrier、EO_polymer、ITO、III_V、graphene、plasmonic、SiN_other、other（SiGe / GeSi 电吸收调制器、PZT、AlN 压电、磷烯 / MoS2 等，具体写在 `material_text`）。

**约定**：
- `VpiL` 单位 V·cm；`Vpi` 单位 V（VCSEL 一条为 mV）。原文给区间的记区间（`value_num` 下限、`value_num_hi` 上限）。
- `eo_bandwidth` 单位 GHz，低速器件用 MHz。代工厂"过程控制监测"（process control monitoring，缩写也是 PCM，不是相变材料）给出的带宽也记，`condition` 写明；受测试设备限制的写在 `condition`。
- `data_rate` 按原文：Gb/s、Gbaud、GS/s；原文只写 "10 GHz"、"5 MHz" 的照记 GHz / MHz，`note` 写明。
- `extinction_ratio`：调制消光比或静态谐振消光比，`condition` 写明是哪一种；原文写成负数（"−13.12 dB"）的存正值，`note` 注明。
- `energy_per_bit`：fJ/bit；按符号给的记 fJ/symbol 或 aJ/symbol。作者用实测电容、Vrms 算出的能量记 `measured`，`condition` 写 "calculated"；按文献模型估的记 `predicted`。原文给 pJ 的在 `value_num` 换算成 fJ，`note` 注明。
- `length`：调制段或电极长度；只给占地面积的，`value_num` 取长边，`note` 写明。
- 器件规格（例如 "56 GHz 带宽的 EAM"）本文没有重测的，记 `measured`，`note` 写 "device specification; not re-measured"。
- 系统级能效（pJ/MAC、TOPS/W）不在 A2 记（留给系统类 J）。
- B1/B2/G1 的脚本顺带记的 1 篇（ACS Photonics 2024 11:5306 电吸收调制的多波长 DFB 激光器阵列，4 条）也在 A2 表里，筛选表 `candidate` 列为 `no (extra)`，`keyword_hits_A2` 记 0。

## 9. A4（其他非易失 / 可编程元件）约定

**纳入标准**：论文自己做的、能编程并保持状态的光学元件（相变材料除外，见 A3）：铁电（BTO、HZO-on-LN、PZT、P(VDF-TrFE) 掺杂石墨烯、PMN-PT 镧系发光忆阻器）、MEMS、磁光（Ce:YIG）、电荷俘获 / 浮栅（碲 LuminoMem）、光学忆阻器（III–V / HfO2、PZT 光忆阻器）、其他（光致变色水凝胶、光写入液晶 / 偶氮染料、电容型模拟存储驱动的 PN 微环）。

**不收（登记为 `not_A4`）**：
- 相变材料（A3）；
- 输出是电信号的光电突触、传感器内计算器件（光电晶体管、二维材料忆阻器、视觉传感器等，属于 I1）；
- 会自行恢复的易失光致变化（例如做储备池的荧光粉）；
- 非光学的忆阻器、磁畴储备池、微波器件；
- 只在引言或对比表里出现的。

**参数名**：levels, retention, write_voltage, write_energy, switching_time, endurance, insertion_loss, standby_power, phase_shift, extinction_ratio, wavelength。

**材料（`material`）**：ferroelectric、MEMS、magneto_optic、charge_trap、memristor、other。

**约定**：
- `retention` 单位按原文（s、hours、weeks、years；易失的电容存储为 ms）。外推的（"10 年"、"可超过 1 年"）记 `predicted`。
- `levels` 单位 levels 或 states；只给位数的记 bits。
- `write_voltage` 可以是区间或负值；`write_energy` 按原文单位（fJ、pJ、nJ、pJ/µm²）；`switching_time` 多为编程脉宽或开关时间，`condition` 写明。
- `phase_shift` 单位 π；只给谐振移动的记 nm，`note` 写明。
- 上标丢失（"105 cycles" 即 10^5、"104s" 即 10^4 s）在 `value_num` 改正，`note` 注明。
- NC 2026 电容型模拟存储（DEOAM）是易失的（一个时间常数约 0.83 ms），因为是可编程权重单元而收在 A4（material = other），`note` 注明。
- 自由空间或发光读出的存储（光致变色水凝胶、镧系发光忆阻器、LuminoMem、液晶偶氮染料）也收，`device` 写明读出方式。

## 10. A6（MZI 网格 / 酉矩阵处理器）约定

**纳入标准**：论文自己做的可编程相干线性光学处理器——MZI 网格（Reck、Clements、对角、简化实值网格等）、可编程波导网格（方形 / 六边形循环网格、MEMS 耦合器网格、相变材料或 BTO 的非易失网格），以及有矩阵保真度数据的相干交叉阵列（NC 2024 "Perfect linear optics" 的 Xbar、Nat Comput Sci 2026 INSPIRE 的 4 × 4 网格）和其他可编程酉变换结构（相变材料耦合波导阵列、交错移相阵列）。网格做在硬件上；同篇里的仿真扩展也记（`status` = simulated / predicted）。

**不收（登记为 `not_A6`）**：
- 非相干交叉阵列 / 广播-加权、微环 / 微盘网格或权重库、AWG、FIR / 延时线滤波电路、固定的无源核心、衍射 / 超表面；
- 只有理论或仿真的（包括 Reck 1994、Clements 2016、Miller 2015 这类架构论文）；
- 光纤网络、时间或频率合成维度的网络、微波 PCB 实现；
- MZI 只作输入衰减器或只属于单个神经元的。

**参数名**：mesh_size, mzi_count, architecture, fidelity, loss_per_stage, total_insertion_loss, extinction_ratio, crosstalk, calibration, total_power, bandwidth, wavelength。

**平台（`platform`）**：SOI、SiN、LNOI、silica_PLC、III_V、other（Si–BTO 混合、正文没写平台的等）。

**约定**：
- `mesh_size` 单位 ports，`value_num` 存 N（N × N 或 N 个模式）；可编程波导网格存接入网格的端口数，`condition` 写明。
- `mzi_count` 单位 MZIs（可编程单元 PUC、TBU、MEMS 可调耦合器都按 MZI 计，`note` 写明）或 phase shifters（只给移相器数的）。只给公式的（"N(N + 1)/2"）`value_num` 留空，按本文 N 算出的个数写在 `note`。
- `fidelity` 照原文的量纲记，**统计前要按 `unit` 分开**：`%`（保真度或 R²）、`fraction`（0–1 的保真度或 R²）、`similarity`（0–1 的相关系数 / 余弦相似度）、`bit`（分辨率或编程精度）、`MSE`、`dB`（系数误差）、`relative error %`（相对 Frobenius 误差，越小越好）。不是 % 的都在 `note` 说明。
- `crosstalk` 存负值；"抑制 > X dB"、"期望与非期望端口之比 25 dB" 存为 < −X、−25，`note` 写明。有一条原文给的是 %（< 1%），单位记 %。
- 原文写成负透过率的插入损耗（"−14 to −21 dB"）存正值，`note` 写明。
- `architecture`、`calibration` 没有数值：`value_text` 照抄原文短语，补充说明写在 `condition`。
- `total_power` 是整个网格的电功耗；按"全部加 2π 的最坏情况"估的记 `predicted`。
- 同篇里加热器的 Pπ 记入 A1（见第 24 节）；网格里的电光或非易失移相器数据分别记在 A2、A4。

## 11. B1（微梳 / 多波长光源）约定

**纳入标准**：给本文处理器提供并行波长通道的多波长光源，参数是本文实验里测得或给出的：微梳（Si3N4、CMOS 兼容高折射率掺杂二氧化硅 Hydex、AlGaAs 微环里的孤子、孤子晶体、暗脉冲、混沌梳；自己做的、合作者提供的、商用封装的 turnkey 模块都收）、电光梳（相位 / 强度调制器生成）、锁模光纤激光器或超连续谱 / ASE 经滤波切片后当通道用的、单片多波长激光器阵列（同时记入 B2）。买来的光源在 `material_text` 开头写 "commercial"。

**不收（登记为 `not_B1`）**：
- 梳只当脉冲时钟、采样脉冲或泵浦–探测脉冲用（梳线不作通道）；
- 用多台独立的商用可调激光器当通道（梳只在展望里提）；
- 梳只在仿真里假设参数、或只是展望；
- 没有多波长光源的。

**参数名**：comb_spacing, line_count, power_per_line, pump_power, wavelength。

**平台（`platform`）**：Si3N4、Hydex、LN、AlGaAs、silica、electro_optic_comb、other（材料没写的微梳、激光器阵列、切片的宽带光源等，具体写在 `material_text`）。

**约定**：
- `comb_spacing` 按原文记 GHz 或 nm。同一篇既给 FSR、又给实际取线间隔（例如隔一根取线）的分别记，`condition` 写明；电光梳的间隔等于驱动射频频率的，`condition` 写明。
- `line_count` 单位 lines。"产生的线数" 和 "计算中实际用的线数" 都可能有，`condition` 写明；"over 100" 记 `>`。
- `pump_power` 按原文 mW 或 dBm：微梳多为放大后进入微环前或片上的功率，电光梳记种子激光功率，`condition` 写明。商用模块的泵浦功率是器件规格，`note` 写 "device specification; not re-measured"。
- `wavelength`：泵浦波长、梳中心、或所用线的范围 / 列表，`condition` 写明是哪种；设计值（例如 REC 光栅的设计波长）记 `predicted`。
- `power_per_line`：单线功率（片上、放大后或直接输出），`condition` 写明。
- 激光器阵列做 WDM 光源的（ACS Photonics 2024 EA-MWL、LSA 2025 32 通道 DFB 阵列、Sci Adv 2025 HITOP 七个 VCSEL）在 B1 和 B2 各记一份：B1 记间隔、通道数、单通道功率，B2 记激光器参数。

## 12. B2（激光器 / VCSEL 阵列，作光源或神经元）约定

**纳入标准**：本文处理器里当光源、调制器或神经元用的激光器和激光器阵列：VCSEL（含注入锁定的、阵列）、DFB 和 DFB-SA、FP 和 FP-SA、量子点激光器、纳米 / 微腔激光器（光子晶体、金属纳米盘、微柱）、自注入锁定激光器等。芯片上自己做的、合作者提供的、商用分立器件都收，前提是参数是本文测的（商用的 `material_text` 写 commercial）；数值模型里给出 B2 参数的也收（`status` = simulated）。

**不收（登记为 `not_B2`）**：
- 只当光源用的台式可调激光器、商用多端口光源；
- 只被提名、没有参数的泵浦激光器；
- 只在展望或补充讨论里提出、用文献参数的 VCSEL 实现；
- 只有归一化速率方程参数的数值研究；
- 属于该类但正文没有 B2 数值的，也登记为 `not_B2` 并写明理由。

**参数名**：device_count, threshold_current, output_power, modulation_bandwidth, energy, wavelength。

**平台（`platform`）**：VCSEL、DFB（含 DFB-SA）、QD_laser、FP（含 FP-SA）、microlaser（纳米 / 微腔激光器）、fiber_laser、other（类型没写的半导体激光器）。

**约定**：
- `threshold_current` 单位 mA；DFB-SA、FP-SA 记增益区阈值，可饱和吸收区偏压写在 `condition`。光泵浦的纳米激光器记泵浦功率阈值（单位 μW，`note` 写明）。原文只说 "偏置在阈值附近" 的偏置电流照记，`note` 写明不是拟合的阈值。
- `output_power` 按原文 mW 或 dBm，μW 在 `value_num` 换算成 mW（`note` 注明）。
- `device_count` 单位 lasers；"5 × 5"、"8 × 8" 的 `value_num` 存 25、64，`note` 写明。
- `energy` 是激光器自己的每符号 / 每运算 / 每帧能量，算法写在 `condition`；系统级能耗不记。
- `wavelength` 是发射 / 主模波长，偏振模或多模的写在 `condition`。
- 激光器当脉冲神经元的，激光器参数（阈值电流、输出功率、波长）记 B2，脉冲参数记 G1，同一篇两张表都有。

## 13. G1（光子脉冲神经元）约定

**纳入标准**：本文实现或建模的光子脉冲神经元，即有可激发 / 阈值–发放–复位行为、输出是光脉冲的器件：DFB-SA、FP-SA、光注入 VCSEL、硅微环（自脉冲 / 可激发，含电驱动）、相变材料神经元、RTD 驱动 VCSEL 的光电神经元、激子极化激元凝聚体、纳米 LED / 纳米激光器（模型）、微柱激光器、DOPO 神经元、发光忆阻神经元、自注入锁定激光器，以及原文称为 "graded-like spiking" 的激光器。实验值记 measured，模型值记 simulated。

**不收（登记为 `not_G1`）**：
- 输出是电信号的光电突触、光电神经元、视觉传感器和传感器内计算器件（I1 类；关键词 "spike" 多来自光刺激脉冲）；
- 只有突触（STDP）没有神经元的、只在软件里跑的 SNN；
- 原文明确说不是脉冲神经元的 graded neuron（LPR 2026 可编程时间动力学、Optica 2024 集成激光 graded neuron，两篇都是双段量子点激光器）；
- 自脉冲只作储备池动力学的无源微环网络；
- 属于该类但正文没有 G1 数值的，也登记为 `not_G1` 并写明理由（4 篇：ACS Photonics 2025 12:2828、OEA 2026 9:250350、Photonics Res 2021 9:B119、Photonics Res 2021 9:B87）。

**参数名**：pulse_width, refractory_period, threshold, energy_per_spike, firing_rate, wavelength。

**平台（`platform`）**：VCSEL、DFB_SA、FP_SA、microring、PCM、other（RTD–VCSEL、无可饱和吸收区的 FP 注入锁定、graded-like DFB、极化激元、纳米 LED / 纳米激光器、微柱、DOPO、发光忆阻、自注入锁定激光器，具体写在 `material_text`）。

**约定**：
- `pulse_width` 是输出脉冲的宽度（FWHM 或持续时间）；输入扰动的脉宽不记。
- `refractory_period` 照原文（区间照记）；绝对不应期和相对不应期分开记。
- `firing_rate` 是最大发放率或自脉冲频率，单位 GHz（MHz 在 `value_num` 换算，`note` 注明）；由 "1 / 不应期" 推出的照原文记，`condition` 写明。
- `threshold` 是激发阈值，单位照原文（输入光功率 μW / dBm、输入能量 fJ / pJ、驱动电压 V）；激光器的阈值电流记在 B2。
- `energy_per_spike` 照原文单位（fJ、pJ、nJ）。作者用本文测得的功率 × 时间等算出的记 measured，`condition` 写 calculated；方法只在看不到的补充材料里的，照记 measured，`note` 写 "estimate; …"。只记神经元的能量，含 DAC / ADC 的系统能耗不记。
- `wavelength` 是神经元工作、发射或注入波长，`condition` 写明是哪种。

## 14. C1（光电探测器）约定

**纳入标准**：论文自己的器件以光电探测器、光电二极管、光电晶体管、光电传感器或图像传感器的身份出现（或有明确的探测器工作模式，例如"探测 / 突触"双模器件），并给出本文测得的指标；只给了工作波长或响应波段的也记。代工 PDK 的探测器做在作者自己的芯片上、数据是作者测的，也算（`material_text` 写 PDK）。

**不收（登记为 `not_C1`）**：
- 探测器只用于读出、全文没有本文探测器指标的系统论文；
- 商用探测器 / 探测器阵列、从 PDK 或文献抄来的数值、仿真里假设的响应度；
- 只以光电突触、忆阻器、存储器或神经形态视觉器件（人工视网膜等）身份出现的器件——属于 I1，以后在 I1 里记；
- 理论论文（散粒噪声、零差探测分析等）。

**参数名**：responsivity, bandwidth, dark_current, NEP, wavelength。

**材料（`material`）**：Ge、InGaAs、Si、graphene、2D_other（MoS2、WSe2、MoTe2、黑磷、VSe2 及各种二维异质结）、perovskite（含钙钛矿量子点与石墨烯 / 碳纳米管的复合）、organic、other（Ga2O3、PbS、AgBiS2、铌酸锂热释电等，具体写在 `material_text`；正文没写材料的写 "material not stated"）。

**约定**：
- `responsivity` 单位 A/W；mA/W、μA/W、nA/mW、pA/μW 在 `value_num` 换算成 A/W，`note` 注明。双极 / 栅控可编程器件给的区间照记，下限可以是负值。
- `bandwidth` 单位 GHz：3-dB 带宽，或由上升时间、截止频率推出的带宽；Hz、kHz、MHz 在 `value_num` 换算，`note` 注明；偏压写在 `condition`。
- `dark_current` 单位 nA（fA、pA、μA 换算）；暗电流密度单位 nA/cm2（μA/cm2 换算），`note` 写 "dark-current density"。
- `NEP` 单位 W/√Hz（pW/Hz1/2 等换算）。比探测率 D*（Jones）不单独成条。
- `wavelength`：测量波长、响应波段（`range`）或几个测量波长（`list`），单位 nm（μm 换算）。
- 同一篇有几个器件的（例如 Optica 2025 多端口探测器一篇里的 16 端口 PD、SI 里的大面积 PD、作者实测的 AMF PDK 参考 PD），按器件分别记，用 `device` 和 `material_text` 区分。
- 上标丢失的（"1.4 × 108"）在 `value_num` 改正，`note` 注明。

## 15. D1（全光非线性元件）约定

**纳入标准**：论文自己的全光非线性元件（光入光出、响应随光强变化）：可饱和吸收（含反饱和吸收，二维材料、MXene、碳纳米管、量子点膜等）、Kerr、SOA 和 EDFA 的增益饱和、量子点光致发光、原子蒸气（EIT、饱和吸收）、热光双稳、相变材料、微环非线性、χ(2)（PPLN 倍频耗尽）、Ge 自由载流子吸收、受激布里渊放大、光折变晶体、像增强器等。实测的记 measured；仿真只要给了物理数值（强度、功率、光学厚度、材料参数）也收，记 simulated 或 predicted。

**不收（登记为 `not_D1`）**：
- 非线性是光电的（探测器驱动调制器、探测器 + 放大器等）——记在 D2；
- DFB-SA、FP-SA、可激发激光器等脉冲神经元（G1 / B2），只作光源的光梳（B1），储备池（F1），伊辛机（H1），做边缘检测的超表面（E2）；
- 只有归一化模型、没有物理数值的仿真；
- 非线性在数字电路、FPGA 或计算机里做的，或靠相机测强度后再由 SLM 重新编码的；
- 线性光学加数据编码得到的"非线性映射"（多次散射腔、数据重复编码、衍射网络的编码非线性、DMD 二值掩模）；
- SOA / EDFA 只补偿损耗的；
- 商用元件只当黑盒、没有表征的（例如 Photonics Res 2025 13:915 的像增强器）。

**参数名**：threshold, response_time, modulation_depth, function_shape, gain, wavelength。

**机理（`material` 列）**：saturable_absorber、Kerr、SOA、quantum_dot、atomic_vapor、thermo_optic_bistable、PCM（含 Te 熔化）、2D_material、microring_nonlinear、other（PPLN 的 χ(2)、Ge 自由载流子吸收、InGaAsP 载流子非线性、受激布里渊放大、EDFA、光折变 SBN:60、像增强器等，具体写在 `material_text`）。同一篇里反饱和吸收（RSA）的样品和可饱和吸收的样品一样记 saturable_absorber；thermo_optic_bistable 也用于只有光热非线性、没有双稳的器件（全表一致），看 `function_shape` 和 `material_text`。

**约定**：
- `threshold`：激活阈值、饱和强度或非线性开始出现的功率 / 能量，单位照原文（mW、μW、dBm、W、fJ、pJ、mW/μm2、nW/μm2、mW/cm2、W/cm2、MW/cm2）；nW 在 `value_num` 换算成 mW，μW/mm2 换算成 mW/cm2，`note` 注明。是哪一种阈值写在 `condition`。
- `response_time`：响应、恢复或开关时间（fs、ps、ns；μs 换算成 ns）。原文只给带宽的两条（Photonics Res 2025 布里渊放大器 ≥ 40 GHz、eLight 2026 PPLN 模型预测约 146 GHz）单位记 GHz，`note` 写 "reported as bandwidth, not as a time"。
- `modulation_depth`：调制深度、透过率变化或对比度，单位 % 或 dB；原文给小数的（ΔT = 0.237）在 `value_num` 换算成 %，`note` 注明。
- `function_shape` 没有数值（`value_num` 空、`unit` 空）：`value_text` 写原文对激活函数形状的描述（ReLU-like、sigmoid、tanh、双稳滞回等），D1 参数名装不下的数值说明（工作能量、激活损耗、偏置电压）也写在这里，数字都在引文里。
- `gain` 单位 dB。
- `wavelength`：工作、信号、泵浦、激发或发射波长，`condition` 写明是哪种。
- 商用元件（SOA、EDFA、量子点膜）作激活、作者测了传递曲线的，记 measured，`material_text` 写 commercial。

## 16. D2（光电非线性激活单元）约定

**纳入标准**：光先被探测器变成电信号，再经放大器、调制器或液晶回到光（或电输出直接送下一层）的非线性激活单元：探测器 + 放大器（APD / PD + TIA）、探测器驱动调制器（片上 Ge 探测器直接驱动微环、SiGe PD + TIA + 微环、透明光电晶体管 + 液晶、Si 光电二极管 + 液晶像素、平衡探测器 + 放大器驱动下一级 MZM），以及用电驱动微环 / MOSCAP 的电光传递函数、栅控二维光电探测器的非线性光响应作激活的。关键词候选只有 27 篇，另外 12 篇是在 C1、D1 候选里看到的，顺带抽了；还有 1 篇是标题 / 摘要补查补的（Nat Photon 2019 13:454 飞法级光–电–光转换器）（筛选表 `candidate` 列都为 `no (extra)`）。

**不收（登记为 `not_D2`）**：
- 光电振荡器（OEO）用作伊辛机、混沌源、强化学习加速或储备池的（H1 / F1）；
- 用于视觉的、输出电脉冲的光电神经元（I1）；
- 激活在 FPGA 或计算机里做的；
- 审稿意见文件。

**参数名**：bandwidth, energy_per_activation, programmable, function_shape, wavelength。

**平台（`platform`）**：PD_modulator、PD_amplifier、EO_feedback、other（电压驱动的 MOSCAP / PN 微环、二维光电晶体管 ORS、纳米线 FET 神经元、栅控 VSe2/WSe2 光电探测器等，具体写在 `material_text`）。

**约定**：
- `bandwidth` 单位 GHz（MHz 在 `value_num` 换算，`note` 注明）；受放大器或探测器限制的、由脉冲展宽推出的、仿真里电滤波器的带宽，都在 `condition` 写明。
- `energy_per_activation` 只放能量（fJ）；功率不记在这里。
- D2 没有增益、阈值、对比度这几个参数名，这类数值写在 `function_shape` 的文字里（数字都在引文里），例如 Optica 2025 硅光调制器神经元 14.1 dB 的光–光增益、Sci Adv 2025 NOMA 液晶 2.8 V 的阈值电压和 120 的对比度。
- `programmable`：怎么改激活函数（栅压、偏置点、开关切换函数和它的梯度），文字。
- 同一篇里探测器本身的指标记在 C1（例如 Sci Adv 2025 NOMA 的 Si 光电二极管 0.3 A/W、eLight 2025 异步光循环加速器的 Ge 探测器 0.9 A/W、Sci Bull 71:486 VSe2/WSe2 探测器的响应度、Nat Photon 2019 13:454 光子晶体探测器的 1 A/W）。

## 17. E2（计算超表面 / 模拟空间微分器）约定

**纳入标准**：论文自己的（或数值设计的）平面或薄层器件，对光场直接做模拟空间运算：一阶、二阶、混合空间微分，拉普拉斯，边缘检测，角点检测，希尔伯特变换，卷积核，积分，时空混合微分等。平台包括介质和金属超表面、光子晶体平板、薄膜和多层膜（含 Fabry–Pérot 膜、Tamm 等离激元、Kretschmann 表面等离激元结构）、超透镜、光写入液晶器件、单晶（YVO4 等）、平面界面（光自旋霍尔效应、交叉偏振反射）、交叉偏振片、二色偏振片、透镜天线网络、3D 打印太赫兹衍射层，以及在平板波导内做空间运算的片上超表面"元系统"（Nat Commun 2019 10:3547）。实验的、纯数值设计的都收；微波、太赫兹器件也收。做空间微分的衍射网络（LPR 2025 20:2502108、PhotoniX 2025 6:53）同时记在 E1 和 E2。

**不收（登记为 `not_E2`）**：
- 片上波导、微环、AWG、薄膜铌酸锂、MZI 卷积处理器（边缘检测核在芯片上算）；
- 时间微分器、积分器（微环、微盘、薄膜铌酸锂微波光子引擎、微波混响腔、时域 ENZ 超材料，包括把图像串成时域信号再微分的），以及合成频率维里的卷积；
- 光电突触、传感器内计算器件（I1），边缘检测靠器件响应或电子卷积完成的；
- 只拍光场图像、微分在数字端算的（Nanophotonics 2021 10:3709 超透镜阵列）；
- "differentiation" 指别的意思的（自动微分、梯度估计、突触可塑性）。

**参数名**：operation, NA, bandwidth, efficiency, resolution, polarization, wavelength。

**平台（`platform`）**：dielectric_metasurface、metallic_metasurface（金属或等离激元超表面，含微波、太赫兹金属结构）、photonic_crystal_slab、thin_film（薄膜、多层膜、金属膜，含格林函数多层板）、other（液晶器件、晶体、平面界面、交叉偏振片、二色偏振片、天线网络、3D 打印太赫兹衍射层、显示在 SLM 上的衍射网络、结构泵浦的非线性上转换、材料没写的螺旋超透镜、GRIN 板加超屏等，具体写在 `material_text`）。

**约定**：
- `operation`、`polarization` 是文字（`value_num` 空、`unit` 空），数字都在引文里；同一篇做几种运算的分开记。
- `NA`：单位 NA（数值孔径）或 deg（角带宽、截止角、"0–90°" 一类的角度范围）。有的是器件本身的工作 NA，有的是成像系统（物镜、4f 系统）的 NA，`condition` 写明。
- `bandwidth`：单位 nm，有两种写法：带宽宽度（单值，例如 40 nm）和工作波段（`range`，`value_num`–`value_num_hi` 是波段的起止波长）。照明光源的带宽、线宽也记，`condition` 以 "illumination" 开头。分数带宽记 %（`note` 写明），太赫兹器件有一条记 THz。
- `efficiency`：单位 %，`condition` 写明是哪种效率（透射效率、交叉偏振转换效率、衍射效率、相对理想运算的峰值强度、仿真的平均透射率等）。
- `resolution`：单位 μm（nm、mm 在 `value_num` 换算，`note` 写明）或 lp/mm；时间分辨率记 fs（ps 换算）；角空间频率（cy/mrad）和以 λ 为单位的照原文记，不换算。由 NA 推出的分辨率记 `predicted`，仿真的 PSF 大小记 `simulated`。
- `wavelength`：单位 nm（μm、mm 换算，`note` 写明）。微波、太赫兹器件按原文的频率记 GHz / THz（`note` 写 "given as a frequency"）；少数光学设计也只给了频率（例如 746.7 THz），照原文记。
- 数值设计（包括微波 SRR、毫米波 GRIN 结构）记 `simulated`；实验演示过的运算记 `measured`。
- µ 丢失的已改正：Nat Commun 2017 8:15391 的 "7.2 mm" 记为 7.2 μm，Sci Adv 2020 6:eabc4385 的 "100 m" 记为 100 μm（`note` 写明）。

## 18. E3（SLM / DMD 硬件）约定

**纳入标准**：光计算实验里用到的 SLM、DMD 和类似的可编程空间调制器——衍射层、权重 / 卷积核、伊辛机自旋编码、储备池、光计算系统的输入编码、相位光调制器等——并且至少给出一项波长以外的硬件参数：像素数、帧率、位深、像素间距，或实际使用的区域 / 宏像素大小。器件规格（该型号的像素数、间距、刷新率）和本文的实际用法都记。

**不收（登记为 `not_E3`）**：
- 只给型号或波长、没有其他参数的，或只给了衍射效率这类不在参数表里的；
- 规格只出现在仿真设定或估算里的（假设的像素间距、"可换成某型号"）；
- SLM / DMD 只给非光学处理器（事件相机加电子网络、数字模型）投测试目标或产生测试光束的；
- 传输矩阵测量方法；
- 衍射层是 3D 打印或光刻的、输入是 VCSEL 阵列的（没有 SLM / DMD）；
- "DMD" 指差分模式时延（differential mode delay）的。

**参数名**：pixel_count, frame_rate, bit_depth, pixel_pitch, wavelength。

**平台（`platform`）**：
- `LCoS_SLM`：文中写明 LCoS 或反射式液晶 SLM 的，以及已知的反射式 LCoS 产品线：Holoeye PLUTO / GAEA / LETO / LUNA / ERIS / PLUTO-TELCO / LC-R 720 / Pluto-NIR，Meadowlark 各系列（HSP512L、HSP1K、HSP192、HSP1920、P1920、E-Series、XY Phase、UHSP1K），Hamamatsu X10468 / X13138 / X13267 / X15213 / X15223，Santec SLM-100 / SLM-200，Thorlabs Exulus，UPOLabs HDSLM80R / 80R Plus / 80R Pro / 80RA / 36R，SmartVision SVC2K52L；
- `DMD`；
- `transmissive_SLM`：透射式液晶 SLM（Holoeye LC2012、扭曲向列 LC SLM）和当透射掩模用的 LCD 面板（708H、Sony LCX029）；
- `other`：类型没写的 SLM（CAS Microstar FSLM 系列、Holoeye HES6001、LBTEK-2K-8、型号和类型都没写的），自发光显示（OLED、Sony ECX335S 微显示，`material_text` 写 "emissive input display, not a modulator"），TI DLP6750 MEMS 相位光调制器（PLM），光子晶体腔阵列 SLM。

**约定**：
- `pixel_count` 单位 pixels，`value_num` 是乘积（1920 × 1080 → 2073600）。器件规格的 `note` 写 "device specification"；实际使用的区域、每层神经元数、宏像素（每个自旋、每个超像素的像素数）写在 `condition`。统计器件分辨率时按 `note` 筛。
- `frame_rate` 单位 Hz（kHz 换算）；器件规格和本文实际运行的速率都记。运行速率常受相机、控制程序或另一台 SLM 限制，`condition` 写明（"system rate …"、"limited by …"）。
- `bit_depth` 单位 bit 或 levels：器件规格（8 bit、10 bit）和编码实际用的位数 / 级数都记。二值 DMD、ON/OFF 模式记 1 bit；编码用的相位级数记 levels（例如二值相位 0 / π 记 2 levels）。Photonics Res 2022 10:2667 写的 "2-bit" DMD 照原文记，`note` 写明。
- `pixel_pitch` 单位 μm；实际使用的（合并后的）像素大小也记，`condition` / `note` 写 "used pixel size"。
- `wavelength` 单位 nm。
- 同一篇有几台 SLM / DMD 的按器件分开记（`device`、`material_text` 区分），所以一篇论文可以同时有几种平台。
- 上标丢失的已改正：PRX 2020 10:041037 的 "128 × 104" 记为 1,280,000（128 × 10^4），`note` 写明。

## 19. F1（延时 / 物理储备池计算）约定

**纳入标准**：论文自己的储备池计算（RC）硬件或数值设计：
- 单个非线性节点加延时反馈：带光反馈或光注入的半导体激光器（DFB、FP、VCSEL）、光电振荡环、电光相位 / 波长延时动力学、相干驱动的无源光纤腔、八字形光纤腔；
- 片上无源储备池（MMI 节点和波导延时线、耦合微环阵列）和片上非线性器件；
- 频分复用储备池（Si3N4 微梳、相位调制器梳）；
- 空间储备池（SLM / DMD 加散射介质或扩散片，再加相机）、多模光纤混沌储备池；
- 不带反馈环、但论文自己称为储备池的系统：下一代储备池（NG-RC）硅芯片、量子点激光器 graded neuron、电信器件（NOLM / SOA）的 ELM / RC、时间 Floquet 层、光注入 VCSEL 的准卷积编码等；
- 量子储备池（连续变量压缩光、量子忆阻器；纯数值的也收）；
- 脉冲储备池（无源硅微环、自注入锁定激光器）。

实验的、纯数值的都收。Nat Commun 2011 2:468（Appeltant 等）是电子 Mackey–Glass 延时电路，作为延时储备池的起点保留，平台记 other，`material_text` 写明 "not photonic"。

**不收（登记为 `not_F1`）**：
- 器件级物理储备池（30 篇）：储备池就是单个器件本身的衰减记忆，如忆阻器、光电突触晶体管、光电探测器、长余辉或发光材料。这些归 I1（I1 抽了其中 29 篇；另 1 篇是触觉输入的发光晶体管，输入不是光，I1 也不收）。
- 磁性 / 自旋电子学储备池（2 篇，不是光子的）；
- 只提到储备池、本身不是储备池的论文：MZI 复数光芯片、训练隐藏层权重的折叠时间深度网络、衍射 RNN。另有两篇纯理论：延时系统到深度卷积网络的映射，以及采样噪声与本征任务。
- 审稿意见文件 1 个。

**参数名**：virtual_nodes, delay, sampling_rate, task_metric, wavelength。

**平台（`platform`）**：
- `fiber_loop`：光纤延时环 / 光纤腔（光电延时环、相干驱动无源光纤腔、八字形光纤腔、相位调制器梳的光纤环）；
- `laser_feedback`：带光反馈或光注入的半导体激光器（DFB、FP、VCSEL、自注入锁定激光器；含数值模型）；
- `integrated`：片上储备池（无源 MMI / 微环网络、Si3N4 微梳、量子点激光器、片上 OPO、NG-RC 芯片等）；
- `free_space`：自由空间（SLM / DMD、散射介质、相机；连续变量量子储备池）；
- `other`：其他，具体写在 `material_text`：电子延时电路、多模光纤、电信器件 NOLM / SOA、时间 Floquet 层、不带反馈环的光注入激光器、钙钛矿微激光器等。

一篇论文里有对照器件的（例如带反馈的 TDRC 对照），按器件分开记，所以一篇可以有两种平台。

**约定**：
- `virtual_nodes`：单位 nodes；量子比特储备池记 qubits。时分复用的虚拟节点和物理节点（相机像素、SLM 宏像素、梳线、MMI 节点、输出端口、波长分量）都记，`condition` 写明是哪一种；物理节点的 `condition` 一般写 "physical" 或 "not virtual"。
- `delay`：包括以下几种，`condition` 写明是哪一种：
  - 反馈环延时 τ；
  - 节点间隔 θ；
  - 节点的响应时间或记忆时间；
  - 片上延时线的增量延时；
  - 片上总传播时延。
  单位 ps、ns、μs、ms。另有两种特殊单位：Appeltant 2011 的数值以节点时间常数 T 为单位（单位记 `T`）；无源片上储备池的节点间延时按符号周期给的，记 `symbol periods`。
- `sampling_rate`：照原文的单位记：GSa/s、MSa/s、Gbaud / GBaud、GHz、MHz、Hz，以及按吞吐量给的 images/s、frames/s、words/s。按单个样本处理时间给的记 `s per image`、`μs per datapoint`、`ms per digit`；这三种是倒数，比较前要换算。
- `task_metric`：
  - `unit` 就是指标名：NMSE、NRMSE、RMSE、SER、BER、log(BER)、WER %、accuracy %、error %、memory capacity、SSIM、dB Q-factor gain、Lyapunov times；
  - `condition` 以 "task …" 开头，写明任务（Santa Fe、Mackey–Glass、NARMA10、信道均衡、口语数字、图像分类等）和配置；
  - "从 X 降到 Y" 的只记最后的 Y。
- `wavelength`：单位 nm（μm 换算）。有一条按频率给的，记 THz。
- 数值研究记 `simulated`；"可提升到 …" 一类的记 `predicted`。

## 20. H1（光子伊辛机 / 组合优化硬件）约定

**纳入标准**：求解伊辛、XY、QUBO、最大割等组合优化问题的光学或光电硬件，以及它们的数值设计：
- 时分复用 DOPO 相干伊辛机（测量反馈或光延时耦合）；
- 光电参量振荡器 / 光电振荡器伊辛机；
- 空间光子伊辛机（SLM、DMD、波分复用、焦平面分割）；
- 片上伊辛机（MZI 网格循环采样器、耦合微腔 DOPO、光电耦合振荡器芯片、薄膜铌酸锂调制器）；
- 模拟光计算机（microLED + SLM）；
- 其他物理系统：极化激元 XY 模拟器、多芯光纤激光器、Kerr 孤子、偏振振荡器、干涉仪伊辛机、级联调制器 Hopfield 机等。

CIM 动力学的数值 / 理论研究也收（振幅不均匀修正、参量振荡器网络、景观退火、捕获–修正等），记 `simulated`。光子算法只在 FPGA 上跑的（Nat Commun 2020 11:249 PRIS）、以及数字孪生的结果也照收，`material_text` 分别写明 "electronic, not photonic"、"digital twin"。

**不收（登记为 `not_H1`）**：
- 关键词误报 76 篇：关键词 `Ising` 把 promising、rising、comprising 这类词也算进去了。按单词边界重新数，这些论文是 0 次，根本不讲伊辛模型。
- 只顺带提到伊辛机的（矩阵处理器、卷积加速器、超表面成像、光学生成模型等）和不是伊辛机的（VO2 电子振荡器、用伊辛模型配置 MZI 网格的算法、把 DOPO 网络当脉冲神经元、把储备池动力学映射成横场伊辛模型、最小功耗原理理论），共 17 篇；
- 审稿意见文件 1 个。

**参数名**：spin_count, connectivity, solve_time, success_probability, wavelength。

**平台（`platform`）**：
- `spatial_SLM`：空间光子伊辛机，SLM 或 DMD 编码自旋，相机或探测器读出；模拟光计算机也归这里；
- `time_multiplexed_DOPO`：时分复用简并光参量振荡器脉冲的相干伊辛机（光纤腔或自由空间腔）；
- `integrated`：片上伊辛机，含数值设计；
- `other`：其他，具体写在 `material_text`：
  - 光电参量振荡器（OEPO）/ 光电振荡器（时分复用的微波光子脉冲）；
  - 极化激元凝聚体、多芯光纤激光器、Kerr 孤子、偏振振荡器；
  - 自由空间干涉仪、级联调制器环；
  - CIM 理论模型、FPGA 实现等。

**约定**：
- `spin_count`：单位 spins。以下几种都记，`condition` 写明是哪一种：
  - 机器容量（腔内脉冲数）；
  - 实际解的问题规模；
  - 扫描的最大规模；
  - 预测容量（记 `predicted`）。
  一句里列了几个规模的（"N = 10, 20, … 100"），记 `list` 或分开记。
- `connectivity`：文字（`value_num` 空、`unit` 空），照原文写耦合方式（全连接、最近邻、Mattis 秩一、任意 J 矩阵、二部图等）。实现方式（测量反馈、光延时线、SLM 振幅、焦平面分割、波分复用）写在 `condition`。
- `solve_time`：单位 ns、μs、ms、s。以下几种都记，`condition` 写明是哪一种：
  - 每次迭代时间、腔往返时间；
  - 退火时间、到达目标能量的时间、收敛时间；
  - time-to-solution（99% 置信）；
  - 器件响应时间。
- `success_probability`：单位 %。基态概率（每次运行找到基态的比例）、成功率、跨实例的成功比例都记，`condition` 写明定义。"20 次里 4 次" 一类的换算成 %，`note` 写明。近似比（达到最优割值或能量的百分之几）不记。
- `wavelength`：单位 nm（μm 换算）。
- 数值研究记 `simulated`；按更快的器件外推的时间和容量记 `predicted`。

## 21. I1（传感内计算 / 光电突触）约定

**纳入标准**：论文自己做的、以光为输入、有记忆或可塑性的器件及其阵列，都是实验数据：
- 光电突触晶体管：二维、氧化物、有机、钙钛矿、量子点、碳纳米管等沟道，含浮栅、铁电栅、电解质栅和光栅控结构；
- 两端器件：光电忆阻器、光门控忆阻器、异质结或光电二极管型突触；
- 光可写的多比特光电存储器（光写入，电擦除或光擦除）；
- 传感内计算器件和阵列：栅压或偏压可调光响应度（正负光电导）的图像传感器、视网膜形态传感器、事件型视觉单元、偏振 / 光谱 / 中红外视觉器件；
- 器件级物理储备池：用单个器件的衰减记忆做储备池（F1 留给 I1 的 30 篇都在 I1 清单里，抽了 29 篇）；
- 材料本身有记忆、光进光出的光突触：长余辉 / 持续发光荧光粉、上转换纳米晶、光致变色薄膜、发光突触。它们用发光强度或透射率读出，不是集成波导上的光子权重；
- 光电器件和电学存储器集成的单元（例如光电二极管 + 忆阻器），参数照器件记。

**不收（登记为 `not_I1`，共 64 篇）**：
- 集成光子权重元件 15 篇，已记在 A3 / A4 / A5：
  - 相变材料波导或光纤突触、相变材料微环和光子晶体腔；
  - 光致变色水凝胶波导、铁电–石墨烯波导上的 "光学忆阻器"。
- 微环和微梳光网络 7 篇，已记在 A1 / A5 / B1：
  - 硅微环权重库（论文称 "microring synapse"）；
  - 微环 / MZI 光芯片；
  - 微梳光神经网络。
- 光子脉冲神经元 13 篇，已记在 G1 / B2：DFB-SA、FP-SA、VCSEL-SA 激光器，RTD 光电神经元，极化激元凝聚体，nanoLED。
- 其他类已记的 5 篇：全光非线性激活 3 篇（D1）、光电激活神经元 1 篇（D2）、微激光器储备池 1 篇（F1）。
- 自由空间系统 4 篇，已记在 E1 / E3：衍射网络加事件相机、DMD / SLM 加散射介质、多模光纤散斑加 SLM 衍射网络。
- 系统或电路级的论文 8 篇。其中有系统指标的记在 J（不在 J 关键词候选里的 2 篇也补进了 J 的清单，见第 22 节）：
  - 硅光传感内计算系统；
  - CMOS 混合图像传感芯片；
  - CMOS 图像传感器上的被动超表面 / 色素光谱滤波片；
  - 被动等离激元偏振超表面；
  - 商用事件相机加软件 SNN；
  - μLED 光互连；
  - 量子光学自旋玻璃联想记忆。
- 输入不是光的 5 篇：
  - 触觉或摩擦电输入的发光器件；
  - 机械发光薄膜；
  - 纯电驱动的 MXene 超级电容突触、质子电化学突触。
- 电编程、光只用于读出或输出的 6 篇：
  - 光学读出或电致变色的有机电化学晶体管；
  - 反射读出的 BiFeO3 FP 忆阻器；
  - 发光忆阻器 2 篇；
  - LuminoMem 浮栅存储器（A4 已记）。
- 属于该类、但文中没有 I1 数值的 1 篇：Nano Lett 2025 26:967 WS2 激子光突触。

**参数名**：wavelength_range, responsivity, PPF_index, conductance_states, nonlinearity_factor, retention, energy_per_event, dynamic_range, endurance, array_size。

**材料（`material`）**：
- `2D`：二维材料及其范德华异质结，例如 MoS2、WSe2、ReS2、黑磷、石墨烯、α-In2Se3、CuInP2S6、h-BN 隧穿层；也包括二维沟道加量子点或有机层的复合结构。
- `oxide`：氧化物，例如 IGZO、In2O3、ZnO、Ga2O3、WO3、TiOx、HfO2、CeO2、MoOx、FeOx、PZT、BiVO4、ITO / Nb:SrTiO3。
- `organic`：有机小分子、聚合物和有机异质结，例如 pentacene、DNTT、BTBT、P3HT、DPP 类聚合物、CDot-PANI、光致变色分子。
- `perovskite`：卤化物钙钛矿，例如 MAPbI3、CsPbBr3 量子点、二维 / 准二维钙钛矿、无铅钙钛矿衍生物；钙钛矿量子点加碳纳米管或二维沟道的复合结构也归这里。
- `Si`：硅，例如硅纳米晶 / P3HT、非晶硅径向结、ITO/n-Si 异质结、商用硅光电二极管。
- `III_V`：III–V 族，例如 InP 纳米片、InP 量子点、InGaAs 光电二极管、GaAs 纳米线、AlGaN/GaN 纳米线。
- `other`：其他，具体写在 `material_text`，例如：
  - 长余辉 / 持续发光荧光粉、镧系上转换纳米晶；
  - 金刚石、碳纳米管、Te 或 Bi 薄膜、PbS、AgBiS2、CdSe 量子点 / PZT、GLSO 硫系玻璃；
  - NbN 超导纳米线单光子探测器。

一篇论文里有两种器件的按器件分开记，所以一篇可以有两种材料（只有 1 篇：商用硅光电二极管和钙钛矿光电二极管）。

**约定**：
- `wavelength_range`：单位 nm（μm 换算）。有三种写法，`condition` 写明是哪一种，以及光强、脉宽：
  - 响应波段，记 `range`，例如 "365–1550 nm"；
  - 突触测试用的几个刺激波长，记 `list`；
  - 单个刺激波长。
- `responsivity`：单位 A/W（mA/W、μA/W 换算）。
  - C1 已经记了响应度的论文（同一器件的探测器指标），I1 不再记响应度；波长照记，`condition` 写 "responsivity in C1"。
  - 正负光电导的双极器件，负的响应度记负值；可编程区间（"±160 mA/W"）记 `±`。
- `PPF_index`：单位 %，照原文记。
  - 多数是 A2/A1 × 100%（大于 100% 为易化）。小于 100% 的 9 条是按 (A2 − A1)/A1 × 100% 给的：7 条文中写明，2 条由数值推断，`note` 写明。
  - 原文给比值的（例如 "1.42"）换算成 % 记，共 8 条，`note` 写明。
  - 电脉冲测的 PPF 也记，`condition` 写明。
- `conductance_states`：单位 states。
  - 光编程（或电编程）的可区分电导态、电流态、发光态都记。
  - "N-bit" 记 2^N 个态。
  - 储备池用 N 位光脉冲序列得到的可区分响应数也记在这里（例如 4 位 → 16 个），`condition` 写明。
- `nonlinearity_factor`：无量纲。主要是 LTP / LTD 权重更新的非线性因子，定义不一（NL、α、β、ν、A 等），`condition` 写明。另有一条是光电流随时间的幂指数 α（Iph ∝ t^α）。
- `retention`：单位 s、min、h（年换算成 h，1 年 = 8766 h）。
  - 记状态能保持多久。
  - 论文只给拟合的衰减 / 弛豫时间常数（τ、1/e 衰减时间）当记忆时间的，也记，`condition` 写明。
  - 同一篇既给保持时间又给 τ 的，一般只记保持时间。例如 Nat Commun 2020 11:5934 记 3600 s / 1200 s，不记 8.61 s / 1.43 s 的 τ。
  - 外推的（例如 "11.1 年"）记 `predicted`。
- `energy_per_event`：单位 aJ、fJ、pJ、nJ、μJ、mJ（zJ、J 换算）；另有 2 条按面积归一化，记 nJ/cm2。
  - `condition` 写明怎么算的：电能（I × V × t）、入射光能（光功率 × 脉宽，或光功率密度 × 面积 × 脉宽），或两者之和。
  - 同一句列了几个值的，换成同一单位记 `list`。
- `dynamic_range`：单位 ratio、dB、%。
  - ratio：开关比、Gmax/Gmin、光暗电流比；
  - dB：多为线性动态范围（LDR），也有存储动态范围；
  - %：调制深度或权重变化幅度。
- `endurance`：单位 cycles。
  - 光写 / 电擦、光写 / 光擦和纯电学的循环都记，`condition` 写明。
  - 几次到几十次的重复性测试也记。
  - 机械弯折次数不记。
- `array_size`：单位 devices，记阵列的器件总数（行 × 列；`value_text` 照抄，例如 "32 × 32"）。只记实际做出来的阵列，仿真里的阵列不记。
- 电学模式测的指标也记，例如电脉冲编程的开关比、保持、耐久、电导态、能量、PPF：
  - `condition` 写明是电学的；
  - 后面的脚本统一以 "electrical: …" 开头；
  - 前面的写在句中或句尾，例如 "(electrical)"、"gate pulses"。
- 准确率不记，系统级指标归 J。但 J 只看自己的候选清单，I1 的 250 篇里只有 38 篇在其中，其余论文的准确率两边都没有记（见第 24 节）。
- 1112 条里没有仿真记录；外推或估算的 6 条记 `predicted`。

## 22. J（系统级指标）约定

**纳入标准**：论文自己的光计算 / 光电计算系统给出的系统级数值，即吞吐量（算力）、能效、计算密度、延时、精度、矩阵规模、准确率、时钟 / 符号率。实验值、仿真值和预测值都收，用 `status` 区分。器件级数值不收，它们归 A–I 各类。

**候选**：
- v4 关键词清单里 J 命中 ≥ 4 次的 539 篇，去掉 3 个审稿意见文件，剩 536 篇。其他类筛选时注明 "J" 的 7 篇都在其中。
- I1 不收的论文里，有 2 篇被写成 "有系统指标的留给 J"，但不在这 536 篇里，补在清单末尾：Nat Commun 2024 15:505（散射介质光子联想记忆）、Science 2026 394:212（量子光学自旋玻璃联想记忆）。筛选表里它们的 `candidate` 列为 `no (extra)`，`keyword_hits_J` 记 0。
- 两部分合并成 538 篇的 `worklist_J.json`。10-30 晚按标题 / 摘要又补了 11 篇（第 26 节），清单共 549 篇。J 只看这 549 篇，不在清单里的论文即使文中有准确率或算力也没有记（见第 24 节）。

**不收（登记为 `not_J`，共 100 篇）**：
- 器件级论文 16 篇：相变材料存储器和移相器，铁电、磁光、忆阻类光子存储器，微环调制器，耦合波导酉矩阵等。器件参数已记在 A1–A6。
- 计算超表面 / 模拟微分器 10 篇（E2 已记），文中没有系统级计算指标。
- 系统数值已记在其他类、此外没有别的系统级数值的 39 篇，例如：
  - 衍射网络：准确率、网络规模在 E1，帧率在 E3；
  - 储备池：在 F1；
  - 伊辛机、光子玻尔兹曼机：在 H1；
  - 光逻辑、比较器：线速率在 A2；
  - 光电突触阵列：在 I1。
- 数值或理论研究 13 篇：只有相对比较、设计误差或缩放公式，没有自己的系统数值。
- 指标只属于电子部分的 10 篇：GPU / CPU / FPGA 的速度和功耗、CMOS 估算、电子伊辛求解器、光子 ADC 加 GPU 后端等。
- 其他 12 篇：
  - 只有 SSIM / PSNR / MSE / mIoU、检测灵敏度、安全性指标、联想记忆容量、期权定价的收敛等非 J 指标（期权定价那篇 Photonics Res 2023 11:1703 是补查补的）；
  - 只有相对提升，或单位无法解读；
  - 可用的文字版里没有系统数值。

综述、展望、评论 93 篇（含 5 篇 News & Views）只登记不抽。重复文件 11 个：10 个截断文件名的副本，1 个录用稿副本。

**参数名**：throughput, energy_efficiency, compute_density, latency, precision, matrix_size, accuracy, clock_rate。

**平台（`platform`，按该数值所属的硬件记）**：
- `MZI`：相干干涉网格 / MZI 处理器，含由 MZI、定向耦合器组成的相干交叉阵列。
- `MRR_WDM`：非相干波分复用处理器。包括微环权重库、broadcast-and-weight、微梳 + 微环；微梳时间–波长交织（WaveShaper 权重）也归这里，`material_text` 写明。
- `PCM`：相变材料光子张量核 / 交叉阵列 / 存内光计算。
- `diffractive_free_space`：衍射 / 超表面网络（自由空间）。片上衍射 metaline 也归这里，`material_text` 写 "on-chip"。
- `SLM_free_space`：自由空间 SLM / DMD 矩阵乘法、4f / 傅里叶光学卷积、散射介质加 SLM / DMD 的计算。
- `reservoir`：光子储备池计算系统。
- `spiking`：光子脉冲神经网络系统。
- `in_sensor`：传感内 / 近传感计算系统（会计算的传感阵列）。计算部分是衍射网络的也归这里，网络参数在 E1。
- `microwave`：微波光子处理器、射频域计算，含微波超表面计算。
- `hybrid`：数值同时覆盖光学和电子两部分的光电混合系统；伊辛机和用电子做矩阵乘法的光电系统也归这里。
- `other`：其他，具体写在 `material_text`。例如：
  - 薄膜铌酸锂张量核；
  - 延时线 / 多模干涉 / 模分复用卷积器；
  - 逆向设计的纳米光子介质；
  - VCSEL 阵列、光纤阵列；
  - 光逻辑张量核、光互连；
  - 用全光非线性元件搭的网络。

一篇论文里的数值属于不同硬件的，按硬件分开记，所以一篇可以有两种平台（11 篇）。

**约定**：
- `value_text` 照抄；`value_num` 用原文的单位前缀，不换算（"trillion operations per second" 这类文字写法记 TOPS）。例外是本节最后一条列的单位换算，`note` 写明原文。
- `throughput`：
  - 单位：POPS、TOPS、GOPS、MOPS；PMAC/s、TMAC/s、GMAC/s；PFLOPS、TFLOPS、GFLOPS、MFLOPS；images/s、frames/s、inferences/s、samples/s。
  - 两种按比特算的单位照原文记，不能和 OPS 比：Gb/s/MAC（按比特归一的吞吐量）、Tb/s（光逻辑张量核的逻辑容量）。
  - 论文写明 "1 MAC = 2 OPs" 的写在 `condition`。
- `energy_efficiency`：
  - 单位：POPS/W、TOPS/W、GOPS/W、MOPS/W、TMAC/s/W、TFLOPS/W；aJ/OP、fJ/OP、pJ/OP、nJ/OP；zJ/MAC、aJ/MAC、fJ/MAC、pJ/MAC；photons/MAC。
  - 每次推理 / 每帧记 fJ–mJ/inference，`condition` 写 per frame / per image；每像素记 pJ/pixel、nJ/pixel；按比特的记 pJ/b/MAC，光逻辑记 fJ/bit。
  - TOPs/J 记为 TOPS/W。
  - `condition` 写能量边界：只算光学、含激光器、含电子、只算芯片等。
- `compute_density`：单位 POPS/mm2、TOPS/mm2、GOPS/mm2、MOPS/mm2、PMAC/s/mm2、TMAC/s/mm2、GMAC/s/mm2、TFLOPS/mm2；光逻辑处理器为 Gb/s/mm2。
- `latency`：
  - 单位 fs、ps、ns、μs、ms、s。
  - `condition` 写是什么时间：单次 MVM、单层或端到端，光传播时间，含不含电子部分。
  - 每像素的延时记 ps，`condition` 写 "per pixel"。
- `precision`：单位 bits。系统计算精度和系统里权重元件的精度都记，`condition` 写明是哪一种。
- `matrix_size`：单位 weights 或 neurons。
  - weights：矩阵元素数 N × M，`value_text` 照抄，例如 "64 × 64"，`value_num` 记 4096；
  - neurons：神经元 / 通道数，照原文。
- `accuracy`：单位 %。
  - 每个任务 / 数据集记主要结果：实验值记 `measured`；文中给了对应的仿真 / 理想值的，另记 `simulated`。
  - 只在训练集上的准确率不记。
  - 偏微分方程求解、模拟计算给的 "computational accuracy" 也记在这里，`condition` 写明。
- `clock_rate`：
  - 单位 THz、GHz、MHz、kHz、Hz；GS/s、MS/s（原文写 GSa/s 的照抄在 `value_text`，单位记 GS/s）；GBd、MBd、kBd（原文写 Gbaud / GBaud 的照抄，单位记 GBd）。
  - 按 OOK（一个符号一个比特）给的线速率（Gb/s）记 GBd；原文把 giga-symbols per second 缩写成 "GS s−1" 的也记 GBd。都在 `note` 写明。
- `status`：
  - `measured`：演示系统在演示工作点的数值。用实验自己的时钟 × 运算数、实际元件的功耗算出的数也算。
  - `simulated`：数值结果、用实测器件曲线仿真的网络、数字对照。
  - `predicted`：预测、外推、按比例放大、"could reach"、理论峰值、假设的未来元件。
  - 具体判法见下面四条。
- 能量预算的判法：
  - 每一项都属于演示装置的（实测值，或实际所用器件的手册值 / 典型值），记 `measured`（计算值）。
  - 加进了文献或假设的 DAC、ADC、TIA、激光器电光转换效率、替换或集成元件的，或按假设 / 归一化的速率算的，记 `predicted`，`note` 写明哪一项是假设的。
  - 片上加热器功耗按实测调谐算的，仍记 `measured`。
- 速率的判法：
  - 速率取器件上限的，以及由它推出的所有指标，记 `predicted`。例如 "performance upper limit reference benchmark"、DFB-SA 最大自脉冲频率、相机上限帧率、电光带宽。
  - 按器件响应时间折算的时钟（例如 260 ps 神经元 → 3.85 GHz）同样记 `predicted`。
  - 按实际芯片内部延时算出的延时仍记 `measured`，`condition` 写明不含什么。
- 全芯片所有通道同时工作的最大值（"peak computational capacity"），而实验一次只用了部分通道的，记 `predicted`。论文另给实验中数值的，另记一条 `measured`。
- 说法和依据不一致的：
  - 摘要说成已实现、SI 显示是估算的，记 `predicted`，`note` 说明。例如 Sci Adv 2026 12:eaef7533 的 1694 fps 假设用 10 MHz EOM 代替实验用的 500 Hz VOA。
  - 用只是提出的元件（"can be utilized"、"can be scaled up"）算出的延时或速度，记 `predicted`。
  - 能耗推导在 SI 某节、而可用的文字版里没有那一节的，照论文的说法记（说成已实现的就记 `measured`），`note` 写 "basis could not be checked"。
  - 正文和 SI 不一致的，按给出推导的那处记，`note` 写明。
- 每个数值只记在一类里（核对程序会检查）：
  - E1 或 F1 已抽的论文，J 不记准确率和矩阵规模；
  - H1 已抽的，J 不记矩阵规模，也不记伊辛机的迭代 / 求解时间（在 H1 `solve_time`）；
  - A6 已抽的，J 不记矩阵规模；A5 已抽的，J 不记矩阵规模和精度；
  - 同一篇里其他类已经记过同一含义的数值，J 不再记，即使出自另一句。例如 A2 的 `data_rate`（就是系统符号率时）、E3 帧率、F1 采样率、G1 每次发放能量、I1 每次事件能量、D1 响应时间；
  - J 的记录不能与其他类同一篇出自同一句的同一个数重复。
- 不记：
  - 其他工作的文献值、对比表；电子基线（GPU / CPU）；只作对比用的常规方案的数值；每个 epoch 的训练曲线；
  - 只有相对说法的（"比 CPU 低四个数量级的延时"），以及模糊量级（"几十 POPS"）；
  - 按面积归一的能效（TOPS/W/mm2）、IoU / mIoU（不是准确率）、单位无法解读的（"GMAC/pJ"）；
  - 只属于电子部分的指标（GPU 上的 SNN、带 GPU 后端的光子 ADC）；
  - 光电突触或忆阻器每个光 / 电脉冲的能量。这是器件级的，归 I1 `energy_per_event`。
- 给电子集群用的光互连，只记系统延时和精度，平台记 `other`。
- 传感内 / 忆阻器储备池：每种输入组合的储备池状态都实测、读出层在软件里的，记 `measured`；用器件表征统计 "生成" 数据集的，记 `simulated`。
- 单位换算（`value_num` 换算，`note` 写原文）：
  - mW/TOPS、W/TOPS、W/PetaOPS → TOPS/W；
  - μJ/OP → nJ/OP；
  - 以 J 给的每帧能量 → mJ/inference；
  - 指数丢失的 OPs/J → POPS/W；
  - 原文 "pJ/OPS"、"fJ/OPS" 指每次运算能量的 → pJ/OP、fJ/OP；
  - 光逻辑每比特能量 → fJ/bit；
  - KOPS → MOPS。

## 23. 数量

**A3**
- 论文：155 篇候选 → 87 篇抽取、43 篇综述、24 篇非 A3、1 篇重复。
- 记录：1636 条（实测 1471，仿真 155，预测 10）。
- 材料：GST 723、Sb2Se3 408、Sb2S3 129、GSST 82、other 50、GSSe 44、N-GST 44、Sb 37、Te 26、Se 24、GSSST 23、AIST 19、SbTe 14、GeTe 13。
- 参数最多的几类：脉冲幅度 190、脉宽 175、开关能量 160、对比度 151、波长 110、膜厚 104、单元长度 96、电平数 89。

**E1**
- 论文：254 篇候选 → 190 篇抽取、44 篇综述（含评论、展望）、18 篇非 E1、2 篇重复。另有 1 篇在库里有两个文件名，记录挂在带 SI 的那个文件名下。标题 / 摘要补查又补了 12 篇（第 26 节），全部抽取。有记录的论文共 203 篇。
- 与 v3.3 判断的对照：v3.3 认为是本文器件的 195 篇 → 179 篇抽取、12 篇不属于 E1、2 篇其实是评论、2 篇是重复文件；v3.3 认为不是本文器件（也不是综述）的 15 篇 → 10 篇其实有自己的衍射网络设计（多为纯数值），已抽取，5 篇确实不属于 E1；v3.3 归为综述的 44 篇 → 42 篇确是综述 / 展望 / 评论，2 篇其实是研究论文（1 篇抽取，1 篇不属于 E1）。
- 记录：1875 条（实测 1235，仿真 639，预测 1）。
- 按主要平台分的论文数（每篇取实测记录里最多的平台）：SLM/DMD 44、纯数值 36、3D 打印聚合物 30、介质超表面 25、片上 19、双光子打印 17、PCB 微波 17、其他材料（石英等）13、液晶 2。
- 有实际加工层的论文 154 篇；"实际加工层数"记录共 167 条：1 层 46 条、2 层 55 条、3 层 36 条、4 层 16 条、5 层 11 条、6 层 3 条（同一篇可能有几种实验配置）。
- 参数条数：精度 343、层数 251、像素间距 197、每层神经元数 188、波长 161、层间距 152、加工方式 140、效率 100、输出距离 99、层尺寸 89、输入距离 64、频率 56、相位级数 35。

**A1**
- 论文：127 篇关键词候选 → 67 篇抽取、49 篇非 A1（多为加热器只切换相变材料，或调谐不是热光）、10 篇综述、1 篇重复；另从 A5 候选里顺带抽了 20 篇（另 1 篇重复），A2/A4/A6 的脚本顺带记了 15 篇。有记录的论文共 102 篇。
- 记录：247 条（实测 228，仿真 8，预测 11）。
- 加热器材料（记录数 / 论文数）：TiN 108 / 44、metal_other 68 / 23、not_stated 51 / 30、doped_Si 11 / 5、ITO 7 / 2、graphene 2 / 1。
- 参数条数：调谐功率 70、Pπ 52、电阻 43、加热器长度 25、响应时间 21、调谐效率 20、热串扰 14、插入损耗 2。
- 实测 Pπ（mW）45 条：1.26–200 mW，中位数 20 mW。TiN 21 条：硅波导上的 18 条为 1.26–35 mW，SiN MZI 上 2 条（12、18.8 mW），二氧化硅 PLC 上 1 条（200 mW）；其他金属 7 条，12–161 mW；没写材料的 14 条，1.3–90 mW；ITO 2 条（22.01、25.78 mW），石墨烯 1 条（10.2 mW）。电阻 43 条：54 Ω 到 6.03 kΩ（另有轻掺杂硅 433 kΩ 一条）。

**A5**
- 论文：227 篇候选 → 120 篇抽取、69 篇非 A5（多为环只作光梳源或只被引用）、34 篇综述 / 展望、4 篇重复。
- 记录：467 条（实测 437，仿真 23，预测 7）。
- 平台（记录数 / 论文数）：SOI 374 / 93、other 40 / 9、SiN 32 / 10、LNOI 13 / 5、III_V 8 / 3。
- 参数条数：半径 73、环数 / 通道数 65、FSR 54、权重精度 52、Q 49、波长 47、消光比 46、线宽 24、调谐效率 23、通道间隔 22、串扰 12。
- Q（49 条）：SOI 多为 10^3–10^5；LNOI 测试环 0.9–3 × 10^6；光纤微球 1.4 × 10^7；InP 带 SOA 增益补偿的等效 Q 约 5 × 10^7（由积分时间算出，`condition` 已注明）。

**A2**
- 论文：320 篇候选 → 51 篇抽取、222 篇非 A2（多为商用 / 台式调制器、热光调制、自由空间器件、非易失器件）、45 篇综述 / 展望、2 篇重复；另由 B1/B2/G1 的脚本顺带记了 1 篇；标题 / 摘要补查的 1 篇（Nat Photon 2019 13:454）不收，它的调制器只在光–电–光转换器里表征，数值记在 D2。有记录的论文共 52 篇。
- 记录：203 条（实测 195，仿真 1，预测 7）。
- 材料（记录数 / 论文数）：Si_carrier 82 / 22、TFLN 77 / 17、other 29 / 9、III_V 8 / 2、graphene 4 / 1、plasmonic 3 / 1。
- 参数条数：电光带宽 47、速率 42、消光比 24、Vπ 20、波长 18、插入损耗 14、VπL 13、每比特能量 13、长度 12。
- 实测 VπL（V·cm）：TFLN 2.2–3.62；硅载流子 0.09（MOSCAP 微环）–0.92；磷烯 0.33、PZT 0.5、AlN 压电推挽 50–65。实测电光带宽：TFLN 2.5 GHz（集总电极）到约 100 GHz（另有一条 6-dB 带宽 100 GHz）；硅载流子 3.8 GHz 到 > 110 GHz（另有 4 条 MHz 级的低速器件）。

**A4**
- 论文：291 篇候选 → 18 篇抽取、197 篇非 A4（多为相变材料、输出为电信号的光电突触 / 传感器内计算器件）、55 篇综述 / 展望、21 篇重复（多为截断文件名和只有 SI 的文件）；标题 / 摘要补查的 1 篇（Nat Nanotechnol 2026 片上全光开关磁化，电学读出）不收。
- 记录：108 条（实测 105，预测 3）。
- 材料（记录数 / 论文数）：ferroelectric 57 / 10、memristor 21 / 2、other 14 / 3、MEMS 7 / 1、charge_trap 6 / 1、magneto_optic 3 / 1。
- 参数条数：写入电压 16、保持时间 14、写入时间 12、写入能量 12、耐久 10、插入损耗 10、电平数 9、相移 9、波长 7、消光比 6、静态功耗 3。

**A6**
- 论文：237 篇关键词候选 → 75 篇抽取、125 篇非 A6（多为非相干交叉阵列、微环网格、衍射 / 延时线电路、纯理论或仿真）、36 篇综述 / 展望、1 篇重复；另从 A2 候选里顺带抽了 1 篇（Adv Sci 2026 铌酸锂电光处理器）。有记录的论文共 76 篇。
- 记录：398 条（实测 382，仿真 12，预测 4）。
- 平台（记录数 / 论文数）：SOI 330 / 63、SiN 23 / 5、silica_PLC 17 / 3、other 15 / 3、LNOI 13 / 2。
- 参数条数：网格规模 60、架构 60、校准 / 训练方法 49、保真度 40、MZI 数 39、总插入损耗 26、串扰 26、波长 23、消光比 22、每级损耗 21、带宽 18、总功耗 14。
- 网格规模（`mesh_size` 条数，列举几种规模的按最大的算）：4 × 4 最多（28 条），其次 8 × 8（9）、6 × 6（7）、3、5（各 4）、16（3）；另有按接入端口计的 9、10、28。
- 保真度（40 条）的单位：% 20、fraction 7、bit 5、similarity 4、relative error % 2、MSE 1、dB 1。实测的 % 保真度从 90%（多端口处理器）到 99.997%（NC 2024 Xbar）；0–1 刻度的实测保真度 0.921（直接编程）到 0.999（Science 2015 六模处理器）。

**B1**
- 论文：47 篇关键词候选 → 29 篇抽取、10 篇综述 / 展望、8 篇非 B1（梳只当脉冲或时钟光源、多台可调激光器当通道、梳只在仿真里假设等）；另顺带抽了 2 篇激光器阵列当 WDM 光源的（ACS Photonics 2024 EA-MWL、Sci Adv 2025 HITOP）。有记录的论文共 31 篇。
- 记录：111 条（实测 109，仿真 1，预测 1）。
- 平台（记录数 / 论文数）：Si3N4 37 / 10、other 32 / 12、electro_optic_comb 20 / 4、Hydex 19 / 5、AlGaAs 3 / 1。
- 参数条数：梳间隔 35、线数 33、波长 22、泵浦功率 15、单线功率 6。
- 梳间隔（按 GHz 给的 28 条）：电光梳 2–84 GHz；Hydex 孤子晶体 48.9–50.2 GHz；Si3N4 多为 100 GHz（另有 485 GHz 的自注入锁定微梳）；AlGaAs 91 GHz（隔一根取线为 182 GHz）；切片光源 25–36 GHz。按 nm 给的 7 条：0.32–0.8 nm。
- 计算中实际使用的线数 2–108 根；产生的线数最多约 150 根（混沌梳）。

**B2**
- 论文：54 篇关键词候选 → 31 篇抽取、14 篇综述 / 展望、9 篇非 B2（台式或商用多端口光源、只有归一化参数的数值研究、只提名的泵浦激光器等）；另从 G1 候选里顺带抽了 8 篇（DFB-SA、FP-SA、FP、量子点激光器神经元的激光器参数）。有记录的论文共 39 篇。
- 记录：102 条（实测 100，仿真 1，预测 1）。
- 平台（记录数 / 论文数）：VCSEL 43 / 12、DFB 37 / 15、FP 10 / 6、microlaser 7 / 3、other 3 / 2、QD_laser 2 / 1。
- 参数条数：波长 31、阈值电流 28、输出功率 17、激光器数 15、调制带宽 6、能量 5。
- 实测阈值电流：VCSEL 0.3–2.96 mA；DFB / DFB-SA 7.92–86 mA；FP / FP-SA 8–30 mA；双段量子点激光器约 200 mA；光泵浦光子晶体纳米激光器为泵浦功率 3–4 μW。
- 实测调制带宽：VCSEL 2–13.6 GHz（商用 VCSEL 7 GHz）；半导体激光二极管 > 10 GHz。阵列规模 2–64 个激光器（VCSEL 5 × 5、8 × 8；DFB-SA 2、4、16 通道；DFB 32 通道）。

**G1**
- 论文：164 篇关键词候选 → 33 篇抽取、82 篇非 G1（大多是输出为电信号的光电突触 / 传感器内计算器件）、40 篇综述 / 展望、9 篇重复（截断文件名）。
- 记录：76 条（实测 66，仿真 9，预测 1）。
- 平台（记录数 / 论文数）：other 32 / 12、DFB_SA 21 / 11、microring 9 / 4、FP_SA 7 / 3、PCM 4 / 2、VCSEL 3 / 2。
- 参数条数：波长 25、发放率 14、每脉冲能量 13、脉宽 10、不应期 8、阈值 6。
- 实测最大发放率：RTD 光电神经元约 10 MHz、电驱动硅微环 250 MHz、DFB-SA 0.77–5.23 GHz、FP-SA 1.43–3.34 GHz、无可饱和吸收区的 FP 注入锁定 5 GHz。
- 实测脉宽约 10 ps（激子极化激元凝聚体）、15 ps（FP-SA Q 开关）到 200 ns（无源硅微环）；实测不应期从微柱激光器的 < 200 ps（绝对）到 RTD 神经元的约 90 ns。
- 每脉冲能量从 7.329 fJ（FP-SA，估算）到 1.5 nJ（相变材料神经元一个完整周期），口径不一（见第 24 节）。

**C1**
- 论文：251 篇关键词候选 → 61 篇抽取、147 篇非 C1（多为探测器只用于读出、没有本文探测器指标的系统论文，商用或从 PDK 引来的数值，只以光电突触 / 传感器内计算器件出现的 I1 器件，以及 1 篇纯计算（DFT + NEGF）的论文）、30 篇综述 / 展望、13 篇重复（全标题副本、SI 文件、接收稿副本）；标题 / 摘要补查又补了 1 篇（Nat Photon 2019 13:454 的 InGaAs 光子晶体探测器）。有记录的论文共 62 篇。
- 记录：181 条（实测 180，预测 1）。
- 材料（记录数 / 论文数）：2D_other 77 / 27、Ge 39 / 11、other 18 / 7、organic 17 / 4、Si 10 / 3、perovskite 9 / 5、InGaAs 6 / 3、graphene 5 / 2。
- 参数条数：响应度 70、波长 53、暗电流 26、带宽 20、NEP 12。
- 实测响应度：Ge 光电二极管 0.413–1.08 A/W；有增益的光电晶体管 / 光电导器件高得多（二维 6515、8500 A/W，钙钛矿量子点复合 5.1 × 10^7、1.4 × 10^8 A/W）；栅压或偏压可编程的双极器件给的是 −60 到 +60 mA/W 一类的区间。
- 实测带宽：Ge 3.1 GHz 到 > 65 GHz；二维、有机、石墨烯光电导器件 33.8 Hz 到 230 MHz。实测暗电流：Ge 0.013 nA 到约 20 μA（高速 PD），二维器件 8.6 × 10^−5 到 0.95 nA。NEP 1.4 × 10^−15 到 2.4 × 10^−11 W/√Hz。

**D1**
- 论文：217 篇关键词候选 → 53 篇抽取、113 篇非 D1（多为线性光学 / 衍射 / 数字激活的系统论文、非线性是光电的（记入 D2），以及脉冲神经元、储备池、伊辛机；另有 3 篇核对后移出：PPLN 没有本文表征、液晶 Kerr 单元对输入是线性的、光电子发射显微读出没有光输出）、48 篇综述 / 展望、3 篇重复。标题 / 摘要补查 4 篇：2 篇抽取（Nature 2025 649:330 可编程片上倍频、Adv Mater 2025 37:2507612 钙钛矿微线极化激元），2 篇不收。有记录的论文共 55 篇。
- 记录：192 条（实测 172，仿真 16，预测 4）。
- 机理（记录数 / 论文数）：other 81 / 22、saturable_absorber 33 / 6、thermo_optic_bistable 16 / 4、SOA 12 / 5、PCM 12 / 2、Kerr 10 / 4、atomic_vapor 10 / 5、microring_nonlinear 9 / 4、2D_material 5 / 2、quantum_dot 4 / 2。
- 参数条数：函数形状 67、波长 46、阈值 43、响应时间 20、调制深度 11、增益 5。
- 实测阈值（按单位分）：功率 24 nW（布里渊放大器）到 15.13 mW（可饱和吸收），另有一条 14.12 W（见第 24 节）；能量 0.42–120 fJ，另有 0.51 pJ（可饱和吸收，每次激活）、0.9–4.6 pJ（相变材料）、约 20 pJ（PPLN 脉冲泵浦的起始能量）、175 pJ（极化激元凝聚，每个神经元平均）；功率密度 0.13–0.64 mW/cm2（钙钛矿膜、量子点膜）、0.1–0.738 mW/μm2（热光双稳）、10–20 W/cm2（Kerr，逻辑 0 和 1 两种输入之间）、3.404 MW/cm2（可饱和吸收）。
- 实测响应时间：约 18 fs（本征开关时间）、46–75 fs（全光开关、ReLU，含 (47.3 ± 3.0) fs），0.48–300 ps（可饱和吸收、相变材料等），约 6 ns（CsPbBr3 载流子寿命），约 20 μs（像增强器）。

**D2**
- 论文：27 篇关键词候选 → 5 篇抽取、17 篇非 D2（多为光电振荡器用作伊辛机、混沌源或强化学习加速，视觉用的光电神经元，以及激活实际在数字端完成的）、5 篇综述 / 访谈；另从 C1、D1 候选里顺带抽了 12 篇，标题 / 摘要补查补了 1 篇（Nat Photon 2019 13:454）。有记录的论文共 18 篇。
- 记录：65 条（实测 57，仿真 3，预测 5）。
- 平台（记录数 / 论文数）：PD_modulator 35 / 11、other 23 / 6、PD_amplifier 7 / 2。
- 参数条数：函数形状 31、波长 10、带宽 10、可编程方式 9、每次激活能量 5。
- 带宽：实测 2.2 MHz（MOSCAP 微环）、43 MHz（RF 光子处理器，受放大器和探测器限制）、约 90 MHz（eLight 2025 波长中继单元）、约 105 MHz（LSA 2025 14:328，由拟合的 1.67 ns RC 延时得出）、3.3 GHz（Nat Photon 2019 13:454 光–电–光转换）、5.4 GHz（PN 微环）、8 GHz（APD + TIA，器件规格）、> 12 GHz（Nature 2022 片上深度网络的放大器，器件规格）；仿真 12.5 GHz；预测约 1 GHz。
- 每次激活能量：实测 3.2 fJ/bit（Nat Photon 2019 13:454，电阻负载探测器每比特的耗散）、100 fJ（Sci Adv 2025 NOMA 每像素）、约 200 fJ（Nat Commun 2026 17:4798，由 20 pW 下的实测工作估算）；预测 69 fJ（透明光电晶体管 + 液晶）、约 4 fJ。

**E2**
- 论文：139 篇关键词候选 → 84 篇抽取、35 篇非 E2（多为片上卷积处理器、时间微分器 / 积分器，以及 I1 光电突触和传感器内计算器件）、16 篇综述 / 展望、4 篇重复（全标题副本、带 SI 的副本）。标题 / 摘要补查 19 篇：16 篇抽取（边缘增强成像超表面、片上空间积分 / 希尔伯特变换、求解积分方程的超材料、微波计算超表面等），3 篇不收（偏振逻辑、射频电路网络、声学时域求解）。有记录的论文共 100 篇。
- 记录：509 条（实测 350，仿真 133，预测 26）。
- 平台（记录数 / 论文数）：dielectric_metasurface 266 / 46、other 91 / 28、photonic_crystal_slab 57 / 8、thin_film 52 / 8、metallic_metasurface 43 / 11（1 篇有两种平台）。
- 参数条数：波长 125、运算 121、分辨率 76、偏振 68、NA 50、效率 38、带宽 31。
- 实测 NA 0.029–0.966（22 条，0.34 和 0.5 最多）；仿真 NA 最高 0.99。按角度给的 6 条：实测 0.5°，仿真 3°–90°（截止角、角度范围）。
- 实测效率 5%–98%（27 条，定义不一，见第 24 节）。
- 实测分辨率 0.76–560 μm（34 条，多数在 1–10 μm），另有 28.5–228 lp/mm 4 条。
- 实测波长 405 nm–10.6 μm（86 条）；按频率记的波长 16 条：GHz 10 条（实测 5 条，都是微波计算超表面或求解方程的结构），THz 6 条（实测 2 条；仿真 4 条里有 2 条是只给了频率的光学设计）。

**E3**
- 论文：191 篇关键词候选 → 116 篇抽取、48 篇非 E3（多为只给型号或波长、没有硬件参数的，规格只在仿真里出现的，以及 SLM / DMD 只给非光学处理器投测试目标的）、25 篇综述 / 展望、2 篇重复（SI 文件）。
- 记录：551 条，全部记 measured（都是本文实验所用硬件的参数）。
- 平台（记录数 / 论文数）：LCoS_SLM 336 / 86、DMD 129 / 30、other 68 / 21、transmissive_SLM 18 / 7（27 篇用了两种以上）。
- 参数条数：像素数 187、波长 125、像素间距 103、帧率 76、位深 60。
- 器件规格（`note` 为 device specification 的记录）：LCoS 像素间距 3.6–20 μm（8 μm 最多，其次 12.5 μm、9.2 μm），DMD 7.56–13.7 μm；LCoS 刷新率 50–714 Hz（60 Hz 最多），DMD 1031 Hz（8 bit 灰度）到 23,148 Hz（二值）；像素数 0.26–9.8 百万（1920 × 1080、1920 × 1200 最多）；位深 8 bit 或 10 bit。
- 实测波长 450–1617 nm，532 nm 最多（40 条），其次 1550、520、633 nm。

**F1**
- 论文：109 篇关键词候选 → 47 篇抽取、38 篇非 F1（其中 30 篇是器件级物理储备池，留给 I1）、22 篇综述 / 展望、2 篇重复。标题 / 摘要补查补了 10 篇（硅光储备池芯片、深度储备池、MZI–SOA 网格储备池、光子极限学习机等），全部抽取。有记录的论文共 57 篇。
- 记录：391 条（实测 293，仿真 95，预测 3）。
- 平台（记录数 / 论文数）：other 109 / 17、integrated 105 / 17、laser_feedback 94 / 13、fiber_loop 44 / 6、free_space 39 / 8（4 篇有两种平台）。
- 参数条数：任务指标 172、节点数 74、延时 55、波长 49、速率 41。
- 实测节点数 3–50,000（57 条）。时分复用的虚拟节点最多 29,088（Nat Commun 2022 13:7847，节点复用）；空间储备池 / 极限学习机的物理节点最多 50,000（PRX 2020 10:041037，相机像素）、16,384（Nat Mach Intell 2019 1:530，SLM 宏像素）和 15,625（LPR 2026 e72040，相机像素）。
- 实测延时：节点间隔、响应时间和片上延时线 16.7–284 ps（12 条）；ns 级 0.05–1022 ns（19 条，含 16.8、63.33、100 ns 一类的反馈环延时，最长的是 PRL 2025 134:017301 的 200 m 光纤环 1.022 μs）；μs 级 0.5–475 μs（5 条，含两条区间）；ms 级 2 条：Appeltant 2011 电子电路的节点时间常数 10 ms，Nat Commun 2023 14:4421 光流体记忆的弛豫时间 10–70 ms。
- 实测速率：5–60 Gbaud（6 条，含 1 条 GBaud）、0.01–17.6 GSa/s（7 条）、1–50 MSa/s；按吞吐量给的有 1.74 × 10^7、1.91 × 10^7、3.47 × 10^7 images/s 和约 10^6 words/s；另有 Nat Commun 2014 5:3541 扫描的输入比特率 0.125–12.5 Gbit/s。
- 实测任务指标（比较前要按任务分组）：NMSE 0.0001–0.561（31 条）、NRMSE 0.01–0.299（9 条）、SER 0–0.07（10 条）、WER 0–8.9%（7 条）、准确率 47.83%–100%（46 条）、BER 4 × 10^−7 – 0.06（5 条），另有 NRMSD、解密成功率各 1 条。
- 实测波长 400–2090 nm（47 条），1550 nm 附近最多。

**H1**
- 论文：196 篇关键词候选 → 50 篇抽取、94 篇非 H1（其中 76 篇是关键词误报）、49 篇综述 / 展望、3 篇重复；标题 / 摘要补查又补了 1 篇（Sci Adv 2020 6:aay5853 求解子集和的光子芯片）。有记录的论文共 51 篇。
- 记录：276 条（实测 228，仿真 39，预测 9）。
- 平台（记录数 / 论文数）：other 103 / 20、spatial_SLM 71 / 14、time_multiplexed_DOPO 55 / 9、integrated 47 / 9（1 篇有两种平台）。
- 参数条数：自旋数 93、连接方式 51、成功概率 51、求解时间 50、波长 31。
- 实测最大规模：
  - 空间光子伊辛机 262,144 自旋（Photonics Res 2026 14:4109，512 × 512）、75,076（PRL 2019 122:213902）；
  - DOPO 相干伊辛机 123,572 个脉冲、100,000 自旋（Sci Adv 2021 7:eabh0952）；
  - 光电振荡器类 102,400 自旋（LPR 2026 e71996，四通道并行）；
  - 片上 16,384 自旋（ACS Photonics 2024 11:1703，薄膜铌酸锂调制器）。
- 实测成功概率 0.2%–100%（40 条；口径不一，见第 24 节）。
- 实测求解时间：
  - 往返或每次迭代：
    - 片上 1.71 ns 到 370 μs（ACS Photonics 2024 11:1703 方案 II 的每次迭代）；
    - 腔往返 16 ns（自由空间腔）到 84 μs（16 km 光纤腔）；
    - SLM 类 0.01–0.085 s；
    - DAQ 反馈的光电振荡器 1 s。
  - 收敛、到达目标能量或 time-to-solution：150 ns（片上四自旋演化）到 22.0 ms（十万自旋 CIM 的 890 圈）。
  - Dammann 光栅 SPIM 的总收敛时间约 1200 s。
- 实测波长 520–1559 nm（31 条），1550 nm 和 532 nm 最多。

**I1**
- 论文：375 篇关键词候选（命中 ≥ 8 次的 379 篇去掉 4 个审稿意见文件）→ 228 篇抽取、64 篇非 I1、46 篇综述 / 展望、37 篇重复（截断文件名的副本）。另按标题补了 19 篇关键词命中不到 8 次的论文，全部抽取；10-30 晚的标题 / 摘要补查又补了 3 篇（第 26 节），也全部抽取。有记录的论文共 250 篇。
- 记录：1112 条（实测 1106，预测 6）。
- 材料（记录数 / 论文数）：2D 414 / 89、oxide 268 / 61、organic 225 / 48、perovskite 100 / 24、other 69 / 20、III_V 24 / 5、Si 12 / 4（1 篇有两种材料）。
- 参数条数：波长 260、阵列规模 131、保持时间 115、动态范围 111、每次事件能量 107、电导态数 95、PPF 95、耐久 92、响应度 56、非线性因子 50。
- 实测波长 213 nm – 4.6 μm（260 条：列举几个波长的 125 条、响应波段 42 条、单个波长 93 条）。单个刺激波长里 365 nm、405 nm 最多。到 2 μm 以上中红外的只有 5 篇（3.1–4.6 μm）。
- 实测响应度 56 条（只记 C1 没有记的）：
  - < 1 A/W 22 条，1–1000 A/W 19 条，≥ 1000 A/W 15 条；
  - 最高的是 LSA 2022 11:337 的 4.1 × 10^8 和 1.78 × 10^8 A/W，其次 Nat Commun 2018 9:2966 的约 1.2 × 10^7 A/W、Nat Commun 2023 14:2281 的接近 10^7 A/W；
  - 双极器件的负响应度：−0.40 A/W（ACS Photonics 2023 10:1575）、−0.10 A/W（AFM 2023 33:2303198）。
- 实测 PPF 31%–6594%（95 条，中位数 152%）：
  - 100%–200% 68 条，≥ 200% 18 条；小于 100% 的 9 条是按 (A2 − A1)/A1 给的；
  - 最大的 6594% 和 1531% 出自 NSR 2026 驻极体有机单晶（分别是 3 × 3 阵列和单个器件，光强、栅压不同）；> 1200% 出自 Adv Mater 2023 35:2304390（光子雪崩纳米晶的发光）。
- 实测电导态数 4–1024（95 条，中位数 16，16 个最多）：
  - 100 个以上的 14 条。最多的是 AFM 2025 35:2509119 的 1024 个（10 bit），其次 723（Adv Mater 2026 e74894）、599（Nat Commun 2018 9:5106）、512（Nat Commun 2026 17:4957）；
  - 按 N 位光脉冲序列数的可区分响应 22 条（多用于储备池），多为 4 位 → 16 个、5 位 → 32 个。
- 实测非线性因子 −0.5 到 3.45（50 条，中位数 1.28；定义不一，见第 24 节）。
- 实测保持时间 111 条，中位数约 2000 s：
  - ≥ 10^3 s 76 条，≥ 10^4 s 32 条；
  - ≥ 10^6 s 4 条：Adv Opt Mater 2023 12:2301652 的 8 × 10^6 s、Nat Commun 2025 16:4311 的 30 天，以及 Adv Mater 2025 37:2508889、Adv Mater 2026 38:e73861 的 > 10^6 s；
  - 外推的 4 条记 `predicted`：Nat Nanotechnol 2024 20:93 的 11.1 年，ACS Nano 2026 20:7670 的 3 × 10^7 s 和 78,000 s，Nat Commun 2026 17:4957 的 795 s（超出 100 s 监测窗口的线性拟合外推）。
- 实测每次事件能量 103 条绝对能量，另有 2 条按面积归一化：
  - 59 zJ（Nat Mater 2026 有机突触的光触发能量）到 4.13 mJ（Adv Photonics 2026 8:046001，一个近红外脉冲照到 1 mm × 1 mm 器件上的光能）；
  - 中位数约 0.62 pJ；≤ 1 fJ 的 26 条，≤ 1 pJ 的 53 条，> 1 nJ 的 17 条；
  - aJ 级和 1 fJ 以下的，大多是在很低的读电压（1 μV–1 mV）下按 I × V × t 算的电能。
- 实测动态范围：
  - ratio 88 条，中位数 10^5，10^6 以上 32 条。最高 10^9 有两条，都是电学开关比（AFM 2024 34:2400105 铁电 ReS2 晶体管、Nat Nanotechnol 2025 20:1633 氮化硼光子忆阻器的阻变比）；
  - dB 17 条，29–199 dB；
  - % 6 条。
- 实测耐久 3 – 10^11 次（92 条，中位数 550 次）：
  - < 100 次的重复性测试 21 条；
  - 10^6 次以上的 8 条都是电学开关循环（铁电、反铁电、阻变），最高的是 Nat Commun 2026 17:5367 反铁电 > 10^11 次；
  - 光脉冲循环最多约 3.5 × 10^5 次（Nat Commun 2026 17 无线数据聚合那篇，350,000 个异步光信号）。
- 实测阵列规模 4 – 327,680 个器件（131 条，121 篇）：
  - 9 个（3 × 3）最多（19 条），其次 25（5 × 5，15 条）、64（8 × 8，12 条）；
  - 1000 个以上的 11 条：Nat Commun 2025 16:4311 的 640 × 512 CMOS 集成有机焦平面阵列、Nat Photon 2023 17:629 的 18,000 个晶体管（2.5 × 5 cm2 玻璃基板）、64 × 64 两篇（ACS Photonics 2026 13:2645、Nat Electron 2026 9:630）、32 × 32 六篇、Nat Nanotechnol 2024 20:93 的 128 × 8。

**J**
- 论文：
  - 536 篇关键词候选（命中 ≥ 4 次的 539 篇去掉 3 个审稿意见文件）→ 334 篇抽取、98 篇非 J、93 篇综述 / 展望 / 评论（含 5 篇 News & Views）、11 篇重复（10 个截断文件名的副本，1 个录用稿副本）；
  - 另补的 2 篇：1 篇抽取，1 篇非 J；
  - 标题 / 摘要补查的 11 篇：10 篇抽取，1 篇非 J；
  - 有记录的论文共 345 篇。
- 记录：1587 条（实测 888，仿真 237，预测 462）。
- 平台（记录数 / 论文数）：other 418 / 85、MRR_WDM 283 / 49、MZI 178 / 41、diffractive_free_space 158 / 37、in_sensor 124 / 42、SLM_free_space 115 / 23、PCM 90 / 22、microwave 73 / 14、hybrid 63 / 20、spiking 44 / 11、reservoir 41 / 12（11 篇有两种平台）。
- 参数条数：准确率 559、能效 333、吞吐量 285、延时 139、计算密度 97、时钟 / 符号率 83、精度 56、矩阵规模 35。
- 预测值的比例因参数而异，比较前先按 `status` 筛：
  - 能效 333 条里预测 209 条，计算密度 97 条里 62 条，吞吐量 285 条里 141 条，延时 139 条里 42 条；
  - 准确率没有预测值（实测 332，仿真 227）。
- 实测吞吐量 143 条。按 OPS 给的 101 条（78 篇）：
  - 片上和光纤系统（MZI、MRR_WDM、PCM、储备池、微波、other 等）69 条，中位数约 0.8 TOPS。最高的是：
    - Nat Commun 2024 15:10841 的 211 TOPS（储备池，60 Gbaud）；
    - Nat Commun 2026 17:11107 的 120.8 TOPS（微环，128 / 64 Gbaud）；
    - Nat Commun 2026 17:9271 的 65.04 TOPS；
    - Nat Commun 2025 16:10332 的 64.4 TOPS（微波）。
  - 自由空间、衍射、传感内和光电混合系统 32 条，中位数约 28 TOPS。最高的几条都是按等效运算数算的：
    - Science 2025 390:1259（LightGen）的 3.57 × 10^4 TOPS；
    - Nature 2023 623:48（ACCEL）的约 4.55 × 10^3 TOPS；
    - Optica 2020 7:1812 的 4 POPS（按等效滑窗卷积运算数）；
    - LSA 2026 15 传感内光纤计算的约 2.61 POPS。
  - 光电混合的 Nature 2025 640:368 是 262 TOPS（2 GHz 时钟，有间歇错误）。
- 实测吞吐量的其他单位：
  - 按 MAC/s 给的 12 条：10 GMAC/s – 8.19 TMAC/s，另有 Optica 2021 8:1388 按等效 MAC 算的 1.3 PMAC/s；
  - FLOPS 6 条；
  - 每秒帧 / 图像 / 推理 / 样本 22 条，最高是 eLight 2025 5:29 的每秒 2500 万帧（40 μs 识别 1000 张图）；
  - Tb/s、Gb/s/MAC 各 1 条。
- 实测能效 122 条。按 OPS/W 或每次运算能量给的 72 条（54 篇），换算成 TOPS/W（1 pJ/OP = 1 TOPS/W）中位数约 2.4 TOPS/W，但跨了约 13 个数量级，主要是能量边界不同：
  - 最低的几条含全部台式仪器：Photonics Res 2025 13:B120 的 1.23 × 10^−3 GOPS/W，LSA 2025 14:245 的约 1.41 MOPS/W（整套装置 72.5 W），LPR 2025 19:2501417 的 0.65 μJ/OP；
  - 最高的几条只算光学运算的能量：
    - LSA 2026 15 传感内光纤计算的 8.7 × 10^18 OPs/J（"direct energy efficiency"；同文含 SLM、相机的系统能效是 3.29 TOPs/J 和 0.15 POPs/J）；
    - Nature 2023 623:48（ACCEL）的 7.48 × 10^4 TOPS/W；
  - 片上系统里最高的是 OEA 2026 9:250332 的 0.608 fJ/OP（能量边界未说明）和 LPR 2025 19:2401583 的 751.88 TOPS/W（只算片上器件）。
- 实测能效的其他单位：
  - 按 MAC 给的 20 条：10 aJ/MAC（Science 2022 378:270，时间积分接收所需的光能）到 1.1 × 10^7 fJ/MAC（Optica 2025 13:172，20 kHz 热调制）；
  - 每次推理 / 每帧 21 条：约 0.5 fJ（Nat Commun 2025 16:359，探测到的光能）到约 17.6 J（Adv Photonics 2026 8:046012，整套仪器）；
  - photons/MAC 5 条（每次乘法 0.013–3.1 个光子）、TFLOPS/W 2 条，pJ/b/MAC、fJ/bit 各 1 条。
- 实测计算密度 34 条。按 OPS 给的 26 条，中位数约 0.47 TOPS/mm2。面积口径不一（单元、芯片、封装），见 `condition`。最高的是：
  - Science 2025 390:1259 的 262 TOPS/mm2（按 136.5 mm2 封装面积）；
  - Optica 2022 9:792 的 118 TOPS/mm2（按 34 µm2 的单元面积）；
  - Nat Commun 2026 17:11107 的 48.05 TOPS/mm2（按 3.1 × 2.2 mm2 的芯片）。
- 实测延时 97 条（79 篇），0.11 ps – 15 s，中位数约 60 ns：
  - 10 ps 以下 3 条、10 ps – 1 ns 20 条，多是按芯片尺寸和有效折射率算的光传播时间，最短的是 Nat Commun 2025 16:10297 的 0.11 ps；
  - 1 ns – 1 μs 32 条，1 μs – 1 ms 18 条，1 ms – 1 s 20 条，后两段多由 SLM、相机或电子部分决定；
  - 1 s 以上 4 条，都受低速调制器或 CPU 软件限制：Sci Adv 2022 8:eabm2956 生成一个数字约 15 s，PhotoniX 2025 6:5 的 12.26 s 和 4.02 s，Sci Adv 2026 12:eaef7533 的 11.66 s。
- 实测精度 53 条（43 篇）：3–10 bits，中位数 6 bits；5 bits 最多（9 条），8 bits 有 6 条。
- 实测矩阵规模 31 条：
  - weights 30 条，2 – 405,000。最大的是 Sci Adv 2025 11:eadu0228（HITOP）用 7 × 7 通道时分复用跑的 405,000 个参数；
  - 一次实现的较大矩阵有 Nat Commun 2025 17:1250 的 4900 → 16、Photonics Res 2022 11:299 的 180 × 224、Sci Adv 2026 12:eaee9649 的 200 × 200、Nature 2025 640:368 每个张量核的 128 × 128；
  - neurons 1 条（Nature Sensors 2026 存内光计算的 5280 个存储神经元）。
- 实测时钟 / 符号率 76 条：
  - 符号率 44 条，12.5 kBd – 128 GBd，中位数约 19 GBd。最高的是 Nat Commun 2026 17:11107 的 128 Gbaud、Science 2026 392:eady5344 的 112 GBaud（5 km 光纤，受设备限制）、Nature 2025 648:576 的 106 GBaud；
  - 采样率 9 条，0.1–256 GS/s，最高的是 Nature 2024 627:80 的 256 GSa/s；
  - 时钟频率 23 条，100 Hz – 128 GHz（LSA 2026 15:348 的 128 GHz 是等效信号频率）。
- 准确率：实测 332 条（185 篇），仿真 227 条（137 篇），中位数都约 94%。按 `condition` 里的数据集名粗分：
  - MNIST 实测约 115 条（中位数约 94%）、仿真约 84 条；
  - Fashion-MNIST 实测 20 条（中位数约 89%）；
  - Iris 实测 22 条（中位数约 96%）；
  - CIFAR-10 实测 9 条（45.6%–94.8%）；
  - ImageNet 实测 2 条（59.5%、85.2%）；
  - 其余是手势 / 动作识别、心电 / 医学图像、语音、通信均衡等专用任务。比较时要按任务分组。

## 24. 已知问题（用的时候注意）

- PDF 转文字时有些符号丢了：µ 变成 "m"、"l" 或私用区字符（），λ 变成私用区字符或直接消失，π 变成 ，Ω 有时直接消失（"178.4 ."），"~" 有时变成 "B"（"B10 mW"），上标指数丢失（"10−4" 实为 10^−4，"105" 实为 10^5，"1.43×107" 实为 1.43 × 10^7，"2002" 实为 200²），小数点有时变成冒号或带空格（"0:75"、"0 . 75" 即 0.75）。`value_text` 照抄原文，正确的数值在 `value_num`，并在 `note` 说明。
- ACS Photonics 2018（ITO 加热器，A3）写的 "5s duration" 按原文记为 5 s；不能排除是丢了 µ 的 5 µs，已在 `note` 标出。
- A3：有的论文把晶化叫 "write"、非晶化叫 "erase"（或反过来），见第 4 节。
- E1：同一篇里实验用的网络和数值扩展设计常常参数不同，靠 `status`、`layer_type` 和 `condition` 区分，用的时候别混。
- E1：Taichi（Science 2024）CIFAR-10 的 76.68% / 93.65% 文中没说是否片上实测（用 ±5% 误差模型评估），记为 simulated。
- A1：`tuning_power` 里既有单个器件的（2π、偏置点、满量程），也有系统级合计（NSR 2026 光互连一条路由路径 1.789 W、LPR 2025 整个网络 290 mW），用 `condition` 区分，统计时要筛。
- A1：NC 2022 片上衍射网络（IDNN）写 "2π 平均 0.77 mW (2.2 mA)"，按 350 Ω 算 I²R 约 1.7 mW，与 0.77 mW 不符，按原文记并在 `note` 标出。
- A1：LSA 2024 微波光子处理器（SoC）对加热器的描述前后不一（掺杂硅 / 金属），材料记 not_stated；文中的 "around 2000 Ohms" 和 "<2.5 mA、<4.5 mW" 也对不上（2.5 mA 过 2000 Ω 约 12.5 mW），两条都照原文记，`note` 标出。
- A1：Nat Commun 2020 11:406（可编程微盘阵列）写 280 pm / 31.1 mW 得 24.6 pm/mW，实际约 9.0 pm/mW；Nat Commun 2020 11:4119（耦合 DOPO）正文 13.5 mW、SI 写 10.9 mW；LPR 2026 2502580 的 1.26 mW/π 和 ∼3 kHz 没说是本文实测还是代工厂 PDK 的值。都照原文记，`note` 标出。
- A1：同一器件在两篇论文里都报了的（Nat Commun 2017 8:636 和 LPR 2017 11:1700219 是同一块南安普顿芯片，110 ± 15 mW/π），以及同一篇里同一个量换单位记了两条的（Nat Commun 2026 17:11107 的 6.95 GHz/mW 和 0.056 nm/mW），`note` 写了 "count once"，统计时只算一次。
- A5：eLight 2025 异步光循环加速器把 3.6 nm 的 FSR 给了小环、8.14 nm 给了大环，与周长关系相反，按原文记，`note` 标出。
- A5：Nat Photon 2025 DTU 正文写环 "radii of 10 μm"，SI 一处写 "diameter of 10 μm"；实测 FSR ≈ 10 nm 与 10 µm 半径相符，记为半径，`note` 标出。
- A5：weight_precision 混有器件级（权重分辨率）和系统级（MVM 计算精度）的数值，`condition` 写明，统计时要筛。
- A2：有几条带宽不是本文重测的：NC 2025 百层网络（> 35 GHz，代工过程监测）、NP 2025 DTU（25–45 GHz，代工过程监测）、NC 2025 汉明距离处理器（56 GHz，器件规格）。`condition` / `note` 已写明，比较实测带宽时要筛掉。
- A2：`data_rate` 混有器件验证速率和系统运行速率（例如 PACE 加速器的 1 GHz 时钟、10 MHz 权重刷新），`condition` 写明。
- A2：Opto-Electron Adv 2026 磷烯调制器的器件结构文中描述不全（光纤锥 / 环辅助 MZI），材料记 other。
- A4：电平数的单位有 levels、states、bits 三种（"8 bits" 另记 256 个状态），统计时要统一。
- A4：保持时间有实测（小时、周）也有外推（"10 年"、"可超过 1 年"，记 `predicted`）。
- A6：保真度的定义和单位很杂（见第 10 节），比较前先按 `unit` 分组；`relative error %` 越小越好，与其他相反。
- A6：收了几种不是 MZI 网格的可编程结构（相干交叉阵列、相变材料耦合波导阵列、交错移相阵列、MEMS 耦合器网格、BTO / 相变材料非易失网格），用 `architecture` 和 `device` 区分。
- A6：可编程波导网格（NC 2024 通用可编程处理器的 28 个端口、LSA 2022 的 3 × 3 天线阵列 9 个端口）的 `mesh_size` 是接入端口数，不是 N × N 矩阵大小，`condition` 已写明。
- A6 / A1：有 15 篇 A6 / A2 论文顺带给了加热器的 Pπ 或调谐功率（共 21 条 A1 记录，脚本是 `g017`、`g021`、`g211`、`g231`、`g266`、`g359`、`g372`、`g430`、`g468`、`g510`、`g575`、`g576`、`g587`、`g610`、`g663`）。这些论文不在 A1 候选清单里。最后合并时这些记录已并入 A1 表；它们是 A2/A4/A6 的脚本写出的，所以完整的 A1 表要用 `run_all_PNN.py` 一起重跑（见第 25 节）。
- B1：微梳来源混杂：自己做的、合作者的、商用封装模块（Qaleido 等）、商用锁模光纤激光器或超连续谱切片，`material_text` 写明（开头写 commercial 的是买来的）。
- B1：同一篇常有几种配置（例如 LPR 2026 硅多用途芯片的 5 线 40 GHz、5 线 0.32 nm、32 线 2 GHz 电光梳），"产生的线数" 和 "实际使用的线数" 也都有，统计时按 `condition` 筛。
- B1：Nanophotonics 2025 频分复用储备池的 100 GHz FSR 出自建模部分（文中说与实验器件一致）；NC 2026 例外点信号广播的 100 GHz 是主腔设计 FSR，实际激发的是 4 孤子晶体。
- B1 / B2：ACS Photonics 2024 EA-MWL 的四个波长是光栅设计值（`predicted`）；实测平均间隔 0.70 nm，与设计的 0.8 nm（100 GHz）差 0.10 nm。
- B2：光泵浦纳米激光器（NC 2025 对称保护零模）的阈值是平均泵浦功率（μW），不是电流；LSA 2026 FAST-ONN 的 300 μA 是 "偏置在阈值附近" 的电流。
- B2：OEA 2024 VCSEL 储备池写 "threshold current of 2.16 mA52"，看起来引自文献 52，没有记。
- B2：属于该类但没有 B2 数值、登记为 `not_B2` 的有 Nanophotonics 2023 12:869、12:949（数值研究）、Optica 2024 11:1690（量子点 graded neuron，只给 10.2 GHz 重复率和 12 ps 脉宽）等，见 `B2_screening.csv`。
- G1：同一课题组在 ACS Photonics 2025 12:3364 写 DFB-SA "19.99 fJ per spike"，在 OEA 2023 6:230140 写 "19.99 pJ"，两条照原文记、`note` 互相标出，单位有一处可能是笔误。
- G1：每脉冲能量的口径不一：只算光能量的（FP-SA 7.329 fJ、纳米激光器 54 fJ）、激光器电功率 ÷ 发放率的（DFB-SA 7.7 pJ/OP）、含静态泵浦的（硅微环约 20 pJ）、整个神经元周期的（相变材料 1.5 nJ）。`condition` 写明，比较前要分组。
- G1：ACS Photonics 2025 13:433 graded-like 激光器的 0.42 pJ 和对照 DFB-SA 的 38.7 pJ 是按 "注入方波后输出功率的变化 × 脉宽" 算的（SI Note VII），只含储备池激光器。
- G1：发放率有直接测的自脉冲频率，也有由 "1 / 不应期" 推出的，`condition` 写明。
- A2：B1/B2/G1 这批里有 1 篇不在 A2 候选清单的论文给了自己的电吸收调制器数据（ACS Photonics 2024 EA-MWL：3-dB 带宽 > 20 GHz、静态消光比 > 16 dB、25 Gb/s 动态消光比 > 8 dB，4 条 A2 记录，脚本 `h008`），最后合并时已并入 A2 表；它们是 B1/B2/G1 的脚本写出的，所以完整的 A2 表要用 `run_all_PNN.py` 一起重跑（见第 25 节）。
- C1：有增益的光电晶体管 / 光电导器件（响应度到 10^3–10^8 A/W）和 p-i-n 光电二极管（Ge 0.4–1.1 A/W）不能直接比较，统计前按 `material` 和 `device` 分开；栅控 / 偏压可编程的双极器件给的响应度区间含负值。
- C1：带宽口径不一：Ge 光电二极管是 3-dB 带宽（GHz 级），二维、有机、石墨烯光电导器件多由时间响应或截止频率推出（Hz 到 MHz 级），`condition` 写明。
- C1：eLight 2025 异步光循环加速器的 0.9 A/W 出自功耗估算一句（"In our experiment, these parameters are … ηPD=0.9 A/W"），文中没写怎么测的，记 measured，`note` 标出。
- C1：Sci Adv 2025 NOMA 的暗电流有两条：暗电流密度 10 nA/cm2 和每像素约 10 fA（像素约 100 μm2），单位不同，统计时分开。
- D1：阈值的含义和单位都很杂（激活阈值、饱和强度、非线性起始功率；功率、能量、功率密度），比较前必须按 `unit` 分组，并看 `condition`。
- D1：`response_time` 里有两条单位是 GHz（带宽，`note` 已写明），统计响应时间时要筛掉。
- D1：Adv Photonics 2025 7:046003 的阈值写成 "∼14.12 W"，装置里没有放大器，可能是单位笔误；照原文记，`note` 标出，统计阈值时别用。
- D1：Photonics Res 2021 9:B71 的饱和强度 16.6 μW/mm2 是由 Rb 原子常数算出来的（predicted）；同一期 9:B128 的 ∼16 μW/mm2 只出现在功耗估算里，也记 predicted（实验拟合的饱和功率是 0.6 μW，见 `note`）。两条的 `value_num` 都已换算成 mW/cm2。
- D1：`function_shape` 记录最多（67 条），是文字，不能做数值统计；工作能量、激活损耗、偏置电压等装不下的数值也写在这里。
- D2：只有 18 篇。D2 没有增益、阈值、对比度这几个参数名，这类数值写在 `function_shape` 的文字里（见第 16 节）。
- D2：带宽的口径不一：激活单元本身的、受放大器或探测器限制的系统带宽（RF 光子处理器 43 MHz）、由脉冲展宽推出的（eLight 2025 波长中继单元约 90 MHz）、仿真里电滤波器的带宽（Photonics Res 12:85 OEO-ANN 12.5 GHz），`condition` 写明。
- D2：Photonics Res 12:85 OEO-ANN 是纯仿真；文中平衡探测器的 0.8 A/W 是假设值，没有记入 C1。
- C1 / D2 / I1：同一器件既是探测器又是激活单元的（Sci Adv 2025 NOMA、eLight 2025 波长中继单元、Sci Bull 71:486 VSe2/WSe2、Nat Photon 2019 13:454 飞法级光–电–光转换器），探测器指标记 C1，激活参数记 D2。I1 也没有记这些器件（这四篇不在 I1 候选清单里）。
- E2 / E1：做空间微分的衍射网络（LPR 2025 20:2502108 变焦边缘检测衍射网络、PhotoniX 2025 6:53 太赫兹衍射微分器）同时记在 E1 和 E2，合并统计时别重复算。
- E2：`bandwidth` 混有带宽宽度（单值）和工作波段（`range`）两种写法，照明光源的带宽也在里面，统计前按 `qualifier` 和 `condition` 分开。
- E2：`NA` 混有器件本身的工作 NA 和成像系统的 NA（例如 Sci Adv 2026 12:eaed8301 角点检测的 ~0.34 是系统 NA），还有按角度给的；单位 NA 和 deg 分开统计。
- E2：`efficiency` 的定义不一（透射率、交叉偏振转换效率、衍射效率、相对理想运算的峰值强度、仿真的平均透射率），`condition` 写明，比较前要分组。
- E2：`resolution` 有实测的、由 NA 推出的（`predicted`）和仿真的 PSF 大小；单位有 μm、lp/mm、fs、cy/mrad（Sci Adv 2024 10:eadk0024 长波红外边缘编码器，角空间频率，不换算）和 λ。
- E2：Science 2014 343:160 计算超材料是毫米波数值设计，λ0 = 3 mm 换算成 3 × 10^6 nm 记在 `wavelength`；PDF 文字里 λ0 显示为 "l0"。
- E2：Nat Commun 2019 10:3547 的片上超表面元系统在平板波导内做空间运算，收进 E2（`material_text` 写明）；其他片上波导卷积处理器都不收。
- E2：PRL 2022 128:193601 量子暗场显微的"本征空间微分"由两块交叉偏振片完成，没有微纳结构，平台记 other。
- E2：PRL 2018 121:173004 非局域超表面是微波 SRR 数值设计（f0 = 1.23 GHz），39° 和 56° 分别是二阶、一阶微分超表面的截止角（单位 deg）。
- E3：`pixel_count`、`pixel_pitch`、`frame_rate` 都混有器件规格和本文实际用法（使用区域、宏像素、系统运行速率）。统计器件规格时只取 `note` 含 "device specification" 的记录。
- E3：光计算系统的输入显示（把数据集图像编码成光的 SLM / DMD）记了，只给非光学处理器投测试目标的没记。NP 2025 19:486 光纤端面衍射网络在表征装置里用 SLM（LBTEK-2K-8）投输入图像，按这一条记了系统帧率（约 100 fps，受 SLM 限制）和波长。
- E3：Photonics Res 2025 14:B171 的 "8-μm pixel pitch" 原文说与 "the spatial light modulators' specifications" 一致，没说是哪台（装置里有 Hamamatsu X10468-07 和 Holoeye Pluto-2-NIR-011），`device` 记为 "spatial light modulators of the setup (unspecified)"。
- E3：Sci Adv 2023 9:eadg4391 的波长写成 "(1550 and 1568 nm, respectively)"，看不出哪个是空间模块（DMD）的，两个都记（`list`），`condition` 引了原文。
- E3：Sci Adv 2023 9:eadf8437 的 "It has a frame rate of up to 714 Hz" 紧跟在 Meadowlark P1920 那句之后，按 P1920 记，引文连前一句一起给出。
- E3：Sci Adv 2023 9:eadg6238 的像素间距由 "two pixels of SLM with 16 μm" 推出（8 μm），`note` 写明；Sci Adv 2024 10:eadn2031 的 36.8 μm、Sci Adv 2023 9:eadf8437 的 18.4 μm 是实际使用的像素大小，不是器件间距。
- E3：自发光显示（OLED、微显示）不是调制器，平台记 other，`material_text` 写 "emissive input display, not a modulator"；当透射掩模用的 LCD 面板记 transmissive_SLM。
- E3：二值相位编码有记 1 bit 的，也有记 2 levels 的（看原文写的是 "binary mode" 还是 "binary phase (0 and π)"），统计位深时这两种要合并看。
- F1 / H1 与其他类有重叠的论文：同一篇论文的不同器件分别记在各类，按论文合并统计时要去重。
  - F1 与 B2 重叠 10 篇（储备池激光器的阈值、波长等记在 B2），与 E3 重叠 8 篇（空间储备池 / 极限学习机用的 SLM / DMD），与 G1 4 篇（脉冲储备池），与 A5 3 篇（微环），与 B1、D1 各 2 篇，与 A1、A6、E1 各 1 篇；系统指标与 J 重叠 10 篇。
  - H1 与 E3 重叠 11 篇（空间伊辛机用的 SLM / DMD），与 C1 3 篇，与 A2、A6 各 2 篇，与 A1、B2 各 1 篇；与 J 5 篇。
- F1：`virtual_nodes` 混有时分复用的虚拟节点和物理节点（相机像素、SLM 宏像素、梳线、MMI 节点、输出端口、波长分量），`condition` 写明；比较虚拟节点数时要筛。
- F1：`delay` 混有反馈环延时、节点间隔、响应 / 记忆时间、片上延时线增量和片上总时延，`condition` 写明。两种特殊单位：Nat Commun 2011 2:468 的 θ = 0.2、τ = 80 以节点时间常数 T 为单位（实验电路 T = 10 ms）；Nanophotonics 2023 12:925 和 Nat Photon 2026 20:1062 的节点间延时是 0.5 个符号周期（`symbol periods`）。
- F1：`sampling_rate` 单位照原文，Gbaud 和 GBaud 两种写法都有，统计时合并。按单个样本处理时间给的三条（`s per image`、`μs per datapoint`、`ms per digit`）要取倒数才能和速率比较。
- F1：`task_metric` 必须按 `unit` 和任务分组比较。给成百分数的几条已换算：Nat Commun 2026 17:1225 的 "6% NRMSE"、"1% NRMSE" 记为 0.06 和 0.01，Sci Adv 2026 12:eaeb3077 的 "SER = 7 ± 2.3%" 记为 0.07（`note` 写明）。Nanophotonics 2020 9:4163 的误码率按原文记为 log(BER)（负数）。
- F1：几篇无反馈环、或更像 ELM 的系统因为论文自己称为储备池而收了：Nat Commun 2024 15:10841 NG-RC 硅芯片、Optica 2024 11:1690 量子点激光器、Nanophotonics 2025 14:2761 电信器件 ELM / RC、Nat Commun 2022 13:2651 时间 Floquet、Nanophotonics 2025 14:2723 多模光纤。
- F1：PRL 2012 108:244101（多延时波长动力学）的 PDF 文字里 "=" 显示为 "¼"、小数点显示为 ":"，"±" 和 "μ" 是控制字符；Optica 2015 2:438 也有控制字符。这些记录的 `value_text` 照抄原文，`value_num` 是改正后的数，`note` 写明。最大延时 "238" 按 μs 记。
- H1：76 篇关键词误报（"ising" 出现在 promising、rising 等词里）已逐篇核对后登记为 `not_H1`，理由写在 `H1_screening.csv`。
- H1：`success_probability` 的口径不一，`condition` 写明：
  - 每次运行找到基态的比例；
  - 跨实例的成功比例（PRL 2021 126:143901 是在 SK 图上统计的 success fraction）；
  - 落在能量最低的 5% 组态里的比例（PRL 2019 122:213902 的 87%）；
  - 满足全部子句的运行比例（Sci Adv 2026 12:eaeb7930 Kerr 孤子的 5%）；
  - 收敛到最优解的比例（Nature 2025 640:361 PACE 的 > 92.72%）；
  - 由次数换算的（Nat Commun 2019 10:3516 的 4 / 20、8 / 20，PRL 2023 131:063801 的 304 / 150,000）。
- H1：`solve_time` 混有每次迭代时间、腔往返时间、退火时间、到达目标能量的时间、time-to-solution 和器件响应时间，比较前按 `condition` 分组。
- H1：µ 丢失后变成 "m" 的已按物理关系改正，`note` 写明：
  - Science 2016 354:603 的 "5 ms" 往返时间记为 5 μs（5082 个脉冲 × 1 ns），"about 70 ms" 记为 70 μs（文中说比 SA 的 3.2 ms 快近 50 倍）；
  - Science 2016 354:614 的 "1.6 ms" 往返、"120 ms"、"200 ms" 记为 μs（该文图的坐标轴是 µs）；
  - Sci Adv 2021 7:eabh0952 的 µ 是私用区字符，5.43 和 785 记为 μs。
- H1：Nat Commun 2020 11:249（PRIS）的 63 ns 每步时间和 100 自旋是在 FPGA（电子）上测的，平台记 other；Nature 2025 645:354（AOC）的 20 万变量脑部扫描重建是数字孪生的结果，记 `simulated`。
- H1：`spin_count` 同一篇里常有几种：机器容量（腔内脉冲数）、实际解的问题规模、扫描最大规模、预测容量，统计 "最大规模" 时按 `condition` 和 `status` 筛。
- H1 / E3：空间光子伊辛机的 SLM / DMD 硬件参数记在 E3，伊辛机参数记在 H1（例如 Sci Adv 2023 9:eadg6238 波分复用 SPIM）。
- I1 与 C1 重叠 34 篇：同一器件的探测器指标（响应度、暗电流、带宽、NEP）记在 C1，I1 只记突触 / 传感内计算参数，这些论文的响应度不在 I1 里。I1 和其他类没有重叠，按论文合并统计时只需对 C1 去重。
- 其他类筛选时注明 "属于 I1" 的论文都在 I1 清单里（F1 30 篇、C1 43 篇、A4 131 篇、G1 58 篇、E2 6 篇、A2 2 篇、D2 2 篇、E3 1 篇，有重叠）。其中 5 篇核对后不收：
  - ACS Nano 2026 20:19458 触觉输入的发光晶体管；
  - Nat Commun 2024 15:1930 发光忆阻器；
  - Adv Opt Mater 2026 14:e71780 电致变色有机电化学晶体管；
  - Nat Commun 2026 17:4798 纳米线光电神经元（记在 D2）；
  - Optica 2026 13:822 衍射网络加事件相机（记在 E1 / E3）。
- I1：`PPF_index` 的定义不一，比较前先看 `note`：
  - 多数是 A2/A1 × 100%；
  - 小于 100% 的 9 条是 (A2 − A1)/A1 × 100%，其中 7 条文中写明，2 条由数值推断（`note` 写明）；
  - AFM 2025 35:2419651 把公式写成 PPF = 100% × I1/I2，照原文记；
  - LPR 2026 e71660 只给了电学 PPF 的定义，光学那条没说。
- I1：`dynamic_range` 单位有 ratio 88、dB 17、% 6 三种，要分开统计：
  - ratio 里混有光暗电流比、Gmax/Gmin、晶体管开关比和 HRS/LRS 阻变比，电学的 `condition` 写明；
  - 有一条比值小于 1：Adv Opt Mater 2021 9:2100654 反向光存储的 I365/Idark = 1.1 × 10^−7；
  - Sci Adv 2026 12:eaed9436 的 "10 pS to 8 μS" 是由两端点算出的比值（`note` 写明）；
  - dB 里多数是光探测的线性动态范围，也有存储动态范围；Nat Commun 2024 15:2471 的 180 dB 对应约 10^9 的电流开关比，最大的是 Nat Electron 2022 5:84 视觉适应器件的 199 dB；
  - % 的 6 条含义各不相同：THz 调制深度（Adv Sci 2026 e75145 的 37.9%）、透射率调制（ACS Photonics 2025 12:2637 的约 77%、Adv Opt Mater 2015 3:1400472 的约 40%）、电导增强（Nat Commun 2026 17:6521 的 1320%）、权重变化（Adv Mater 2018 31:e1806227 的 6000%；Adv Opt Mater 2026 e71891 的 −6.5% 记的是绝对值 6.5）。
- I1：`energy_per_event` 的算法不一，比较前按 `condition` 分组：
  - 电能 I × V × t，常在很低的读电压下算，所以有 zJ–aJ 级的值；
  - 入射光能，等于光功率密度 × 面积 × 脉宽，μJ–mJ 级；
  - 光电合计。
- I1：`energy_per_event` 的其他注意事项：
  - 2 条按面积归一化的不能和绝对能量比：AFM 2026 36:e76468 的 45 nJ/cm2；LSA 2026 15 β-Ga2O3 光突触的 3.31 × 10^−13 J/μm2，换算成 33,100 nJ/cm2，上标在 PDF 文字里丢了；
  - 同一句里的几个值换成了同一单位：ACS Nano 2022 16:19523 的 620 fJ 记为 0.62 pJ，Adv Mater 2026 e75098 的 7.5 fJ 记为 0.0075 pJ，InfoMat 2026 铁电视觉器件的 400 pJ 记为 0.4 nJ；
  - 2 条估算记 `predicted`：Adv Opt Mater 2022 10:2201104 按 100 μm2 面积估的 5.85 fJ，Adv Photonics 2026 8:046001 的约 3.3 nJ。
- I1：`retention` 里有 7 条（6 篇）是衰减或弛豫时间，不是 "状态保持了多久"，比较保持时间时要筛掉：
  - 拟合时间常数 τ：AFM 2021 32:2107925 的 73.0 s、ACS Photonics 2025 12:2637 的 287 s、AFM 2026 e78910 的 τ2 2.06–30.6 s；
  - InfoMat 2021 3:e12198 的 15.7 s / 27.9 s 也是拟合的 τ，论文自己称为 retention time；
  - 1/e 衰减时间：OEA 2022 5:210069 的 40 s 和 2 min；
  - 降到峰值 10% 的时间：Adv Opt Mater 2021 9:2002030 的 > 600 s。
- I1：`endurance` 混有光学循环和电学开关循环，`condition` 写明。10^6 次以上的 8 条都是电学循环。AFM 2026 36:e76960 按脉冲数计（"3000 pulses"，摘要写 "over 3000 cycles"）。
- I1：电学模式的记录（电脉冲编程的开关比、保持、耐久、电导态、能量、PPF）没有单独的标记列。较晚的脚本在 `condition` 开头写 "electrical: …"，较早的写成 "(electrical)"、"gate pulses"、"electrically programmed" 一类的描述。只要光学指标时，按 `condition` 筛（含 electric / gate pulse / voltage pulse 等字样）。
- I1：`conductance_states` 混有光编程和电编程的态数，以及按 N 位光脉冲序列数的可区分响应（22 条，多用于储备池），`condition` 写明。"N-bit" 记 2^N。
- I1：`nonlinearity_factor` 的定义和符号约定不一：拟合模型的 A、β、ν、αp / αd 等，例如 Adv Mater 2026 e75254 的 A_LTD = −0.5。另有一条是光电流幂指数 α：Nat Commun 2020 11:5934 的 1.52。只能在同一定义里比较。
- I1：`responsivity` 和 C1 一样，有增益的光电晶体管（10^3–10^8 A/W）和光电二极管型器件（< 1 A/W）不能直接比较；负值是双极器件的负光电导。
- I1：混合结构只有一个 `material` 标签，一般取论文强调的主体，多为沟道或光敏层。例如 PbS 量子点敏化的 IGZO 记 oxide，CsPbBr3 量子点光栅控的碳纳米管记 perovskite。全部组成写在 `material_text`，按材料比较时要看这一列。
- I1：9 篇只记了波长（文中没有其他可抽的 I1 数值，或探测器数值在 C1）：ACS Nano 2020 14:9796、ACS Nano 2025 19:30823、ACS Nano 2026 20:25816、AFM 2024 34:2409578、Adv Sci 2026 e77288、LPR 2026 e71637、NSR 2026 13:nwag029、Nat Commun 2023 14:1938、Nat Commun 2025 17:1250。其中：
  - AFM 2024 34:2409578 的 12 × 12 阵列是物理不可克隆（PUF）安全阵列，不是突触阵列，没有记；
  - ACS Nano 2026 20:25816 的 5 × 5 阵列是模拟的，没有记。
- I1：PDF 文字的问题（`value_text` 照抄或只去掉控制字符，正确数值在 `value_num`，`note` 写明）：
  - 上标指数丢失，144 条；
  - W−1 的负号、µ 是私用区字符；
  - × 号变成控制字符：InfoMat 2023 5:e12399、InfoMat 2023 6:e12493、InfoMat 2026 8:e70156，`value_text` 去掉了控制字符；
  - 引用编号粘在数值后面：Nat Commun 2022 13:1485 的 "> 20039" 是 > 200 加文献 39；
  - 句子被图注或换页隔开：AFM 2023 33:2303198、AFM 2024 34:2400039，引文是接续的那一段；
  - 单位跨行：Nat Commun 2017 8:14734 的 "A W-1"。
- I1：文中前后不一的，按 `note` 说明记：
  - AFM 2024 34:2401534：摘要和 SI 写 18.51 fJ，正文结论写 18.56 fJ，记 18.51 fJ；
  - AFM 2025 36:2514177：红光波长 SI 图注写 755 nm，正文写 785 nm，记 785 nm；
  - Adv Opt Mater 2022 10:2201104：保持时间结果部分引 > 4000 s，摘要和结论写 > 4500 s，记 > 4500 s；
  - LPR 2026 20:e71384：PPF 正文写 172.99%，SI 表 S2 写 196%，记 172.99%。
- J：只看自己的 549 篇清单（536 篇关键词候选、补的 2 篇、标题 / 摘要补查的 11 篇）。不在清单里的论文，文中的系统级数值没有记：
  - I1 的 250 篇里只有 38 篇在 J 清单里（36 篇抽取，其中 33 篇记了准确率），其余 212 篇的识别准确率两边都没有记（I1 按分工不记准确率）；
  - E2 的 100 篇里只有 12 篇在 J 清单里，11 篇登记为不属于 J，1 篇（Nature 2026 654:917）抽取；
  - 需要这些论文的系统数值时，要回原文。
- J 与其他类的分工：同一篇论文的器件参数在 A–I 各类，系统指标在 J。
  - J 有记录的 345 篇里，278 篇在其他类也有记录，67 篇只在 J。
  - 按第 22 节的分工，E1、F1 已抽的论文，准确率和矩阵规模只在 E1 / F1；H1 已抽的，矩阵规模和伊辛机求解时间只在 H1；A6 已抽的，矩阵规模只在 A6；A5 已抽的，矩阵规模和精度只在 A5。
  - 其他类已记同一含义的数值，J 不再记：A2 系统符号率、E3 帧率、F1 采样率、G1 每次发放能量、I1 每次事件能量、D1 响应时间。
  - 所以按论文汇总系统指标时，要把 J 和这几类合起来看。
- J：不同单位族之间不能直接比较：
  - 按比特算的 Tb/s、Gb/s/MAC、fJ/bit、pJ/b/MAC、Gb/s/mm2（光逻辑、比特归一）；
  - 每次推理 / 每帧、每像素的能量；
  - photons/MAC；
  - MAC 和 OPS：只有论文写明 1 MAC = 2 OPs 的才能换算，见 `condition`。
- J：自由空间、衍射和光电混合系统的 OPS 多按光传播的等效运算数（每层 N² 个连接 × 帧率）算，不能和片上张量核按调制速率算的 OPS 直接比。
- J：同一篇常给几种口径，比较时按 `condition` 区分。例如 Science 2025 390:1259（LightGen）：
  - "conservative calculation" 的系统算力 3.57 × 10^4 TOPS（262 TOPS/mm2、664 TOPS/W）；
  - 串行端到端实验速度 2.49 × 10^2 TOPS（480 Hz 输入）；
  - 两者都记 `measured`，差两个数量级；理论值 5.69 × 10^9 TOPS 记 `predicted`。
- J：能效的能量边界差别很大，比较前按 `condition` 分组：只算光学（探测光能、激光功率），只算片上器件，含驱动电子，含全部台式仪器。同一篇常同时给几种，例如 LSA 2026 15 传感内光纤计算的 "direct energy efficiency" 8.7 × 10^18 OPs/J 和系统能效 3.29 TOPs/J。
- J：`status` 的分界（第 22 节）比原文的说法严。论文说 "experimentally achieve"、"in our experiment" 的数值，凡是用了假设速率、文献元件功耗、器件上限或全芯片峰值的，都记 `predicted`，`note` 写明。例如：
  - Nat Commun 2026 17:11107 的约 26.7 TOPS/W、LPR 2025 19:2402016 的 13.9 pJ/MAC：能量预算里的 DAC / ADC / TIA 是文献值（后者只算光学的 8.95 pJ/MAC 仍记 `measured`）；
  - Optica 2026 13:457、OEA 2026 9:250319、LPR 2025 19:2500864：都是按 5 GHz 的 DFB-SA 最大自脉冲频率算的（2.5 TOPS、1.39 TOPS/W、987.65 GOPS/W 等）；
  - LPR 2024 18:2400565（薄膜铌酸锂 ZEN-1）的 0.64 TOPS、30 TOPS/W：按约 20 GHz 电光带宽（20 GSa/s）算，演示用的 AWG 低于 5 GHz；
  - LPR 2022 16:2100732 的 54.7 TOPS、13.69 TOPs/J：按相机上限 21.7 kHz 算；
  - Sci Adv 2022 8:eabm2956 的 0.0046 TOPS/W：原文说 "in our experiment"，但用了假设的 10 GHz 速率和元件；
  - Sci Adv 2026 12:eaef7533 的 1694 fps：按 10 MHz EOM 估算，实验用 500 Hz VOA，每张图 11.66 s；
  - NSR 2026 13:nwag350 的 15.36 TOPS 是 192 维全芯片最大值，实验用 49 维（3.92 TOPS，另记 `measured`）；Nat Commun 2026 17:9920 的 1.92 TOPS 是 16 通道并行的峰值，文中芯片的计算速度是 120 GOPS；
  - Adv Photonics 2025 7:016007（微梳求解偏微分方程）：17.92 ps 的组成没有写清楚，记 `predicted`；实验系统约 16 ms 一次 MVM，记 `measured`；
  - eLight 2026 6:10 的 1,968 fps：文中没有依据，SI 写 SLM 和相机每帧各 16.7 ms，记 `predicted`。
- J：能耗等数值的推导在 SI、而可用的文字版没有那一节的，照论文的说法记，共 15 篇 22 条 `measured`（`note` 写 "basis could not be checked" 或 "not in the available text"）。例如：
  - Optica 2022 10:162 的约 5.16 pJ/MAC、Optica 2023 10:1709 的 4.48 fJ/OP；
  - Sci Adv 2025 11:eads7475 的 1.47 TOPS/W、PhotoniX 2025 6:45 的约 7 TOPS/W；
  - OEA 2026 9:250332 的 0.608 fJ/OP（表 2 的基准，文中没有推导，也没说哪几层在 RAMZI 上）；
  - ACS Photonics 2024 SOA + APD 网络的 8 GFLOPS 和约 81.1 pJ/OP。
  当作 "实测" 用之前最好回原文核对。
- J：同一组的三篇 DFB-SA 脉冲神经网络芯片论文（Optica 2026 13:457、OEA 2026 9:250319、LPR 2025 19:2500864）给出相同的基准数值，按论文合并统计时不要当成三个独立结果。
- J：准确率的 `measured` 只表示用了实验硬件。不少论文的输入编码、部分层或读出层在电子端，`condition` 写明哪些层在光学硬件上。仿真值多是用实测器件曲线或噪声模型仿真的网络。
- J：文中前后不一的，按 `note` 说明记：
  - LSA 2026 15:348：按 128 GHz × 190 ÷ 32.59 W 照写记 0.75 TOPS/W，正文表 1 写约 0.76 TOPS/W；
  - Optica 2025 12:1079：计算密度在摘要和引言写 5.84 TOPS/mm2，分析部分写 5.48 TOPS/mm2，记分析值 5.48；
  - Optica 2026 13:1423：9.3 TOPS/W、3.66 TOPS/mm2 由实验的 2.8 MFLOPS 和约 29.96 W 推不出来，依据在缺失的 SI 里，记 `predicted`；
  - Nat Commun 2025 16:10382（百层光子深度学习）：正文 85.2%，SI 表 S1 写 85.4%，记 85.2%；
  - Nat Commun 2025 16:10332：延时正文 53.3 ns，SI 写 55.53 ns（含 2.33 ns 空气传播）；能效正文 0.26 TOPS/W，表 S6 写 0.25 TOPs/W；
  - Sci Adv 2024 10:eado3937：正文 95.2%，SI 写实验和仿真都是 95.3%；
  - eLight 2025 5:29：正文把 77.3 TOPS / 9.50 × 10^2 TOPS/W 配给 2 类、21.1 TOPS / 2.59 × 10^2 TOPS/W 配给 10 类，SI 的推导正好相反，按 SI 的推导记；
  - Adv Sci 2026 e78340：CIFAR-10 正文写完整混合流程 86.6%，图 5 图注写混合流程 85.7%、纯数字网络 86.6%，记正文值并在 `note` 标出；
  - Optica 2024 11:583：结论说 "can achieve" 5.485 pJ/MAC，表 2 把 5.485 列在功耗下、效率列 4.21 pJ，记 `predicted` 的 5.485 pJ/MAC；
  - Adv Sci 2026 13:2515689：每个微环 2.725 TOPS，正文说可实现，SI 说只是理论上限，记 `predicted`；
  - NML 2025 17:261：正文 0.34 pJ，摘要和亮点写 "< 0.34 pJ"；
  - LPR 2023 17:2300001：句子写 "2 × 2 nonnegative-valued"，实际网络是 2 × 2 实数矩阵，按网络记；
  - Optica 2025 12:1252：1 Tbit/s 是 "currently" 的逻辑容量（10 波长 × 4 空间通道 × 25 Gbit/s），文中没说 40 个通道同时工作过；
  - Nat Commun 2026 17（MXene Kerr 全光逻辑单元）：可微逻辑门网络的 MNIST 97.7%、CIFAR-10 50.7%，文中没说网络在硬件上跑过（只演示了逻辑门），记 `simulated`；
  - Sci Adv 2026 12:eaed9436：正文没写有多少张测试图在 Fe-FET 硬件上跑过；
  - ACS Photonics 2024 SOA + APD 网络：硬件推理准确率写 "more than 90%"，图 4 只给了单个样本的实验信号。
- J：PDF 文字的问题（`value_text` 照抄，正确数值在 `value_num`，`note` 写明）：
  - 上标指数丢失 56 条（26 篇），例如 "3.57 × 104 TOPS" 实为 3.57 × 10^4；
  - µ 变成私用区字符或双写的数学符号，照抄；
  - 句子被图注或换页隔开 12 条（9 篇），引文是接续的那一段；
  - Nat Commun 2025 16:10382 的 "856.85 271" 里 271 是 SI 的行号。
- J：单位照原文、需要换算才能比较的：mW/TOPS、W/TOPS 一类已换成 TOPS/W；pJ/OPS、fJ/OPS 一类的写法按每次运算能量记成 pJ/OP、fJ/OP；Sci Adv 2022 8:eabm2956 的 4 KOPS 记为 0.004 MOPS；Optica 2025 12:1252 的 0.32 pJ 每比特记为 320 fJ/bit。
- 全部类：`section` 列是按规范化全文里的章节标题自动推的（SI 前面加 "SI "），PDF 转文字后标题丢失或错位时会不准，引用位置以 `src`、`page`、`char_offset` 为准。
- I1：Nat Commun 2026 17（全光控忆阻储备池 AOCM）的每脉冲能量是做 J 时发现漏记的，最后合并时补进了 I1（`n390.py`）：405 / 650 nm 光脉冲约 80 / 800 nJ 记一条 `list`，电学操作约 2 pJ 记一条；文中的推导在 SI Note 4，可用的文字版里没有。

## 25. 自己核对、重跑

数据不含论文全文和核对脚本。需要复核某条记录时，按 `page` 和 DOI 查原文。

## 26. 独立抽查和补查（2026-10-30）

**做法**：请没参与抽取的 agent 对照全文和本 README 逐条判。判定分三种：correct、wrong（数值、单位、状态、标签、器件 / 材料描述、条件、参数含义，或是不是本文自己的结果，任一项错）、disputed（原文本身两种读法都说得通）。每条判定都附原文证据，证据文字都由程序核对过，能在规范化全文的对应位置原样找到。核对 agent 只读不改；每条报出的问题由下载 agent 回原文核对后改脚本（从不直接改表），再全部重跑。判定、证据、报告和改动清单在 `check\` 子文件夹。

**第一轮**（4 个 agent，每类随机抽 20 条，19 类共 380 条；抽样种子 = SHA-256(发布版 README 的 SHA-256 + 一次性盐值) 的前 8 位，盐值由核对 agent 自己生成）。结果（correct / wrong / disputed）：

| 类 | 结果 | 类 | 结果 | 类 | 结果 | 类 | 结果 |
|---|---|---|---|---|---|---|---|
| A1 | 18 / 2 / 0 | A6 | 17 / 2 / 1 | D1 | 15 / 4 / 1 | F1 | 19 / 1 / 0 |
| A2 | 19 / 1 / 0 | B1 | 19 / 0 / 1 | D2 | 17 / 3 / 0 | G1 | 19 / 1 / 0 |
| A3 | 19 / 1 / 0 | B2 | 18 / 1 / 1 | E1 | 19 / 1 / 0 | H1 | 20 / 0 / 0 |
| A4 | 18 / 2 / 0 | C1 | 18 / 2 / 0 | E2 | 20 / 0 / 0 | I1 | 18 / 0 / 2 |
| A5 | 19 / 0 / 1 |  |  | E3 | 20 / 0 / 0 | J | 19 / 0 / 1 |

合计 wrong 21 条（5.5%），disputed 7 条。数值抄错、单位换算错、上标解析错的一条都没有，错误都在含义一层：
- 状态：用假设、仿真或设计参数算出的值标成 measured（TCAD 电容算的能量、假设热阻算的 Pπ、仿真图里的设计例子、摘要里实验和仿真混说的一句）；
- 参数含义：设定电平当对比度，易失模式的速度记在非易失器件下，损耗的增量记成总插损，输入能量当阈值，系统延时记成激活函数形状；
- 描述：material_text 写成同一篇里另一个器件或芯片的；加热器材料原文其实写了，却记 not_stated；
- 标签：色心记成量子点；Rb 饱和吸收两篇用了两种机理标签；
- 写法：列举几个值没用 `list`；A6 的 `architecture`、`calibration` 里混进了短语里的第一个数字（文献编号、下标）。

按"每类 20 条最多错 1 条"，A1、A4、A6、C1、D1、D2 六类没通过。

**第二轮**：
- A1、A4、A6、C1 各重抽 20 条（不含第一轮抽过的）：A1 16 / 3 / 1，又没通过；A4 19 / 1 / 0、A6 19 / 1 / 0、C1 19 / 1 / 0，通过。
- D1（187 条）、D2（59 条）逐条复核：D1 154 / 30 / 3，D2 52 / 6 / 1。D1 的错误主要是：文献或商用器件的规格当本文实测（EDFA、SOA）；同一篇几个器件的描述配错；阈值的含义（输入能量、驱动强度）和状态（只在功耗估算里出现的记成实测）；漏记的响应时间和增益。
- A1 两次没通过，全部 225 条逐条复核：208 / 12 / 5。错误主要是：Methods 里写明的加热器材料记成 not_stated；偏置 MZI 各输出口的开关功率当成 Pπ；device、material_text 写成同一篇里另一个器件的。

**怎么改的**：报出的错误逐条核对原文后改脚本，再按错误类型把全表筛了一遍。主要的：
- 加热器材料：原记 not_stated 的论文里有 14 篇原文写了材料，已改；反过来，有 2 篇只给同一篇里的另一个器件（测试结构、补偿阵列）写了材料，被借用的那几条改为 not_stated；
- 用假设、仿真或估算参数算出的值改为 `predicted`，仿真图里的值改为 `simulated`；只在功耗估算里出现的（A1 两条、D1 一条等）也改为 `predicted`；
- 删掉不该有的记录：引自文献或商用器件规格、重复记的、不是该参数含义的（各自原因见改动清单）；I1 一条保持时间拆成实测（监测窗口内）和外推两条；
- 整篇移出：C1 一篇（纯 DFT + NEGF 计算）、D1 三篇（PPLN 没有本文表征；液晶 Kerr 单元对输入是线性的；光电子发射显微读出、没有光输出）、A6 一篇（SI 写明 16 × 16 MZI 阵列是数值仿真）；
- 列举值统一用 `list`（约 90 条）；"0 到 X" 的扫描范围记 `max`；`>=`、`<=` 改为 `≥`、`≤`；文字型参数（A6 `architecture`、`calibration`，D1 / D2 `function_shape` 等）的 `value_num` 一律留空；
- 核对 agent 指出的漏记数值，核对原文后补了（A1 22 条，D1、D2 若干条），每条都带引文；
- 原文前后不一、改不了的，照原文记并在 `note` 标出（例如 LSA 2024 13:14 的 ~2000 Ω 与 <4.5 mW 对不上，Nat Commun 2020 11:406 的 24.6 pm/mW 与 280 pm / 31.1 mW 对不上，Nat Commun 2020 11:4119 正文 13.5 mW、SI 10.9 mW）。

全部改动（含每条涉及的脚本）见 `check\PNN_params_check_fixes.md`。

**标题 / 摘要补查**：候选清单是按全文的关键词计数选的（第 2 节），用词不同的论文会漏掉（例如 "photonic reservoir"、"extreme learning machine"、"metasurface … edge-enhanced imaging"）。逐篇看了所有类都没筛过的论文的标题和摘要，补了 59 篇，加在各清单末尾（`candidate` 列为 `no (extra)`，关键词计数记 0），其中 54 篇有记录：
- E1 12 篇；E2 16 篇（另 3 篇不属于 E2：偏振逻辑、射频电路、声学时域）；F1 10 篇（光子储备池、极限学习机）；H1 1 篇；I1 3 篇；J 10 篇（另 1 篇不属于 J）；D1 2 篇（另 2 篇不属于 D1）；C1、D2 1 篇（Nat Photon 2019 13:454）；A2、A4 各 1 篇核对后不收。
- 其余没筛过的 77 个文件（社论、新闻评论、综述、没有器件数值的理论、非光子系统、库里只有 SI 的）和原因列在 `check\PNN_unscreened_2026-10-30.md`。

**改完以后**：十九类合计 10087 条、1133 篇（发布版 9870 条、1090 篇）。各类记录数（篇数）：

| 类 | 发布版 | 现在 | 类 | 发布版 | 现在 | 类 | 发布版 | 现在 |
|---|---|---|---|---|---|---|---|---|
| A3 | 1637（87） | 1636（87） | B1 | 111（31） | 111（31） | E2 | 462（84） | 509（100） |
| E1 | 1802（191） | 1875（203） | B2 | 102（39） | 102（39） | E3 | 551（116） | 551（116） |
| A1 | 224（102） | 247（102） | G1 | 77（33） | 76（33） | F1 | 346（47） | 391（57） |
| A5 | 468（120） | 467（120） | C1 | 182（62） | 181（62） | H1 | 274（50） | 276（51） |
| A2 | 202（52） | 203（52） | D1 | 190（56） | 192（55） | I1 | 1104（247） | 1112（250） |
| A4 | 109（18） | 108（18） | D2 | 60（17） | 65（18） | J | 1565（335） | 1587（345） |
| A6 | 404（77） | 398（76） |  |  |  |  |  |  |

`verify_params.py` 19 类全部 0 条有问题；`run_all_PNN.py`（3265 个脚本）、`run_all_A3.py`（89 个）、`run_all_E1.py`（226 个）从头重跑，0 个失败，这里的表就是那次重跑的结果。第 23 节的数量都按现在的表重算过。
