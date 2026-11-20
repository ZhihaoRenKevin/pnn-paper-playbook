---
name: pnn-t1t2-figure-caption
description: Actionable T1/T2 PNN Figure Caption drafting and revision playbook calibrated exclusively on 525 verbatim main-text captions (plus 145 Extended Data captions) from 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 dilution). Use whenever writing or linting captions for Nature vs Science journals.
---

# How to Write and Revise T1/T2 PNN Figure Captions (`pnn-t1t2-figure-caption`)

Use this skill to draft razor-sharp, journal-compliant captions that let a referee understand the entire figure without flipping back to the main text. Calibrated from `525` T1/T2 captions (`222` native-primary `weight=2.0`).

---

## 1. How to Write From Scratch (Exact Journal Syntax + 3-Part Formula)

### Step 1: Lock the Exact Target-Journal Typography
- ***Nature* / *Nature Photonics* / *Nature Electronics* / *Nature Nanotechnology* / *Nature Computational Science***:
  `Fig. 1 | [6-8 word noun-phrase title]. a, [Panel a description]. b, [Panel b description].`
  (Pipe `|` after figure number; lowercase bold bare letter + comma `a,`, `b,`, `c,`; NEVER `(a)` or `A:` in Nature Portfolio!).
- ***Science***:
  `Fig. 1. [6-8 word noun-phrase title]. (A) [Panel A description]. (B) [Panel B description].`
  (Period `.` after figure number; uppercase parenthesized `(A)`, `(B)`, `(C)`).

### Step 2: Draft the 3 Mandatory Caption Elements
1. **Bold Lead-In Title (5-9 words, Pure Noun Phrase)**:
   - Zero finite claim verbs (`demonstrates`, `achieves`, `proves`). Write `Architecture and operating principle of the programmable diffractive processor.`: NOT `Our chip achieves 93% accuracy in image classification.`
2. **Per-Panel Descriptions (`30-50` words per panel, `140-220` words total per figure)**:
   - State **what is plotted** + **physical distinction** (`in the presence/absence of`, `as a function of`, `compared with`) + **encoding key** (`filled circles, measured; dashed line, FDTD simulation`).
   - Include **micrograph scale bars** explicitly (`scale bar, 50 um`).
   - Group tightly related sub-panels cleanly (`c,d, Measured (c) and simulated (d) transmission matrices...`) to stay concise.
3. **Statistical & Symbol Footer (Last 1-2 Sentences)**:
   - Define every error bar (`error bars denote +-1 s.d. across n = 5 independent trials`), shaded band (`shaded regions show 95% CI`), and any abbreviation introduced in the artwork.

---

## 2. How to Revise an Existing Caption (3-Pass Surgery)

### Pass 1: Strip Main-Text Prose & Verbose Titles
- Convert full-sentence titles (`"The fabricated chip shows high accuracy and low loss"`) into crisp noun phrases (`"Inference accuracy and optical-core energy efficiency"`).
- Cut long interpretations (`"which clearly proves the superiority of our method"`) out of the caption: keep only what is directly visible in the panel plus one short factual takeaway if needed.

### Pass 2: Fix Missing Scientific Disclosures (Top Referee Triggers)
- Missing **scale bar** on SEM/optical micrograph -> add `(scale bar, X um)`.
- Missing **sim-vs-exp key** -> add `(symbols, experiment; solid curves, simulation)`.
- Missing **error-bar definition & `n`** -> add `Data represent mean +- s.d. (n = X chips/runs).`
- Wrong panel syntax (`(a)` in a *Nature Photonics* draft) -> switch to `a,`.

### Pass 3: Concrete Before -> After Rewrite
- **Before (T3 / Incorrect Syntax / Missing Disclosures)**:
  > *"Figure 2: Our device achieves ultra-high modulation and great accuracy. (a) SEM image of the chip. (b) Transmission spectrum showing good agreement between experiment and simulation. (c) Classification accuracy for different epochs. Clearly, our device works very well."*
- **After (T1/T2 *Nature Photonics* Native-Grade Caption)**:
  > *"Fig. 2 | Electro-thermal calibration and classification fidelity of the diffractive core. a, False-colour scanning electron micrograph of the 64-element silicon slot array with TiN microheaters (scale bar, 50 um). b, Measured (filled circles) and FDTD-simulated (dashed curves) transmission spectra across four heater bias powers (0-24 mW) at 1550 nm. c, Held-out classification accuracy as a function of in-situ training epoch for the hardware processor (crimson) compared with the matched digital baseline (charcoal dashed) and untrained-core control (slate). Shaded bands and error bars represent +-1 s.d. across n = 5 independent training runs."*

### Pass 4: Mandatory CLI Lint Gate
```bash
python3 scripts/pnn_caption_tool.py lint path/to/caption.txt --journal "Nature Photonics"
python3 scripts/pnn_caption_tool.py query --tier T1 --fig 1 --native-only --top 3
```

---

## 3. Compact Pass/Fail Checklist
- [ ] Exact journal header & panel syntax (`Fig. N |` + `a,` for Nature; `Fig. N.` + `(A)` for Science).
- [ ] Lead-in title is a `5-9` word noun phrase with zero finite claim verbs.
- [ ] Every micrograph states a scale bar; every data plot distinguishes measured vs simulated and defines error bars + `n`.
- [ ] Target `30-50` words per panel (`<=240` words total); zero em-dashes or `"clearly shows"` filler.

## 4. References & CLI
- Native-weighted exemplars: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_captions_corpus.jsonl`](./references/t1t2_captions_corpus.jsonl) (`222/525` native-primary `weight=2.0` sorted first).
