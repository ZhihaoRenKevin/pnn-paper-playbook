#!/usr/bin/env python3
"""
Scientific Technology Naming & Short-Form CLI (`sci-tech-naming`).
Zero third-party dependencies (Python 3.9+ standard library only).

Strict Tier Architecture:
- Naming craft exemplars & reveal norms: STRICTLY T1 & T2 ONLY (113 Research Articles, 31 verified exemplars)
- Taken-acronym & prior-art collision check: ALL TIERS T1-T4 (6,490 published papers across 7 photonics/PNN catalogs + AI/quantum/hardware brands)

Subcommands:
  exemplars   List verbatim-verified T1/T2 named technology exemplars & reveal stats
  check       Run exact, phonetic, and Levenshtein-1 collision check across 6,490 papers
  score       Compute 100-point scientific naming scorecard (pronounceability, linkage, uniqueness, conciseness, claim-safety, hygiene)
  generate    Combinatorially generate, collision-filter, and rank pronounceable feature-linked names across 4 archetypes
  audit-draft Audit a manuscript draft for T1/T2 naming hygiene (colon-free title, abstract reveal, consistent spelling, zero mixed aliases)
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REF_DIR = SKILL_DIR / "references"
EXEMPLARS_PATH = REF_DIR / "t1t2_verified_exemplars.jsonl"
TAKEN_PATH = REF_DIR / "all_tier_taken_acronyms.json"

VOWELS = set("aeiouy")

VALID_ONSETS_2 = {
    "bl", "br", "ch", "cl", "cr", "dr", "fl", "fr", "gl", "gr",
    "kl", "kr", "ph", "pl", "pr", "qu", "sc", "sh", "sk",
    "sl", "sm", "sn", "sp", "st", "sw", "th", "tr", "tw", "wh",
}
VALID_ONSETS_3 = {"str", "spr", "spl", "scr", "shr", "thr", "sch", "sph", "phr", "chr"}
VALID_CODAS_2 = {
    "ch", "ck", "ct", "ft", "gh", "lb", "ld", "lf", "lk", "lm", "ln", "lp",
    "lt", "mp", "nc", "nd", "ng", "nk", "ns", "nt", "nx", "ph", "pt", "rb",
    "rc", "rd", "rf", "rg", "rk", "rl", "rm", "rn", "rp", "rs", "rt", "sh",
    "sk", "sp", "st", "th", "wn", "xt",
}

CLAIM_TRAP_PATTERNS = [
    (r"\ball[- ]optical\b", "Avoid 'All-Optical' in the permanent name unless weights, activation, and control use zero electronics (C12 trap)"),
    (r"\bdeep\b", "Avoid 'Deep' in the name unless hardware physically cascades >=3 nonlinear layers (C5/C12 trap)"),
    (r"\buniversal\b", "Avoid 'Universal' in the name unless proven across diverse model families (C12 trap)"),
    (r"\bgeneral\b|\bagi\b", "Avoid 'General' or 'AGI' in the technology name unless broad multi-task generalization is experimentally proven"),
    (r"\bbrain[- ]?like\b|\bsuperhuman\b", "Avoid hype metaphors like 'Brain-like' or 'Superhuman' in formal technology names"),
    (r"\bultimate\b|\bperfect\b|\brevolutionary\b|\bnovel\b|\bfirst\b", "Avoid subjective or priority-claim adjectives ('Ultimate', 'Perfect', 'Novel', 'First') inside a technology name"),
    (r"\bzero[- ]loss\b|\blossless\b|\bsupremacy\b", "Avoid absolute physical claims ('Zero-loss', 'Supremacy') inside a technology name"),
]

OVERUSED_GENERIC = {
    "APEX", "NOVA", "HYPER", "OMNI", "ULTRA", "SMART", "FLEX", "FAST", "META",
    "PRIME", "CORE", "CHIP", "SYNC", "WAVE", "PULSE", "FLUX", "SPARK", "LIGHT",
    "OPTIC", "PHOTON", "NANO", "MICRO", "SUPER", "TURBO", "MEGA", "GIGA",
}

# Curated crisp 1-2 syllable positive scientific/engineering anchor words for semantic backronym matching
BACKRONYM_ANCHORS = [
    ("PACE", "speed and low latency"),
    ("SOLO", "single-layer or standalone simplicity"),
    ("PRISM", "spectral separation and optical routing"),
    ("SCOPE", "broadband sensing or observation"),
    ("PHASE", "coherent phase engineering"),
    ("PULSE", "ultrafast pulsed operation"),
    ("SLIM", "compact on-chip footprint"),
    ("CLAD", "waveguide cladding and planar integration"),
    ("SLOT", "subwavelength slot waveguide physics"),
    ("SLAB", "planar slab diffraction"),
    ("GRID", "dense photonic array"),
    ("CAST", "optical broadcasting or projection"),
    ("FLOW", "continuous optical signal flow"),
    ("TUNE", "programmable tuning"),
    ("LOCK", "phase or resonance locking"),
    ("LINK", "photonic interconnectivity"),
    ("NODE", "networked computing node"),
    ("MESH", "interferometric waveguide mesh"),
    ("SPAN", "broadband or multi-octave span"),
    ("GAIN", "optical gain or efficiency boost"),
    ("EDGE", "edge AI computing"),
    ("SCAN", "rapid beam or spectral scanning"),
    ("SIFT", "spectral filtering or feature extraction"),
    ("SPEC", "spectroscopic precision"),
    ("LENS", "diffractive focusing"),
    ("BEAM", "guided optical beam"),
    ("SNAP", "fast switching or one-shot capture"),
    ("STEP", "discrete phase stepping"),
    ("SPIRE", "upward scaling"),
    ("GLIDE", "low-loss propagation"),
    ("SLIDE", "continuous phase shifting"),
    ("SHIFT", "frequency or phase conversion"),
    ("DRIFT", "controlled tuning (caution: also thermal drift)"),
    ("SPLIT", "beam splitting or multiplexing"),
    ("SWEEP", "wideband spectral sweep"),
    ("STEER", "beam steering"),
    ("SCALE", "scalable chip architecture"),
    ("SHARP", "high-Q sharp resonance"),
    ("SWIFT", "high-speed modulation"),
    ("CLEAR", "low-loss transparent window"),
    ("PIVOT", "reconfigurable switching"),
    ("CREST", "peak resonance efficiency"),
    ("SORA", "clean 2-syllable open sound"),
    ("MIRA", "mirror / optical clarity (2-syllable)"),
    ("VERA", "high-fidelity accuracy (2-syllable)"),
    ("LIMA", "light / line matrix (2-syllable)"),
    ("CALM", "low-noise stable operation"),
    ("SILO", "silicon + slot / localized optics"),
    ("SOLA", "slot / optical array (2-syllable)"),
    ("POLA", "polarization / programmable optical array"),
    ("MODA", "modular optical diffractive array"),
    ("CODA", "coherent optical diffractive architecture"),
    ("DIFO", "diffractive optical unit"),
    ("LOTA", "low-loss optical tunable array"),
    ("ROTA", "reconfigurable optical tunable array"),
    ("PODA", "programmable optical diffractive array"),
    ("SODA", "silicon optical diffractive array"),
    ("BIMO", "bilayer integrated modulator"),
    ("DUMO", "dual-mode modulator"),
    ("SICO", "silicon carbide optical platform"),
    ("PICO", "photonic integrated computing operator"),
    ("SIPO", "silicon photonic operator"),
    ("DIRO", "diffractive integrated routing operator"),
    ("PLANA", "planar integrated photonics"),
    ("SPECTRA", "multi-wavelength spectral processing"),
    ("PHOTIX", "photonic matrix processing"),
    ("DIFFRA", "diffractive photonic engine"),
    ("SLOTA", "slot-array photonic architecture"),
    ("LATTICE", "periodic photonic array"),
    ("NEXUS", "multi-port photonic interconnect"),
    ("AURA", "optical field halo"),
    ("HALO", "ring / circular resonator"),
    ("VIVO", "live in-situ real-time adaptation"),
    ("ORBIT", "ring resonator circulation"),
    ("RINGO", "microring optical engine"),
    ("TENSOR", "tensorized photonic compute"),
    ("VECTOR", "vector-matrix multiplication"),
    ("QUANTA", "quantum photonic interface"),
    ("BRAGG", "Bragg-scattering / grating physics"),
    ("KERR", "chi(3) Kerr nonlinear photonics"),
    ("POCKEL", "linear electro-optic Pockels effect"),
]

# Semantic root map for intelligent Portmanteau & Compound generation
FEATURE_ROOT_MAP = {
    "diffractive": ["Diff", "Slab", "Wave"],
    "diffraction": ["Diff", "Slab", "Wave"],
    "programmable": ["Pro", "Tune", "Re", "Flex"],
    "reconfigurable": ["Re", "Tune", "Flex", "Swap"],
    "tunable": ["Tune", "Shift", "Flex"],
    "slot": ["Slot", "Slit"],
    "metaline": ["Meta", "Line"],
    "metasurface": ["Meta", "Surf"],
    "silicon": ["Si", "Sili", "Planar"],
    "soi": ["Si", "Sili"],
    "photonic": ["Pho", "Phot", "Opto", "Light"],
    "optical": ["Opt", "Opto", "Light"],
    "on-chip": ["Chip", "Slab", "Planar"],
    "integrated": ["Int", "Chip", "Mono"],
    "chip": ["Chip", "Core", "Slab"],
    "processor": ["Core", "Proc", "Engine", "Unit"],
    "accelerator": ["Boost", "Drive", "Core"],
    "computing": ["Comp", "Core", "Logic"],
    "neural": ["Neuro", "Net", "Syn"],
    "network": ["Net", "Mesh", "Web"],
    "microring": ["Ring", "Halo", "Loop"],
    "ring": ["Ring", "Halo", "Loop"],
    "resonator": ["Res", "Ring", "Cav"],
    "bilayer": ["Bi", "Dual", "Twin"],
    "dual": ["Dual", "Bi", "Twin"],
    "electro-optic": ["Volt", "Pock", "EO"],
    "pockels": ["Pock", "Volt", "Lin"],
    "thermo-optic": ["Therm", "Heat", "TO"],
    "heater": ["Therm", "Heat"],
    "modulator": ["Mod", "Tune", "Gate"],
    "modulation": ["Mod", "Tune"],
    "phase-change": ["Phase", "Latch", "Memo"],
    "non-volatile": ["Latch", "Memo", "Hold"],
    "nonvolatile": ["Latch", "Memo", "Hold"],
    "memory": ["Memo", "Store", "Ram"],
    "in-memory": ["Memo", "Store"],
    "mid-ir": ["Mir", "Mid"],
    "mid-infrared": ["Mir", "Mid"],
    "infrared": ["Mir", "Infra"],
    "sensing": ["Sense", "Spec", "Scan"],
    "sensor": ["Sense", "Spec", "Scan"],
    "gas": ["Gas", "Spec"],
    "quantum": ["Quant", "Q"],
    "frequency": ["Freq", "Band", "Shift"],
    "conversion": ["Shift", "Cast", "Bridge"],
    "converter": ["Shift", "Cast", "Bridge"],
    "bragg": ["Bragg", "Mix", "Shift"],
    "four-wave": ["Mix", "Kerr", "Quad"],
    "kerr": ["Kerr", "Mix"],
    "sic": ["Carb", "SiC"],
    "carbide": ["Carb", "SiC"],
    "scaln": ["Scan", "Nit", "ScAlN"],
    "aln": ["Nit", "AlN"],
    "niobate": ["Lino", "Pock"],
    "nonlinear": ["Kerr", "Spark", "Act"],
    "activation": ["Act", "Fire", "Gate"],
    "training": ["Train", "Grad", "Learn"],
    "in-situ": ["Live", "Situ", "Self"],
    "forward": ["Fwd", "Pass"],
    "coherent": ["Coh", "Sync", "Phase"],
    "broadband": ["Wide", "Span", "Band"],
    "spectral": ["Spec", "Band", "Prism"],
    "wavelength": ["Wave", "Band", "Spec"],
    "multiplexing": ["Mux", "Multi", "Band"],
    "wdm": ["Band", "Mux", "Spec"],
    "parallel": ["Para", "Multi", "Grid"],
    "compact": ["Mini", "Slim", "Micro"],
    "low-power": ["Eco", "Lean", "Pico"],
    "ultralow": ["Lean", "Pico", "Slim"],
    "high-speed": ["Swift", "Fast", "Pulse"],
    "bayesian": ["Bayes", "Prob", "Stoch"],
    "generative": ["Gen", "Synth"],
    "edge": ["Edge", "Node"],
    "audio": ["Vox", "Sonic", "Wave"],
    "vision": ["Vis", "Opti", "Eye"],
    "imaging": ["Vis", "Lens", "View"],
    "array": ["Grid", "Array", "Line"],
    "waveguide": ["Guide", "Slab", "Line"],
    "interferometer": ["Mesh", "Inter", "Phase"],
}

MODALITY_SUFFIXES = {
    "processor": ["Core", "PU", "Unit", "Chip", "Engine"],
    "chip": ["Chip", "Core", "PU"],
    "modulator": ["Mod", "Gate", "Tune", "Switch"],
    "network": ["Net", "Mesh", "Core"],
    "method": ["Flow", "Learn", "Pass", "Grad"],
    "platform": ["Lab", "Hub", "Base", "Line"],
    "sensor": ["Sense", "Spec", "Scan", "Scope"],
    "converter": ["Shift", "Bridge", "Cast", "Link"],
    "engine": ["Core", "Engine", "Drive"],
    "core": ["Core", "Unit", "PU"],
    "unit": ["Unit", "PU", "Core"],
}


def safe_read_text(arg: str) -> str:
    """Safely read text from either a file path or a literal string without Errno 63."""
    if not arg:
        return ""
    if "\n" not in arg and len(arg) < 240:
        p = Path(arg)
        try:
            if p.exists() and p.is_file():
                return p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            pass
    return arg


def load_exemplars() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if EXEMPLARS_PATH.exists():
        with open(EXEMPLARS_PATH, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
    return rows


def load_taken_bank() -> Dict[str, Any]:
    if TAKEN_PATH.exists():
        with open(TAKEN_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def split_morphemes(name: str) -> List[str]:
    """Split CamelCase, hyphenated, or known 2-root compounds into readable morphemes."""
    # First split by hyphen/space/underscore
    parts = [p for p in re.split(r"[\-\s_]+", name) if p]
    out: List[str] = []
    for p in parts:
        # Split CamelCase: LightGen -> Light, Gen; oRAM -> o, RAM
        if any(c.islower() for c in p) and any(c.isupper() for c in p):
            sub = re.findall(r"[A-Z]+(?=[A-Z][a-z]|\b)|[A-Z]?[a-z]+|[0-9]+", p)
            out.extend(sub if sub else [p])
        else:
            out.append(p)
    # Also detect glued 2-root compounds in TitleCase/lowercase like Netcast -> Net + cast
    known_tails = (
        "cast", "core", "chip", "flow", "gate", "gen", "grid", "line", "link",
        "lock", "mesh", "mod", "net", "node", "opt", "pass", "phot", "proc",
        "ring", "scan", "sense", "shift", "slab", "slot", "span", "spec",
        "steer", "surf", "sync", "tune", "unit", "wave", "ram", "pu", "tu",
    )
    refined: List[str] = []
    for tok in out:
        low = tok.lower()
        split_done = False
        if len(low) >= 6 and low.isalpha():
            for tail in known_tails:
                if low.endswith(tail) and len(low) - len(tail) >= 3:
                    head = low[:-len(tail)]
                    if any(c in VOWELS for c in head):
                        refined.append(tok[:-len(tail)])
                        refined.append(tok[-len(tail):])
                        split_done = True
                        break
        if not split_done:
            refined.append(tok)
    return refined


def cluster_is_valid_english_boundary(cluster: str, pos: str) -> bool:
    """Check whether a consonant cluster is smoothly pronounceable in English."""
    c = cluster.lower()
    if len(c) <= 1:
        return True
    if pos == "onset":
        if len(c) == 2:
            return c in VALID_ONSETS_2
        if len(c) == 3:
            return c in VALID_ONSETS_3
        return False
    if pos == "coda":
        if len(c) == 2:
            return c in VALID_CODAS_2 or (c[0] == c[1] and c[0] in "lsmfnpzrt")
        if len(c) == 3:
            return c in {"tch", "dge", "ght", "nch", "nth", "rth", "lth", "rst", "nst", "mpt", "nct", "lts", "nds", "nts", "cks", "ngs"}
        return False
    # Medial cluster: valid if splittable into (valid coda) + (valid onset)
    if len(c) == 2:
        # Almost any C1 + C2 across a syllable boundary works unless identical harsh stop or impossible pair
        if c in VALID_ONSETS_2 or c in VALID_CODAS_2:
            return True
        if c[0] == c[1] and c[0] in "lmnrstcpbdfgkz":
            return True
        # Common cross-syllable pairs (e.g. n+p, r+m, l+v, m+b, c+t, t+m, p+t, k+s, d+l)
        return c[0] in "lmnrscptkdfbgvz" and c[1] in "lmnrscptkdfbgvwzhy"
    if len(c) == 3:
        for i in (1, 2):
            left, right = c[:i], c[i:]
            left_ok = (len(left) == 1) or (left in VALID_CODAS_2)
            right_ok = (len(right) == 1) or (right in VALID_ONSETS_2)
            if left_ok and right_ok:
                return True
        return False
    if len(c) == 4:
        for i in (1, 2):
            left, right = c[:i], c[i:]
            left_ok = (len(left) == 1) or (left in VALID_CODAS_2)
            right_ok = (len(right) == 2 and right in VALID_ONSETS_2) or (len(right) == 3 and right in VALID_ONSETS_3)
            if left_ok and right_ok:
                return True
        return False
    return False


def analyze_phonotactics(name: str) -> Dict[str, Any]:
    """Evaluate pronounceability, syllable count, and spoken ergonomics of a short name."""
    morphemes = split_morphemes(name)
    alpha_only = re.sub(r"[^A-Za-z]", "", name)
    digits = re.findall(r"[0-9]", name)
    if not alpha_only:
        return {
            "pronounceable_as_word": False,
            "is_crisp_3_initialism": False,
            "spoken_syllables": len(name),
            "vowel_ratio": 0.0,
            "max_consonant_cluster": len(name),
            "morphemes": morphemes,
            "speech_label": "invalid",
            "issues": ["Name contains no letters"],
            "score_30": 0,
        }

    issues: List[str] = []
    all_morphemes_pron = True
    total_word_syl = 0
    worst_cc = 0

    for m in morphemes:
        ml = re.sub(r"[^a-z]", "", m.lower())
        if not ml:
            continue
        v_cnt = sum(1 for ch in ml if ch in VOWELS)
        # Check consonant runs inside this morpheme
        runs = list(re.finditer(r"[^aeiouy]+", ml))
        m_pron = v_cnt > 0
        for run in runs:
            cl = run.group(0)
            if len(cl) > worst_cc:
                worst_cc = len(cl)
            pos = "onset" if run.start() == 0 else ("coda" if run.end() == len(ml) else "medial")
            if not cluster_is_valid_english_boundary(cl, pos):
                m_pron = False
        if len(ml) == 1 and ml not in ("a", "i", "o"):
            m_pron = False
        if not m_pron:
            all_morphemes_pron = False
        # Syllable estimate for this morpheme
        if m_pron:
            vg = re.findall(r"[aeiouy]+", ml)
            s = len(vg)
            if ml.endswith("e") and s > 1 and not ml.endswith("le") and len(ml) > 3:
                s -= 1
            total_word_syl += max(1, s)
        else:
            total_word_syl += len(ml)

    # Special case: 2-letter ALL-CAPS token like "PU" or "TU" at end of compound is spelled out (2 syl)
    # Full short name check
    is_all_caps = name.isupper() and len(alpha_only) == len(name)
    is_crisp_3_init = is_all_caps and len(alpha_only) == 3 and not all_morphemes_pron and len(digits) == 0
    # Even if 3-letter ALL-CAPS has a vowel like AOC, OPO, QRC, check whether people say it as letters
    if is_all_caps and len(alpha_only) == 3 and alpha_only.lower() in {"aoc", "opo", "ffm", "dpu", "dtu", "ptc", "qrc", "mdr", "oem"}:
        is_crisp_3_init = True

    pron_as_word = all_morphemes_pron and len(alpha_only) >= 3 and len(digits) == 0
    # Check vowel ratio across full name
    v_total = sum(1 for ch in alpha_only.lower() if ch in VOWELS)
    v_ratio = round(v_total / max(1, len(alpha_only)), 3)
    if v_ratio < 0.22 and pron_as_word:
        pron_as_word = False

    if pron_as_word:
        spoken_syl = total_word_syl
        speech_label = "word (~%d syl, smooth)" % spoken_syl
    elif is_crisp_3_init:
        spoken_syl = 3
        speech_label = "3-letter initialism (%s, 3 syl)" % "-".join(alpha_only)
    else:
        # Spelled out letter-by-letter + digits
        spoken_syl = len(alpha_only) + len(digits)
        if "W" in alpha_only.upper():
            spoken_syl += 2  # 'double-u' adds 2 syllables!
        speech_label = "spelled-out (%d syl)" % spoken_syl

    # Compute 0-30 pronounceability score
    score = 0
    if pron_as_word:
        score = 26
        if spoken_syl in (1, 2):
            score += 4
        elif spoken_syl == 3:
            score += 1
        else:
            score -= 5
            issues.append("Too many syllables (%d); tighten to 1-2 syllables for talk impact" % spoken_syl)
        if not (0.28 <= v_ratio <= 0.62):
            score -= 2
            issues.append("Vowel ratio (%.2f) is slightly off ideal 0.28-0.62 range" % v_ratio)
    elif is_crisp_3_init:
        score = 22
        if len(set(alpha_only)) < 3:
            score -= 2
            issues.append("Repeated letter inside 3-letter initialism reduces spoken distinction")
    else:
        # Spelled-out initialism or alphanumeric
        if spoken_syl <= 3:
            score = 19
        elif spoken_syl == 4:
            score = 13
            issues.append("4-syllable spelled-out initialism; hard to remember compared to a 1-2 syllable pronounceable name")
        else:
            score = max(2, 14 - 3 * (spoken_syl - 3))
            issues.append("Tongue-twister (%d spoken syllables); replace with a 1-2 syllable pronounceable backronym or portmanteau" % spoken_syl)

    # Penalize stuttering repeated consonants (DD, NN, MM) in ALL-CAPS non-word initialisms
    if not pron_as_word and re.search(r"([BCDFGHJKLMNPQRSTVWXZ])\1", alpha_only.upper()):
        score -= 4
        issues.append("Repeated consonant stutter (e.g., DD/MM/NN) makes spoken delivery awkward")

    if worst_cc >= 4 and not pron_as_word:
        score -= 3
        issues.append("Heavy consonant cluster (max run = %d) blocks word pronunciation" % worst_cc)

    score = max(0, min(30, score))
    return {
        "pronounceable_as_word": pron_as_word,
        "is_crisp_3_initialism": is_crisp_3_init,
        "spoken_syllables": spoken_syl,
        "vowel_ratio": v_ratio,
        "max_consonant_cluster": worst_cc,
        "morphemes": morphemes,
        "speech_label": speech_label,
        "issues": issues,
        "score_30": score,
    }


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            ins = curr[j - 1] + 1
            dele = prev[j] + 1
            sub = prev[j - 1] + (0 if ca == cb else 1)
            curr.append(min(ins, dele, sub))
        prev = curr
    return prev[-1]


def phonetic_skeleton(s: str) -> str:
    """Collapse repeated letters & common phonetic equivalents to catch spoken lookalikes."""
    u = re.sub(r"[^A-Z0-9]", "", s.upper())
    u = u.replace("PH", "F").replace("CK", "K").replace("QU", "KW")
    u = u.replace("2", "D")  # D2NN ~ DDNN
    # Collapse consecutive duplicates: OMDNN -> PDN
    out = []
    for ch in u:
        if not out or out[-1] != ch:
            out.append(ch)
    return "".join(out)


def check_collision(short: str, taken_bank: Dict[str, Any]) -> Dict[str, Any]:
    """Run exact, normalized, phonetic, and Levenshtein-1 collision check across all 6,490 papers."""
    cand_u = short.strip().upper()
    cand_alnum = re.sub(r"[^A-Z0-9]", "", cand_u)
    cand_skel = phonetic_skeleton(cand_u)

    exact_hits: List[Dict[str, Any]] = []
    near_hits: List[Dict[str, Any]] = []

    for k, info in taken_bank.items():
        k_alnum = re.sub(r"[^A-Z0-9]", "", k)
        if k == cand_u or (cand_alnum and k_alnum == cand_alnum):
            exact_hits.append({"key": info.get("short", k), "count": info.get("count", 1), "domains": info.get("domains", []), "examples": info.get("examples", [])})
            continue
        if len(cand_alnum) >= 3 and len(k_alnum) >= 3:
            dist = levenshtein(cand_alnum, k_alnum)
            same_skel = (len(cand_skel) >= 3 and phonetic_skeleton(k) == cand_skel)
            if dist == 1 or same_skel:
                # Filter noisy single-letter differences on common short words unless strong photonics landmark
                doms = info.get("domains", [])
                is_landmark = any("Landmark" in d or "Internal" in d or "PNN" in d or "Standard" in d for d in doms)
                if same_skel or is_landmark or info.get("count", 0) >= 3:
                    near_hits.append({
                        "key": info.get("short", k),
                        "reason": "phonetic-lookalike" if same_skel else "edit-dist-1",
                        "count": info.get("count", 1),
                        "domains": doms,
                        "examples": info.get("examples", [])[:1],
                    })

    near_hits.sort(key=lambda x: (-int(x["reason"] == "phonetic-lookalike"), -x["count"], x["key"]))
    is_overused = cand_alnum in OVERUSED_GENERIC

    if exact_hits:
        doms = exact_hits[0]["domains"]
        if any("Landmark" in d or "PNN_" in d or "SiC_" in d or "ScAlN_" in d or "LN_" in d or "PCM_" in d or "Quantum_" in d or "PIC_" in d for d in doms):
            status = "HARD_COLLISION"
            score_20 = 0
        else:
            status = "DOMAIN_COLLISION"
            score_20 = 4
    elif is_overused:
        status = "OVERUSED_GENERIC"
        score_20 = 8
    elif near_hits:
        # Check if phonetic-lookalike with a major landmark (e.g. OMDNN <-> PDNN / D2NN)
        strong_near = [h for h in near_hits if h["reason"] == "phonetic-lookalike" or any("Landmark" in d or "PNN_T1" in d for d in h["domains"])]
        if strong_near:
            status = "NEAR_COLLISION_HIGH"
            score_20 = 10
        else:
            status = "NEAR_COLLISION_MILD"
            score_20 = 16
    else:
        status = "CLEAR"
        score_20 = 20

    return {
        "candidate": short,
        "status": status,
        "score_20": score_20,
        "is_overused_generic": is_overused,
        "exact_hits": exact_hits[:5],
        "near_hits": near_hits[:6],
    }


def compute_feature_linkage(short: str, full: str, features: List[str]) -> Dict[str, Any]:
    """Score 0-25 for how transparently the short form & full name encode the core technical features."""
    if not features:
        return {"score_25": 15, "matched_in_short": [], "matched_in_full": [], "mapping": "No --features supplied (neutral 15/25)"}

    clean_feats = [f.strip().lower() for f in features if f.strip()]
    short_low = re.sub(r"[^a-z]", "", short.lower())
    full_low = (full or "").lower()

    # Check direct morpheme/stem match inside short form
    matched_short: List[str] = []
    letter_hits: List[str] = []
    used_pos = -1

    for feat in clean_feats:
        words = [w for w in re.split(r"[\s\-/]+", feat) if len(w) >= 2]
        roots = set()
        # Check whole compound phrase first (e.g., 'on-chip', 'phase-change', 'electro-optic')
        if feat in FEATURE_ROOT_MAP:
            for rv in FEATURE_ROOT_MAP[feat]:
                roots.add(rv.lower())
        for w in words:
            if w in ("on", "in", "to", "of", "by", "for", "and", "the"):
                continue
            roots.add(w[:4] if len(w) >= 4 else w)
            roots.add(w[:3] if len(w) >= 3 else w)
            for rk, rvals in FEATURE_ROOT_MAP.items():
                if rk == w or (len(w) >= 4 and len(rk) >= 4 and (rk in w or w in rk)):
                    for rv in rvals:
                        roots.add(rv.lower())
        # Check if any 3+ char root appears directly in short_low
        root_hit = next((rt for rt in sorted(roots, key=len, reverse=True) if len(rt) >= 3 and rt in short_low), None)
        if root_hit:
            matched_short.append(feat + " (root '" + root_hit + "')")
            continue
        # Otherwise check sequential initial-letter anchor inside short_low
        for w in words:
            ch = w[0]
            idx = short_low.find(ch, used_pos + 1)
            if idx != -1:
                used_pos = idx
                letter_hits.append(ch.upper() + "<-" + w)
                matched_short.append(feat + " (letter '" + ch.upper() + "')")
                break
            elif ch in short_low:
                letter_hits.append(ch.upper() + "<-" + w)
                matched_short.append(feat + " (letter '" + ch.upper() + "')")
                break

    # Check full-name coverage of features
    matched_full: List[str] = []
    for feat in clean_feats:
        words = [w for w in re.split(r"[\s\-/]+", feat) if len(w) >= 2]
        if any((w[:4] if len(w) >= 4 else w) in full_low for w in words):
            matched_full.append(feat)

    # Check if every letter of short (when backronym/initialism) maps cleanly into full name words
    full_words = re.findall(r"[A-Za-z]+", full or "")
    full_initials = "".join(w[0].lower() for w in full_words)
    seq_in_full = 0
    pos = -1
    for ch in short_low:
        nxt = full_low.find(ch, pos + 1)
        if nxt != -1:
            pos = nxt
            seq_in_full += 1
    full_subseq_ratio = seq_in_full / max(1, len(short_low)) if full_words else 0.0

    n_f = max(1, len(clean_feats))
    short_cov = min(1.0, len(matched_short) / min(n_f, 4))
    full_cov = min(1.0, len(matched_full) / min(n_f, 4)) if full_words else 0.6

    # Bonus for semantic root match (not just 1-letter initial)
    n_root_matches = sum(1 for x in matched_short if "(root '" in x)
    root_bonus = min(4.0, 2.0 * n_root_matches)

    raw = 11.0 * short_cov + 7.0 * full_cov + 3.0 * full_subseq_ratio + root_bonus
    score = max(0, min(25, int(round(raw))))
    return {
        "score_25": score,
        "matched_in_short": matched_short,
        "matched_in_full": matched_full,
        "full_subseq_ratio": round(full_subseq_ratio, 2),
    }


def score_candidate(short: str, full: str, features: List[str], taken_bank: Dict[str, Any]) -> Dict[str, Any]:
    """Compute the complete 100-point Scientific Technology Name Scorecard."""
    phon = analyze_phonotactics(short)
    coll = check_collision(short, taken_bank)
    link = compute_feature_linkage(short, full, features)

    # 4. Conciseness (0-10)
    alpha_len = len(re.sub(r"[^A-Za-z]", "", short))
    full_words = [w for w in re.split(r"\s+", (full or "").strip()) if w]
    conc_issues: List[str] = []
    conc = 10
    if alpha_len < 3:
        conc -= 4
        conc_issues.append("Short form <3 letters is easily confused with units or symbols")
    elif alpha_len > 8:
        conc -= 4
        conc_issues.append("Short form >8 letters (%d) is too long for figure labels and talks" % alpha_len)
    elif alpha_len > 7:
        conc -= 1
    if full_words:
        if len(full_words) > 7:
            conc -= 3
            conc_issues.append("Full name has %d words; tighten to 3-5 crisp words" % len(full_words))
        elif len(full_words) == 6:
            conc -= 1
        elif len(full_words) < 2:
            conc -= 2
            conc_issues.append("Provide a 3-5 word descriptive full technology name alongside the short form")
    conc = max(0, conc)

    # 5. Claim Safety (0-10)
    claim_issues: List[str] = []
    check_blob = (short + " " + (full or "")).lower()
    claim = 10
    for pat, msg in CLAIM_TRAP_PATTERNS:
        if re.search(pat, check_blob, re.I):
            claim -= 4
            claim_issues.append(msg)
    if ":" in (full or ""):
        claim -= 2
        claim_issues.append("Avoid colons inside the technology name or T1/T2 paper title (0.0% colon rate in 113 T1/T2 titles)")
    claim = max(0, claim)

    # 6. Typographic Hygiene & Awkward-Sound Guard (0-5)
    typo = 5
    typo_issues: List[str] = []
    awkward_tokens = ("DIE", "POO", "DUD", "BAD", "SAD", "LAG", "BUG", "ROT", "ERR", "WAR", "BUM", "FAP", "SUCK")
    up_short = short.upper()
    if any(tok == up_short or (len(tok) >= 3 and (up_short.startswith(tok) or up_short.endswith(tok))) for tok in awkward_tokens):
        typo -= 3
        typo_issues.append("Avoid awkward or negative English syllable/homophone inside '%s'" % short)
    if re.search(r"[0-9]", short):
        typo -= 2
        typo_issues.append("Digits/superscripts (like D2NN) break plain-text search, BibTeX, and smooth speech")
    if "-" in short:
        typo -= 1
        typo_issues.append("Hyphenated short form adds visual clutter unless extending a hardware class (like o-RAM)")
    if not short.isascii():
        typo -= 2
        typo_issues.append("Non-ASCII or Greek characters break filenames, BibTeX keys, and code repositories")
    typo = max(0, typo)

    total = phon["score_30"] + link["score_25"] + coll["score_20"] + conc + claim + typo
    grade = "A+ (T1/T2 Ready)" if total >= 88 else ("A (Strong)" if total >= 78 else ("B (Usable, Polish Needed)" if total >= 65 else ("C (Weak)" if total >= 50 else "D (Replace)")))

    all_issues = phon["issues"] + conc_issues + claim_issues + typo_issues
    if coll["status"] in ("HARD_COLLISION", "DOMAIN_COLLISION"):
        ex_msg = coll["exact_hits"][0]["examples"][0] if (coll["exact_hits"] and coll["exact_hits"][0].get("examples")) else (coll["exact_hits"][0]["key"] if coll["exact_hits"] else "")
        all_issues.insert(0, "Exact prior-art collision (%s): %s" % (coll["status"], ex_msg))
    elif coll["status"] == "OVERUSED_GENERIC":
        all_issues.insert(0, "Overused generic tech word; lacks distinctive identity in photonics/AI literature")
    elif coll["status"] == "NEAR_COLLISION_HIGH":
        all_issues.insert(0, "High phonetic/edit-distance collision risk with: " + ", ".join(h["key"] for h in coll["near_hits"][:3]))

    return {
        "short": short,
        "full": full,
        "total_100": total,
        "grade": grade,
        "breakdown": {
            "pronounceability_30": phon["score_30"],
            "feature_linkage_25": link["score_25"],
            "uniqueness_20": coll["score_20"],
            "conciseness_10": conc,
            "claim_safety_10": claim,
            "typographic_hygiene_5": typo,
        },
        "speech": phon["speech_label"],
        "spoken_syllables": phon["spoken_syllables"],
        "pronounceable_as_word": phon["pronounceable_as_word"],
        "collision_status": coll["status"],
        "exact_hits": coll["exact_hits"],
        "near_hits": coll["near_hits"],
        "feature_matches": link["matched_in_short"],
        "issues": all_issues,
    }


def build_backronym_expansion(word: str, features: List[str], modality: str) -> str:
    """Draft a concise illustrative full-name phrase linking the user's features."""
    clean = [f.strip() for f in features if f.strip()]
    base = " ".join(clean[:4])
    if modality and modality.lower() not in base.lower():
        base = base + " " + modality
    return base.strip()


