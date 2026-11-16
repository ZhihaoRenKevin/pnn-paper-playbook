#!/usr/bin/env python3
"""
PNN Scientific Research CLI Toolkit (`pnn_research_toolkit.py`)
Part of the `pnn-paper-playbook` skill (`v3.4.1`).

Provides 13 research subcommands backed by the files in `references/`: 10,087 device and
system parameter records from 1,133 papers in 19 classes (`A1..J`), derived atlases, SOTA and
benchmark ledgers, a citation table and a directory of 140 research groups. The skill ships
no text from the papers: each record gives value, unit, status, condition, page and DOI.
`referee-simulator` and `figure-blueprint` also use files from a local PNN library when one is
available (set PNN_LIBRARY_ROOT); without it they say so:

  1. lit-search           Multi-criteria literature search across library_index.csv & cards
  2. related-work         Rank related-work candidates by platform, with DOIs and the closest prior work
  3. sota-table           Generate publication-ready Markdown/LaTeX Table 1 & Pareto CSV
  4. energy-latency-audit Compute 4-boundary energy, step latency, crossover N*, & integer k/n check
  5. referee-simulator    Simulate a 3-Referee Pre-Mortem + R18b 4-point blind-test checks
  6. reviewer-finder      List leading groups for a platform as reviewer candidates
  7. figure-blueprint     Retrieve Qwen2.5-VL-7B visual blueprints for Fig. 1..8 by platform & tier
  8. draft-linter         Lint a manuscript/rebuttal (.md/.txt/.tex/.docx) against T1-T3 rules
  9. atlas                Query device_parameter_atlas.csv by class/param/label/status/--top
 10. materials            Query materials_atlas.csv by material family/class/param
 11. coverage             Query device_coverage.csv by class/label with thin-cell flagging
 12. benchmark            Query benchmark_ledger.csv by task/platform
 13. idea-gen             Generate grounded research idea cards (R1-R4) from derived tables (`R20`)
"""

import argparse
import csv
import json
import math
import os
import re
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

CANDIDATE_RN_DIRS = [SKILL_DIR.parent]


def find_rn_dir() -> Path:
    env_root = os.environ.get("PNN_LIBRARY_ROOT", "").strip()
    env_dirs = [Path(env_root) / "08_Reading_Notes", Path(env_root)] if env_root else []
    for d in env_dirs + CANDIDATE_RN_DIRS:
        try:
            if (d / "_work").is_dir():
                return d
        except Exception:
            pass
    return SKILL_DIR.parent


RN_DIR = find_rn_dir()
WORK_DIR = RN_DIR / "_work"


def parse_year_from_stem(stem: str, row_year: str = "") -> int:
    if row_year and str(row_year).strip().isdigit():
        y = int(str(row_year).strip())
        if 1980 <= y <= 2030:
            return y
    m = re.search(r"_(\d{2})V\d+", stem)
    if m:
        yy = int(m.group(1))
        return 1900 + yy if yy >= 80 else 2000 + yy
    m2 = re.search(r"_(\d{2})_", stem)
    if m2:
        yy = int(m2.group(1))
        return 1900 + yy if yy >= 80 else 2000 + yy
    return 0


