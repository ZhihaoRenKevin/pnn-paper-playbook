# 派生表（device parameter atlas 等）说明

写入：下载 agent，2026-10-30。这些表全部由 `build_derived.py` 从 `PNN_params` 的 19 张记录表算出，不含任何手填的数。同样的输入每次生成逐字节相同的文件；`derived_manifest.json` 记了程序、每个输入和每个输出的 SHA-256。

```
python build_derived.py <PNN_params 文件夹> <00_Index\library_manifest.json> <输出文件夹>
```

## 1. 文件

| 文件 | 内容 |
|---|---|
| `device_parameter_atlas.csv` / `.md` | 类别 × 标签 × 参数：记录数、篇数（实测 / 仿真 / 预测分开）、实测的最小值 / 中位数 / 最大值、每种状态的最好值（带 record_id、原文写法、年份、tier、condition）、实测篇数按年份和 tier 分布。标签 `*` 行是整类合计；`.md` 只列有实测数据的行 |
| `materials_atlas.csv` / `.md` | 同样的统计按材料族重排；`papers_via_label` 是靠类别标签归入的篇数，其余是靠 material_text 里出现的材料名归入的 |
| `materials_assignment.csv` | 每条记录归入了哪个材料族、靠标签还是靠文字、匹配到的是哪几个字 |
| `device_coverage.csv` / `.md` | 每类每个标签有几篇论文、几篇有实测、几篇只有仿真或预测，按 tier 和年份分布，有实测数据的参数有哪些 |
| `benchmark_ledger.csv` / `.md` | J 类准确率按任务和平台分组：篇数（实测 / 仿真）、实测中位数、实测最好值（带 record_id、条件）、按年份和 tier 的篇数 |
| `benchmark_task_assignment.csv` | 每条 J 准确率记录被分到哪个任务、依据是 condition 里的哪几个字 |
| `PNN_atlas_spec.json` | 下面第 2 节的全部规则：单位组和换算系数、每个参数"越大越好 / 越小越好 / 不比较"、材料族规则、任务规则 |
| `derived_manifest.json` | SHA-256 和计数 |

## 2. 规则（与 `build_derived.py` 文档字符串、`PNN_atlas_spec.json` 一致）

1. 表里每个数要么来自一条记录（旁边给 record_id），要么是记录的计数 / 中位数。
2. 单位只在同一单位组内换算（例如 fs、ps、ns、μs、ms、s 都换成 μs；aJ/OP、fJ/OP、pJ/OP 换算成 TOPS/W）；不在任何组里的单位单独成行，不比较。µ（U+00B5）和 μ（U+03BC）视为同一个字符。
3. 每条记录只出一个值：区间或列举取对该参数更好的一端（越大越好取上端；越小越好取大于 0 的最小端，dBm 除外）；不比较的参数取 `value_num`；A6、E2 的 `bandwidth` 写成波长区间（两端都 ≥ 200 nm）时是工作波段，取宽度。
4. 最好值：同一状态里最大（或最小）的一条，并列按 record_id。方向不对的界不参加（越大越好时的 `<`、`≤`，越小越好时的 `>`、`≥`），越小越好时 0 和负值不参加（dBm 除外）。混了不同任务的参数（E1 准确率、F1 任务指标、J 准确率）不给最好值，J 准确率在台账里按任务分开比较。
5. `best_measured_calc` = yes：最好值那条记录的 condition 或 note 写了是算出来 / 估算的。按各类的规则它仍然算实测（例如 J 用实验自己的时钟 × 运算数算出的吞吐量），引用前要看 condition。
6. 中位数、范围只用实测记录；仿真、预测的单独计数、单独给最好值，从不和实测混在一起。
7. 年份取文件名里期刊名后面的两位数；tier 取论文所在的库文件夹（01–04 → T1–T4）。
8. 材料族：靠类别标签（例如 A3 的 `material`、A5 的 `platform`），或靠 material_text 里出现的材料名（化学式区分大小写）。A3 只按标签归（它的标签就是相变材料本身）；Si、SiO2 等在 C1、D1、I1 里多半只是衬底，不按文字归。一条记录可以属于几个材料族；靠文字归入的，那个材料可能是器件的另一部分（例如 MZI 网格里的 Ge 探测器），引用时要看 material_text。
9. 台账任务：按 condition（再按 value_text）里出现的第一个任务规则归类；condition 写 "same …" 而没有任务名的，沿用同一篇上一条准确率记录的任务；其余记为 unspecified。

## 3. 用的时候注意

- 篇数少不等于没人做过：这只是本库（截至下载日）里的情况；出 idea 之前要联网查新。
- "最好值"是本库记录里的极值，不是公认的纪录；不同论文的测量条件（偏置、波长、器件尺寸、能量边界）不同，比较前读 condition 和原文。
- 数值的出处和含义以 `<代号>_records.jsonl` 为准；派生表只做汇总。每个引用的数都要能回到一条 record_id。
- 库里没有的维度：论文的"功能"标签、代码 / 数据可用性、加工路线（v3.5 再做）。
