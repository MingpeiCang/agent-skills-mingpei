# Quality Gate

Run this check before returning any rewrite.

## Hard Constraints

The rewrite must preserve:

- scientific claim
- entities, materials, methods, and systems
- numbers and units
- polarity
- modality and hedge strength
- causal and contrast relations
- source sentence boundaries by default
- sentence-count changes only when boundary planning justifies a merge or split under explicit safety rules

## Source Repair Rules

When the source contains minor corruption, repair only what is clearly recoverable.

Allowed repairs:

- normalize broken punctuation and spacing
- remove obvious citation residue such as dangling reference numbers
- repair clear compound splits such as `statelevel` -> `state level`
- repair line-merge artifacts when one clause is obviously unrelated debris
- normalize apostrophes and dashes if the source encoding is broken

Do not guess when:

- the damaged token could be more than one plausible term
- an omitted clause changes the scientific meaning
- the source appears to contain two unrelated merged sentences and the boundary is unclear

## Rewrite Decision Ladder

Ask these in order:

1. Is the source already in the target style?
2. If yes, can `minimal_polish` improve only punctuation, grammar, or clarity?
3. If no, would a clearer rhetorical frame improve the sentence without changing the claim?
4. If the source is noisy, is the intended wording still recoverable?

Choose the least aggressive rewrite that produces a better sentence.

## Boundary Safety Check

Before you return the rewrite, confirm:

1. Did I decide any merge or split before rewriting rather than during ad hoc sentence polishing?
2. Did I preserve every technical claim?
3. Did I preserve every number, unit, qualifier, and named entity?
4. Did I keep the same hedge strength?
5. Did I preserve the causal, contrastive, and inferential relations?
6. Did I preserve every protected span exactly?
7. Did I record the source-to-output mapping when boundaries changed?
8. Does the boundary change improve clarity rather than merely changing sentence count?

If any answer is `no`, revise the rewrite.

## Self-Check Questions

Before you return the rewrite, confirm:

1. Did I preserve every technical claim?
2. Did I preserve every number, unit, qualifier, and named entity?
3. Did I keep the same hedge strength?
4. Did I preserve the causal, contrastive, and inferential relations?
5. Did I avoid importing domain nouns from examples?
6. Did I avoid adding significance language not present in the source?
7. Is the rewrite more readable or more clearly structured than the source?

If any answer is `no`, revise the rewrite.

## Quantitative Style Checks

Use these as guardrails, not hard limits.

### Sentence Length Check

| Section | Target Range | Flag If Outside |
|---------|-------------|-----------------|
| Abstract | 19–30 words | < 10 or > 50 |
| Main | 18–32 words | < 10 or > 50 |
| Results | 19–34 words | < 10 or > 60 |
| Methods | 16–30 words | < 10 or > 50 |

- If the rewrite is significantly longer than the source and outside the target range, tighten it.
- If the rewrite is significantly shorter, check that no content was lost.

### Voice and Tense Check by Section

| Section | Expected Voice | Expected Tense |
|---------|---------------|----------------|
| Abstract | active (75%) | present simple (40.8%) |
| Main | active (67%) | present simple (38.1%) |
| Results | active (69%) | present (31.8%) + past (15.1%) |
| Methods | passive (60%) | past participle (29.4%) |

- If rewriting Methods text, do not force active voice — passive is the correct register.
- If rewriting Abstract text, do not force past tense — present is standard for stating findings.
- If rewriting Results text, past simple is acceptable for reporting specific experiments.

### Hedging Balance Check

| Section | Hedge Density (per 1,000 words) |
|---------|-------------------------------|
| Abstract | 6.8 |
| Main | 7.0 |
| Results | 7.2 |
| Methods | 3.3 |

- Do not remove hedges that are present in the source unless the user explicitly asks for stronger claims.
- Do not add hedges that are not in the source.
- Methods sections should have the lowest hedge density — procedural text does not need `may` or `might`.

### Clause Depth Check

- Target dependency tree depth: 4–9 edges for most sentences
- Flag sentences with depth 13+ as potential split candidates
- Methods sections trend shallower (50.5% in 4–6 range) — keep Methods sentences simple

## Overclaim Checklist

Flag and soften claims when:

| Flag word | Safer replacement |
|-----------|------------------|
| prove | show, demonstrate, suggest |
| conclusively | strongly, consistently |
| unprecedented | to our knowledge, rarely reported |
| best | among the strongest |
| unqualified first | to our knowledge, the first to |
| superior | improved, enhanced |
| always | in all tested cases |
| never | in no case examined |

Also flag when:
- a laboratory result is written as an immediate field-wide solution
- a single system is described as universally applicable
- correlation is rewritten as mechanism
- a comparison lacks a fair baseline
- a future application is stated as an achieved outcome

## When Near-Copy Is Correct

A near-copy is acceptable when:

- the source is already well aligned with the target style
- the only needed changes are local cleanup
- any larger rewrite would risk losing precision

The skill is not rewarded for changing more words. It is rewarded for making the best sentence under strict meaning preservation.
