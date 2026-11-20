#!/usr/bin/env python3
"""CLI toolkit for `pnn-t1t2-abstract`: query T1/T2 PNN abstracts, lint drafts, and print blueprints."""
from __future__ import annotations
import argparse, json, re, sys
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
    return [json.loads(l) for l in (REF_DIR / "t1t2_abstract_corpus.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

def split_sentences(text: str) -> list[str]:
    prot = text
    for ab in ("Fig.", "et al.", "e.g.", "i.e.", "vs.", "s.d.", "a.u."):
        prot = prot.replace(ab, ab.replace(".", "<D>"))
    prot = re.sub(r"(\d)\.(\d)", r"\1<D>\2", prot)
    return [s.replace("<D>", ".").strip() for s in re.split(r"(?<=[\.\?\!])\s+(?=[A-Z0-9\(])", prot.strip()) if len(s.strip()) >= 8]

def cmd_query(args):
    rows = load_corpus()
    if getattr(args, "native_only", False):
        rows = [r for r in rows if r.get("native_tier") == "native_primary"]
    rows.sort(key=lambda r: (-float(r.get("prose_weight", 1.0)), 0 if r.get("tier") == "T1" else 1))
    out = []
    for r in rows:
        if args.tier and r["tier"].upper() != args.tier.upper(): continue
        if args.journal and args.journal.lower() not in r["journal"].lower(): continue
        if args.claim_class and r["claim_class"].upper() != args.claim_class.upper(): continue
        if args.platform and args.platform.lower() not in (r.get("platform") or "").lower(): continue
        if args.keyword and args.keyword.lower() not in (r.get("abstract_verbatim","") + " " + r.get("title","")).lower(): continue
        out.append(r)
    print(f"Matched {len(out)} T1/T2 Research Abstracts (showing top {min(len(out), args.top)}):")
    for r in out[:args.top]:
        print("=" * 84)
        print(f"[{r['tier']} | {r.get('country_primary','?')} w={r.get('prose_weight',1.0):.1f} | {r['journal']} {r['year']} | Class {r['claim_class']} | {r['platform']}] {r['title']}")
        print(f"Words: {r['abstract_words']} | Sentences: {r['abstract_sent_count']} | Moves: {' -> '.join(r.get('abs_moves') or [])}")
        print(f"Gap cue: {r.get('abs_gap','')} | Comparator paired: {r.get('abs_comp')} | Dual op-points: {r.get('abs_dual_op')}")
        if r.get("abstract_verbatim"):
            print("Verbatim:", r["abstract_verbatim"])

def cmd_lint(args):
    txt = safe_read_text(args.file)
    txt = re.sub(r"\s+", " ", txt).strip()
    words = txt.split()
    sents = split_sentences(txt)
    wc, sc = len(words), len(sents)
    sent_lens = [len(s.split()) for s in sents] or [0]
    short_pct = round(100.0 * sum(1 for x in sent_lens if x <= 18) / max(1, len(sent_lens)), 1)
    tier = args.tier.upper()
    w_lo, w_hi = (130, 210) if tier == "T1" else (140, 225)
    print(f"=== PNN {tier} Abstract Audit ===")
    print(f"Word count: {wc} (target {w_lo}-{w_hi}) | Sentences: {sc} (target 6-8) | Mean sent len: {sum(sent_lens)/max(1,len(sent_lens)):.1f}w | Short(<=18w): {short_pct}%")
    flags = []
    if wc < w_lo or wc > w_hi:
        flags.append(f"Word count {wc} outside {tier} IQR window ({w_lo}-{w_hi} words).")
    if sc < 5 or sc > 9:
        flags.append(f"Sentence count {sc} outside {tier} sweet spot (6-8 sentences).")
    if not re.search(r"\b(?:However|Although|Despite|Unfortunately|Nevertheless)\b", txt):
        flags.append("Missing explicit gap pivot ('However, ...') in sentence 2-3.")
    if not re.search(r"\b(?:Here,?\s+we|We\s+(?:propose|demonstrate|report|present|show))\b", txt):
        flags.append("Missing explicit 'Here we propose/demonstrate...' breakthrough anchor.")
    if not re.search(r"\b\d+(?:\.\d+)?\s*(?:%|TOPS|GOPS|GHz|GBaud|ps|ns|µs|us|fJ|pJ|aJ|mW|W|dB|bit|bits|nm|µm|um|mm|fold|times)\b", txt, re.I):
        flags.append("No quantified measured metric with unit found.")
    if not re.search(r"\b(?:compared\s+(?:with|to)|higher\s+than|lower\s+than|faster\s+than|orders?\s+of\s+magnitude|exceeding|versus|vs\.?|theoretical|digital|GPU|electronic|times|fold)\b", txt, re.I):
        flags.append("No comparator/baseline paired with headline metric.")
    if re.search(r"\b(?:fJ|pJ|aJ|TOPS/W|GOPS/W)\b", txt) and not re.search(r"\b(?:optical|core|modulator|laser|system|wall[- ]plug|chip|electrical|DAC|ADC)\b", txt, re.I):
        flags.append("Energy metric present without stating energy accounting boundary.")
    flags.extend(check_voice_hygiene(txt))
    if not flags:
        print("PASS: No structural or voice defects detected.")
    else:
        for i, fl in enumerate(flags, 1):
            print(f"  [{i}] {fl}")

def main():
    ap = argparse.ArgumentParser(description="PNN T1/T2 Abstract Craft CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pq = sub.add_parser("query", help="Query verbatim T1/T2 research abstracts")
    pq.add_argument("--tier", default=""); pq.add_argument("--journal", default="")
    pq.add_argument("--claim-class", default=""); pq.add_argument("--platform", default="")
    pq.add_argument("--keyword", default=""); pq.add_argument("--top", type=int, default=5)
    pq.add_argument("--native-only", action="store_true", help="Filter strictly to native-English-country primary authors (US/GB/CA/AU/NZ/IE, weight 2.0)")
    pl = sub.add_parser("lint", help="Lint a draft abstract file or text string")
    pl.add_argument("file", help="Path to draft text file or literal text")
    pl.add_argument("--tier", default="T1", choices=["T1", "T2"])
    args = ap.parse_args()
    if args.cmd == "query": cmd_query(args)
    else: cmd_lint(args)

if __name__ == "__main__":
    main()
