#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-introduction`: query T1/T2 PNN Introductions and lint drafts."""
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


def load_corpus():
    return [json.loads(l) for l in (REF_DIR / "t1t2_intro_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.funnel and args.funnel.lower() not in (r.get("int_funnel") or "").lower(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.journal and args.journal.lower() not in r["journal"].lower(): continue
        out.append(r)
    print(f"Matched {len(out)} T1/T2 Research Introductions (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print("=" * 84)
        print(f"[{r['tier']} | {r.get('country_primary','?')} w={r.get('prose_weight',1.0):.1f} | {r['journal']} {r['year']} | Class {r['claim_class']} | {r['platform']}] {r['title']}")
        print(f"Words: {r['intro_words']} | Paras: {r.get('int_paras')} | Funnel: {r.get('int_funnel')} | Hook: {r.get('int_hook')} | 'Here we' para: {r.get('int_hw_para')}")
        if r.get("intro_verbatim"):
            print("Excerpt:", r["intro_verbatim"][:700], "..." if len(r["intro_verbatim"]) > 700 else "")

def cmd_lint(args):
    txt = safe_read_text(args.file)
    paras = [p.strip() for p in re.split(r"\n\s*\n", txt.strip()) if len(p.strip().split()) >= 15]
    wc = len(txt.split())
    pc = len(paras)
    tier = args.tier.upper()
    w_lo, w_hi = (380, 720) if tier == "T1" else (420, 820)
    print(f"=== PNN {tier} Introduction Audit ===")
    print(f"Words: {wc} (target {w_lo}-{w_hi}) | Paragraphs: {pc} (target 3-5)")
    flags = []
    if wc < w_lo or wc > w_hi:
        flags.append(f"Word count {wc} outside {tier} target range ({w_lo}-{w_hi}).")
    if pc < 3 or pc > 6:
        flags.append(f"Paragraph count {pc} outside {tier} sweet spot (3-5 paragraphs).")
    if re.search(r"\b(?:Section\s+2|remainder\s+of\s+this\s+paper|rest\s+of\s+the\s+paper\s+is\s+organized)\b", txt, re.I):
        flags.append("Paper-organization TOC detected (avoided by 98-100% of T1/T2 PNN papers).")
    if not re.search(r"\b(?:However|Nevertheless|Although|Despite|Unfortunately)\b", txt):
        flags.append("Missing explicit technical gap / prior-art limitation pivot ('However, ...').")
    if not re.search(r"\b(?:Here,?\s+we|In\s+this\s+(?:work|Article|Letter)|we\s+propose|we\s+demonstrate)\b", txt, re.I):
        flags.append("Missing explicit proposal/breakthrough anchor in the closing paragraph(s).")
    if paras and not re.search(r"\d", paras[-1]):
        flags.append("Final Introduction paragraph has no quantitative scale/metric summary.")
    flags.extend(check_voice_hygiene(txt))
    if not flags:
        print("PASS: Introduction structure matches T1/T2 PNN empirical standards.")
    else:
        for i, fl in enumerate(flags, 1):
            print(f"  [{i}] {fl}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Introduction Craft CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query T1/T2 research Introductions")
    pq.add_argument("--tier", default=""); pq.add_argument("--funnel", default="")
    pq.add_argument("--platform", default=""); pq.add_argument("--journal", default="")
    pq.add_argument("--top", type=int, default=5)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pl = sub.add_parser("lint", help="Lint a draft Introduction file")
    pl.add_argument("file"); pl.add_argument("--tier", default="T1", choices=["T1", "T2"])
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    else: cmd_lint(args)

if __name__ == "__main__":
    main()
