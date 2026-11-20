#!/usr/bin/env python3
"""
Standalone Zero-Dependency AIGC, Non-Defensive & Native-Register Scientific Writing Auditor
Part of `low-aigc-nondefensive-writing` skill (v2.0).

Supports `.md`, `.txt`, `.tex`, and `.docx` (via standard-library zipfile + XML).
Subcommands:
  audit          AIGC Risk (0-100) + Defensiveness Risk (0-100) + burstiness & sentence flags
  vocab-upgrade  Detect non-native/formulaic low-register phrasing & recommend empirically
                 native-enriched (US/UK/CA/AU, 2.0x weight) T1/T2 Nature/Science upgrades
  native-lexicon Browse empirically ranked high-register verbs, collocations, overused clichés,
                 and verbatim native-primary T1/T2 grammar exemplars
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = Path(__file__).resolve().parent
REF_DIR = SCRIPT_DIR.parent / "references"
NATIVE_BANK_PATH = REF_DIR / "native_t1t2_vocab_grammar_bank.json"

AI_HYPE_WORDS = [
    "transformative", "groundbreaking", "pivotal", "pioneering", "unprecedented",
    "seamless", "seamlessly", "holistic", "compelling", "meticulous", "meticulously",
    "delve", "underscore", "underscores", "underscoring", "showcase", "showcasing",
    "elucidate", "orchestrate", "paradigm shift", "landscape", "cornerstone",
    "testament", "unlock", "unlocking", "revolutionize", "usher in", "intricate",
    "cutting-edge", "rapidly evolving", "garnered increasing attention",
    "lays the groundwork", "opens new avenues", "broad application prospects",
    "poised to transform", "at the heart of", "realm of", "utilize", "utilizing",
]

AI_BANNED_OPENERS = [
    "Thus,", "Hence,", "Yet,", "Notably,", "Importantly,", "Interestingly,",
    "Remarkably,", "Strikingly,", "Specifically,", "More specifically,",
    "In particular,", "Subsequently,", "Obviously,", "Clearly,", "Collectively,",
    "Overall,", "Looking ahead,", "Looking forward,", "Moving forward,", "As such,",
    "Taken together,",
]

PART_TAIL_RE = re.compile(
    r",\s+(?:enabling|allowing|providing|offering|achieving|demonstrating|"
    r"highlighting|underscoring|leading\s+to|resulting\s+in|paving|thereby|"
    r"making|showing|yielding|ensuring|facilitating)\b",
    re.I,
)
NOT_ONLY_RE = re.compile(r"\bnot\s+only\b.{1,100}\bbut\s+also\b", re.I)
COLON_REVEAL_RE = re.compile(r"\b(?:challenge|bottleneck|problem|limitation|advantage|feature|reason|secret|goal|key)\s*:\s+[a-z]", re.I)
WRAP_UP_RE = re.compile(r"(?:Taken\s+together|Collectively|Overall|In\s+summary),?\s+(?:these|our)\s+(?:results|findings|observations)\s+(?:demonstrate|underscore|highlight|confirm|validate)", re.I)

# Defensiveness patterns
NEG_POLICING_RE = re.compile(
    r"\b(?:does\s+not\s+constitute|do\s+not\s+claim|is\s+not\s+claimed\s+as|not\s+claimed\s+as|"
    r"should\s+not\s+be\s+(?:interpreted|viewed|construed|taken|mistaken)|"
    r"is\s+not\s+intended\s+(?:as|to\s+be)|cannot\s+be\s+considered\s+as|"
    r"we\s+do\s+not\s+intend\s+to\s+claim|not\s+a\s+full[- ]scale)\b",
    re.I,
)
WEASEL_DOUBLE_RE = re.compile(
    r"\b(?:may\s+potentially|could\s+possibly|might\s+potentially|might\s+tentatively|"
    r"may\s+tentatively|appears?\s+to\s+suggest|seems?\s+to\s+indicate|"
    r"to\s+some\s+extent|plausibly|arguably|somewhat\s+limits?|relatively\s+modest)\b",
    re.I,
)
APOLOGETIC_RE = re.compile(
    r"\b(?:admittedly|unfortunately,?\s+(?:our|the\s+current|this)|"
    r"(?:a\s+)?(?:major|serious|severe)\s+(?:weakness|drawback|flaw)\s+of\s+our|"
    r"only\s+a\s+(?:small|toy|preliminary|proof[- ]of[- ]concept)|"
    r"merely\s+a\s+(?:proof|proxy|preliminary|emulation)|"
    r"we\s+sincerely\s+apologize|we\s+regret\s+that|had\s+to\s+resort\s+to)\b",
    re.I,
)
CAVEAT_ECHO_RE = re.compile(
    r"\b(?:only\s+(?:an?\s+)?(?:emulation|proxy|simulation|optical\s+core)|not\s+end[- ]to[- ]end|"
    r"not\s+held[- ]out|not\s+full[- ]system|within[- ]session\s+only)\b",
    re.I,
)

# Concrete non-native / low-register upgrade rules grounded in Stage 1D (49 native_primary vs 51 non_native T1/T2 papers)
FALLBACK_UPGRADE_RULES = [
    ("suffer from", r"\bsuffer(?:s|ed|ing)?\s+from\b", "are limited by / are bound by / incur (native T1/T2 uses 'limited by' 2.0x and 'bound by' 2.5x more)", "limited by"),
    ("versatile", r"\bversatile\b", "name exact operating modes or tasks (non-native uses 'versatile' 2.7x more than US/UK T1/T2)", "viable"),
    ("dramatically", r"\bdramatically\b", "state the measured numerical factor, e.g. 'by 14x' or 'by two orders of magnitude' (non-native 1.9x more)", "orders of magnitude"),
    ("accordingly", r"\baccordingly\b", "use 'consequently', 'in turn', or direct causal phrasing (non-native 2.2x more)", "in turn"),
    ("to this end", r"\bto this end\b", "start directly with the mechanism or 'to address this bottleneck' (non-native 1.8x more)", "address"),
    ("in particular", r"\bin particular\b", "delete filler or name the specific physical case directly (non-native 1.8x more)", "given that"),
    ("specifically", r"\bspecifically\b", "usually deletable; state the quantitative condition directly (non-native 1.6x more)", "such that"),
    ("moreover / furthermore / besides", r"\b(?:moreover|furthermore|besides)\b", "vary with 'in addition', 'in turn', semicolon clause balance, or direct subject flow", "albeit"),
    ("meanwhile", r"\bmeanwhile\b", "replace with 'in parallel', 'whereas', or 'by contrast'", "whereas"),
    ("it is worth noting / notably", r"\bit is worth noting\b|\bnotably\b", "delete meta-signposting and lead with the physical result", "nonetheless"),
    ("play a vital/crucial/key role", r"\bplay(?:s|ed|ing)?\s+an?\s+(?:vital|crucial|important|key|pivotal)\s+role\b", "replace with a direct native verb: 'governs', 'dictates', 'limits', or 'accounts for'", "dictate"),
    ("empower", r"\bempower(?:s|ed|ing)?\b", "replace with 'enable', 'afford', 'support', or 'drive'", "afford"),
    ("pave the way", r"\bpav(?:e|es|ed|ing)\s+the\s+way\b", "state the concrete physical scaling route or next target", "in principle"),
    ("in recent years", r"\bin recent years\b", "delete throat-clearing; open directly with the physical bottleneck", "bound by"),
    ("great / immense potential", r"\b(?:great|immense|enormous|promising)\s+potential\b", "state the concrete projected figure or viable application scope", "viable"),
    ("tremendous / huge", r"\btremendous(?:ly)?\b|\bhuge\b", "quantify the exact scale or use 'orders of magnitude'", "orders of magnitude"),
    ("in order to", r"\bin order to\b", "tighten to plain 'to' in most technical clauses", "such that"),
    ("due to the fact that", r"\bdue to the fact that\b", "tighten to 'because' or 'given that'", "given that"),
    ("make use of", r"\bmak(?:e|es|ing)\s+use\s+of\b|\bmade\s+use\s+of\b", "replace with 'harness', 'exploit', or plain 'use'", "harness"),
    ("a lot of / lots of", r"\ba lot of\b|\blots of\b", "replace with 'numerous', 'substantial', or the exact count", "account for"),
]


def load_native_bank() -> dict:
    if NATIVE_BANK_PATH.exists():
        return json.loads(NATIVE_BANK_PATH.read_text(encoding="utf-8"))
    return {}


def read_input_text(path_or_text: str) -> str:
    if len(path_or_text) > 240 or "\n" in path_or_text:
        return path_or_text
    p = Path(path_or_text)
    try:
        if not p.exists():
            return path_or_text
    except OSError:
        return path_or_text
    if p.suffix.lower() == ".docx":
        with zipfile.ZipFile(p) as z:
            xml_bytes = z.read("word/document.xml")
        root = ET.fromstring(xml_bytes)
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        paras = []
        for para in root.findall(".//w:p", ns):
            texts = [t.text for t in para.findall(".//w:t", ns) if t.text]
            if texts:
                paras.append("".join(texts))
        return "\n\n".join(paras)
    return p.read_text(encoding="utf-8", errors="replace")


def split_sentences(text: str) -> list[str]:
    t = re.sub(r"\s+", " ", text).strip()
    for ab in ("Fig.", "Figs.", "et al.", "e.g.", "i.e.", "vs.", "Eq.", "Ref.", "Refs.", "s.d.", "s.e.m.", "a.u.", "No.", "Vol."):
        t = t.replace(ab, ab.replace(".", "<D>"))
    t = re.sub(r"(\d)\.(\d)", r"\1<D>\2", t)
    return [s.replace("<D>", ".").strip() for s in re.split(r"(?<=[\.\?\!])\s+(?=[A-Z0-9\(])", t) if len(s.split()) >= 4]


def audit_text(text: str, verbose: bool = False) -> dict:
    clean = re.sub(r"\s+", " ", text).strip()
    wc = max(1, len(clean.split()))
    sents = split_sentences(text)
    slens = [len(s.split()) for s in sents] or [20]
    mean_len = sum(slens) / len(slens)
    std_len = math.sqrt(sum((x - mean_len) ** 2 for x in slens) / len(slens))
    short15_pct = 100.0 * sum(1 for x in slens if x <= 15) / len(slens)

    max_mono_run = cur_run = 0
    for x in slens:
        if 17 <= x <= 26:
            cur_run += 1
            max_mono_run = max(max_mono_run, cur_run)
        else:
            cur_run = 0

    ai_hits = []
    for w in AI_HYPE_WORDS:
        cnt = len(re.findall(r"\b" + re.escape(w) + r"\b", clean, re.I))
        if cnt:
            ai_hits.append((w, cnt))
    ai_total = sum(c for _, c in ai_hits)
    ai_1k = 1000.0 * ai_total / wc

    opener_hits = []
    for op in AI_BANNED_OPENERS:
        cnt = len(re.findall(r"(?:^|[\.\!\?]\s+)" + re.escape(op), clean))
        if cnt:
            opener_hits.append((op, cnt))
    opener_total = sum(c for _, c in opener_hits)
    opener_1k = 1000.0 * opener_total / wc

    pt_cnt = len(PART_TAIL_RE.findall(clean))
    pt_1k = 1000.0 * pt_cnt / wc
    em_cnt = clean.count("\u2014")
    em_1k = 1000.0 * em_cnt / wc
    notonly_cnt = len(NOT_ONLY_RE.findall(clean))
    colon_cnt = len(COLON_REVEAL_RE.findall(clean))
    wrap_cnt = len(WRAP_UP_RE.findall(clean))

    neg_pol = NEG_POLICING_RE.findall(clean)
    weasel = WEASEL_DOUBLE_RE.findall(clean)
    apol = APOLOGETIC_RE.findall(clean)
    echoes = CAVEAT_ECHO_RE.findall(clean)

    aigc_score = 0.0
    if len(slens) >= 5 and std_len < 7.5:
        aigc_score += min(25.0, (7.5 - std_len) * 6.0)
    if max_mono_run >= 5:
        aigc_score += min(12.0, (max_mono_run - 4) * 3.0)
    aigc_score += min(25.0, max(0.0, pt_1k - 1.0) * 6.0)
    aigc_score += min(25.0, ai_1k * 8.0)
    aigc_score += min(15.0, opener_1k * 6.0)
    aigc_score += min(15.0, em_1k * 8.0 + notonly_cnt * 4.0 + colon_cnt * 3.0 + wrap_cnt * 5.0)
    aigc_score = round(min(100.0, aigc_score), 1)

    def_score = 0.0
    def_score += min(45.0, len(neg_pol) * 18.0)
    def_score += min(25.0, len(apol) * 14.0)
    def_score += min(20.0, len(weasel) * 8.0)
    if len(echoes) >= 2:
        def_score += min(20.0, (len(echoes) - 1) * 10.0)
    def_score = round(min(100.0, def_score), 1)

    flagged_sents = []
    for idx, s in enumerate(sents, 1):
        reasons = []
        if "\u2014" in s:
            reasons.append("em-dash")
        if PART_TAIL_RE.search(s):
            reasons.append("participial_tail")
        if NOT_ONLY_RE.search(s):
            reasons.append("not_only_but_also")
        if WRAP_UP_RE.search(s):
            reasons.append("ai_wrapup_tail")
        s_ai = [w for w in AI_HYPE_WORDS if re.search(r"\b" + re.escape(w) + r"\b", s, re.I)]
        if s_ai:
            reasons.append("ai_hype:" + ",".join(s_ai[:3]))
        s_op = [op for op in AI_BANNED_OPENERS if s.startswith(op)]
        if s_op:
            reasons.append("ai_opener:" + s_op[0])
        if NEG_POLICING_RE.search(s):
            reasons.append("DEFENSIVE:negative_policing")
        if APOLOGETIC_RE.search(s):
            reasons.append("DEFENSIVE:apologetic_self_deprecation")
        if WEASEL_DOUBLE_RE.search(s):
            reasons.append("DEFENSIVE:double_weasel_hedge")
        if reasons:
            flagged_sents.append({"sent_idx": idx, "words": len(s.split()), "reasons": reasons, "text": s[:220]})

    return {
        "word_count": wc,
        "sentence_count": len(sents),
        "aigc_risk_0to100": aigc_score,
        "defensiveness_risk_0to100": def_score,
        "burstiness": {
            "mean_words": round(mean_len, 1),
            "std_words": round(std_len, 1),
            "short_le15w_pct": round(short15_pct, 1),
            "max_monotonous_17_26w_run": max_mono_run,
        },
        "aigc_rates_per_1k": {
            "participial_tails_1k": round(pt_1k, 2),
            "ai_hype_1k": round(ai_1k, 2),
            "ai_openers_1k": round(opener_1k, 2),
            "em_dashes_1k": round(em_1k, 2),
            "not_only_count": notonly_cnt,
            "colon_reveals": colon_cnt,
            "wrap_up_cliches": wrap_cnt,
        },
        "defensive_counts": {
            "negative_policing": len(neg_pol),
            "apologetic_self_deprecation": len(apol),
            "double_weasel_hedges": len(weasel),
            "caveat_echoes": len(echoes),
        },
        "top_ai_words": sorted(ai_hits, key=lambda x: -x[1])[:8],
        "top_ai_openers": sorted(opener_hits, key=lambda x: -x[1])[:8],
        "flagged_sentences": flagged_sents,
    }


def build_native_example_lookup(bank: dict) -> dict:
    ex_map = {}
    for bucket in ("high_register_verbs", "high_register_collocations"):
        for item in bank.get(bucket, []):
            exs = item.get("verbatim_native_examples") or []
            if exs:
                ex_map[item["term"].lower()] = exs[0]
    return ex_map


def vocab_upgrade_analysis(text: str, bank: dict) -> dict:
    clean = re.sub(r"\s+", " ", text).strip()
    wc = max(1, len(clean.split()))
    ex_map = build_native_example_lookup(bank)

    hits = []
    for label, pat, fix, ref_term in FALLBACK_UPGRADE_RULES:
        found = re.findall(pat, clean, re.I)
        if found:
            ex = ex_map.get(ref_term.lower())
            hits.append({
                "pattern": label,
                "count": len(found),
                "upgrade_guidance": fix,
                "native_t1t2_exemplar": ex,
            })

    # Detect heavy verb/phrase repetition typical of non-native drafts
    rep_checks = [
        ("propose", r"\bpropos(?:e|es|ed|ing)\b", 2, "Vary 'propose' with 'introduce', 'present', 'demonstrate', 'formulate', or 'construct' (native T1/T2 uses 'propose' 1.7x less)"),
        ("achieve", r"\bachiev(?:e|es|ed|ing)\b", 2, "Vary 'achieve' with 'attain' (2.1x native lift), 'yield' (1.8x), 'reach', 'deliver', or 'sustain'"),
        ("realize", r"\brealiz(?:e|es|ed|ing)|realis(?:e|es|ed|ing)\b", 2, "Vary 'realize' with 'implement', 'execute', 'construct', 'instantiate', or 'attain'"),
        ("based on", r"\bbased on\b", 3, "Vary 'based on' with 'built from', 'driven by', 'using', 'via', or 'comprising'"),
    ]
    repetitions = []
    for lbl, pat, thr, tip in rep_checks:
        c = len(re.findall(pat, clean, re.I))
        # Flag if count >= thr AND rate > 6 per 1k words (or >= thr in short snippet <250w)
        if c >= thr and (wc < 250 or (1000.0 * c / wc) > 5.0):
            repetitions.append({"term": lbl, "count": c, "guidance": tip})

    # Count native high-register strengths already present
    native_strengths = []
    for bucket in ("high_register_verbs", "high_register_collocations"):
        for item in bank.get(bucket, []):
            if item.get("native_to_non_native_lift", 1.0) >= 1.35:
                pat = item.get("pattern")
                if pat and re.search(pat, clean, re.I):
                    native_strengths.append(item["term"])

    # Compute Native Register Readiness Score (0-100)
    penalty = sum(min(16, h["count"] * 7) for h in hits) + sum(min(10, r["count"] * 3) for r in repetitions)
    bonus = min(15, len(native_strengths) * 4)
    score = max(0, min(100, 90 - penalty + bonus))

    return {
        "word_count": wc,
        "native_register_score_0to100": score,
        "cliche_hits": hits,
        "repetition_alerts": repetitions,
        "native_strengths_present": sorted(set(native_strengths)),
    }


def cmd_vocab_upgrade(args):
    bank = load_native_bank()
    txt = read_input_text(args.target)
    res = vocab_upgrade_analysis(txt, bank)
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return
    sc = res["native_register_score_0to100"]
    lbl = "T1/T2 NATIVE-GRADE" if sc >= 85 else ("SOLID (MINOR POLISH)" if sc >= 68 else "NEEDS NATIVE REGISTER UPGRADE")
    print("=== Native-English-Country T1/T2 Vocabulary & Grammar Upgrade Audit ===")
    print("Basis: 49 US/UK/CA/AU native-primary (2.0x) vs 51 non-native T1/T2 research articles (586k words, 0 T3/T4)")
    print("Words: %d | Native Register Score: %d / 100 [%s]" % (res["word_count"], sc, lbl))
    if res["native_strengths_present"]:
        print("Native-enriched high-register terms already present: " + ", ".join(res["native_strengths_present"][:12]))
    if res["cliche_hits"]:
        print("\nLow-Register / Non-Native Overused Patterns Detected (%d):" % len(res["cliche_hits"]))
        for i, h in enumerate(res["cliche_hits"], 1):
            print("  %d. '%s' (%dx) -> %s" % (i, h["pattern"], h["count"], h["upgrade_guidance"]))
            ex = h.get("native_t1t2_exemplar")
            if ex:
                print("     Native %s (%s %s, %s): \"%s\"" % (ex.get("tier", ""), ex.get("journal", ""), ex.get("year", ""), ex.get("country", ""), ex.get("sentence", "")[:175]))
    if res["repetition_alerts"]:
        print("\nVerb / Preposition Repetition Alerts:")
        for r in res["repetition_alerts"]:
            print("  - '%s' repeated %dx -> %s" % (r["term"], r["count"], r["guidance"]))
    if not res["cliche_hits"] and not res["repetition_alerts"]:
        print("\nCLEAN: Zero non-native formulaic clichés or heavy verb repetition detected.")


def cmd_native_lexicon(args):
    bank = load_native_bank()
    if not bank:
        print("Native lexicon bank not found at %s" % NATIVE_BANK_PATH, file=sys.stderr)
        sys.exit(1)
    cat = args.category
    if args.json:
        if cat == "verbs":
            print(json.dumps(bank.get("high_register_verbs", [])[:args.top], indent=2, ensure_ascii=False))
        elif cat == "collocations":
            print(json.dumps(bank.get("high_register_collocations", [])[:args.top], indent=2, ensure_ascii=False))
        elif cat == "cliches":
            print(json.dumps(bank.get("overused_non_native_patterns", [])[:args.top], indent=2, ensure_ascii=False))
        else:
            print(json.dumps(bank.get("native_syntax_exemplars", {}), indent=2, ensure_ascii=False))
        return

    print("=== Empirical Native-Country T1/T2 High-Register Lexicon (49 US/UK/CA/AU vs 51 Non-Native Papers) ===")
    if cat == "verbs":
        for i, x in enumerate(bank.get("high_register_verbs", [])[:args.top], 1):
            print("%2d. %-14s | lift=%.2fx (nat=%.2f vs non=%.2f /10k) | %s" % (i, x["term"], x["native_to_non_native_lift"], x["native_per_10k"], x["non_native_per_10k"], x["guidance"]))
            if x.get("verbatim_native_examples"):
                ex = x["verbatim_native_examples"][0]
                print("    Ex [%s %s %s, %s]: %s" % (ex["tier"], ex["journal"], ex["year"], ex["country"], ex["sentence"][:165]))
    elif cat == "collocations":
        for i, x in enumerate(bank.get("high_register_collocations", [])[:args.top], 1):
            print("%2d. %-18s | lift=%.2fx (nat=%.2f vs non=%.2f /10k) | %s" % (i, x["term"], x["native_to_non_native_lift"], x["native_per_10k"], x["non_native_per_10k"], x["guidance"]))
            if x.get("verbatim_native_examples"):
                ex = x["verbatim_native_examples"][0]
                print("    Ex [%s %s %s, %s]: %s" % (ex["tier"], ex["journal"], ex["year"], ex["country"], ex["sentence"][:165]))
    elif cat == "cliches":
        for i, x in enumerate(bank.get("overused_non_native_patterns", [])[:args.top], 1):
            print("%2d. %-28s | nat/non=%.2fx | Fix: %s" % (i, x["term"], x["native_to_non_native_lift"], x["guidance"]))
    else:
        for k, exs in bank.get("native_syntax_exemplars", {}).items():
            print("\n--- Grammar Pattern: %s (%d verbatim native T1/T2 examples) ---" % (k, len(exs)))
            for ex in exs[:3]:
                print("  [%s | %s %s | %s] %s" % (ex["tier"], ex["journal"], ex["year"], ex.get("country", "US"), ex["sentence"]))


def main():
    ap = argparse.ArgumentParser(description="Low-AIGC, Non-Defensive & Native-Register Scientific Manuscript Auditor (v2.0)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("audit", help="Audit a .docx/.md/.txt/.tex file or literal text for AIGC & defensiveness")
    pa.add_argument("target", help="File path (.docx/.md/.txt/.tex) or quoted text")
    pa.add_argument("--verbose", action="store_true", help="Print all flagged sentences (default top 12)")
    pa.add_argument("--json", action="store_true", help="Output machine-readable JSON")

    pv = sub.add_parser("vocab-upgrade", help="Audit draft for non-native/low-register phrasing & suggest native T1/T2 upgrades")
    pv.add_argument("target", help="File path (.docx/.md/.txt/.tex) or quoted text")
    pv.add_argument("--json", action="store_true", help="Output JSON")

    pl = sub.add_parser("native-lexicon", help="Browse empirical native-country T1/T2 high-register vocabulary & grammar")
    pl.add_argument("--category", choices=["verbs", "collocations", "cliches", "syntax"], default="verbs")
    pl.add_argument("--top", type=int, default=15)
    pl.add_argument("--json", action="store_true", help="Output JSON")

    args = ap.parse_args()
    if args.cmd == "vocab-upgrade":
        cmd_vocab_upgrade(args)
        return
    if args.cmd == "native-lexicon":
        cmd_native_lexicon(args)
        return

    txt = read_input_text(args.target)
    res = audit_text(txt, verbose=args.verbose)
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return

    a_stat = "PASS" if res["aigc_risk_0to100"] < 20 else ("WARN" if res["aigc_risk_0to100"] < 40 else "HIGH RISK")
    d_stat = "PASS" if res["defensiveness_risk_0to100"] < 15 else ("WARN" if res["defensiveness_risk_0to100"] < 35 else "HIGH RISK")
    print("=== Low-AIGC & Non-Defensive Scientific Writing Audit ===")
    print(f"Words: {res['word_count']} | Sentences: {res['sentence_count']}")
    print(f"AIGC Risk Score:          {res['aigc_risk_0to100']:5.1f} / 100 [{a_stat}]  (Pre-LLM T1/T2 target <20)")
    print(f"Defensiveness Risk Score: {res['defensiveness_risk_0to100']:5.1f} / 100 [{d_stat}]  (Pre-LLM T1/T2 target <15)")
    b = res["burstiness"]
    print(f"Burstiness: mean={b['mean_words']}w, std={b['std_words']}w (human T1/T2 ~12w, target >=9w), <=15w={b['short_le15w_pct']}%, max_uniform_run={b['max_monotonous_17_26w_run']}")
    r = res["aigc_rates_per_1k"]
    print(f"AIGC Signals (/1k): participial_tails={r['participial_tails_1k']} (target <=1.2) | ai_hype={r['ai_hype_1k']} (0.0) | ai_openers={r['ai_openers_1k']} (0.0) | em_dashes={r['em_dashes_1k']} (0.0) | not_only={r['not_only_count']} | wrapups={r['wrap_up_cliches']}")
    dc = res["defensive_counts"]
    print(f"Defensive Signals:  negative_policing={dc['negative_policing']} | apologetic={dc['apologetic_self_deprecation']} | double_weasel={dc['double_weasel_hedges']} | caveat_echoes={dc['caveat_echoes']}")
    if res["top_ai_words"]:
        print("Top AI words:", ", ".join(f"{w}({c})" for w, c in res["top_ai_words"]))
    if res["top_ai_openers"]:
        print("Top banned openers:", ", ".join(f"{w}({c})" for w, c in res["top_ai_openers"]))
    flagged = res["flagged_sentences"]
    if flagged:
        limit = len(flagged) if args.verbose else min(12, len(flagged))
        print(f"\nFlagged sentences ({len(flagged)} total, showing {limit}):")
        for f in flagged[:limit]:
            print(f"  [S{f['sent_idx']} | {f['words']}w | {', '.join(f['reasons'])}] {f['text']}")
    else:
        print("\nCLEAN: Zero AIGC or defensive self-policing sentences flagged.")


if __name__ == "__main__":
    main()
