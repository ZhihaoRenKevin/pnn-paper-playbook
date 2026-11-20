#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-editorial-audit`: Tier-Fit evaluator + 16-Point Full-Manuscript Gatekeeper."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"

AI_HYPE_WORDS = [
    "transformative", "groundbreaking", "pivotal", "pioneering", "unprecedented",
    "seamless", "seamlessly", "holistic", "compelling", "meticulous", "meticulously",
    "delve", "underscore", "underscores", "showcase", "showcasing", "elucidate",
    "orchestrate", "paradigm shift", "landscape", "cornerstone", "testament",
    "unlock", "unlocking", "revolutionize", "usher in", "not only", "but also",
    "rapidly evolving", "garnered increasing attention", "lays the groundwork",
    "opens new avenues", "broad application prospects", "poised to transform",
]

AI_BAD_OPENERS = [
    "Thus,", "Notably,", "Importantly,", "Interestingly,", "Remarkably,",
    "Strikingly,", "Specifically,", "More specifically,", "In particular,",
    "Subsequently,", "Obviously,", "Clearly,", "Collectively,", "Overall,",
    "Looking ahead,", "Looking forward,", "Moving forward,", "As such,", "Yet,",
]

def check_voice_hygiene(text: str) -> list[str]:
    issues = []
    if "\u2014" in text or "--" in text:
        cnt = text.count("\u2014")
        issues.append(f"Em-dash detected ({cnt}x): remove em-dashes for crisp T1/T2 clarity.")
    low = text.lower()
    hits = [w for w in AI_HYPE_WORDS if re.search(r"\b" + re.escape(w) + r"\b", low)]
    if hits:
        issues.append("AI/promotional vocabulary detected: " + ", ".join(hits[:8]))
    bad_op = [op for op in AI_BAD_OPENERS if re.search(r"(?:^|[\.\!\?]\s+)" + re.escape(op), text)]
    if bad_op:
        issues.append("Non-author / AI sentence openers detected: " + ", ".join(bad_op[:6]))
    return issues

def safe_read_text(arg: str) -> str:
    if len(arg) > 240 or "\n" in arg:
        return arg
    p = Path(arg)
    try:
        return p.read_text(encoding="utf-8", errors="replace") if p.exists() else arg
    except OSError:
        return arg


TRIGGER_WORDS = ["all-optical", "real-time", "deep", "nonlinear", "scalable", "non-volatile", "held-out", "distillation", "perfect", "first"]

def cmd_tier_fit(args):
    score = 0
    gaps = []
    if args.measured_e2e: score += 3
    else: gaps.append("Missing end-to-end hardware task measurement (emulation/simulation alone caps at T3/T4).")
    if args.ablation: score += 2
    else: gaps.append("Missing physics ablation proving optical core beats untrained-core & input-bypass baselines.")
    if args.real_task: score += 2
    else: gaps.append("Missing task beyond toy MNIST/Iris/XOR (95-97% of T1/T2 papers include real-signal/higher-dim tasks).")
    if args.gpu_bench: score += 2
    else: gaps.append("Missing matched-precision comparison vs named GPU/ASIC with 4-tier energy accounting.")
    if args.novel_mechanism: score += 2
    else: gaps.append("Story reads incremental; apply T1/T2 Story-Elevation (bug-to-feature, orthogonal synergy, or bottleneck kill-shot).")
    verdict = "T1 READY (Nature / Science)" if score >= 10 else ("T2 READY (Nat. Photon. / Nat. Electron. / Nat. Nanotech.)" if score >= 7 else "T3/T4 CURRENTLY (close gaps before T1/T2 submission)")
    print(f"=== PNN T1/T2 Editorial Tier-Fit Assessment (Class {args.claim_class.upper()}) ===")
    print(f"Score: {score}/11 -> Verdict: {verdict}")
    for i, g in enumerate(gaps, 1):
        print(f"  [Gap {i}] {g}")

