---
name: sci-tech-naming
description: Design memorable, pronounceable, feature-linked scientific technology names and short forms (acronyms, semantic backronyms, portmanteaus, hardware-class parallels) for Nature/Science-tier papers, chips, architectures, methods, platforms, and software. Calibrated strictly on T1 & T2 research articles (113 papers, 31 verbatim-verified coined exemplars; zero T3/T4 dilution) for naming craft and title/abstract reveal rules, paired with an ALL-TIER (T1-T4, 6,490 papers across 7 photonics/PNN catalogs + AI/quantum/hardware brands) collision-check database. Activate whenever naming a new device, chip, photonic architecture, algorithm, platform, or software tool, or replacing a clunky consonant-cluster acronym (e.g., OMDNN, POMMM, OAM-MDNN).
---

# Scientific Technology Naming & Short-Form Playbook (`sci-tech-naming`)

## 1. Strict Tier Separation & Empirical Basis
- **Naming Craft, Reveal Conventions & Archetypes (STRICTLY T1 & T2 ONLY)**: Distilled from `113` T1 and T2 research articles (`33` T1: *Nature*, *Science*; `80` T2: *Nature Photonics*, *Nature Electronics*, *Nature Nanotechnology*, *Nature Computational Science*, *Nature Materials*, *Nature Physics*, *Nature Machine Intelligence*, *Nature Sensors*; `0` T3/T4 papers; `0` reviews), with `31` coined technology names verified verbatim in fulltext (`references/t1t2_verified_exemplars.jsonl`).
- **Prior-Art & Acronym Collision Check (ALL TIERS T1-T4)**: Checks candidates against `1,059+` unique taken acronyms and branded names mined from `6,490` published paper records across 7 photonics and optical-computing catalogs (`PNN 1,475` + `SiC/FWM 1,397` + `ScAlN 720` + `LN PIC 853` + `PCM 1,759` + `PIC NAF 182` + `Quantum PIC 104`) plus landmark AI, quantum, semiconductor, and internal group project names (`references/all_tier_taken_acronyms.json`).
- **Division of Labour**: Pair with `pnn-t1t2-abstract` for Title and Abstract S3 reveal integration, `author house-style guidelines` + `low-aigc-nondefensive-writing` for prose polish, and `pnn-paper-playbook` for full literature SOTA lookups.

---

## 2. Empirical T1/T2 Naming Rules (Verified on 113 Research Articles)
1. **Zero Colons in T1/T2 Titles (`0/113 = 0.0%`)**: Never write `"MYCHIP: A programmable on-chip diffractive processor"` in a *Nature*, *Science*, or *Nature*-subjournal title. Keep the title descriptive, colon-free, and `6-10` words.
2. **Reveal the Short Form in Abstract S2-S4 (`83.9%` of named T1/T2 systems) or Opening Results (`12.9%`)**:
   - Only `1/113` (`0.88%`, `Taichi`, *Science* 2024) embeds a coined brand directly inside the title, and even there it sits as a plain appositive noun without a colon (`"Large-scale photonic chiplet Taichi empowers 160-TOPS/W..."`).
   - `26/31` (`83.9%`) of named T1/T2 technologies introduce the full name + short form in the Abstract (for example, `"all-analog chip combining electronic and light computing (ACCEL)"`, `"all-optical generative chip, LightGen"`, `"delocalized photonic deep learning framework (Netcast)"`, `"analog optical computer (AOC)"`, `"diffractive processing unit (DPU)"`, `"in situ physical gradient descent (INSPIRE)"`).
   - `4/31` (`12.9%`, including `PACE`, `SOLO`, `PAT`, `PTC`) keep even the Abstract pure descriptive physics and reveal the short form cleanly at the start of the Introduction or Results.
3. **Talk-Readiness Beats Letter-Packing**: A name lives in conference talks (OFC, CLEO, faculty interviews), referee discussions, and citation sentences (`"compared with PACE and ACCEL"`). If a colleague cannot pronounce it smoothly in 1-2 syllables on the first try, the name fails.

---

## 3. The 5 Winning T1/T2 Naming Archetypes

