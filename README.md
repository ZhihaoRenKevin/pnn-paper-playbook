# pnn-paper-playbook

An agent skill for photonic neural network (PNN) and optical computing research. It helps an AI agent that reads `SKILL.md` skills (Claude Code and the Claude app, Codex, Gemini CLI, Antigravity, GitHub Copilot, Cursor and others) plan, write, benchmark and revise PNN papers. It works from measured device and system parameters taken from 1,133 published papers.

The source library holds 1,475 papers from 1989 to 2026 (46 *Nature* / *Science*, 126 *Nature* sub-journal, 280 *Nature Communications* / *Science Advances* and 1,023 other high-impact journal papers). It was assembled in October and November 2026.

## What is inside

| Path | Contents |
|---|---|
| `SKILL.md` | The playbook. It covers claim classes and journal tiers, titles, abstracts, figures, metrics and energy-boundary rules, and reviewer concerns with response tactics. It also covers choosing materials, positioning novelty, grants and talks, and generating ideas. |
| `references/PNN_params/` | 10,087 parameter records in 19 device and system classes, from `A1` thermo-optic phase shifters to `J` system-level metrics. Each record gives the value as reported, its number and unit, and its status (8,153 measured, 1,372 simulated, 562 predicted). It also gives the material, device, condition, page and section. `README_PNN_params.md` defines every class and field (in Chinese). |
| `references/derived/` | Tables computed from the records by fixed rules: a device parameter atlas, a materials atlas, coverage counts and a benchmark accuracy ledger. |
| `references/citations.csv` | DOI, journal, year, volume, article number, title and authors for all 1,475 papers. |
| `references/library_index.csv` | Tier, platform, materials, functions and headline value for each paper. |
| `references/metrics_sota.md`, `Metrics_SOTA_table.xlsx` | SOTA ledgers for 11 platforms × 7 metrics, with measured and projected values kept apart. |
| other `references/*.md` | Reviewer playbook (concern codes C1–C14 from 2,241 referee comments), global groups directory, house styles of leading groups, figure archetypes, checklists, physics and training notes, writing templates. |
| `scripts/pnn_research_toolkit.py` | 13 sub-commands; needs only Python 3.8 or later and its standard library. |

The 13 sub-commands are `lit-search`, `related-work`, `sota-table`, `energy-latency-audit`, `referee-simulator`, `reviewer-finder`, `figure-blueprint`, `draft-linter`, `atlas`, `materials`, `coverage`, `benchmark` and `idea-gen`.

<!-- v3.5-companion-skills-readme begin -->

## Dedicated T1/T2 How-to-Write & How-to-Revise Companion Skills (`skills/`, v3.5.0)

Version `3.5.0` separates **factual literature/parameter lookup (all tiers T1-T4, 1,475 papers, root skill)** from **manuscript writing, figure, and rebuttal craft (strictly T1 & T2 research articles, `n = 113`, zero T3/T4 or review dilution, with `2.0x` native-English-country `US/GB/CA/AU` weighting on all writing skills)**. Every companion skill provides step-by-step drafting recipes, 4-pass revision workflows, original Before -> After examples, and a zero-dependency Python CLI, while distributing **no verbatim text from published papers or peer-review files**.

| Companion Skill (`skills/<name>/`) | Actionable Scope | Standalone CLI |
| :--- | :--- | :--- |
| `pnn-t1t2-editorial-audit` | Pre-drafting tier-fit, story elevation & 16-point pre-submission audit | `pnn_editorial_audit_tool.py` |
| `pnn-t1t2-abstract` | Colon-free title + 7-sentence T1/T2 abstract drafting & revision | `pnn_abstract_tool.py` |
| `pnn-t1t2-introduction` | 4-paragraph funnel drafting, diplomatic prior-art critique & revision | `pnn_intro_tool.py` |
| `pnn-t1t2-results` | Claim-first Results subheadings, operator mapping & ablation narration | `pnn_results_tool.py` |
| `pnn-t1t2-figure-color` | Empirical CIELAB `#HEX` palettes (520 pages) & Machado CVD checker | `pnn_color_tool.py` |
| `pnn-t1t2-figure-caption` | *Nature* (`Fig. 1 |` `a,`) vs *Science* (`Fig. 1.` `(A)`) caption linter | `pnn_caption_tool.py` |
| `pnn-t1t2-figure-arrangement` | Fig. 1-5 storyboarding, panel ceilings, hero layout & ED/SI triage | `pnn_arrangement_tool.py` |
| `pnn-t1t2-data-presentation` | Physical-quantity chart selection & 5 mandatory physics ablations | `pnn_data_pres_tool.py` |
| `pnn-t1t2-benchmarking` | 4-tier energy accounting, GPU parity & all-tier SOTA bridge | `pnn_benchmark_tool.py` |
| `pnn-t1t2-conclusion` | Journal-exact closing headings, limitations & scaling roadmap | `pnn_conclusion_tool.py` |
| `pnn-t1t2-methods` | Reproducible 7-subsection Methods & Data/Code disclosure audit | `pnn_methods_tool.py` |
| `pnn-t1t2-si` | SI TOC, Supplementary Note blueprint & Main/SI sync audit | `pnn_si_tool.py` |
| `pnn-t1t2-rebuttal` | 5-beat T1/T2 rebuttal framework & kill-shot C1-C8 defense moves | `pnn_rebuttal_tool.py` |
| `low-aigc-nondefensive-writing` | Low-AIGC humanization, non-defensive authority & native `vocab-upgrade` | `aigc_nondefensive_auditor.py` |
| `sci-tech-naming` | Pronounceable feature-linked tech naming + all-tier collision checker | `tech_naming_tool.py` |