def generate_candidates(features: List[str], modality: str, taken_bank: Dict[str, Any], top_n: int) -> List[Dict[str, Any]]:
    """Combinatorially synthesize, collision-filter, and score feature-linked candidates across 4 archetypes."""
    clean_feats = [f.strip().lower() for f in features if f.strip()]
    mod = (modality or "processor").strip().lower()
    if mod not in clean_feats:
        all_kws = clean_feats + [mod]
    else:
        all_kws = list(clean_feats)

    # Extract semantic roots from input features
    feat_roots: List[Tuple[str, str]] = []  # (root_Title, source_feature)
    seen_roots = set()
    for kw in all_kws:
        matched_any = False
        if kw in FEATURE_ROOT_MAP:
            for rv in FEATURE_ROOT_MAP[kw]:
                if rv.lower() not in seen_roots:
                    seen_roots.add(rv.lower())
                    feat_roots.append((rv, kw))
                    matched_any = True
        words = [w for w in re.split(r"[\s\-/]+", kw) if len(w) >= 2 and w not in ("on", "in", "to", "of", "by", "for")]
        for w in words:
            w_hit = False
            for rk, rvals in FEATURE_ROOT_MAP.items():
                if rk == w or (len(w) >= 4 and len(rk) >= 4 and (rk in w or w in rk)):
                    for rv in rvals:
                        if rv.lower() not in seen_roots:
                            seen_roots.add(rv.lower())
                            feat_roots.append((rv, kw))
                            w_hit = True
            if not w_hit and not matched_any and len(w) >= 4:
                cand_r = w[:4].capitalize()
                if any(c in VOWELS for c in cand_r.lower()) and cand_r.lower() not in seen_roots:
                    seen_roots.add(cand_r.lower())
                    feat_roots.append((cand_r, kw))

    candidates: Dict[str, Tuple[str, str, str]] = {}  # upper -> (short, archetype, full_hint)
    default_full = build_backronym_expansion("", clean_feats, mod)

    def add_cand(short: str, arch: str, full_hint: str):
        k = short.upper()
        if len(re.sub(r"[^A-Za-z]", "", short)) < 3 or len(short) > 10:
            return
        if k not in candidates:
            candidates[k] = (short, arch, full_hint)

    # 1. Archetype B: Semantic Portmanteaus / Compounds (Root1 + Root2 from distinct features)
    for (r1, f1), (r2, f2) in itertools.permutations(feat_roots[:18], 2):
        if f1 == f2:
            continue
        if r1.lower() == r2.lower():
            continue
        # Avoid clunky double letters at boundary
        if r1[-1].lower() == r2[0].lower():
            fused = r1 + r2[1:]
        else:
            fused = r1 + r2
        if 5 <= len(fused) <= 9:
            add_cand(fused, "Portmanteau / Semantic Compound", default_full)

    # 2. Archetype C: Hardware-Class Parallels (Root + Modality Suffix)
    suffixes = MODALITY_SUFFIXES.get(mod, ["Core", "Unit", "PU", "Chip"])
    for r1, f1 in feat_roots[:14]:
        for suf in suffixes:
            if r1.lower() == suf.lower():
                continue
            if suf in ("PU", "TU", "RAM"):
                # Strictly 3-letter Hardware-Class Initialism (*PU / *TU) or clean *RAM (avoid awkward *PU words like SlabPU/ProPU)
                if suf == "RAM" and len(r1) <= 4:
                    add_cand(r1 + "RAM", "Hardware-Class Parallel", default_full)
                elif len(r1) >= 2:
                    add_cand(r1[0].upper() + suf, "Hardware-Class Parallel", default_full)
            else:
                fused = r1 + suf
                if 5 <= len(fused) <= 9:
                    add_cand(fused, "Hardware-Class Parallel", default_full)

    # 3. Archetype A: Pronounceable Semantic Backronyms (Lexicon anchor matching + CV synthesis)
    kw_letters = set()
    kw_initials = set()
    for kw in all_kws:
        for w in re.split(r"[\s\-/]+", kw):
            if w:
                kw_initials.add(w[0].lower())
                for ch in w[:4].lower():
                    kw_letters.add(ch)

    for anchor, meaning in BACKRONYM_ANCHORS:
        al = anchor.lower()
        init_hits = sum(1 for ch in al if ch in kw_initials)
        sal_hits = sum(1 for ch in al if ch in kw_letters)
        # Require strong genuine letter anchoring to user's keywords
        if init_hits >= 2 and sal_hits >= max(3, len(al) - 1):
            add_cand(anchor, "Pronounceable Semantic Backronym", default_full)

    # Synthesize pronounceable 4-6 letter backronym blends directly from feature syllables
    syl_chunks = []
    for kw in clean_feats[:6]:
        w = re.sub(r"[^a-z]", "", kw.split()[0])
        if len(w) >= 2:
            # First CV or CVC chunk
            m_cv = re.match(r"^([^aeiouy]{0,2}[aeiouy])", w)
            if m_cv:
                syl_chunks.append((m_cv.group(1), kw))
            if len(w) >= 3 and any(c in VOWELS for c in w[:3]):
                syl_chunks.append((w[:3], kw))
    for (c1, f1), (c2, f2) in itertools.permutations(syl_chunks[:12], 2):
        if f1 == f2:
            continue
        if c1[-1] == c2[0]:
            continue  # Avoid awkward double-letter seams like PROOS
        for c3, f3 in syl_chunks[:10]:
            if f3 in (f1, f2) or c2[-1] == c3[0]:
                continue
            blend = (c1 + c2 + c3[0]).upper()
            if 4 <= len(blend) <= 6 and not re.search(r"([AEIOU])\1", blend):
                add_cand(blend, "Pronounceable Semantic Backronym", default_full)
        blend2 = (c1 + c2).upper()
        if 4 <= len(blend2) <= 6 and not re.search(r"([AEIOU])\1", blend2):
            add_cand(blend2, "Pronounceable Semantic Backronym", default_full)

    # 4. Archetype D: Crisp 3-Letter Mechanism Initialisms
    distinct_words = []
    for kw in all_kws:
        for w in re.split(r"[\s\-/]+", kw):
            if len(w) >= 2 and w not in distinct_words:
                distinct_words.append(w)
    for w1, w2, w3 in itertools.combinations(distinct_words[:7], 3):
        ini = (w1[0] + w2[0] + w3[0]).upper()
        if len(set(ini)) == 3:
            add_cand(ini, "Crisp 3-Letter Mechanism Initialism", (w1 + " " + w2 + " " + w3).title())

    # Score all candidates and strictly filter out hard collisions & low-pronounceability noise
    scored: List[Dict[str, Any]] = []
    for short, arch, full_hint in candidates.values():
        res = score_candidate(short, full_hint, clean_feats, taken_bank)
        if res["collision_status"] in ("HARD_COLLISION", "DOMAIN_COLLISION", "OVERUSED_GENERIC"):
            continue
        if arch != "Crisp 3-Letter Mechanism Initialism" and not res["pronounceable_as_word"]:
            # Allow *PU hardware parallels (e.g. DPU-style) only if <= 3 letters
            if not (arch == "Hardware-Class Parallel" and len(short) == 3):
                continue
        if res["spoken_syllables"] > 3:
            continue
        res["archetype"] = arch
        scored.append(res)

    scored.sort(key=lambda x: (-x["total_100"], x["spoken_syllables"], -x["breakdown"]["feature_linkage_25"], len(x["short"]), x["short"]))

    # Diversify top_n across archetypes so the user gets balanced options
    picked: List[Dict[str, Any]] = []
    by_arch: Dict[str, List[Dict[str, Any]]] = {}
    for item in scored:
        by_arch.setdefault(item["archetype"], []).append(item)

    arch_order = [
        "Pronounceable Semantic Backronym",
        "Portmanteau / Semantic Compound",
        "Hardware-Class Parallel",
        "Crisp 3-Letter Mechanism Initialism",
    ]
    # Round-robin pick top diverse entries first (ensures at least 2-3 per archetype if available)
    per_arch_idx = {a: 0 for a in arch_order}
    picked_keys = set()
    while len(picked) < top_n:
        progressed = False
        for a in arch_order:
            lst = by_arch.get(a, [])
            idx = per_arch_idx[a]
            while idx < len(lst) and lst[idx]["short"].upper() in picked_keys:
                idx += 1
            if idx < len(lst):
                picked.append(lst[idx])
                picked_keys.add(lst[idx]["short"].upper())
                per_arch_idx[a] = idx + 1
                progressed = True
                if len(picked) >= top_n:
                    break
        if not progressed:
            break

    picked.sort(key=lambda x: (-x["total_100"], x["spoken_syllables"], x["short"]))
    return picked