def load_library_rows():
    li_path = REF_DIR / "library_index.csv"
    if not li_path.exists():
        ci_path = WORK_DIR / "cards_index.csv"
        if ci_path.exists():
            li_path = ci_path
        else:
            return []
    with open(str(li_path), encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_csv_file(path: Path):
    if not path.exists():
        return []
    with open(str(path), encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


# ------------------------------------------------------------------------------
# v3.4.1 helpers: label aliases (derived tables), free-text platform terms,
# citation table, library-file check
# ------------------------------------------------------------------------------
V341_LABEL_ALIASES = {
    "mrr": ["MRR_WDM", "microring"], "microring": ["MRR_WDM", "microring"], "micro-ring": ["MRR_WDM", "microring"],
    "ring": ["MRR_WDM", "microring"], "wdm": ["MRR_WDM"],
    "tfln": ["LNOI"], "ln": ["LNOI"], "linbo3": ["LNOI"], "lithium niobate": ["LNOI"],
    "sin": ["SiN", "Si3N4"], "si3n4": ["SiN", "Si3N4"], "silicon nitride": ["SiN", "Si3N4"],
    "si": ["SOI"], "silicon": ["SOI"],
    "metasurface": ["dielectric_metasurface", "metallic_metasurface", "metasurface_dielectric"],
    "diffractive": ["diffractive_free_space"], "d2nn": ["diffractive_free_space"],
    "slm": ["SLM_free_space", "spatial_SLM", "slm_dmd", "DMD", "LCoS_SLM", "transmissive_SLM"],
    "dmd": ["DMD", "slm_dmd"], "lcos": ["LCoS_SLM"],
    "phase-change": ["PCM"], "in-sensor": ["in_sensor"], "insensor": ["in_sensor"], "in sensor": ["in_sensor"],
    "laser": ["DFB", "DFB_SA", "FP", "FP_SA", "QD_laser", "VCSEL", "microlaser"],
    "comb": ["electro_optic_comb", "MRR_WDM"], "microcomb": ["electro_optic_comb", "MRR_WDM"],
    "iii-v": ["III_V", "AlGaAs"], "inp": ["III_V"], "gaas": ["III_V", "AlGaAs"],
    "silica": ["silica_PLC", "Hydex"], "plc": ["silica_PLC"],
    "photonic crystal": ["photonic_crystal_slab"], "phc": ["photonic_crystal_slab"],
    "rf": ["microwave", "pcb_microwave"], "pcb": ["pcb_microwave"],
    "liquid crystal": ["liquid_crystal", "LCoS_SLM"],
    "free space": ["free_space", "SLM_free_space", "diffractive_free_space"],
    "free-space": ["free_space", "SLM_free_space", "diffractive_free_space"],
    "fiber": ["fiber_loop"], "fibre": ["fiber_loop"],
    "on-chip": ["on_chip", "integrated"], "on chip": ["on_chip", "integrated"],
    "polymer": ["3d_printed_polymer", "two_photon_polymer"],
    "dopo": ["time_multiplexed_DOPO"], "cim": ["time_multiplexed_DOPO"],
}

V341_TEXT_TERMS = {
    "mrr": ["mrr", "microring", "micro-ring", "ring resonator", "weight bank", "broadcast-and-weight"],
    "mzi": ["mzi", "mach-zehnder", "mach\u2013zehnder"],
    "pcm": ["pcm", "phase-change", "phase change", "gst", "sb2se3", "sb2s3", "gsst"],
    "tfln": ["tfln", "lnoi", "lithium niobate", "linbo3"],
    "diffractive": ["diffractive", "d2nn"],
    "metasurface": ["metasurface", "meta-optic", "metalens"],
    "spiking": ["spiking", "spike"],
    "ising": ["ising", "annealer", "combinatorial optimization"],
    "in-sensor": ["in-sensor", "in sensor", "near-sensor"],
    "microcomb": ["microcomb", "kerr comb", "soliton comb", "frequency comb"],
    "slm": ["slm", "dmd", "spatial light modulator", "lcos"],
}
V341_TEXT_SYNONYM = {
    "microring": "mrr", "micro-ring": "mrr", "ring": "mrr", "mach-zehnder": "mzi", "phase-change": "pcm",
    "lnoi": "tfln", "ln": "tfln", "linbo3": "tfln", "lithium niobate": "tfln", "d2nn": "diffractive",
    "meta-optic": "metasurface", "insensor": "in-sensor", "in sensor": "in-sensor", "comb": "microcomb",
    "dmd": "slm", "lcos": "slm",
}


def v341_text_terms(q: str):
    ql = (q or "").strip().lower()
    if not ql:
        return []
    return V341_TEXT_TERMS.get(V341_TEXT_SYNONYM.get(ql, ql), [ql])


def v341_resolve_labels(q, available):
    """Labels in `available` that match q: exact (case-insensitive) first, then the alias table."""
    avail = sorted(set(available))
    exact = [a for a in avail if a.lower() == q.strip().lower()]
    if exact:
        return exact
    canon = V341_LABEL_ALIASES.get(q.strip().lower(), [])
    return [a for a in avail if a in canon]


def v341_no_label(kind: str, q: str, available):
    print(f'no {kind} matches "{q}"; available {kind}s: ' + ", ".join(sorted(set(available))))


_V341_CITES = None


def v341_citations():
    global _V341_CITES
    if _V341_CITES is None:
        p = REF_DIR / "citations.csv"
        _V341_CITES = {}
        if p.exists():
            with open(str(p), encoding="utf-8-sig", newline="") as fh:
                _V341_CITES = {r["stem"]: r for r in csv.DictReader(fh)}
    return _V341_CITES


def v341_fold(s) -> str:
    """Lower-case and strip accents, so 'Ozcan' matches 'Özcan'."""
    return "".join(ch for ch in unicodedata.normalize("NFKD", str(s or "")) if not unicodedata.combining(ch)).lower()


def v341_require(path: Path, what: str):
    if not path.exists():
        sys.stderr.write(f"error: {what} not found at {path}. This sub-command needs the PNN library folder "
                         f"08_Reading_Notes/_work (set PNN_LIBRARY_ROOT to the PNN_Literature folder).\n")
        sys.exit(3)


# ==============================================================================
# 1. MULTI-CRITERIA LITERATURE SEARCH (`lit-search` — R15.1)
# ==============================================================================
def filter_library_rows(args):
    rows = load_library_rows()
    tiers_allowed = {t.strip().upper() for t in args.tier.split(",") if t.strip()} if getattr(args, "tier", "") else set()
    plat_q = [p.strip().lower() for p in (getattr(args, "platform", "") or "").split(",") if p.strip()]
    mat_q = [m.strip().lower() for m in (getattr(args, "material", "") or "").split(",") if m.strip()]
    func_q = [f.strip().lower() for f in (getattr(args, "function", "") or "").split(",") if f.strip()]
    task_q = (getattr(args, "task", "") or "").strip().lower()
    cls_q = {c.strip().upper() for c in (getattr(args, "claim_class", "") or "").split(",") if c.strip()}
    tword_q = (getattr(args, "title_word", "") or "").strip().lower()
    auth_q = v341_fold(getattr(args, "author", "") or "").strip()
    grp_q = v341_fold(getattr(args, "group", "") or "").strip()
    cites = v341_citations()
    kw_q = (getattr(args, "keyword", "") or "").strip().lower()
    ymin = getattr(args, "year_min", 0) or 0
    ymax = getattr(args, "year_max", 9999) or 9999
    if getattr(args, "year", 0):
        ymin = ymax = args.year
    plat_terms = sorted({t for pq in plat_q for t in v341_text_terms(pq)})
    excl_rev = bool(getattr(args, "exclude_reviews", False))
    only_meas = bool(getattr(args, "only_measured", False))

    tier_rank = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}
    matched = []
    for r in rows:
        stem = (r.get("stem") or r.get("base") or "").strip()
        if not stem:
            continue
        tier = (r.get("tier") or "T4").strip().upper()
        is_rev = str(r.get("is_review", "")).strip().lower() == "true" or (r.get("claim_class") or "").strip().lower() == "review"
        if excl_rev and is_rev:
            continue
        if tiers_allowed and "ALL" not in tiers_allowed and tier not in tiers_allowed:
            continue
        yr = parse_year_from_stem(stem, r.get("year", ""))
        if yr and (yr < ymin or yr > ymax):
            continue
        if cls_q and (r.get("claim_class") or "").strip().upper() not in cls_q:
            continue

        plat_str = f"{r.get('platform', '')} {r.get('primary_platform', '')}".lower()
        mat_str = (r.get("materials") or "").lower()
        func_str = (r.get("functions") or "").lower()
        title_str = f"{r.get('title', '')} {stem}".lower()
        full_blob = f"{stem} {r.get('title', '')} {plat_str} {mat_str} {func_str} {r.get('headline_measured', '')}".lower()

        if plat_q and not any(pq in plat_str or pq in mat_str for pq in plat_terms):
            continue
        if mat_q and not any(mq in mat_str or mq in plat_str for mq in mat_q):
            continue
        if func_q and not any(fq in func_str or fq in full_blob for fq in func_q):
            continue
        if task_q and task_q not in full_blob:
            continue
        if tword_q and tword_q not in title_str:
            continue
        cit = cites.get(stem, {})
        if auth_q and auth_q not in v341_fold(f"{cit.get('first_author', '')}; {cit.get('last_author', '')}; {cit.get('corresponding_authors', '')}"):
            continue
        if grp_q and grp_q not in v341_fold(f"{cit.get('last_author', '')}; {cit.get('corresponding_authors', '')}; {cit.get('last_author_institution', '')}"):
            continue
        if kw_q and kw_q not in full_blob:
            continue
        if only_meas and (is_rev or (r.get("headline_measured") or "not stated") in ("not stated", "simulated", "predicted")):
            continue

        matched.append((tier_rank.get(tier, 9), -yr, stem, r, yr))

    matched.sort(key=lambda x: (x[0], x[1], x[2]))
    return matched


def cmd_lit_search(args):
    matched = filter_library_rows(args)
    limit = args.limit
    shown = matched if limit <= 0 else matched[:limit]
    cites = v341_citations()

    print(f"# PNN Library Literature Search Results (`{len(matched)}` matched, showing `{len(shown)}`)")
    print("| # | Tier | Year | Class | Platform | Materials | Functions | Headline Measured | First / last author | DOI | Paper Stem & Card Path |")
    print("|---:|:---:|:---:|:---:|---|---|---|---|---|---|---|")
    for i, (_, _, stem, r, yr) in enumerate(shown, 1):
        c = cites.get(stem, {})
        fl = f"{c.get('first_author', '')} / {c.get('last_author', '')}" if c else ""
        print(f"| {i} | `{r.get('tier', 'T4')}` | {yr} | `{r.get('claim_class', '')}` | {r.get('platform', '')} | {r.get('materials', '')} | "
              f"{r.get('functions', '')} | {r.get('headline_measured', 'not stated')} | {fl} | {c.get('doi', '')} | "
              f"`{stem}` (`08_Reading_Notes/paper_cards/{stem}.md`) |")


# ==============================================================================
# 2. RELATED WORK SYNTHESIS & COMPETITOR ANALYSIS (`related-work` — R15.2)
# ==============================================================================
V341_STOP = {
    "a", "an", "the", "of", "on", "in", "for", "with", "and", "or", "to", "by", "using", "based", "via", "from", "at",
    "photonic", "optical", "neural", "network", "networks", "computing", "chip", "integrated", "device", "devices",
}


def cmd_related_work(args):
    topic = (args.topic or "").strip()
    matched = filter_library_rows(args)
    cites = v341_citations()
    toks = []
    for t in re.split(r"[\s,;+/()]+", topic.lower()):
        if len(t) >= 2 and t not in V341_STOP and t not in toks:
            toks.append(t)
    groups = [sorted(set([t] + v341_text_terms(t))) for t in toks]
    if groups:
        scored = []
        for tr, nyr, stem, r, yr in matched:
            title = (cites.get(stem, {}).get("title") or stem).lower()
            meta = f"{r.get('platform', '')} {r.get('materials', '')} {r.get('functions', '')}".lower()
            body = f"{r.get('headline_measured', '')}".lower()
            hit_groups, score = 0, 0
            for g in groups:
                w = 3 if any(t in title for t in g) else 2 if any(t in meta for t in g) else 1 if any(t in body for t in g) else 0
                hit_groups += 1 if w else 0
                score += w
            need = 1 if len(groups) == 1 else 2
            if hit_groups >= need:
                scored.append((-score, -hit_groups, tr, nyr, stem, r, yr))
        scored.sort()
        matched = [(tr, nyr, stem, r, yr) for _, _, tr, nyr, stem, r, yr in scored]

    shown = matched[: max(3, args.limit)]
    by_plat = defaultdict(list)
    for _, _, stem, r, yr in shown:
        by_plat[(r.get("platform") or "other").split(",")[0].strip()].append((stem, r, yr))

    print(f"# Related Work Candidates (`Topic: {topic or 'Custom Filter'}`)")
    print(f"- **Matched In-Library Papers**: `{len(matched)}` (top `{len(shown)}` shown, ranked by topic words in title > platform/material/function)")
    print("- These are candidates from the library index, not finished prose: read each paper before citing, "
          "and search journals and preprints after the library cut-off.\n")

    print("## 1. Candidates Grouped by Platform")
    for plat, items in by_plat.items():
        print(f"- **{plat}**: " + "; ".join(
            f"`{st}` ({yr}{', doi:' + cites[st]['doi'] if st in cites and cites[st].get('doi') else ''})" for st, _, yr in items))

    print("\n## 2. Closest `1–3` Candidates (`C1` / `C8` / `R18b-4`)")
    print("| Candidate | Tier | DOI | Platform & Material | Function | Headline Status | Page |")
    print("|---|:---:|---|---|---|---|---|")
    for _, _, stem, r, yr in shown[:3]:
        print(f"| `{stem}` | `{r.get('tier', '')}` | {cites.get(stem, {}).get('doi', '')} | `{r.get('platform', '')}` (`{r.get('materials', '')}`) | "
              f"{(r.get('functions') or '').split(';')[0]} | **{r.get('headline_measured', 'not stated')}** | {r.get('page', 'p.1')} |")



# ==============================================================================
# 3. SOTA TABLE GENERATOR (`sota-table`)
# ==============================================================================
def v341_sota_ledger_rows():
    """Rows of the two ledgers in references/metrics_sota.md, mapped by header name.

    Section 3 ("Complete `Measured_SOTA` Ledger") holds measured values; section 4
    ("Separate `Projected_Simulated_SOTA` Ledger") holds projected / simulated values.
    """
    text = (REF_DIR / "metrics_sota.md").read_text(encoding="utf-8", errors="ignore")
    rows, section, header = [], None, None
    for line in text.splitlines():
        if line.startswith("## "):
            section = "Measured" if "Measured_SOTA` Ledger" in line else ("Projected/Sim" if "Projected_Simulated_SOTA` Ledger" in line else None)
            header = None
            continue
        if section is None or not line.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if header is None:
            header = [re.sub(r"[`*]", "", c).strip().lower() for c in cells]
            continue
        if set(line.replace("|", "").strip()) <= set(":- "):
            continue
        rec = dict(zip(header, cells))
        rec["evidence"] = section
        rows.append(rec)
    return rows


def cmd_sota_table(args):
    if not (REF_DIR / "metrics_sota.md").exists():
        sys.stderr.write(f"error: cannot find {REF_DIR / 'metrics_sota.md'}\n")
        sys.exit(3)
    terms = v341_text_terms(args.platform) if args.platform.strip().lower() != "all" else []
    cites = v341_citations()
    seen, picked = set(), {"Measured": [], "Projected/Sim": []}
    for r in v341_sota_ledger_rows():
        plats = [p.strip().lower() for p in re.sub(r"[`*]", "", r.get("platform", "")).split(",")]
        if terms and not any(t in p for t in terms for p in plats):
            continue
        clean = {k: re.sub(r"[`*]", "", v).strip() for k, v in r.items()}
        key = (clean.get("platform"), clean.get("metric"), clean.get("value"), clean.get("unit"), clean.get("file"), clean.get("page"), clean["evidence"])
        if key in seen:
            continue
        seen.add(key)
        picked[clean["evidence"]].append(clean)

    n_m, n_p = len(picked["Measured"]), len(picked["Projected/Sim"])
    print(f"# SOTA Comparison Table for Platform: `{args.platform}`")
    print(f"- **Source**: `references/metrics_sota.md` §3 Measured ledger (`{n_m}` rows) and §4 Projected / Simulated ledger (`{n_p}` rows); duplicates removed.")
    print("- **Rule (`C2`/`C8`/`C10`)**: measured and projected / simulated values are printed in separate tables; never merge them into one column.\n")
    csv_out = []
    for title, ev in (("A. Measured", "Measured"), ("B. Projected / Simulated", "Projected/Sim")):
        rows = picked[ev][: args.limit] if args.limit > 0 else picked[ev]
        print(f"## {title} (`{len(rows)}` of `{len(picked[ev])}`)")
        print("| Work | Tier | DOI | Platform | Metric | Value & Unit | Boundary | Evidence | Page |")
        print("| :--- | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |")
        for r in rows:
            stem = re.sub(r"\.pdf$", "", r.get("file", ""))
            ev_txt = ev if ev == "Measured" else (r.get("status") or "projected")
            val_unit = f"{r.get('value', '')} {r.get('unit', '')}".strip()
            print(f"| `{stem}` | {r.get('tier', '')} | {cites.get(stem, {}).get('doi', '')} | {r.get('platform', '')} | {r.get('metric', '')} | "
                  f"**{val_unit}** | {r.get('boundary', '')} | `[{ev_txt}]` | {r.get('page', '')} |")
            csv_out.append({"work_stem": stem, "doi": cites.get(stem, {}).get("doi", ""), "tier": r.get("tier", ""), "platform": r.get("platform", ""),
                            "metric": r.get("metric", ""), "value_unit": val_unit, "boundary_condition": r.get("boundary", ""),
                            "evidence_type": ev_txt, "page": r.get("page", "")})
        print("")
    if args.ours:
        parts = [p.strip() for p in args.ours.split("|")]
        while len(parts) < 6:
            parts.append("stated in text")
        print("## C. This Work")
        print("| Work | Metric | Value & Unit | Boundary | Evidence | Source |")
        print("| :--- | :--- | :--- | :--- | :---: | :--- |")
        print(f"| **{parts[0] or 'This Work'}** | {parts[1]} | **{parts[2]}** | {parts[3]} | `[{parts[4]}]` | {parts[5]} |")
        csv_out.append({"work_stem": parts[0] or "This Work", "doi": "", "tier": "", "platform": args.platform, "metric": parts[1],
                        "value_unit": parts[2], "boundary_condition": parts[3], "evidence_type": parts[4], "page": ""})
    if args.csv:
        with open(str(Path(args.csv)), "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["work_stem", "doi", "tier", "platform", "metric", "value_unit", "boundary_condition", "evidence_type", "page"])
            w.writeheader()
            w.writerows(csv_out)
        print(f"[OK] Exported {len(csv_out)} SOTA rows to CSV: {args.csv}")


# ==============================================================================
# 4. SPEED, ENERGY, CROSSOVER & INTEGER-SPLIT AUDITOR (`energy-latency-audit`)
# ==============================================================================
def cmd_energy_latency_audit(args):
    args.acc_raw = args.acc_pct
    args.acc_pct = float(args.acc_pct)
    n_in = args.n_in
    n_out = args.n_out
    n_ctrl = args.n_controls
    macs_full = n_in * n_out
    ops_full = 2 * macs_full
    dof_compression = macs_full / max(1, n_ctrl)

    t_dac_us = args.dac_settle_us
    t_settle_us = args.tau_us
    t_adc_us = args.adc_avg * args.adc_sample_us
    t_readout_us = args.readout_us
    t_step_us = t_dac_us + t_settle_us + t_adc_us + t_readout_us
    f_step_hz = 1e6 / max(1e-6, t_step_us)

    f_fast_hz = args.clock_ghz * 1e9
    gops_fast = (ops_full * f_fast_hz) / 1e9

    p_opt_in_mw = args.laser_opt_mw
    p_opt_det_mw = p_opt_in_mw * (10.0 ** (-args.il_db / 10.0))
    p_laser_wall_mw = p_opt_in_mw / max(0.01, args.laser_wallplug_eff)

    p_b1_mw = p_opt_det_mw
    p_b2_mw = p_laser_wall_mw + args.heater_mw_total
    p_b3_mw = p_b2_mw + args.dac_adc_mw
    p_b4_mw = p_b3_mw + args.fpga_mw

    def fmt_energy(p_mw, rate_hz):
        j_per_op = (p_mw * 1e-3) / max(1e-9, ops_full * rate_hz)
        fj_per_op = j_per_op * 1e15
        pj_per_op = j_per_op * 1e12
        tops_per_w = 1.0 / max(1e-18, j_per_op * 1e12)
        return fj_per_op, pj_per_op, tops_per_w

    print("# PNN Speed, 4-Boundary Energy & ML Split Hygiene Audit (`SKILL.md §18`)")
    print(f"- **Operator Dimensions**: `{n_in} inputs × {n_out} outputs` = **`{macs_full}` MACs/pass** (`{ops_full}` OPs/pass)")
    print(f"- **Physical Controls**: `{n_ctrl}` controls -> **Dimensionality Compression Ratio** = `{macs_full}/{n_ctrl} = {dof_compression:.2f}×`")
    print(f"- **Fast Modulation / Inference Clock**: `{args.clock_ghz:.3f} GHz` -> **`{gops_fast:.2f} GOPS`** (`{gops_fast/1000:.4f} TOPS`)")
    print(f"- **Hardware-in-the-Loop Step Period**: `T_step = {t_step_us:.2f} µs` (`{f_step_hz/1e3:.2f} kHz`)\n")

    print("## 1. Four-Level System Energy Accounting Table (at Fast Clock Rate)")
    print("| Boundary Tag | Included Physical Components | Total Power (mW) | Share of Wall-Plug (%) | Energy / OP (`fJ/OP`) | Energy / OP (`pJ/OP`) | Efficiency (`TOPS/W`) |")
    print("| :--- | :--- | :---: | :---: | :---: | :---: | :---: |")
    for tag, desc, pmw in [
        ("`1. core_optical`", f"Detected optical power (`IL = {args.il_db:.1f} dB`)", p_b1_mw),
        ("`2. laser_plus_core`", f"Laser wall-plug (`{p_laser_wall_mw:.1f} mW`) + Heaters (`{args.heater_mw_total:.1f} mW`)", p_b2_mw),
        ("`3. chip_electrical_io`", f"Laser + Core + DAC/ADC/TIA (`{args.dac_adc_mw:.1f} mW`)", p_b3_mw),
        ("`4. wall_plug_system`", f"Full system incl. FPGA/Host/TEC (`{args.fpga_mw:.1f} mW`)", p_b4_mw),
    ]:
        fj, pj, tw = fmt_energy(pmw, f_fast_hz)
        pct = 100.0 * pmw / max(1e-6, p_b4_mw)
        print(f"| {tag} | {desc} | `{pmw:.2f}` | `{pct:.1f}%` | `{fj:.2f} fJ/OP` | `{pj:.4f} pJ/OP` | `{tw:.3f} TOPS/W` |")

    e_conv_pj = ((args.dac_adc_mw * 1e-3) / max(1.0, (n_in + n_out) * f_fast_hz)) * 1e12
    e_static_pj = ((p_b2_mw * 1e-3) / max(1.0, f_fast_hz)) * 1e12
    e_dig_mac_pj = args.digital_mac_pj
    a_term = e_conv_pj / max(1e-6, e_dig_mac_pj)
    n_star = a_term + math.sqrt(a_term ** 2 + e_static_pj / max(1e-6, e_dig_mac_pj))
    print(f"\n## 2. DAC/ADC Conversion Amortization Crossover (`N*` vs `{e_dig_mac_pj:.2f} pJ/MAC` Digital Baseline)")
    print(f"- **Amortization Crossover Dimension**: **`N* = {n_star:.1f}`**")

    if args.n_test > 0 and args.acc_pct >= 0:
        print(f"\n## 3. Test-Set Integer-Fraction Audit (`n_test = {args.n_test}`, Reported `Acc = {args.acc_pct:.2f}%`)")
        dec = len(str(args.acc_raw).split(".")[1]) if "." in str(args.acc_raw) else 0
        exact_k = round((args.acc_pct / 100.0) * args.n_test)
        implied_pct = 100.0 * exact_k / args.n_test
        diff = abs(implied_pct - args.acc_pct)
        if diff <= 0.5 * 10 ** (-dec) + 1e-9:
            print(f"- **[PASS] Integer Ratio Verified**: `{exact_k} / {args.n_test} = {implied_pct:.2f}%`")
        else:
            print(f"- **[WARNING - REFEREE KILL-SHOT `C7`/`C10`]**: `{args.acc_pct:.2f}%` is NOT an integer ratio of `n_test = {args.n_test}` "
                  f"(nearest: `{exact_k} / {args.n_test} = {implied_pct:.2f}%`).")


# ==============================================================================
# 5. THREE-REFEREE PRE-MORTEM SIMULATOR + R18b BLIND-TEST CHECKS (`referee-simulator`)
# ==============================================================================
def cmd_referee_simulator(args):
    plat_q = args.platform.lower().strip()
    mat_q = (getattr(args, "material", "") or "").lower().strip()
    cls_q = args.claim_class.upper().strip()
    tier_q = args.tier.upper().strip()
    pr_path = WORK_DIR / "pr_comments_v2.jsonl"

    comments_by_code = Counter()
    sample_quotes = {"circuit": [], "device": [], "ml": []}
    plat_terms = v341_text_terms(plat_q) if plat_q != "all" else []
    if not pr_path.exists():
        sys.stderr.write(f"warning: {pr_path} not found; printing the generic R18b checklist without historical referee quotes "
                         "(needs the PNN library folder 08_Reading_Notes/_work; set PNN_LIBRARY_ROOT).\n")
    if pr_path.exists():
        for line in pr_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if not line.strip():
                continue
            try:
                r = json.loads(line)
                txt = r.get("referee_quote") or r.get("text") or ""
                pcode = r.get("primary_concern") or r.get("primary_code") or "C10"
                sev = r.get("severity", "major")
                f_name = r.get("file", "")
                if plat_q == "all" or any(t in txt.lower() or t in f_name.lower() for t in plat_terms) or (mat_q and mat_q in txt.lower()):
                    comments_by_code[pcode] += 1
                    if sev == "major":
                        if pcode in ("C2", "C3", "C8", "C13") and len(sample_quotes["circuit"]) < 4:
                            sample_quotes["circuit"].append((f_name, pcode, txt[:260]))
                        elif pcode in ("C4", "C10", "C11", "C14") and len(sample_quotes["device"]) < 4:
                            sample_quotes["device"].append((f_name, pcode, txt[:260]))
                        elif pcode in ("C1", "C5", "C7", "C9") and len(sample_quotes["ml"]) < 4:
                            sample_quotes["ml"].append((f_name, pcode, txt[:260]))
            except Exception:
                pass

    print(f"# Simulated 3-Referee Pre-Mortem Panel (`Platform={args.platform}`, `Material={args.material or 'auto'}`, `Class={cls_q}`, `Target={tier_q}`)")
    print(f"- **Empirical Corpus Match**: `{sum(comments_by_code.values())}` historical referee comments (`Top codes: {dict(comments_by_code.most_common(6))}`)\n")
    for title, key in [
        ("Referee #1 — Optoelectronic System, Energy & Circuit Auditor (`C2`/`C3`/`C8`/`C13`)", "circuit"),
        ("Referee #2 — Integrated Photonics, Device Physics & Fabrication Auditor (`C4`/`C10`/`C11`/`C14`)", "device"),
        ("Referee #3 — Machine Learning, Benchmark Hygiene & Training Auditor (`C1`/`C5`/`C7`/`C9`)", "ml"),
    ]:
        print(f"## {title}")
        for fn, cd, qt in sample_quotes[key][:3]:
            print(f"  - *[{cd} · `{fn[:55]}...`]*: \"{qt}...\"")
        print("")

    # R18b: 4 Mandatory Blind-Test-Derived First-Round Checks
    print("## 4. Mandatory First-Round Blind-Test Checks (`R18b` — Calibrated on `00_Index/PNN_blind_test_score.md`)")
    print("  1. **`[R18b-1 · C11/C10]` Material-Centric Characterization Completeness** *(mandatory for 2D materials, MXene, perovskites, oxide/ferroelectric synapses, PCMs, or new compositions)*:")
    print("     - Verify core-level **XPS peak deconvolution** (and valence stability under bias), **indexed XRD** ruling out residual parent/impurity phases (e.g., 211 MAX phase or incomplete etching), **Raman mode assignment** matched to exact stoichiometry, and **parent/control sample** baseline response.")
    print("  2. **`[R18b-2 · C4]` Thermo-Optic / Photothermal / Electro-Thermal Crosstalk & Scaling**:")
    print("     - Quantify inter-unit **thermal crosstalk** (dB or $\\Delta\\lambda/\\text{mW}$ vs pitch), wavelength drift under optical/electrical power sweeps, feedback stabilization requirements, and the hard thermal limit on large-scale $N \\times N$ integration.")
    print("  3. **`[R18b-3 · C10/C11]` Foundational Hardware Display (`SEM + Total IL + Uniformity`)**:")
    print("     - Include a **full-array SEM micrograph** with labeled geometric dimensions, **total insertion loss** (fiber-to-fiber coupling + on-chip propagation/device loss breakdown), and **unit-to-unit uniformity** (tuning linearity and power consumption $\\mu \\pm \\sigma$ across cells).")
    print("  4. **`[R18b-4 · C1/C8]` Explicit Differentiation Against the Single Closest Prior-Art Reference**:")
    print("     - State in Introduction ¶3 and SI Table S1 the exact mechanism/system delta against the single closest prior-art paper (e.g., offline computer-trained weights vs on-chip training, single-node time-multiplexed bottleneck vs parallel array, or passive vs reconfigurable).")
    print("\n## 5. Secondary Author Self-Audit (Keep in SI; Do Not Crowd Out Top-10 First-Round Predictions)")
    print("  - Analytical gradient-approximation residuals, leaky-integrator weight decay error bounds, and non-negative weight constraints should be documented in SI Notes as proactive self-audits (`R6`), reserving the top-10 pre-mortem slots for `[R18b-1..4]` + primary `C1–C13` system/experiment attacks.")


# ==============================================================================
# 6. NON-CONFLICTING SUGGESTED REVIEWER FINDER (`reviewer-finder`)
# ==============================================================================
def cmd_reviewer_finder(args):
    plat_q = args.platform.lower().strip()
    terms = v341_text_terms(plat_q) if plat_q != "all" else []
    excl_inst = [v341_fold(x.strip()) for x in args.exclude_inst.split(",") if x.strip()]
    excl_names = [v341_fold(x.strip()) for x in args.exclude_names.split(",") if x.strip()]
    print(f"# Suggested Reviewer Candidates (`Platform={args.platform}`)\n")
    print("- Leading groups from `references/global_groups.md`, ranked by library score. Exclusion is by name and institution "
          "only (no co-authorship check): screen every candidate for conflicts before suggesting.\n")
    gg_md = REF_DIR / "global_groups.md"
    if not gg_md.exists():
        sys.stderr.write(f"error: {gg_md} not found.\n")
        sys.exit(3)
    cats = {"mrr": "wdm", "microcomb": "wdm", "mzi": "coherent", "pcm": "pcm", "tfln": "tfln", "diffractive": "freespace",
            "slm": "freespace", "metasurface": "meta", "ising": "ising", "in-sensor": "insensor", "reservoir": "reservoir"}
    cat = cats.get(V341_TEXT_SYNONYM.get(plat_q, plat_q), "")
    print("| PI Name | Institution & City | Country | Category | Role | Score | Representative Work |")
    print("| :--- | :--- | :--- | :--- | :--- | :---: | :--- |")
    shown = 0
    for line in gg_md.read_text(encoding="utf-8", errors="ignore").splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 10 or not c[0].isdigit():
            continue
        pi = re.sub(r"[*`]", "", c[1]).strip()
        if any(ex in v341_fold(c[2]) for ex in excl_inst) or any(ex in v341_fold(pi) for ex in excl_names):
            continue
        if terms and not (any(t in " ".join(c[4:]).lower() for t in terms) or (cat and f"`{cat}`" == c[4])):
            continue
        score = re.sub(r"[*`]", "", c[6]).split("(")[0].strip()
        print(f"| **{pi}** | {c[2]} | {c[3]} | {c[4]} | {c[5]} | **{score}** | {c[9].split('<br>')[0]} |")
        shown += 1
        if shown >= args.top:
            break
    if not shown:
        print("| (none matched) | | | | | | |")


# ==============================================================================
# 7. VISUAL FIGURE BLUEPRINT SEARCH (`figure-blueprint`)
# ==============================================================================
def cmd_figure_blueprint(args):
    plat_q = args.platform.lower().strip()
    fig_no = args.fig_num
    tiers_allowed = {t.strip().upper() for t in args.tier.split(",") if t.strip()}
    jl_path = WORK_DIR / "qwen25vl_visual_readings.jsonl"
    v341_require(jl_path, "figure readings (qwen25vl_visual_readings.jsonl)")
    plat_terms = v341_text_terms(plat_q) if plat_q != "all" else []
    hits = []
    for line in jl_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
            if fig_no > 0 and int(r.get("fig_num", 0)) != fig_no:
                continue
            if r.get("tier", "") not in tiers_allowed and "ALL" not in tiers_allowed:
                continue
            blob = f"{r.get('base','')} {r.get('caption_verbatim','')} {r.get('qwen25vl_analysis','')}".lower()
            if plat_q == "all" or any(t in blob for t in plat_terms):
                hits.append(r)
        except Exception:
            pass
    hits.sort(key=lambda x: (-float(x.get("tier_weight", 0.5)), x.get("base", "")))
    print(f"# `Qwen2.5-VL-7B` Visual Figure Blueprints (`Platform={args.platform}`, `Fig.{fig_no}`)\n")
    for idx, r in enumerate(hits[: args.limit], 1):
        print(f"### {idx}. `{r['base']}` — **Fig. {r['fig_num']}** (p.{r['page']}, `{r.get('tier','')}`)")
        print(f"- **Qwen2.5-VL-7B Visual Analysis**: {r.get('qwen25vl_analysis', '')}\n")


# ==============================================================================
# 8. MANUSCRIPT & REBUTTAL DRAFT LINTER (`draft-linter`)
# ==============================================================================
def extract_text_any(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        out = []
        with zipfile.ZipFile(str(path), "r") as zf:
            for name in sorted(zf.namelist()):
                if name.startswith("word/") and name.endswith(".xml"):
                    root = ET.fromstring(zf.read(name))
                    for elem in root.iter():
                        if elem.tag.endswith("}t") or elem.tag == "t":
                            if elem.text:
                                out.append(elem.text)
                        elif elem.tag.endswith("}p") or elem.tag == "p":
                            out.append("\n")
        return "".join(out)
    return path.read_text(encoding="utf-8", errors="ignore")


V341_PROMO_WORDS = [
    "seamless", "seamlessly", "leverage", "leverages", "leveraged", "leveraging", "transformative", "groundbreaking",
    "ground-breaking", "unprecedented", "revolutionary", "revolutionize", "revolutionise", "game-changing", "cutting-edge",
]
V341_TRIGGER_WORDS = ["all-optical", "real-time", "real time", "scalable", "deep", "nonlinear"]
V341_ENERGY_RE = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s*(aJ|fJ|pJ|nJ|\u00b5J|μJ|mJ)\b(?!\s*(?:/|per\b))")
V341_EFF_RE = re.compile(r"\b\d+(?:\.\d+)?\s*(?:TOPS/W|TOPS|GOPS|POPS|TOPS\s*W\s*-?1)\b")
V341_BOUNDARY_WORDS = ("core-only", "core only", "optical core", "optical-only", "optical only", "system-level", "system level", "system boundary", "wall-plug", "wall plug", "chip-level", "chip level", "including", "excluding", "boundary", "peripheral", "laser power", "dac", "adc", "electrical power")


def v341_sentences(txt: str):
    out = []
    for ln_no, line in enumerate(txt.splitlines(), 1):
        for sent in re.split(r"(?<=[.!?;])\s+", line):
            if sent.strip():
                out.append((ln_no, sent.strip()))
    return out


def cmd_draft_linter(args):
    p = Path(args.file)
    if not p.exists():
        sys.stderr.write(f"error: file not found: {p}\n")
        sys.exit(2)
    txt = extract_text_any(p)
    sents = v341_sentences(txt)
    issues = 0
    print(f"# PNN Pre-Submission Manuscript & Rebuttal Linter Report (`{p.name}`)")
    print("- Rules: SKILL.md §10.3 items 10-12 and §13; every flag is a prompt to check, not an automatic error.\n")

    dash_lines = [n for n, line in enumerate(txt.splitlines(), 1) if "\u2014" in line]
    print(f"## 1. Em dashes (`—`): `{txt.count(chr(0x2014))}`" + (f" (lines {', '.join(map(str, dash_lines[:12]))})" if dash_lines else ""))
    issues += txt.count(chr(0x2014))

    print("\n## 2. Promotional vocabulary (§13 item 8)")
    found = []
    for w in V341_PROMO_WORDS:
        lines = [n for n, line in enumerate(txt.splitlines(), 1) if re.search(r"\b" + re.escape(w) + r"\b", line, re.I)]
        if lines:
            found.append(f"`{w}` (lines {', '.join(map(str, lines[:8]))})")
    print("- " + ("; ".join(found) if found else "none"))
    issues += len(found)

    print("\n## 3. Trigger words without a number in the same sentence (§10.3 item 10)")
    trig = []
    for n, sent in sents:
        for w in V341_TRIGGER_WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", sent, re.I) and not re.search(r"\d", sent):
                trig.append(f"line {n}: `{w}` in \"{sent[:90]}\"")
    print("\n".join("- " + t for t in trig) if trig else "- none")
    issues += len(trig)

    print("\n## 4. Title length (§2, §13 item 9)")
    title = next((re.sub(r"^#+\s*", "", l).strip() for l in txt.splitlines() if l.strip()), "")
    nw = len(title.split())
    verdict = "too long (> 15 words)" if nw > 15 else ("fits T3/T4 (<= 12)" if nw > 8 else "fits T1/T2 (<= 8)")
    print(f"- `{title[:100]}`: `{nw}` words, {verdict}")
    issues += 1 if nw > 15 else 0

    print("\n## 5. Same metric reported with different values (§10.3 item 11)")
    acc_vals = defaultdict(set)
    for n, sent in sents:
        if re.search(r"accura", sent, re.I):
            for v in re.findall(r"(\d+(?:\.\d+)?)\s*%", sent):
                acc_vals["accuracy (%)"].add(v)
        for v, u in re.findall(r"(\d+(?:\.\d+)?)\s*(TOPS/W|TOPS|GOPS|fJ/MAC|pJ/MAC|aJ/MAC|fJ/OP|pJ/OP|dB/cm|dB)\b", sent):
            acc_vals[u].add(v)
    multi = {k: sorted(v, key=float) for k, v in acc_vals.items() if len(v) > 1}
    if multi:
        for k, v in sorted(multi.items()):
            print(f"- {k}: " + ", ".join(v) + "  (check these are different quantities or conditions, not inconsistent reports)")
    else:
        print("- none")
    issues += len(multi)

    print("\n## 6. Accuracy that is not an integer fraction of the stated test-set size (§13 item 5)")
    sizes = sorted({int(x.replace(",", "")) for x in re.findall(r"(\d[\d,]*)\s+(?:test|testing|held-out)\s+(?:images|samples|examples|digits|sequences|frames|sets?)", txt, re.I)
                    if int(x.replace(",", "")) > 0})
    bad = []
    for n, sent in sents:
        if not re.search(r"accura", sent, re.I):
            continue
        for v in re.findall(r"(\d+\.\d+)\s*%", sent):
            dec = len(v.split(".")[1])
            for size in sizes:
                k = round(float(v) * size / 100.0)
                if abs(100.0 * k / size - float(v)) > 0.5 * 10 ** (-dec) + 1e-9:
                    bad.append(f"line {n}: {v}% is not k/{size} (nearest {k}/{size} = {100.0 * k / size:.{dec}f}%)")
    if not sizes:
        print("- no test-set size stated (\"N test images/samples\"); state n for every accuracy")
    print("\n".join("- " + b for b in bad) if bad else ("- none" if sizes else ""))
    issues += len(bad) + (0 if sizes else 1)

    print("\n## 7. Energy / throughput without unit operation or boundary (§7.2, §13 item 3)")
    und = []
    for n, sent in sents:
        for m in V341_ENERGY_RE.finditer(sent):
            und.append(f"line {n}: `{m.group(0).strip()}` has no unit operation (per MAC / OP / bit / inference)")
        if V341_EFF_RE.search(sent) and not any(b in sent.lower() for b in V341_BOUNDARY_WORDS):
            und.append(f"line {n}: throughput / efficiency without a stated boundary in \"{sent[:80]}\"")
    print("\n".join("- " + u for u in und) if und else "- none")
    issues += len(und)

    print("\n## 8. Dimension written with `*` (§13 item 10)")
    dims = sorted(set(re.findall(r"\b\d+\s*\*\s*\d+\b", txt)))
    print("- " + (", ".join(f"`{d}` -> use ×" for d in dims) if dims else "none"))
    issues += len(dims)

    print("\n## 9. Data and code availability statements (§9, §13 item 11)")
    miss = [h for h in ("data availability", "code availability") if h not in txt.lower()]
    print("- " + ("missing: " + ", ".join(miss) if miss else "both present"))
    issues += len(miss)

    print(f"\n**Flags: {issues}**")


# ==============================================================================
# 9-13. DERIVED ATLAS, MATERIALS, COVERAGE, BENCHMARK & IDEA-GEN (`v3.4`)
# ==============================================================================
V34_CODES = [
    "A1", "A2", "A3", "A4", "A5", "A6",
    "B1", "B2", "C1", "D1", "D2", "E1", "E2", "E3",
    "F1", "G1", "H1", "I1", "J",
]

V34_STATUS_RANK = {"measured": 0, "simulated": 1, "predicted": 2}
V34_UNSPECIFIED_TASK = "unspecified (condition names no task)"

V34_FUNCTION_KEYWORDS = [
    ("activation", ["D1", "D2"]),
    ("nonlinear", ["D1", "D2"]),
    ("spik", ["G1"]),
    ("reservoir", ["F1"]),
    ("ising", ["H1"]),
    ("optimi", ["H1"]),
    ("sensor", ["I1"]),
    ("synap", ["I1"]),
    ("memory", ["A3", "A4", "I1"]),
    ("diffractive", ["E1"]),
    ("edge", ["E2"]),
    ("differentiat", ["E2"]),
    ("metasurface", ["E2"]),
    ("weight", ["A3", "A5", "A6"]),
    ("matrix", ["A3", "A5", "A6"]),
    ("detect", ["C1"]),
    ("modulat", ["A2"]),
    ("phase shift", ["A1", "A2"]),
    ("heater", ["A1"]),
    ("thermo", ["A1"]),
    ("comb", ["B1"]),
    ("laser", ["B2"]),
    ("vcsel", ["B2"]),
    ("slm", ["E3"]),
    ("dmd", ["E3"]),
    ("system", ["J"]),
    ("accelerat", ["J"]),
    ("thermal", ["A1"]),
    ("crosstalk", ["A1", "A5", "A6"]),
    ("microring", ["A5"]),
    ("micro-ring", ["A5"]),
    ("mrr", ["A5"]),
    ("mzi", ["A6"]),
    ("interferomet", ["A6"]),
    ("phase-change", ["A3"]),
    ("phase change", ["A3"]),
    ("pcm", ["A3"]),
    ("non-volatile", ["A3", "A4"]),
    ("nonvolatile", ["A3", "A4"]),
    ("electro-optic", ["A2"]),
    ("photodetect", ["C1"]),
    ("memristor", ["A4", "I1"]),
]

V34_LEDGER_PLATFORM = {
    "A3": "PCM",
    "A5": "MRR_WDM",
    "A6": "MZI",
    "B1": "MRR_WDM",
    "E1": "diffractive_free_space",
    "E3": "SLM_free_space",
    "F1": "reservoir",
    "G1": "spiking",
    "I1": "in_sensor",
}

V34_REVIEWER_BY_RECIPE = {
    "R1": ["C10", "C11", "C6", "C1"],
    "R2": ["C10", "C6", "C4", "C12"],
    "R3": ["C11", "C1", "C4", "C2"],
    "R4": ["C7", "C8", "C9", "C10"],
}


def v34_toint(val) -> int:
    try:
        return int(str(val).strip())
    except ValueError:
        return 0


def v34_tofloat(val):
    try:
        return float(str(val).strip())
    except ValueError:
        return None


def v34_tsv_line(cells) -> str:
    return "\t".join(re.sub(r"[\t\r\n]+", " ", str(c)) for c in cells)


def v34_md_cell(val) -> str:
    s = re.sub(r"[\t\r\n]+", " ", str(val))
    return s.replace("|", " / ")


def v34_read_csv_raw(filename: str):
    p = REF_DIR / "derived" / filename
    with open(str(p), encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.reader(fh))
    hdr = rows[0]
    return hdr, [dict(zip(hdr, r)) for r in rows[1:] if r]


def v34_print_md_table(cols, headers, rows):
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join("---" for _ in headers) + " |")
    for r in rows:
        print("| " + " | ".join(v34_md_cell(r.get(c, "")) for c in cols) + " |")


def cmd_atlas(args):
    if args.top is not None and args.param is None:
        sys.stderr.write("error: --top requires --param\n")
        sys.exit(2)
    hdr, rows = v34_read_csv_raw("device_parameter_atlas.csv")
    labels = None
    if args.label is not None:
        avail = [r["label"] for r in rows if r["code"] == args.cls and (args.param is None or r["param"] == args.param)]
        labels = set(v341_resolve_labels(args.label, avail))
        if not labels and not args.tsv:
            v341_no_label("label", args.label, avail)
            return
    sel = [
        r for r in rows
        if r["code"] == args.cls
        and (args.param is None or r["param"] == args.param)
        and (labels is None or r["label"] in labels)
        and (args.status is None or v34_toint(r.get("n_" + args.status)) >= 1)
    ]
    if args.top is not None:
        sel = [
            r for r in sel
            if r["label"] != "*"
            and r["direction"] in ("min", "max")
            and v34_tofloat(r["best_measured"]) is not None
        ]
        grouped = []
        for lf, unit in sorted({(r["label_field"], r["unit"]) for r in sel}):
            grp = sorted(
                (r for r in sel if r["label_field"] == lf and r["unit"] == unit),
                key=lambda r: (
                    v34_tofloat(r["best_measured"]) if r["direction"] == "min" else -v34_tofloat(r["best_measured"]),
                    r["label_field"],
                    r["label"],
                ),
            )
            grouped += grp[: max(0, args.top)]
        sel = grouped

    if args.tsv:
        out_lines = [v34_tsv_line(hdr)] + [v34_tsv_line([r[h] for h in hdr]) for r in sel]
        print("\n".join(out_lines))
        return

    if not sel:
        print("no measured record in library")
        return

    cols = [
        "code", "label_field", "label", "param", "unit", "direction",
        "papers_measured", "measured_median", "best_measured", "best_measured_text",
        "best_measured_record_id", "best_measured_tier", "best_measured_calc", "best_measured_condition",
        "best_simulated", "best_simulated_record_id", "best_predicted", "best_predicted_record_id",
    ]
    v34_print_md_table(cols, cols, sel)


def cmd_materials(args):
    hdr, rows = v34_read_csv_raw("materials_atlas.csv")
    fam_q = (args.family or "").lower()
    fams = sorted({r["material_family"] for r in rows})
    if not args.tsv and not any(fam_q in f.lower() for f in fams):
        print(f'no material family matches "{args.family}"; available material families: ' + "; ".join(fams))
        return
    sel = [
        r for r in rows
        if fam_q in r["material_family"].lower()
        and (args.cls is None or r["code"] == args.cls)
        and (args.param is None or r["param"] == args.param)
    ]
    if args.tsv:
        out_lines = [v34_tsv_line(hdr)] + [v34_tsv_line([r[h] for h in hdr]) for r in sel]
        print("\n".join(out_lines))
        return

    if not sel:
        print("no measured record in library")
        return

    print("# Materials Atlas (note: papers_via_label counts papers assigned by class label; remaining papers come from material_text)")
    cols = [
        "material_family", "code", "param", "unit", "direction",
        "papers_measured", "papers_via_label", "measured_median",
        "best_measured", "best_measured_text", "best_measured_record_id",
        "best_measured_tier", "best_measured_calc", "best_measured_condition",
        "best_simulated", "best_simulated_record_id", "best_predicted", "best_predicted_record_id",
    ]
    v34_print_md_table(cols, cols, sel)


def cmd_coverage(args):
    hdr, rows = v34_read_csv_raw("device_coverage.csv")
    labels = None
    if args.label is not None:
        avail = [r["label"] for r in rows if r["code"] == args.cls]
        labels = set(v341_resolve_labels(args.label, avail))
        if not labels and not args.tsv:
            v341_no_label("label", args.label, avail)
            return
    sel = [
        r for r in rows
        if r["code"] == args.cls and (labels is None or r["label"] in labels)
    ]
    out_hdr = hdr + ["thin"]
    if args.tsv:
        out_lines = [v34_tsv_line(out_hdr)] + [
            v34_tsv_line([r[h] for h in hdr] + ["thin" if v34_toint(r["papers_with_measured"]) <= 2 else ""])
            for r in sel
        ]
        print("\n".join(out_lines))
        return

    if not sel:
        print("no measured record in library")
        return

    enriched = []
    for r in sel:
        item = dict(r)
        item["thin"] = "thin" if v34_toint(r["papers_with_measured"]) <= 2 else ""
        enriched.append(item)
    cols = [
        "code", "class", "label_field", "label", "papers",
        "papers_with_measured", "papers_simulation_or_prediction_only",
        "records", "papers_by_tier", "papers_by_year", "params_with_measured_data", "thin",
    ]
    v34_print_md_table(cols, cols, enriched)


def cmd_benchmark(args):
    hdr, rows = v34_read_csv_raw("benchmark_ledger.csv")
    task_q = (args.task or "").lower()
    plats = None
    if args.platform is not None:
        avail = [r["platform"] for r in rows]
        plats = set(v341_resolve_labels(args.platform, avail))
        if not plats and not args.tsv:
            v341_no_label("platform", args.platform, avail)
            return
    sel = [
        r for r in rows
        if task_q in r["task"].lower()
        and (plats is None or r["platform"] in plats)
    ]
    if args.tsv:
        out_lines = [v34_tsv_line(hdr)] + [v34_tsv_line([r[h] for h in hdr]) for r in sel]
        print("\n".join(out_lines))
        return

    if not sel:
        print("no measured record in library")
        return

    cols = [
        "task", "platform", "papers", "papers_measured", "papers_simulated",
        "measured_median", "best_measured", "best_measured_text",
        "best_measured_record_id", "best_measured_stem", "best_measured_tier",
        "best_measured_condition", "best_measured_calc", "papers_by_tier",
    ]
    v34_print_md_table(cols, cols, sel)


def v34_load_idea_tables():
    atl_h, atl = v34_read_csv_raw("device_parameter_atlas.csv")
    mat_h, mat = v34_read_csv_raw("materials_atlas.csv")
    cov_h, cov = v34_read_csv_raw("device_coverage.csv")
    led_h, led = v34_read_csv_raw("benchmark_ledger.csv")
    _, ma = v34_read_csv_raw("materials_assignment.csv")
    _, ta = v34_read_csv_raw("benchmark_task_assignment.csv")

    mat_assign = defaultdict(set)
    for a in ma:
        mat_assign[(a["material_family"], a["code"], a["param"])].add(a["record_id"])

    rec_by_id = {}
    rec_by_code = defaultdict(list)
    params_dir = REF_DIR / "PNN_params"
    for p in sorted(params_dir.glob("*_records.jsonl")):
        with open(str(p), encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    rec = json.loads(line)
                    rec_by_id[rec["record_id"]] = rec
                    rec_by_code[rec["code"]].append(rec)

    ctitle = {}
    rp_path = REF_DIR / "reviewer_playbook.md"
    with open(str(rp_path), encoding="utf-8-sig") as fh:
        for line in fh:
            m = re.match(r"^\|\s*`?(C\d+)`?\s*\|\s*([^|]*?)\s*\|", line)
            if m and m.group(1) not in ctitle:
                ctitle[m.group(1)] = m.group(2)

    return {
        "atl_h": atl_h, "atl": atl,
        "mat_h": mat_h, "mat": mat,
        "cov_h": cov_h, "cov": cov,
        "led_h": led_h, "led": led,
        "mat_assign": mat_assign,
        "task_assign": ta,
        "rec_by_id": rec_by_id,
        "rec_by_code": rec_by_code,
        "ctitle": ctitle,
    }


def v34_function_classes(text: str):
    low = text.lower()
    hit = set()
    for kw, cs in V34_FUNCTION_KEYWORDS:
        if kw in low:
            hit |= set(cs)
    return [c for c in V34_CODES if c in hit]


def v34_r2_ok(r) -> bool:
    if r["direction"] not in ("min", "max"):
        return False
    m = v34_tofloat(r["best_measured"])
    if m is None:
        return False
    for k in ("best_simulated", "best_predicted"):
        x = v34_tofloat(r.get(k, ""))
        if x is None:
            continue
        if r["unit"] in ("dB", "dBm"):
            if (x - m >= 10) if r["direction"] == "max" else (m - x >= 10):
                return True
        elif m > 0 and x > 0 and ((x / m >= 10) if r["direction"] == "max" else (m / x >= 10)):
            return True
    return False


def v34_better_key(r):
    v = v34_tofloat(r["best_measured"])
    return v if r["direction"] == "min" else -v


def v34_prior_work(tbl, table_name: str, row):
    rec_by_id = tbl["rec_by_id"]
    rec_by_code = tbl["rec_by_code"]
    if table_name == "device_coverage":
        fld, lab = row["label_field"], row["label"]
        recs = [r for r in rec_by_code.get(row["code"], []) if (r.get(fld) or "(empty)") == lab]
        firsts = []
    elif table_name == "device_parameter_atlas":
        fld, lab = row["label_field"], row["label"]
        recs = [
            r for r in rec_by_code.get(row["code"], [])
            if r["param"] == row["param"] and (fld == "*" or (r.get(fld) or "(empty)") == lab)
        ]
        firsts = [row.get("best_measured_record_id"), row.get("best_simulated_record_id"), row.get("best_predicted_record_id")]
    elif table_name == "materials_atlas":
        ids = tbl["mat_assign"].get((row["material_family"], row["code"], row["param"]), set())
        recs = [rec_by_id[i] for i in ids if i in rec_by_id]
        firsts = [row.get("best_measured_record_id"), row.get("best_simulated_record_id"), row.get("best_predicted_record_id")]
    else:
        ids = {
            a["record_id"] for a in tbl["task_assign"]
            if a["task"] == row["task"] and (row["platform"] == "*" or a["platform"] == row["platform"])
        }
        recs = [rec_by_id[i] for i in ids if i in rec_by_id]
        firsts = [row.get("best_measured_record_id")]

    order, seen = [], set()
    for rid in firsts:
        if rid and rid in rec_by_id and rid not in seen:
            order.append(rec_by_id[rid])
            seen.add(rid)
    order += sorted(
        (r for r in recs if r["record_id"] not in seen),
        key=lambda r: (V34_STATUS_RANK.get(r["status"], 9), r["record_id"]),
    )
    out, stems = [], set()
    for r in order:
        if r["stem"] in stems:
            continue
        stems.add(r["stem"])
        out.append({
            "record_id": r["record_id"],
            "file": r["stem"],
            "page": r.get("page"),
            "doi": v341_citations().get(r["stem"], {}).get("doi", ""),
        })
        if len(out) == 5:
            break
    return out


def v34_target_params(tbl, table_name: str, row, contrast):
    atl = tbl["atl"]
    mat = tbl["mat"]

    def is_ok(a) -> bool:
        return (
            a["direction"] in ("min", "max")
            and v34_toint(a["papers_measured"]) >= 1
            and v34_tofloat(a["best_measured"]) is not None
        )

    def sort_key(a):
        return (-v34_toint(a["papers_measured"]), a["param"], a["unit"])

    def fill_atl(code, fld, lab):
        cand = sorted(
            [a for a in atl if a["code"] == code and a["label_field"] == fld and a["label"] == lab and is_ok(a)],
            key=sort_key,
        )
        if len(cand) < 3 and fld != "*":
            star_rows = sorted(
                [a for a in atl if a["code"] == code and a["label_field"] == "*" and is_ok(a)],
                key=sort_key,
            )
            cand += [a for a in star_rows if a not in cand]
        return cand[:6]

    if table_name in ("device_coverage", "device_parameter_atlas"):
        return fill_atl(row["code"], row["label_field"], row["label"])
    if table_name == "materials_atlas":
        return sorted(
            [m for m in mat if m["material_family"] == contrast["material_family"] and m["code"] == row["code"] and is_ok(m)],
            key=sort_key,
        )[:6]
    matches = [
        a for a in atl
        if a["code"] == "J" and a["label_field"] == "platform" and a["label"].lower() == row["platform"].lower()
    ]
    return fill_atl("J", "platform", matches[0]["label"]) if matches else fill_atl("J", "*", "*")


def v34_experiments(tbl, table_name: str, row):
    led = tbl["led"]
    if table_name == "benchmark_ledger":
        return [l for l in led if l["task"] == row["task"] and l["platform"] == "*"][:1]
    lp = row["label"] if (row["code"] == "J" and row.get("label_field") == "platform") else V34_LEDGER_PLATFORM.get(row["code"])
    if not lp:
        return []
    return sorted(
        [l for l in led if l["platform"] == lp],
        key=lambda l: (-v34_toint(l["papers_measured"]), l["task"]),
    )[:3]


def v34_ordered(hdr, row):
    return {h: row[h] for h in hdr}


def v34_build_search_queries(recipe: str, row):
    if recipe in ("R1", "R2"):
        term = row["label"] if row["label"] not in ("*", "(empty)") else row["class"]
        if recipe == "R1":
            return [
                f'"{term}" "{row["class"]}" photonic computing experiment',
                f'"{term}" optical neural network hardware demonstration',
            ]
        return [
            f'"{term}" "{row["param"]}" photonic device measured',
            f'"{term}" "{row["class"]}" optical computing hardware',
        ]
    if recipe == "R3":
        term = re.split(r" \(| / ", row["material_family"])[0].strip()
        return [
            f'"{term}" "{row["param"]}" photonic device experiment',
            f'"{term}" integrated photonics optical computing',
        ]
    term = re.split(r" \(| / ", row["task"])[0].strip()
    return [
        f'"{term}" "{row["platform"]}" photonic neural network experiment',
        f'"{term}" optical computing hardware benchmark',
    ]


def cmd_idea_gen(args):
    tbl = v34_load_idea_tables()
    cls_set = set(V34_CODES)
    if args.cls is not None:
        cls_set &= {args.cls}
    if args.function is not None:
        cls_set &= set(v34_function_classes(args.function))
    has_cf = args.cls is not None or args.function is not None
    plat_arg, mat_arg, task_arg = args.platform, args.material, args.task
    plat_set = None
    if plat_arg is not None:
        avail = ({r["label"] for r in tbl["cov"] + tbl["atl"] if r["label_field"] == "platform"} | {r["platform"] for r in tbl["led"]})
        plat_set = set(v341_resolve_labels(plat_arg, avail))

    def label_ok(r) -> bool:
        if plat_arg is not None and not (r["label_field"] == "platform" and r["label"] in plat_set):
            return False
        if mat_arg is not None and not (r["label_field"] == "material" and mat_arg.lower() in r["label"].lower()):
            return False
        return True

    lists = {"R1": [], "R2": [], "R3": [], "R4": []}
    if task_arg is None:
        lists["R1"] = [
            ("device_coverage", r, None)
            for r in sorted(
                (r for r in tbl["cov"] if r["code"] in cls_set and label_ok(r) and v34_toint(r["papers_with_measured"]) <= 2),
                key=lambda r: (v34_toint(r["papers_with_measured"]), r["code"], r["label_field"], r["label"]),
            )
        ]
        lists["R2"] = [
            ("device_parameter_atlas", r, None)
            for r in sorted(
                (r for r in tbl["atl"] if r["code"] in cls_set and label_ok(r) and v34_r2_ok(r)),
                key=lambda r: (v34_toint(r["papers_measured"]), r["code"], r["label_field"], r["label"], r["param"], r["unit"]),
            )
        ]
    if task_arg is None and plat_arg is None:
        groups = defaultdict(list)
        for r in tbl["mat"]:
            if r["direction"] in ("min", "max"):
                groups[(r["code"], r["param"], r["unit"], r["direction"])].append(r)
        c3 = []
        for (code, _, _, _), grp_rows in groups.items():
            if code not in cls_set:
                continue
            meas = [r for r in grp_rows if v34_toint(r["papers_measured"]) >= 1 and v34_tofloat(r["best_measured"]) is not None]
            if not meas:
                continue
            best = sorted(meas, key=lambda r: (v34_better_key(r), r["material_family"]))[0]
            for r in grp_rows:
                if r["material_family"] == best["material_family"] or v34_toint(r["papers_measured"]) > 1:
                    continue
                if mat_arg is not None and mat_arg.lower() not in r["material_family"].lower():
                    continue
                c3.append(("materials_atlas", r, best))
        lists["R3"] = sorted(
            c3,
            key=lambda t: (v34_toint(t[1]["papers_measured"]), t[1]["material_family"], t[1]["code"], t[1]["param"], t[1]["unit"]),
        )
    if not has_cf and mat_arg is None:
        lists["R4"] = [
            ("benchmark_ledger", r, None)
            for r in sorted(
                (
                    r for r in tbl["led"]
                    if r["platform"] not in ("*", "other")
                    and r["task"] != V34_UNSPECIFIED_TASK
                    and v34_toint(r["papers_measured"]) <= 1
                    and (task_arg is None or task_arg.lower() in r["task"].lower())
                    and (plat_arg is None or r["platform"] in plat_set)
                ),
                key=lambda r: (v34_toint(r["papers_measured"]), r["task"], r["platform"]),
            )
        ]

    limit_n = max(0, args.limit)
    picked, idx_k = [], 0
    while len(picked) < limit_n and any(idx_k < len(v) for v in lists.values()):
        for rec_code in ("R1", "R2", "R3", "R4"):
            if idx_k < len(lists[rec_code]) and len(picked) < limit_n:
                picked.append((rec_code,) + lists[rec_code][idx_k])
        idx_k += 1

    hdrs = {
        "device_coverage": tbl["cov_h"],
        "device_parameter_atlas": tbl["atl_h"],
        "materials_atlas": tbl["mat_h"],
        "benchmark_ledger": tbl["led_h"],
    }
    tier_col = {
        "device_coverage": "papers_by_tier",
        "benchmark_ledger": "papers_by_tier",
        "device_parameter_atlas": "measured_papers_by_tier",
        "materials_atlas": "measured_papers_by_tier",
    }

    cards = []
    for rank_n, (rec_code, table_name, row, contrast) in enumerate(picked, 1):
        tp = v34_target_params(tbl, table_name, row, contrast)
        cards.append({
            "rank": rank_n,
            "recipe": rec_code,
            "table": table_name,
            "row": v34_ordered(hdrs[table_name], row),
            "contrast_row": v34_ordered(tbl["mat_h"], contrast) if contrast else None,
            "prior_work": v34_prior_work(tbl, table_name, row),
            "target_params": [v34_ordered(tbl["mat_h"] if table_name == "materials_atlas" else tbl["atl_h"], a) for a in tp],
            "reviewer": [{"id": c, "title": tbl["ctitle"].get(c, "")} for c in V34_REVIEWER_BY_RECIPE[rec_code]],
            "experiments": [v34_ordered(tbl["led_h"], l) for l in v34_experiments(tbl, table_name, row)],
            "tiers": row[tier_col[table_name]],
            "search_queries": v34_build_search_queries(rec_code, row),
        })

    classes = [c for c in V34_CODES if c in cls_set]
    payload = {"classes": classes, "cards": cards}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    out = ["classes: " + (", ".join(classes) if classes else "(none)")]
    if not cards:
        if plat_arg is not None and not plat_set:
            out.append(f'no platform label matches "{plat_arg}"; see `coverage --class <code>` for the labels of each class')
        else:
            out.append("no idea card for these filters: no recipe applies, or every matching branch already has 2 or more "
                       "measured papers (check `benchmark` / `coverage` / `atlas` for the measured state)")
        print("\n".join(out))
        return

    for c in cards:
        r = c["row"]
        cr = c["contrast_row"]
        out.append("")
        out.append(f"## Card {c['rank']} [{c['recipe']} · {c['table']}]")
        out.append("【1 空白】")
        if c["table"] == "device_coverage":
            out.append(
                f"- recipe: {c['recipe']} | code: {r['code']} ({r['class']}) | {r['label_field']}: {r['label']} | "
                f"papers: {r['papers']} | papers_with_measured: {r['papers_with_measured']} | "
                f"sim_or_pred_only: {r['papers_simulation_or_prediction_only']} | records: {r['records']}"
            )
        elif c["table"] == "device_parameter_atlas":
            out.append(
                f"- recipe: {c['recipe']} | code: {r['code']} ({r['class']}) | {r['label_field']}: {r['label']} | "
                f"param: {r['param']} ({r['unit']}, direction: {r['direction']}) | "
                f"papers_measured: {r['papers_measured']} | best_measured: {r['best_measured']} ({r['best_measured_text']}, {r['best_measured_record_id']}) | "
                f"best_simulated: {r['best_simulated']} ({r['best_simulated_record_id']}) | best_predicted: {r['best_predicted']} ({r['best_predicted_record_id']})"
            )
        elif c["table"] == "materials_atlas":
            out.append(
                f"- recipe: {c['recipe']} | material_family: {r['material_family']} | code: {r['code']} | "
                f"param: {r['param']} ({r['unit']}, direction: {r['direction']}) | "
                f"papers_measured: {r['papers_measured']} | best_measured: {r['best_measured']} ({r['best_measured_record_id']})"
            )
            if cr:
                out.append(
                    f"- contrast_row: material_family: {cr['material_family']} | code: {cr['code']} | "
                    f"param: {cr['param']} ({cr['unit']}) | papers_measured: {cr['papers_measured']} | "
                    f"best_measured: {cr['best_measured']} ({cr['best_measured_text']}, {cr['best_measured_record_id']})"
                )
        else:
            out.append(
                f"- recipe: {c['recipe']} | task: {r['task']} | platform: {r['platform']} | "
                f"papers: {r['papers']} | papers_measured: {r['papers_measured']} | papers_simulated: {r['papers_simulated']} | "
                f"best_measured: {r['best_measured_text']} ({r['best_measured_record_id']})"
            )

        out.append("【2 前作】")
        if not c["prior_work"]:
            out.append("- (no prior-work record in library for this cell)")
        else:
            for pw in c["prior_work"]:
                out.append(f"- {pw['record_id']} | {pw['file']} | page: {pw['page']} | doi: {pw['doi'] or 'n/a'}")

        out.append("【3 器件参数】")
        if not c["target_params"]:
            out.append("- (no measured directional target parameter row in library)")
        else:
            for tp in c["target_params"]:
                if c["table"] == "materials_atlas":
                    out.append(
                        f"- {tp['material_family']} | {tp['code']} | {tp['param']} ({tp['unit']}, {tp['direction']}) | "
                        f"papers_measured: {tp['papers_measured']} | median: {tp['measured_median']} | "
                        f"best: {tp['best_measured']} ({tp['best_measured_text']}, {tp['best_measured_record_id']})"
                    )
                else:
                    out.append(
                        f"- {tp['code']} | {tp['label_field']}: {tp['label']} | {tp['param']} ({tp['unit']}, {tp['direction']}) | "
                        f"papers_measured: {tp['papers_measured']} | median: {tp['measured_median']} | "
                        f"best: {tp['best_measured']} ({tp['best_measured_text']}, {tp['best_measured_record_id']})"
                    )

        out.append("【4 审稿人会问】")
        for rv in c["reviewer"]:
            out.append(f"- {rv['id']}: {rv['title']}")

        out.append("【5 最小验证实验】")
        if not c["experiments"]:
            out.append("- (no mapped benchmark_ledger platform for this class)")
        else:
            for ex in c["experiments"]:
                out.append(
                    f"- task: {ex['task']} | platform: {ex['platform']} | papers_measured: {ex['papers_measured']} | "
                    f"papers_simulated: {ex['papers_simulated']} | median: {ex['measured_median']} | "
                    f"best: {ex['best_measured_text']} ({ex['best_measured_record_id']})"
                )

        out.append("【6 投稿档次】")
        out.append(f"- library_tiers: {c['tiers'] or '(none)'}")
        out.append("- 投稿档次与证据门槛请对照 SKILL.md §1 与 §14 综合判定。")

        out.append("【7 库外查新】")
        out.append("- 使用者须在给出 idea 前联网检索（本库有下载截止日期，须核对最新期刊与预印本）：")
        for sq in c["search_queries"]:
            out.append(f"- {sq}")

    print("\n".join(out))


def main():
    parser = argparse.ArgumentParser(description="PNN Scientific Research CLI Toolkit (pnn-paper-playbook v3.4.1)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ls = sub.add_parser("lit-search", help="Search the 1,475-paper PNN corpus by platform, material, function, task, tier, year, or title word")
    p_ls.add_argument("--platform", default="", help="Platform filter (e.g. PCM, TFLN, MZI, MRR, diffractive, metasurface, in-sensor, reservoir, Ising)")
    p_ls.add_argument("--material", default="", help="Material filter (e.g. Si, SiN, TFLN, BTO, GST, Sb2Se3, 2D-TMD, MXene, perovskite)")
    p_ls.add_argument("--function", default="", help="Computing function filter")
    p_ls.add_argument("--task", default="", help="Benchmark task filter (e.g. MNIST, CIFAR-10, Ising, equalization)")
    p_ls.add_argument("--claim-class", default="", help="Claim class filter (A..G)")
    p_ls.add_argument("--tier", default="", help="Comma-separated tiers (e.g. T1,T2,T3)")
    p_ls.add_argument("--year-min", type=int, default=0, help="Minimum publication year")
    p_ls.add_argument("--year-max", type=int, default=9999, help="Maximum publication year")
    p_ls.add_argument("--title-word", default="", help="Substring in paper title/stem (e.g. Ising, reservoir)")
    p_ls.add_argument("--author", default="", help="Substring of first, last or corresponding author (references/citations.csv)")
    p_ls.add_argument("--group", default="", help="Substring of last / corresponding author or last-author institution")
    p_ls.add_argument("--year", type=int, default=0, help="Exact publication year")
    p_ls.add_argument("--keyword", default="", help="General keyword substring")
    p_ls.add_argument("--exclude-reviews", action="store_true", help="Exclude review/perspective articles")
    p_ls.add_argument("--only-measured", action="store_true", help="Only return papers with measured headline metrics")
    p_ls.add_argument("--limit", "--top", dest="limit", type=int, default=25, help="Max results to print (0 = unlimited)")
    p_ls.set_defaults(func=cmd_lit_search)

    p_rw = sub.add_parser("related-work", help="Generate grouped Related Work synthesis, 1-3 closest competitors table, and referee alert")
    p_rw.add_argument("--topic", default="", help="Research topic description (e.g. 'TFLN electro-optic tensor core', 'PCM in-memory computing')")
    p_rw.add_argument("--platform", default="")
    p_rw.add_argument("--material", default="")
    p_rw.add_argument("--function", default="")
    p_rw.add_argument("--task", default="")
    p_rw.add_argument("--claim-class", default="")
    p_rw.add_argument("--tier", default="T1,T2,T3")
    p_rw.add_argument("--year-min", type=int, default=0)
    p_rw.add_argument("--year-max", type=int, default=9999)
    p_rw.add_argument("--title-word", default="")
    p_rw.add_argument("--author", default="")
    p_rw.add_argument("--group", default="")
    p_rw.add_argument("--year", type=int, default=0)
    p_rw.add_argument("--keyword", default="")
    p_rw.add_argument("--exclude-reviews", action="store_true", default=True)
    p_rw.add_argument("--only-measured", action="store_true", default=False)
    p_rw.add_argument("--limit", "--max-refs", dest="limit", type=int, default=12)
    p_rw.set_defaults(func=cmd_related_work)

    p_sota = sub.add_parser("sota-table", help="Generate publication-ready Markdown Table 1 & Pareto CSV")
    p_sota.add_argument("--platform", default="diffractive")
    p_sota.add_argument("--limit", type=int, default=15)
    p_sota.add_argument("--ours", default="")
    p_sota.add_argument("--csv", default="")
    p_sota.set_defaults(func=cmd_sota_table)

    p_el = sub.add_parser("energy-latency-audit", help="Compute 4-boundary energy, step latency, crossover N*, and integer k/n test split audit")
    p_el.add_argument("--n-in", type=int, default=16)
    p_el.add_argument("--n-out", type=int, default=16)
    p_el.add_argument("--n-controls", type=int, default=64)
    p_el.add_argument("--clock-ghz", type=float, default=1.0)
    p_el.add_argument("--laser-opt-mw", type=float, default=10.0)
    p_el.add_argument("--laser-wallplug-eff", type=float, default=0.15)
    p_el.add_argument("--il-db", type=float, default=12.0)
    p_el.add_argument("--heater-mw-total", type=float, default=150.0)
    p_el.add_argument("--dac-adc-mw", type=float, default=120.0)
    p_el.add_argument("--fpga-mw", type=float, default=400.0)
    p_el.add_argument("--dac-settle-us", type=float, default=5.0)
    p_el.add_argument("--tau-us", type=float, default=50.0)
    p_el.add_argument("--adc-avg", type=int, default=16)
    p_el.add_argument("--adc-sample-us", type=float, default=2.0)
    p_el.add_argument("--readout-us", type=float, default=10.0)
    p_el.add_argument("--digital-mac-pj", type=float, default=0.35)
    p_el.add_argument("--n-test", type=int, default=100)
    p_el.add_argument("--acc-pct", type=str, default="95.0", help="Reported accuracy in %% as written (its decimals set the k/n tolerance)")
    p_el.set_defaults(func=cmd_energy_latency_audit)

    p_ref = sub.add_parser("referee-simulator", help="Simulate a 3-referee pre-mortem + R18b blind-test checks (adds referee comments from a local PNN library if present)")
    p_ref.add_argument("--platform", default="diffractive")
    p_ref.add_argument("--material", default="")
    p_ref.add_argument("--claim-class", default="B")
    p_ref.add_argument("--tier", default="T2")
    p_ref.set_defaults(func=cmd_referee_simulator)

    p_rev = sub.add_parser("reviewer-finder", help="List leading groups for a platform as reviewer candidates; screen conflicts yourself")
    p_rev.add_argument("--platform", default="diffractive")
    p_rev.add_argument("--exclude-inst", default="", help="Comma-separated institutions to skip, e.g. your own")
    p_rev.add_argument("--exclude-names", default="", help="Comma-separated names to skip, e.g. you and your co-authors")
    p_rev.add_argument("--top", type=int, default=8)
    p_rev.set_defaults(func=cmd_reviewer_finder)

    p_fig = sub.add_parser("figure-blueprint", help="Search Qwen2.5-VL-7B visual figure readings")
    p_fig.add_argument("--platform", default="diffractive")
    p_fig.add_argument("--fig-num", type=int, default=1)
    p_fig.add_argument("--tier", default="T1,T2,T3")
    p_fig.add_argument("--limit", type=int, default=6)
    p_fig.set_defaults(func=cmd_figure_blueprint)

    p_lint = sub.add_parser("draft-linter", help="Lint a manuscript/rebuttal file against SKILL.md §10.3 and §13")
    p_lint.add_argument("file", help="Path to .md, .txt, .tex, or .docx draft")
    p_lint.set_defaults(func=cmd_draft_linter)

    p_atl = sub.add_parser(
        "atlas",
        help="Query references/derived/device_parameter_atlas.csv by class, param, label, status, or --top",
        description=(
            "Read references/derived/device_parameter_atlas.csv and keep rows with code == --class "
            "and matching optional --param, --label, and n_<status> >= 1.\n"
            "Sorting rules: without --top, preserve original CSV file order. With --top N (requires --param), "
            "drop label == '*', direction not in (min, max), and non-numeric best_measured; group by "
            "(label_field, unit) in lexicographic order; sort within each group by best_measured "
            "(ascending for min, descending for max), breaking ties by (label_field, label) lexicographically; "
            "take the first N rows per group."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_atl.add_argument("--class", dest="cls", required=True, help="Device class code (A1..A6, B1..B2, C1, D1..D2, E1..E3, F1, G1, H1, I1, J)")
    p_atl.add_argument("--param", default=None, help="Exact parameter name filter (required when --top is given)")
    p_atl.add_argument("--label", default=None, help="Exact label filter (e.g. GST, SOI, *)")
    p_atl.add_argument("--status", choices=["measured", "simulated", "predicted"], default=None, help="Require n_<status> >= 1")
    p_atl.add_argument("--top", type=int, default=None, help="Top N labels per (label_field, unit) group by best_measured (requires --param)")
    p_atl.add_argument("--tsv", action="store_true", help="Machine-readable TSV output with original CSV columns")
    p_atl.set_defaults(func=cmd_atlas)

    p_mat = sub.add_parser(
        "materials",
        help="Query references/derived/materials_atlas.csv by material family, class, and param",
        description=(
            "Read references/derived/materials_atlas.csv and keep rows whose material_family contains --family "
            "(case-insensitive) and match optional exact --class and --param.\n"
            "Sorting rule: preserve original CSV file order. Default output highlights papers_via_label."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_mat.add_argument("--family", required=True, help="Case-insensitive substring of material_family (e.g. SiN, Sb2Se3, TFLN)")
    p_mat.add_argument("--class", dest="cls", default=None, help="Optional exact device class code")
    p_mat.add_argument("--param", default=None, help="Optional exact parameter name")
    p_mat.add_argument("--tsv", action="store_true", help="Machine-readable TSV output with original CSV columns")
    p_mat.set_defaults(func=cmd_materials)

    p_cov = sub.add_parser(
        "coverage",
        help="Query references/derived/device_coverage.csv by class and optional label, marking thin cells",
        description=(
            "Read references/derived/device_coverage.csv and keep rows with code == --class and optional exact --label.\n"
            "Sorting rule: preserve original CSV file order. Appends column 'thin' ('thin' when papers_with_measured <= 2, else empty)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_cov.add_argument("--class", dest="cls", required=True, help="Device class code (A1..J)")
    p_cov.add_argument("--label", default=None, help="Optional exact label filter")
    p_cov.add_argument("--tsv", action="store_true", help="Machine-readable TSV output with appended 'thin' column")
    p_cov.set_defaults(func=cmd_coverage)

    p_bm = sub.add_parser(
        "benchmark",
        help="Query references/derived/benchmark_ledger.csv by task substring and optional platform",
        description=(
            "Read references/derived/benchmark_ledger.csv and keep rows where task contains --task (case-insensitive) "
            "and optional platform equals --platform (case-insensitive).\n"
            "Sorting rule: preserve original CSV file order."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_bm.add_argument("--task", required=True, help="Case-insensitive task substring (e.g. Fashion-MNIST, CIFAR-10, MNIST)")
    p_bm.add_argument("--platform", default=None, help="Optional case-insensitive exact platform filter (e.g. MZI, MRR_WDM, *)")
    p_bm.add_argument("--tsv", action="store_true", help="Machine-readable TSV output with original CSV columns")
    p_bm.set_defaults(func=cmd_benchmark)

    p_idea = sub.add_parser(
        "idea-gen",
        help="Generate grounded research idea cards via recipes R1-R4 from derived tables and records (R20)",
        description=(
            "Generate grounded idea cards from device_coverage.csv, device_parameter_atlas.csv, materials_atlas.csv, "
            "benchmark_ledger.csv, *_records.jsonl, and reviewer_playbook.md.\n"
            "Sorting and selection rules:\n"
            "  R1 (thin measured coverage, when --task not set): papers_with_measured <= 2, sorted by "
            "(int(papers_with_measured), code, label_field, label) ascending.\n"
            "  R2 (sim/pred ahead of measured by >=10 dB or >=10x, when --task not set): sorted by "
            "(int(papers_measured), code, label_field, label, param, unit) ascending.\n"
            "  R3 (material transfer vs best measured family in (code, param, unit, direction), when --task and --platform not set): "
            "papers_measured <= 1, sorted by (int(papers_measured), material_family, code, param, unit) ascending.\n"
            "  R4 (benchmark gap, when --class, --function, and --material not set): platform not in (*, other), "
            "papers_measured <= 1, sorted by (int(papers_measured), task, platform) ascending.\n"
            "Cards are interleaved round-robin across R1, R2, R3, R4 up to --limit (default 3)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_idea.add_argument("--function", default=None, help="Optional function text mapped by keyword substrings to device classes")
    p_idea.add_argument("--platform", default=None, help="Optional platform filter")
    p_idea.add_argument("--material", default=None, help="Optional material substring filter")
    p_idea.add_argument("--task", default=None, help="Optional benchmark task substring filter")
    p_idea.add_argument("--class", dest="cls", default=None, help="Optional device class code filter (A1..J)")
    p_idea.add_argument("--limit", type=int, default=3, help="Maximum number of idea cards to output (default 3)")
    p_idea.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    p_idea.set_defaults(func=cmd_idea_gen)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