<!-- v3.5-companion-skills-readme end -->

## Install

The skill follows the [Agent Skills](https://agentskills.io/specification) format: one folder with `SKILL.md` at its top, plus `references/` and `scripts/`. Any agent that reads `SKILL.md` skills can use it. The agent reads `SKILL.md` and runs the toolkit when it needs numbers.

**One command for the agents you have.** The [`skills` CLI](https://github.com/vercel-labs/skills) finds the agents installed on your machine and installs the skill for each:

```bash
npx skills add ZhihaoRenKevin/pnn-paper-playbook       # this project only
npx skills add ZhihaoRenKevin/pnn-paper-playbook -g    # all projects
```

**By hand.** Clone the repository into your agent's skills folder. Keep the folder name `pnn-paper-playbook`, the same as the skill's `name`.

```bash
git clone https://github.com/ZhihaoRenKevin/pnn-paper-playbook <skills folder>/pnn-paper-playbook
```

| Agent | Skills folder for all projects | Skills folder for one project |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.agents/skills/` |
| Antigravity | `~/.gemini/config/skills/` | `.agents/skills/` |
| GitHub Copilot | `~/.copilot/skills/` | `.agents/skills/` |
| Cursor | `~/.cursor/skills/` | `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Windsurf | `~/.codeium/windsurf/skills/` | `.windsurf/skills/` |

These folders can change between agent versions. If the skill does not show up, check your agent's documentation. To update, run `git pull` in the skill folder.

**Claude app (claude.ai and desktop).** Upload a zip whose top folder is `pnn-paper-playbook` under Customize → Skills. Code execution must be on for the toolkit to run. The zip is attached to the [latest release](https://github.com/ZhihaoRenKevin/pnn-paper-playbook/releases/latest). GitHub's own "Download ZIP" does not work as it is, because its folder is called `pnn-paper-playbook-main` and Claude looks for a folder named after the skill. To use it, unzip it, rename the folder to `pnn-paper-playbook` and zip that folder again.

## Toolkit examples

Run these from the skill folder, or give the script's full path. Use `python3` where `python` is not Python 3.

```bash
python scripts/pnn_research_toolkit.py --help
python scripts/pnn_research_toolkit.py atlas --class A1 --param P_pi --top 3
python scripts/pnn_research_toolkit.py materials --family Sb2Se3 --class A3 --param loss_per_pi
python scripts/pnn_research_toolkit.py benchmark --task Fashion-MNIST --platform MZI
python scripts/pnn_research_toolkit.py lit-search --platform MRR --tier T1,T2 --top 10
python scripts/pnn_research_toolkit.py sota-table --platform MZI
python scripts/pnn_research_toolkit.py draft-linter my_draft.md
```

`atlas`, `materials`, `coverage` and `benchmark` also take `--tsv`, and `idea-gen` takes `--json`, for machine-readable output.

## Data notes

- The repository holds no text from the papers or from peer-review files. Each record gives the value, unit, status, conditions, page and section, and `references/citations.csv` gives the DOI, so every number can be checked against the paper.
- `figure-blueprint` and the referee history in `referee-simulator` read a local library of the source papers (`PNN_LIBRARY_ROOT`), which is not distributed. Without it they say so: `figure-blueprint` exits with code 3, and `referee-simulator` prints its generic checklist.

## Limits

- The records were extracted with AI assistance. They were checked against the full texts by scripts and by independent sampled audits (`references/PNN_params/README_PNN_params.md` §26), not one by one by hand. Errors remain, so check the paper before citing a number.
- The library has a cut-off and a scope: published journal papers, with MDPI journals excluded. Search the literature again before claiming novelty.
- Group affiliations and roles come from OpenAlex and the papers, and may be out of date.
- Many system-level extremes, such as energy per operation and throughput, are calculated or optical-only figures. The toolkit marks them (`best_measured_calc`, energy boundary); read the condition before quoting them.

## License

- Code (`scripts/`): MIT, see `LICENSE`.
- Documentation and compiled data (`SKILL.md`, `references/`, `verification/`): CC BY 4.0, see `LICENSE-DATA.md`.

The facts and bibliographic metadata of the cited papers are not claimed. When you use a number from the records, cite the original paper.

## Citation

See `CITATION.cff`, or cite as: Zhihao Ren, *pnn-paper-playbook: an agent skill and parameter dataset for photonic neural network research*, version 3.5.0, 2026, https://github.com/ZhihaoRenKevin/pnn-paper-playbook.

## 中文简介

这是一个光子神经网络 / 光计算方向的 agent skill。它帮你规划和撰写论文，选期刊档次，预判和回复审稿意见，也能查询从 1,133 篇已发表论文里整理出的器件与系统参数。不含论文和审稿文件的原文。参数记录保留数值、单位、状态、条件、页码和 DOI，可以逐条回到原文核对。代码采用 MIT 许可，文档和数据采用 CC BY 4.0 许可。

它符合 Agent Skills 格式，可以装进 Claude Code、Claude 网页版与桌面版、Codex、Gemini CLI、Antigravity、GitHub Copilot、Cursor 等支持 `SKILL.md` 的 agent，装法见上面的 Install。工具只需要 Python 3.8 以上，不用另装任何包。