| Rank | Archetype | Speech Feel | Verbatim T1/T2 Exemplars | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Pronounceable Semantic Backronym** | 1-2 syllable real/natural English word | `ACCEL` (*Nature* 2023), `PACE` (*Nature* 2025), `SOLO` (*Nat. Comput. Sci.* 2021), `INSPIRE` (*Nat. Comput. Sci.* 2026), `PAT` (*Nature* 2022), `PhyLL` (*Science* 2023), `DOPO` (*Nat. Photon.* 2016) | **Default #1 choice** for *Nature*/*Science* chips, methods, and training algorithms; links directly to features AND sounds like the headline advantage |
| **2** | **Semantic Portmanteau / Compound Brand** | 2 crisp fused syllables (CamelCase or TitleCase) | `LightGen` (*Science* 2025), `Netcast` (*Science* 2022) | **Flagship chips, platforms, and software**: merges physical medium (`Light`, `Wave`, `Slot`, `Ring`, `Opto`) + key function (`Gen`, `Cast`, `Core`, `Flow`, `Tune`) |
| **3** | **Hardware-Class Parallel (`*PU`, `*Core`, `*RAM`)** | 3 letters or 2 syllables | `DPU` (*Nat. Photon.* 2021), `DTU` (*Nat. Photon.* 2025), `PTC` (*Nature* 2025), `ORRAM` (*Nat. Nanotechnol.* 2019), `o-RAM` (*Nat. Photon.* 2012) | **Computing / memory hardware** competing with electronic GPUs/TPUs/RAM; gives instant architectural intuition |
| **4** | **Crisp 3-Letter Mechanism Initialism** | Exactly 3 letters (3 spoken syllables max) | `AOC` (*Nature* 2025), `FFM` (*Nature* 2024), `QRC` (*Nat. Photon.* 2026), `OPO` (*Nat. Photon.* 2014) | **Minimalist physical mechanisms & training rules** where 3 words already define the core invention cleanly |
| **5** | **Cultural / Physical Metaphor Brand** | 2-3 syllable proper noun | `Taichi` (*Science* 2024); also Quantum *Nature* `Aurora` (2025), `Borealis` (2022) | **Rare flagship systems only**; always pair with a concrete descriptive noun (`"photonic chiplet Taichi"`) so the physics stays clear |

### Anti-Patterns Observed Even in T1/T2 (Avoid Repeating!)
- **Consonant-cluster tongue-twisters (`>=4` spelled-out letters)**: `PDNN` (*Nature* 2022), `POMMM` (*Nat. Photon.* 2025, triple-M mouthful), `OAM-MDNN` (*Nat. Photon.* 2026, 7 spoken syllables), `PTNO`, `CTDS`, `OELG`, and internal drafts like `OMDNN` (5 spelled-out syllables `"pee-dee-dee-en-en"`, double-D + double-N stutter, phonetically indistinguishable from `PDNN` and `D2NN`).
- **Superscripts / digits inside the short form**: `D2NN` (`D^2NN`, *Science* 2018) and `DN2` (*Nat. Photon.* 2025) break plain text, BibTeX, GitHub slugs, and spoken clarity (`"D-two-N-N"` vs `"D-N-two"`).
- **Hidden domain collisions**: `PIN` (*Nat. Comput. Sci.* 2025, shares letters with `p-i-n` photodiode) and `OEM` (*Nat. Nanotechnol.* 2024, collides with Original Equipment Manufacturer).

---

