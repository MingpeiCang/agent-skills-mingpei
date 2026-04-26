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
- sentence count, unless the source already needs semicolon-scale punctuation

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

## When Near-Copy Is Correct

A near-copy is acceptable when:

- the source is already well aligned with the target style
- the only needed changes are local cleanup
- any larger rewrite would risk losing precision

The skill is not rewarded for changing more words. It is rewarded for making the best sentence under strict meaning preservation.
