# Variation Playbook

Use this file when rewriting long articles, section-length batches, or any passage where many nearby sentences share the same rhetorical function.

The goal is controlled variation, not ornamental variation.

## Core Principle

Vary the sentence frame while keeping the same distilled voice. The voice comes from:

- restrained academic confidence
- explicit rhetorical structure
- compact syntax
- repeated use of the same small style-core lexicon

Do not chase novelty with unrelated synonyms.

## Voice and Tense by Section

Match voice and tense to the target section.

| Section | Active % | Passive % | Present | Past | Past Participle |
|---------|----------|-----------|---------|------|----------------|
| Abstract | 75% | 25% | 40.8% | 4.2% | 28.0% |
| Main | 67% | 33% | 38.1% | 7.3% | 29.4% |
| Results | 69% | 31% | 31.8% | 15.1% | 29.3% |
| Methods | 40% | 60% | 19.0% | 13.5% | 29.4% |

- **Abstract**: present tense for stating findings, active voice for `Here we ...` patterns
- **Results**: mix present (general findings) and past (specific experiments). Past simple is highest here (15.1%).
- **Methods**: predominantly past participle in passive constructions. Present simple for describing apparatus or stating equations.
- Do not force active voice in Methods — passive is the correct register

## Transition Economy

Prefer sentence structure and clause order over explicit transitional adverbs when the relation is already clear.

Use explicit transitions only when they add real logical value, such as:

- marking a genuine contrast
- signaling a causal consequence
- introducing an additive point that would otherwise feel abrupt
- synthesizing several preceding results

Avoid transition inflation, for example:

- repeated `however` where simple clause structure is enough
- repeated `therefore` where the inference is already obvious
- repeated `moreover` or `furthermore` used only as stylistic filler

### Section Transition Profiles

Use these frequencies to choose transitions that match the target section register.

| Transition | Abstract | Main | Results | Methods |
|-----------|----------|------|---------|---------|
| however | 60 | 194 | 198 | 162 |
| also | 40 | 317 | 529 | 397 |
| thus | 17 | 84 | 205 | 151 |
| therefore | 9 | 105 | 111 | 168 |
| although | 15 | 116 | 204 | 105 |
| whereas | 10 | 64 | 175 | 88 |
| furthermore | 13 | 44 | 81 | 49 |
| notably | — | — | 97+97 | — |
| then | 7 | 95 | 154 | 812 |
| first | 13 | 128 | 198 | 376 |
| subsequently | — | — | — | 79 |
| finally | 8 | 30 | 64 | 100 |

Key section patterns:
- **Abstract**: minimal transitions — the `Here we ...` opener carries the structure. Use `however` (60) and `also` (40) sparingly.
- **Methods**: `then` dominates (812) — procedural sequencing. `first` (376) and `finally` (100) for step ordering.
- **Results**: richest transition vocabulary. `whereas` (175) and `notably` (97) are Results-signature words. `also` (529) for additive enumeration.
- **Main**: balanced, transitional — `however` (194), `also` (317), `although` (116).

## Repetition Guard

Within a rolling window of 3 to 5 nearby sentences:

- avoid repeating the same 3-word opener unless the discourse clearly demands it
- avoid repeating the same reporting verb more than twice if an equally faithful alternative exists
- avoid using the same implication frame repeatedly, for example three consecutive `This suggests that ...`
- avoid stacking several sentences with the exact same clause shape

Allowed repetitions:

- repeated `However, ...` in a limitations section
- repeated `We use ...` in a methods list
- repeated `These results ...` when the paragraph is intentionally cumulative

Even then, prefer light variation if fidelity allows.

## Rotation By Function

### Repeated result sentences

Rotate among:

- `We show that ...`
- `We find that ...`
- `We observe that ...`
- `Our results indicate that ...`
- `These results demonstrate ...`
- direct assertion without an author frame when the source is already clear

Also rotate clause shapes:

- `X increases with Y`
- `X decreases as Y increases`
- `Under Z, X remains Y`
- `We identify a transition from X to Y`
- `X is directly related to Y`

### Repeated method sentences

Rotate among:

- `We use ... to ...`
- `We employ ... to ...`
- `We determine ... by ...`
- `We quantify ... from ...`
- `We construct ... by integrating ...`
- `We optimize ... by varying ...`

Methods often need the least paraphrase. If the sentence is already good, use `minimal_polish`.

### Repeated contribution sentences

Rotate among:

- `We provide evidence that ...`
- `These findings provide insight into ...`
- `Our results reveal ...`
- `We identify ...`
- `This approach enables ...`
- `Together, these results suggest ...`

Avoid repeatedly starting with `Here we ...` unless the source repeatedly uses explicit author-framed contribution sentences.

### Repeated scope or implication sentences

Rotate among:

- `This suggests that ...`
- `These findings may ...`
- `The framework can be ...`
- `This approach may be useful for ...`
- `This observation may help ...`
- direct hedged statement without a leading implication frame

Guard the hedge level carefully. Variation must not strengthen the claim.

### Repeated transition sentences

Rotate among:

- `However, ...`
- `By contrast, ...`
- `In contrast, ...`
- `As a result, ...`
- `In addition, ...`
- `Furthermore, ...`
- `Moreover, ...`
- `Taken together, ...`
- `In summary, ...`

Choose the transition from logic, not from a desire for variety.

If two nearby sentences already connect naturally through subject continuity or causal structure, prefer no explicit transition in one of them.

## Paragraph-Level Alternation

When a paragraph contains several sentences of the same type:

1. Use one strong author-framed sentence.
2. Follow with one or two less explicit but still stylistically aligned sentences.
3. Use a cumulative transition only when the paragraph is genuinely synthesizing multiple observations.

Example pattern for a results paragraph:

- `We find that ...`
- direct result statement
- `These results indicate that ...`
- `Taken together, ...`

Example pattern for a methods paragraph:

- `We use ...`
- `We determine ...`
- `We construct ...`
- `We optimize ...`

## Lexical Density Control

Do not crowd one sentence with too many style-core markers.

Bad pattern:

- `Our results reveal a robust, general, quantitative, mechanistic picture ...`

Better pattern:

- choose one or two evaluations that the source really supports

## Safe Diversity Moves

- change the reporting verb while preserving function
- swap between active author frame and direct statement
- shorten or expand an appositive
- convert a colon explanation into an `evidence that` or `indicate that` clause
- change a trailing infinitive purpose phrase into a `to ...` or `thereby ...` form when it reads more cleanly
- remove an unnecessary transition adverb when the sentence remains coherent without it

## Unsafe Diversity Moves

- replacing a precise source verb with a broader but less accurate one
- adding significance terms not present in the source
- converting a possibility into a conclusion
- importing topical nouns from previous sentences or exemplars
- introducing a stronger contrast or stronger causality than the source provides
- inserting transitions simply to create surface variety