## 4. The 6 Golden Rules (100-Point Scorecard Criteria)
1. **Pronounceability & Phonotactics (30 pts)**: Target `1-2` spoken syllables (`3-7` letters), smooth CV/CVC flow or clean 2-morpheme CamelCase compound, vowel ratio `0.28-0.58`, zero unpronounceable consonant clusters (`pdd`, `dnn`, `mmm`, `mdnn`), zero stuttering doubled letters in initialisms (`DD`, `MM`, `NN`).
2. **Feature-to-Name Linkage (25 pts)**: At least `2-3` core technical features (physical mechanism + hardware structure + primary performance win) must map transparently into the short form and the `3-5`-word full name. Avoid empty generic hype (`APEX`, `NOVA`, `HYPER`, `OMNI`, `SMART`, `ULTRA`).
3. **Zero Prior-Art Collision Across ALL Tiers (20 pts)**: Always run `scripts/tech_naming_tool.py check <SHORT>`. Reject exact collisions in the `6,490`-paper photonics/PNN bank and landmark AI/quantum/hardware brands; flag edit-distance-1 or phonetic lookalikes (`OMDNN` vs `PDNN`/`D2NN`/`DONN`).
4. **Conciseness & Talk-Readiness (10 pts)**: Short form `3-7` letters (`<=2` spoken syllables if word, strictly `3` letters if initialism); full technology name `3-5` crisp words (never an 8-word laundry list).
5. **Claim-Safety & Editorial Discipline (10 pts)**: Never embed referee claim traps (`C12` overclaiming) inside the permanent technology name. Avoid `All-Optical` if electronics handle weighting/activation/readout, `Deep` if only `1-2` physical layers, or `Universal`, `General`, `AGI`, `Brain-like`, `Ultimate`, `Perfect`, `Novel`, `First`.
6. **Typographic & Cross-Document Hygiene (5 pts)**: Pure ASCII letters (no superscripts, subscripts, Greek letters, or unnecessary hyphens). Lock ONE canonical spelling across Title, Abstract, Figures, SI, Code, and Repository.

---

## 5. Mandatory 5-Step Workflow When Naming a Technology
When the user asks to name a technology, chip, method, platform, or software tool:
1. **Deconstruct into 4 Anchor Slots**:
   - **Physics / Mechanism** (e.g., diffractive, slab, interferometric, electro-optic, Pockels, Bragg-scattering, phase-change)
   - **Hardware / Form** (e.g., on-chip, silicon, slot array, metaline, microring, bilayer, waveguide, chiplet)
   - **Key Differentiator** (e.g., programmable, thermal-tuned, non-volatile, dual-mode, broadband, low-loss, compact)
   - **Task / Output** (e.g., processor, accelerator, modulator, converter, engine, operator, core, router)
2. **Run the Local CLI Generator & Collision Checker**:
   ```bash
   python3 scripts/tech_naming_tool.py generate \
     --features "programmable,diffractive,slot,silicon,on-chip,processor" --modality processor --top 15
   ```
3. **Curate Exactly 6 Strong Candidates Spanning at Least 3 Archetypes** (e.g., 2 Pronounceable Semantic Backronyms, 2 Semantic Portmanteaus, 1 Hardware-Class Parallel, 1 Crisp 3-Letter Initialism).
4. **Score and Collision-Check Every Final Candidate with the CLI**:
   ```bash
   python3 scripts/tech_naming_tool.py score <SHORT> \
     --full "<Full Technology Name>" --features "kw1,kw2,kw3,kw4"
   ```
5. **Deliver a Clean Decision Table + Ready-to-Paste Abstract S3 Reveal**:
   - Columns: `Rank`, `Short Form`, `Pronunciation (Syllables)`, `Full Technology Name`, `Archetype`, `Feature Mapping`, `Score /100`, `Collision Status (6,490 Papers)`.
   - Include a recommended `#1` pick plus a ready-to-paste **colon-free Title** and **Abstract S3 reveal sentence** matched to `pnn-t1t2-abstract` and `author house-style guidelines`.

---

## 6. CLI Quick Reference (`scripts/tech_naming_tool.py`, Zero Pip Deps)
All commands run locally under bare system `/usr/bin/python3`:
- `exemplars [--archetype ...] [--tier T1|T2]`: Inspect the 31 verbatim-verified T1/T2 named technologies and reveal stats.
- `check <SHORT>`: Run exact, phonetic, and Levenshtein-1 collision checks across the `6,490`-paper ALL-TIER bank (`1,059+` keys).
- `score <SHORT> --full "<Full Name>" --features "k1,k2,k3"`: Run the deterministic 100-point scorecard across all 6 dimensions with concrete improvement notes.
- `generate --features "k1,k2,k3,..." [--modality chip|processor|modulator|network|method|platform|sensor] [--top 15]`: Combinatorially generate, collision-filter, and rank pronounceable feature-linked names across 4 archetypes.
- `audit-draft <FILE_OR_TEXT> --short <SHORT> --full "<Full Name>"`: Audit a manuscript draft for T1/T2 naming hygiene (colon-free title, Abstract reveal, consistent casing, zero mixed aliases, zero claim-trap words).
