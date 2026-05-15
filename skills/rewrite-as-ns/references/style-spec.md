# Style Spec

This file captures the distilled target style. Use it as guidance, not as a template catalog to force onto every sentence.

## Primary Style Signals

- precise, high-information phrasing
- restrained academic confidence
- explicit rhetorical structure when useful
- one-sentence completeness
- compact syntax over ornamental paraphrase
- clear clause architecture within the chosen output unit, whether it preserves the original boundary or follows approved boundary planning

## Quantitative Targets

These are quantitative guidelines for Nature-style writing.

### Sentence Length

| Section | Median | P25–P75 | Target Range |
|---------|--------|---------|--------------|
| Abstract | 24 | 19–30 | 19–30 |
| Main | 25 | 18–32 | 18–32 |
| Results | 26 | 19–34 | 19–34 |
| Methods | 22 | 16–30 | 16–30 |

- 73–78% of sentences fall in the 11–30 word range
- Sentences over 50 words appear in fewer than 5% of cases
- Aim for the target range; do not force uniform length

### Passive Voice Ratio

| Section | Passive Rate |
|---------|-------------|
| Abstract | 25% |
| Main | 33% |
| Results | 31% |
| Methods | 60% |

- Methods sections are predominantly passive; respect this convention
- Abstract and Results should favor active voice with selective passive use
- Main sections mix both, with active slightly preferred

### Information Density

| Section | Content Word Ratio | TTR |
|---------|-------------------|-----|
| Abstract | 66.5% | 0.207 |
| Main | 62.4% | 0.081 |
| Results | 62.9% | 0.066 |
| Methods | 58.5% | 0.056 |

- Abstracts have the highest information density and lexical diversity
- Methods are the most formulaic; this is expected and correct

## Lexical Tendencies

These are tendencies, not quotas.

### Verbs (by frequency)

Root verbs (sentence-level predicates), ranked:

| Rank | Verb | Frequency | Typical Function |
|------|------|-----------|-----------------|
| 1 | be | 4,168 | copula, passive auxiliary |
| 2 | use | 1,305 | method |
| 3 | show | 1,256 | result, contribution |
| 4 | perform | 645 | method |
| 5 | have | 469 | possession, result |
| 6 | find | 388 | result |
| 7 | provide | 385 | contribution |
| 8 | observe | 364 | result |
| 9 | obtain | 301 | method, result |
| 10 | calculate | 286 | method |
| 11 | measure | 280 | method |
| 12 | demonstrate | 277 | contribution |
| 13 | suggest | 268 | scope, implication |
| 14 | indicate | 268 | result, scope |
| 15 | reveal | 183 | result, contribution |

Style-core verbs for voice markers: `provide`, `enable`, `suggest`, `support`, `reveal`, `establish`, `capture`

### Adjectives (by frequency)

| Rank | Adjective | Frequency |
|------|-----------|-----------|
| 1 | high | 1,846 |
| 2 | low | 1,054 |
| 3 | large | 937 |
| 4 | mechanical | 825 |
| 5 | different | 761 |
| 6 | same | 702 |
| 7 | small | 656 |
| 8 | single | 614 |
| 9 | human | 545 |
| 10 | magnetic | 484 |
| 11 | thermal | 482 |
| 12 | similar | 451 |
| 13 | experimental | 431 |
| 14 | specific | 403 |
| 15 | soft | 396 |

Style-core adjectives for voice markers: `important`, `general`, `robust`, `relevant`, `quantitative`, `mechanistic`, `novel`, `applicable`

### Adverbs (by frequency)

| Rank | Adverb | Frequency |
|------|--------|-----------|
| 1 | also | 1,283 |
| 2 | then | 1,068 |
| 3 | only | 704 |
| 4 | well | 648 |
| 5 | here | 646 |
| 6 | however | 614 |
| 7 | more | 580 |
| 8 | respectively | 558 |
| 9 | approximately | 521 |
| 10 | far | 509 |
| 11 | thus | 457 |
| 12 | therefore | 393 |

Style-core adverbs for voice markers: `directly`, `generally`, `readily`, `widely`, `closely`, `precisely`, `broadly`

### High-Frequency Bigrams

These appear consistently across sections and are safe to use naturally:

- `of the`, `in the`, `to the`, `with the`, `on the`, `from the`, `by the`
- `can be`, `such as`, `shown in`, `as well as`, `in which`, `that the`
- `here we`, `we show`, `we find`, `show that`, `we demonstrate`

### High-Frequency Trigrams

- `we show that` (Abstract: 34, strongest Abstract signature)
- `here we show` (Abstract: 23)
- `here we report` (Abstract: 17)
- `here we demonstrate` (Abstract: 13)
- `we find that` (Abstract: 10)
- `as well as` (all sections)
- `owing to the` (all sections)
- `as shown in` (Main, Results)
- `was used to` (Methods)
- `at room temperature` (Methods)
- `extended data fig` (Main, Results — reference pattern)

### Reusable Phrase Shapes

- `provide evidence that ...`
- `enable ...`
- `suggest that ...`
- `play an important role in ...`
- `over a wide range of ...`
- `at high resolution`
- `high performance`
- `intrinsic property`
- `orders of magnitude` (77 occurrences)
- `a wide range` (69 occurrences)
- `shed light on` (7 occurrences)
- `pave the way` (5 occurrences)

### Nominalization Patterns

Nature-style writing heavily nominalizes abstract processes. Common suffixes: `-tion`, `-sion`, `-ment`, `-ness`, `-ity`, `-ence`, `-ance`.

