---
name: pnn-t1t2-introduction
description: Actionable T1/T2 PNN Introduction drafting and revision playbook calibrated exclusively on 113 Nature, Science, and Nature-subjournal research articles (2.0x native-English-country weighting; zero T3/T4 dilution). Use whenever writing or restructuring a PNN Introduction, prior-art critique, or final contribution paragraph.
---

# How to Write and Revise a T1/T2 PNN Introduction (`pnn-t1t2-introduction`)

Use this skill to construct or surgically revise a `3-5` paragraph (`420-680` word) *Nature*/*Science*/*Nature Photonics* Introduction that drives straight from physical tension to your chip's breakthrough without textbook filler.

---

## 1. How to Write From Scratch (4-Paragraph Funnel Recipe)

### Step 1: Choose 1 of the 4 T1/T2 Story Funnels
1. **Compute-Crisis Funnel** (for architectures/accelerators, Claim Class B): Electronic data-movement/energy wall -> why optics helps -> why prior optical architectures stall at scale -> your solution.
2. **Missing-Primitive Funnel** (for devices/materials/training, Claim Classes A & C): Optical linear MACs are mature -> the missing physical ingredient (on-chip nonlinearity, non-volatile low-loss weight, in-situ backpropagation) -> why workarounds fail -> your primitive.
3. **Received-Wisdom Inversion Funnel** (highest T1 impact, Claim Class F): Field assumes property X (incoherence, multimode scattering, thermal coupling) is parasitic -> show why that assumption restricts throughput/density -> flip X into a computational resource.
4. **Application-Latency Funnel** (for vision/RF/fiber systems, Claim Classes E & G): Real-time application demands sub-ns latency or >20 GHz bandwidth -> electronic ADC/DSP cannot keep up -> prior optics stays bulky/static -> your integrated system.

### Step 2: Draft Paragraph by Paragraph (Target 450-650 Words Total)
- **Paragraph 1 (90-130w): Concrete Problem & Why Photonics**: Open directly with the physical or computational constraint (never `"In recent years"` or `"has attracted wide attention"`). Establish why light's parallelism, bandwidth, or passive propagation targets that exact bottleneck, citing foundational reviews in grouped ranges.
- **Paragraph 2 (130-170w): Prior-Art Family Audit (Diplomatic & Physical)**: Group competing optical platforms into 2-3 clear families (e.g., coherent MZI meshes, WDM microring banks, free-space diffractive layers). Credit each family's strength in half a clause, then state its **physical scaling limit** (`limited by`, `bound by`, `at the expense of`, `necessitates`) with specific citations. Never dismiss prior work vaguely as `"impractical"` or `"poor"`.
- **Paragraph 3 (110-150w): The Exact Unsolved Gap**: Isolate the 1-3 closest competitor papers individually (the exact authors who will referee your manuscript) and pinpoint the physical trade-off or missing capability that remains open (`whereas`, `however`, `trade-off`).
- **Paragraph 4 (120-160w): `"Here we"` Breakthrough & Quantitative Contract**: Open directly with `"Here we demonstrate/propose..."` (no `"In this paper, Section 2 describes..."` TOC boilerplate!). State (1) the physical mechanism, (2) the fabricated/measured scale, (3) the headline quantitative benchmarks vs matched baselines, and (4) the concrete operational scope (referencing Fig. 1).

---

## 2. How to Revise an Existing Draft (4-Pass Surgery)

### Pass 1: Delete Textbook Padding & Paper-Map Boilerplate
- Delete Paragraph-1 throat-clearing (`"With the rapid development of AI..."`, `"Deep learning has transformed society..."`).
- Delete any `"The remainder of this paper is organized as follows"` block (`98-100%` of T1/T2 papers omit it).
- Cut Introductions longer than `750` words down to `450-650` words by merging repetitive citation summaries.

### Pass 2: Fix Prior-Art Critique Etiquette (Prevent Reviewer Anger)
- Check whether every major competing group (MIT, Cornell, Oxford, Tsinghua, UCLA, UPenn, Lightmatter, Lightelligence, etc. relevant to your platform) is credited fairly.
- Replace dismissive wording (`"previous MZI chips fail due to terrible loss"`) with physics-grounded wording (`"cascaded MZI meshes achieve high linear fidelity, albeit at the expense of quadratic footprint and insertion-loss scaling"`).

### Pass 3: Native High-Register Grammar & Concrete Before -> After
- **Before (Verbose Non-Native / AI Draft)**:
  > *"In recent years, deep neural networks have attracted tremendous attention in many fields. Photonic neural networks are a versatile solution. Previous MZI chips suffer from huge area and high power, and free-space D2NNs are bulky. Moreover, existing works rarely achieve compact reconfigurability. Specifically, Section 2 introduces the design and Section 3 shows results."*
- **After (Sharp T1/T2 Native-Grade Revision)**:
  > *"Matrix-heavy neural inference is increasingly bound by electronic data movement rather than transistor switching speed [1-3]. Photonic circuits bypass this interconnect bottleneck by computing linear transformations passively during optical propagation [4,5]. Existing integrated meshes based on Mach-Zehnder interferometers attain high weight precision, albeit at the expense of quadratic chip area and cascade insertion loss [6,7]; free-space diffractive networks scale to higher neuron counts, whereas alignment sensitivity precludes compact wafer-scale integration [8,9]. Here we demonstrate a programmable silicon slab-diffractive processor that decouples phase tuning from waveguide-mesh depth (Fig. 1). Using 64 thermo-optic slot elements on a 220 nm silicon-on-insulator chip, the processor attains 93.3% held-out classification accuracy (compared with 94.0% digital) within a 0.4 mm^2 active footprint."*

### Pass 4: Mandatory CLI Verification Gate
```bash
python3 scripts/pnn_intro_tool.py lint path/to/intro.txt --tier T1
python3 scripts/pnn_intro_tool.py query --tier T1 --native-only --top 3
```

---

## 3. Compact Pass/Fail Checklist
- [ ] `3-5` paragraphs, `420-680` words (T1) or `450-780` words (T2); zero TOC roadmap paragraph.
- [ ] Opens with a concrete physical/compute tension, zero `"In recent years"` filler.
- [ ] Every prior-art limitation names an objective physical law (`limited by`, `bound by`, `at the expense of`).
- [ ] Final paragraph states `"Here we..."`, quantitative hardware scale, comparator, and Fig. 1 pointer.
- [ ] Zero em-dashes, zero AI openers (`Notably,`, `Specifically,`, `Thus,`).

## 4. References & CLI
- Native-weighted exemplars: [`references/t1t2_annotated_exemplars.md`](./references/t1t2_annotated_exemplars.md) and [`references/t1t2_intro_corpus.jsonl`](./references/t1t2_intro_corpus.jsonl) (`49` native-primary `weight=2.0` sorted first).