def cmd_exemplars(args: argparse.Namespace) -> int:
    rows = load_exemplars()
    if args.tier:
        rows = [r for r in rows if r["tier"].upper() == args.tier.upper()]
    if args.archetype:
        q = args.archetype.lower()
        rows = [r for r in rows if q in r["archetype"].lower()]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    print("=== T1 & T2 Verbatim-Verified Technology Naming Exemplars (n=%d; STRICTLY T1/T2 ONLY, 0 T3/T4) ===" % len(rows))
    print("Empirical T1/T2 Title Colon Rate: 0/113 (0.0%) | Brand-in-Title Rate: 1/113 (0.88%, Taichi inline without colon)")
    print("-" * 108)
    for r in rows:
        print(
            "[%s] %-10s | %-18s | reveal=%-8s | %-34s | %s (%s)"
            % (r["tier"], r["short"], r["pronunciation_guide"][:18], r["reveal_location"], r["archetype"][:34], r["journal"][:20], r["year"])
        )
        print("     Full: %s | Note: %s" % (r["full"], r["why_it_works_or_fails"]))
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    bank = load_taken_bank()
    res = check_collision(args.short, bank)
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    print("=== All-Tier Collision Check (6,490 Published Papers across 7 Photonics/PNN Catalogs, %d Keys) ===" % len(bank))
    print("Candidate : %s" % res["candidate"])
    print("Status    : %s (Uniqueness Score: %d/20)" % (res["status"], res["score_20"]))
    if res["exact_hits"]:
        print("\nEXACT COLLISIONS:")
        for h in res["exact_hits"]:
            print("  - %s (hits=%d, domains=%s)" % (h["key"], h["count"], ", ".join(h["domains"][:3])))
            for ex in h["examples"][:2]:
                print("      * %s" % ex)
    if res["near_hits"]:
        print("\nNEAR / PHONETIC COLLISIONS:")
        for h in res["near_hits"]:
            ex = h["examples"][0] if h["examples"] else ""
            print("  - %s [%s, hits=%d, %s] %s" % (h["key"], h["reason"], h["count"], ", ".join(h["domains"][:2]), ex[:85]))
    if not res["exact_hits"] and not res["near_hits"]:
        print("No exact or phonetic/edit-distance-1 collisions detected in the 6,490-paper bank.")
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    bank = load_taken_bank()
    feats = [x.strip() for x in (args.features or "").split(",") if x.strip()]
    res = score_candidate(args.short, args.full or "", feats, bank)
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    b = res["breakdown"]
    print("=== Scientific Technology Name Scorecard ===")
    print("Short Form : %s   [%s]" % (res["short"], res["speech"]))
    if res["full"]:
        print("Full Name  : %s" % res["full"])
    print("TOTAL SCORE: %d / 100  ->  %s" % (res["total_100"], res["grade"]))
    print("-" * 72)
    print("  1. Pronounceability & Phonotactics : %2d / 30" % b["pronounceability_30"])
    print("  2. Feature-to-Name Linkage         : %2d / 25" % b["feature_linkage_25"])
    print("  3. All-Tier Uniqueness (6,490 pap) : %2d / 20  [%s]" % (b["uniqueness_20"], res["collision_status"]))
    print("  4. Conciseness & Talk-Readiness    : %2d / 10" % b["conciseness_10"])
    print("  5. Claim-Safety (Zero C12 Traps)   : %2d / 10" % b["claim_safety_10"])
    print("  6. Typographic & ASCII Hygiene     : %2d / 5" % b["typographic_hygiene_5"])
    if res["feature_matches"]:
        print("\nFeature Anchors Detected: " + "; ".join(res["feature_matches"]))
    if res["issues"]:
        print("\nActionable Diagnostics:")
        for i, iss in enumerate(res["issues"], 1):
            print("  %d. %s" % (i, iss))
    else:
        print("\nDiagnostics: Zero issues detected. Ready for T1/T2 abstract reveal.")
    return 0