Top nominalized forms: `temperature` (1,212), `function` (553), `structure` (538), `pressure` (537), `density` (495), `motion` (487), `solution` (478), `activity` (465), `distribution` (406), `performance` (399), `transition` (386), `deformation` (337), `resolution` (364), `expression` (362).

Use nominalization to compress clauses (`the deformation of` instead of `how it deforms`), but do not over-nominalize at the expense of readability.

Do not insert these words unless they make the sentence more precise.

## Preferred Openers

Use these only when they match the source function naturally.

- contribution: `Here we ...`, `In this work, we ...`, `We provide ...`
- result: `We show that ...`, `We find that ...`, `We observe that ...`, `Our results indicate that ...`
- method: `We use ...`, `We employ ...`, `We design ...`
- implication: `This suggests that ...`, `These findings may ...`, `In principle, ...`
- transition: `However, ...`, `By contrast, ...`, `In contrast, ...`, `Therefore, ...`, `As a result, ...`

### Opener Frequency by Section (Top 5)

| Opener | Abstract | Main | Results | Methods |
|--------|----------|------|---------|---------|
| The | 10.9% | 16.7% | 16.4% | 25.3% |
| Here | 9.7% | 1.3% | — | — |
| We | 8.5% | 5.9% | 8.6% | 5.8% |
| This | 6.1% | 5.8% | 5.7% | 3.2% |
| Our | 4.7% | 1.4% | 2.0% | — |

- Abstract: `Here we ...` is the signature opener (9.7%), unique to this section
- Methods: `The` dominates (25.3%) — passive, object-first constructions
- Results: `We` is strongest here (8.6%) — active author-framed results

## Section-Specific Voice and Tense

### Abstract

- **Voice**: active preferred (75% active)
- **Tense**: present simple dominant (40.8%), past participle for passive (28.0%)
- **Signature pattern**: `Here we report/demonstrate/show a [X] that [Y]`
- **Hedging**: moderate (6.8 per 1,000 words), `can`, `could`, `may`
- **Density**: highest content-word ratio (66.5%), most lexically diverse (TTR 0.207)

### Main (Introduction / Discussion)

- **Voice**: mixed, slight active preference (67% active)
- **Tense**: present simple (38.1%), past simple for prior work (7.3%)
- **Hedging**: moderate (7.0 per 1,000 words)
- **Pattern**: `The N of` structure (22.3%), `which` relative clauses (10.8%)

### Results

- **Voice**: mixed, slight active preference (69% active)
- **Tense**: present simple (31.8%) + past simple (15.1%) for reporting findings
- **Hedging**: highest density (7.2 per 1,000 words) — results require epistemic care
- **Pattern**: `Compared to/with` (2.5%), `while/whereas/unlike` contrasts (3.5%)
- **Boosting**: `demonstrate`, `indeed`, `show that` strongest here

### Methods

- **Voice**: predominantly passive (60% passive)
- **Tense**: past participle dominant (29.4%) from passive constructions, present simple (19.0%)
- **Hedging**: lowest density (3.3 per 1,000 words) — methods are procedural, not inferential
- **Pattern**: `by + V-ing` (4.7%), `the N of` (17.8%), `then` (814 occurrences)
- **Opener**: `The` dominates (25.3%) — object-first passive style

## Rhetorical Devices

### Contrast (use selectively)

| Expression | Corpus Total | Best Section |
|-----------|-------------|-------------|
| while | 370 | Methods (152) |
| whereas | 337 | Results (175) |
| by contrast | 138 | Results (80) |
| in contrast | 98 | Results (37) |
| unlike | 56 | Results (23) |

### Emphasis (use sparingly)

| Expression | Corpus Total |
|-----------|-------------|
| orders of magnitude | 77 |
| a wide range | 69 |
| unprecedented | 18 |
| most notably | 4 |
| the vast majority | 6 |

### Hedging vs. Boosting Balance

- **Hedging verbs** (per 1,000 words): `can` (highest), `may`, `could`, `suggest`, `indicate`, `would`, `might`
- **Boosting verbs**: `demonstrate` (277 total), `show that` (52 in Abstract), `reveal` (183), `confirm`, `establish`
- Results sections use the most hedging; Methods use the least
- Boosting is concentrated in Results and Main sections

## Clause Depth Guidance

Dependency tree depth targets (measured in edges from root):

| Depth Range | Percentage |
|-------------|-----------|
| 1–3 | 3–7% |
| 4–6 | 40–51% |
| 7–9 | 33–41% |
| 10–12 | 8–13% |
| 13+ | 2–4% |

- Target depth 4–9 for most sentences
- Methods trend shallower (50.5% in 4–6 range)
- Abstract and Results trend slightly deeper
- Sentences with depth 13+ are rare and often candidates for splitting

## Structural Preferences

- prefer explicit `evidence that`, `suggests that`, `indicates that` framing when the source is making an evidential or inferential claim
- make monotonic relations explicit: `increases as`, `decreases with`, `remains ... under`
- keep causal relations visible: `thereby`, `because`, `through`, `by`
- tighten long appositive tails when they obscure the main claim
- keep lists parallel

## Anti-Patterns

- generic filler such as `provides a foundation for ...` unless the source genuinely makes that claim
- inflated significance language not present in the source
- topic nouns imported from unrelated examples
- turning a cautious implication into a direct claim
- adding `Here we ...` to sentences that are not author-framed
- paraphrasing away technical detail to make the sentence sound smoother
