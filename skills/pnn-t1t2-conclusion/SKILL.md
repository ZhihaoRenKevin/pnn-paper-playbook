---
name: pnn-t1t2-conclusion
description: Actionable T1/T2 PNN Conclusion and Discussion drafting and revision playbook calibrated exclusively on 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 dilution). Use whenever writing or revising Discussion/Conclusions headings, disarming limitations, scaling roadmaps, or final closing sentences.
---

# How to Write and Revise a T1/T2 PNN Conclusion & Discussion (`pnn-t1t2-conclusion`)

Use this skill to write a closing section that **earns referee trust** rather than repeating the Abstract or ending in vague hype.

---

## 1. How to Write From Scratch (Exact Heading + 4-Paragraph Architecture)

### Step 1: Pick the Exact Journal Closing Heading
Check the target journal first via `python3 scripts/pnn_conclusion_tool.py heading --journal "<Journal>"`:
- ***Nature Electronics***: `Conclusions` (`100%`)
- ***Nature Computational Science***: `Discussion` (`100%`)
- ***Nature Nanotechnology***: `Conclusions` (`90%`)
- ***Nature Photonics***: `Discussion` (most common) or untitled final paragraphs (never `RESULTS AND DISCUSSIONS`)
- ***Nature* / *Science***: `Discussion` or untitled closing paragraphs integrated smoothly after the final Results block.

### Step 2: Draft the 4-Move Closing Structure (`280-480` Words)
1. **Move 1: Non-Repetitive Conceptual Synthesis (1 short paragraph, `60-90w`)**: State the **architectural or physical principle** your experiments established: do NOT copy-paste the Abstract's metrics verbatim.
2. **Move 2: Disarming, Quantitative Limitations (1 paragraph, `90-140w`)**: Separate **current laboratory packaging limits** (off-chip fiber coupling loss, discrete DAC/ADC boards, thermo-optic holding power) from **fundamental physical limits** (waveguide propagation loss, shot noise, diffraction limit). Name 2-3 real prototype constraints objectively (`limited by`, `bound by`, `albeit`): zero apologetic self-deprecation (`"unfortunately our toy prototype..."`).
3. **Move 3: Engineering Scaling Roadmap (1 paragraph, `90-140w`)**: Tie **each limitation in Move 2** to a concrete, cited hardware upgrade with an explicit projected number and assumptions (e.g., `"Replacing TiN thermo-optic heaters with non-volatile Sb2Se3 or thin-film LiNbO3 phase shifters eliminates static holding power and, in principle, raises projected system efficiency from 1.8 to >40 TOPS/W at N = 256"`). Always label projected values clearly (`projected`, `in principle`, `assuming`).
4. **Move 4: Grounded Horizon Closer (1-2 crisp sentences, `35-55w`)**: Name 1-2 realistic near-term applications (edge sensing, telecom optical DSP, real-time scientific inference) where the demonstrated mechanism is physically **viable**. Zero `"paves the way for a transformative paradigm shift"` clichés!

---

## 2. How to Revise an Existing Draft (Concrete Before -> After)
- **Before (Repetitive + Hype + Apologetic Draft)**:
  > *"In summary, we have proposed a groundbreaking OMDNN chip that achieves 93.3% accuracy and 0.34 pJ/MAC. Admittedly, our prototype is only a small-scale proof-of-concept and does not constitute a full GPU replacement, which is a serious drawback. In the future, with further optimization, this versatile chip will dramatically revolutionize edge AI and pave the way for AGI."*
- **After (Authoritative T1/T2 Native-Grade Discussion)**:
  > *"We have established that planar slab diffraction combined with localized thermo-optic phase control executes programmable linear projections without deep waveguide-mesh cascading. Two engineering bottlenecks currently cap system-level efficiency in our laboratory prototype: static thermal holding power (18 mW per heater) and off-chip electrical I/O conversion, whereas passive silicon slab propagation incurs less than 1.4 dB excess loss. Integrating non-volatile phase-change patches (for example, Sb2Se3) or electro-optic thin-film lithium niobate modulators directly into the same slot layout eliminates static bias power; paired with 3D CMOS co-packaging, this route can in principle lift wall-plug efficiency above 40 TOPS/W at matrix widths N >= 128. Beyond image classification, the compact planar architecture offers a viable hardware front end for sub-nanosecond optical signal equalization and near-sensor spectral inference."*

### Mandatory CLI Verification Gate
```bash
python3 scripts/pnn_conclusion_tool.py heading --journal "Nature Photonics"
python3 scripts/pnn_conclusion_tool.py lint path/to/conclusion.txt --journal "Nature Photonics"
python3 scripts/pnn_conclusion_tool.py query --tier T1 --native-only --top 3
```

---

## 3. Compact Pass/Fail Checklist
- [ ] Heading matches the exact target journal convention (`heading` CLI verified).
- [ ] Synthesis explains the broader physical insight instead of re-listing Abstract sentences.
- [ ] Explicitly separates laboratory packaging bottlenecks from fundamental physical limits.
- [ ] Every limitation is paired with a cited, quantified, clearly labeled projected scaling path.
- [ ] Zero defensive apologies, zero `"pave the way"` / `"transformative"` hype, zero em-dashes.

## 4. References & CLI
- Native-weighted exemplars: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_conclusion_corpus.jsonl`](./references/t1t2_conclusion_corpus.jsonl) (`49` native-primary `weight=2.0` sorted first).