def cmd_generate(args: argparse.Namespace) -> int:
    bank = load_taken_bank()
    feats = [x.strip() for x in args.features.split(",") if x.strip()]
    if len(feats) < 2:
        print("Please provide at least 2 comma-separated features via --features.", file=sys.stderr)
        return 1
    results = generate_candidates(feats, args.modality, bank, args.top)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0
    print("=== Collision-Free Feature-Linked Name Candidates (Top %d across 4 Archetypes) ===" % len(results))
    print("Input Features : %s | Modality: %s" % (", ".join(feats), args.modality))
    print("Collision Bank : 6,490 papers across 7 photonics/PNN catalogs (%d taken keys)" % len(bank))
    print("-" * 108)
    for idx, r in enumerate(results, 1):
        b = r["breakdown"]
        print(
            "%2d. %-11s | %3d/100 | %-26s | %-32s | %s"
            % (idx, r["short"], r["total_100"], r["speech"][:26], r["archetype"][:32], r["collision_status"])
        )
        if r["feature_matches"]:
            print("    Links (P=%d L=%d U=%d): %s" % (b["pronounceability_30"], b["feature_linkage_25"], b["uniqueness_20"], ", ".join(r["feature_matches"][:4])))
    print("\nTip: Pick your favorite 2-3 candidates, refine the 3-5 word full expansion, and re-run `score` + `audit-draft`.")
    return 0