def cmd_full_audit(args):
    txt = Path(args.file).read_text(encoding="utf-8", errors="replace")
    si_txt = Path(args.si).read_text(encoding="utf-8", errors="replace") if args.si and Path(args.si).exists() else ""
    combined = txt + "\n" + si_txt
    print(f"=== PNN {args.tier.upper()} 16-Point Full-Manuscript Pre-Submission Gatekeeper ===")
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    title = lines[0].lstrip("#").strip() if lines else ""
    t_wc = len(title.split())
    checks = [
        ("1. Title <=10w (T1) / <=12w (T2) and zero colons", (t_wc <= (10 if args.tier == "T1" else 12)) and (":" not in title)),
        ("2. Energy accounting boundary stated (core/laser/chip-IO/wall-plug)", bool(re.search(r"\b(?:core[- ]optical|laser\s+power|wall[- ]plug|DAC|ADC|TIA)\b", combined, re.I))),
        ("3. Measured vs Projected metrics explicitly separated", bool(re.search(r"\b(?:measured|experimental)\b", combined, re.I) and re.search(r"\b(?:projected|estimated|extrapolat)\b", combined, re.I))),
        ("4. Optical vs Electronic operation split stated", bool(re.search(r"\b(?:optical\s+domain|electronic|digital\s+readout|O-E-O|optoelectronic)\b", combined, re.I))),
        ("5. Precision / ENOB / RMS error reported", bool(re.search(r"\b(?:ENOB|\d+(?:\.\d+)?[- ]bit|RMS\s+error|bit\s+precision)\b", combined, re.I))),
        ("6. Physics ablation control present", bool(re.search(r"\b(?:ablation|untrained|identity\s+layer|laser\s+off|digital\s+baseline|bypass)\b", combined, re.I))),
        ("7. Real-signal or beyond-toy task included", bool(re.search(r"\b(?:Fashion[- ]MNIST|CIFAR|ImageNet|speech|audio|radar|fiber|fibre|Ising|PDE|in[- ]sensor|generative|ECG|medical)\b", combined, re.I))),
        ("8. Named GPU/ASIC comparator included", bool(re.search(r"\b(?:NVIDIA|A100|H100|V100|RTX|TPU|FPGA|ASIC|CMOS|DSP)\b", combined))),
        ("9. Explicit Limitations / first scaling bottleneck paragraph", bool(re.search(r"\b(?:limitation|limited\s+by|bottleneck|crosstalk|insertion\s+loss|scaling\s+limit)\b", combined, re.I))),
        ("10. Data & Code Availability + repository DOI", bool(re.search(r"\b(?:Data\s+availability|Code\s+availability|GitHub|Zenodo|10\.5281)\b", combined, re.I))),
        ("11. Competing Interests / Ethics statement", bool(re.search(r"\b(?:Competing\s+interests|ethics|IRB|consent)\b", combined, re.I))),
        ("12. Zero raw '4*1' multiplication typos (use '4 x 1')", not bool(re.search(r"\b\d+\s*\*\s*\d+\b", txt))),
        ("13. Zero internal filenames leaked (.py/.csv/.fsp/.mph)", not bool(re.search(r"\b(?:\.py|\.csv|\.fsp|\.mph)\b", combined))),
        ("14. Zero em-dashes (author house-style guidelines)", "\u2014" not in txt),
    ]
    passed = 0
    for label, ok in checks:
        if ok: passed += 1
        print(f"  [{'PASS' if ok else 'FLAG'}] {label}")
    # Trigger word audit (15)
    trig_hits = [w for w in TRIGGER_WORDS if re.search(r"\b" + re.escape(w) + r"\b", txt, re.I)]
    print(f"  [INFO] 15. High-risk claim words to verify with quantitative proof: {', '.join(trig_hits) or 'none'}")
    # Voice hygiene (16)
    vh = check_voice_hygiene(txt)
    print(f"  [{'PASS' if not vh else 'FLAG'}] 16. author-voice & Anti-AIGC check: {'; '.join(vh) if vh else 'clean'}")
    print(f"Summary: {passed}/{len(checks)} structural gates passed.")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Editorial Audit & Tier-Fit CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pt = sub.add_parser("tier-fit", help="Evaluate T1 vs T2 vs T3 readiness before submission")
    pt.add_argument("--claim-class", default="B")
    pt.add_argument("--measured-e2e", action="store_true")
    pt.add_argument("--ablation", action="store_true")
    pt.add_argument("--real-task", action="store_true")
    pt.add_argument("--gpu-bench", action="store_true")
    pt.add_argument("--novel-mechanism", action="store_true")
    pf = sub.add_parser("full-audit", help="Run 16-point automated T1/T2 manuscript gatekeeper")
    pf.add_argument("file"); pf.add_argument("--si", default=""); pf.add_argument("--tier", default="T1", choices=["T1", "T2"])
    args = ap.parse_args()
    if args.cmd == "tier-fit": cmd_tier_fit(args)
    else: cmd_full_audit(args)

if __name__ == "__main__":
    main()