def cmd_audit_draft(args: argparse.Namespace) -> int:
    text = safe_read_text(args.text_or_file)
    short = args.short.strip()
    full = (args.full or "").strip()
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    title = lines[0] if lines else ""

    findings: List[str] = []
    passed: List[str] = []

    # 1. Title colon check
    if ":" in title:
        findings.append("TITLE COLON TRAP: First line contains a colon (':'). In 113 T1/T2 research articles, 0.0% use colons in titles.")
    else:
        passed.append("Title is colon-free (matches 113/113 T1/T2 research articles).")

    # 2. Brand in title check
    if re.search(r"\b" + re.escape(short) + r"\b", title):
        findings.append("TITLE BRAND NOTE: Short form '%s' appears in Title. Only 1/113 (0.88%%, Taichi) T1/T2 papers put a brand in the title; 83.9%% reveal it cleanly in Abstract S2-S4." % short)
    else:
        passed.append("Title stays descriptive; short form reserved for Abstract/Intro reveal.")

    # 3. First-mention definition check
    def_pat = re.compile(r"\(" + re.escape(short) + r"\)|(?:named|called|termed|denoted)\s+['\"\u2018\u201c]?" + re.escape(short) + r"['\"\u2019\u201d]?", re.I)
    if def_pat.search(text):
        passed.append("Short form '%s' is formally introduced with parentheses or a naming cue." % short)
    else:
        findings.append("MISSING FORMAL REVEAL: '%s' is not explicitly introduced via '(SHORT)' or 'named SHORT' in the draft." % short)

    # 4. Capitalization consistency
    variants = set(re.findall(r"\b" + re.escape(short) + r"\b", text, re.I))
    if len(variants) > 1:
        findings.append("INCONSISTENT CASING: Found multiple spellings: " + ", ".join(sorted(variants)))
    elif variants:
        passed.append("Consistent capitalization across all occurrences of '%s'." % short)

    # 5. Mixed-alias trap check (e.g. OMDNN + OM2NN + PDNN in same draft)
    alias_families = [
        {"OMDNN", "OM2NN", "PDNN", "D2NN", "DONN"},
        {"SIALN", "ALNSI", "SCALN"},
    ]
    for fam in alias_families:
        if short.upper() in fam:
            present = [tok for tok in fam if re.search(r"\b" + re.escape(tok) + r"\b", text)]
            if len(present) > 1:
                findings.append("MIXED ALIAS TRAP: Multiple competing short forms found in the same draft: " + ", ".join(sorted(present)))

    # 6. Claim-trap check on full name
    if full:
        for pat, msg in CLAIM_TRAP_PATTERNS:
            if re.search(pat, full, re.I):
                findings.append("FULL-NAME CLAIM TRAP: " + msg)

    print("=== T1/T2 Manuscript Naming Hygiene Audit ===")
    print("Target Name : %s (%s)" % (short, full or "no full name given"))
    print("Status      : %s (%d passed, %d warnings)" % ("CLEAN" if not findings else "NEEDS_ATTENTION", len(passed), len(findings)))
    for p in passed:
        print("  [PASS] %s" % p)
    for w in findings:
        print("  [WARN] %s" % w)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Scientific Technology Naming & Short-Form CLI (T1/T2 craft + 6,490-paper all-tier collision check)")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_ex = sub.add_parser("exemplars", help="List verbatim-verified T1/T2 named technology exemplars")
    p_ex.add_argument("--tier", choices=["T1", "T2"], help="Filter by journal tier (strictly T1 or T2)")
    p_ex.add_argument("--archetype", help="Substring filter on archetype (e.g., Backronym, Portmanteau, Hardware)")
    p_ex.add_argument("--json", action="store_true", help="Output JSON")
    p_ex.set_defaults(func=cmd_exemplars)

    p_chk = sub.add_parser("check", help="Check a candidate short name for collisions across 6,490 all-tier photonics/PNN papers")
    p_chk.add_argument("short", help="Candidate short name (e.g., PACE, LightGen, OMDNN)")
    p_chk.add_argument("--json", action="store_true", help="Output JSON")
    p_chk.set_defaults(func=cmd_check)

    p_sc = sub.add_parser("score", help="Compute the 100-point Scientific Technology Name Scorecard")
    p_sc.add_argument("short", help="Candidate short name")
    p_sc.add_argument("--full", default="", help="Proposed 3-5 word full technology name")
    p_sc.add_argument("--features", default="", help="Comma-separated key differentiating technical features")
    p_sc.add_argument("--json", action="store_true", help="Output JSON")
    p_sc.set_defaults(func=cmd_score)

    p_gen = sub.add_parser("generate", help="Generate, collision-filter, and rank pronounceable feature-linked names")
    p_gen.add_argument("--features", required=True, help="Comma-separated technical features (e.g., 'programmable,diffractive,slot,silicon,processor')")
    p_gen.add_argument("--modality", default="processor", help="Device/system modality (processor, chip, modulator, network, method, platform, sensor, converter)")
    p_gen.add_argument("--top", type=int, default=12, help="Number of ranked diverse candidates to return")
    p_gen.add_argument("--json", action="store_true", help="Output JSON")
    p_gen.set_defaults(func=cmd_generate)

    p_aud = sub.add_parser("audit-draft", help="Audit a manuscript title/abstract/draft for T1/T2 naming hygiene")
    p_aud.add_argument("text_or_file", help="Path to draft file or literal text snippet")
    p_aud.add_argument("--short", required=True, help="Canonical short name")
    p_aud.add_argument("--full", default="", help="Canonical full technology name")
    p_aud.set_defaults(func=cmd_audit_draft)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
