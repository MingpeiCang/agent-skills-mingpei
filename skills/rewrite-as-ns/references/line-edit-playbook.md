# Line Edit Playbook

Use this file when the task is sentence-level manuscript refinement rather than free rewriting.

## Core Discipline

- edit sentence by sentence
- preserve sentence order by default
- do not rewrite an entire paragraph as one block unless the user explicitly asks for that
- improve each sentence locally before attempting any broader reorganization

## Allowed Moves

- tighten redundancy
- clarify clause attachment
- improve parallelism
- repair punctuation, agreement, and local grammar
- replace bloated phrasing with cleaner scientific wording
- strengthen continuity between adjacent sentences through local syntax

## Restricted Moves

- inserting new scientific claims
- changing argument scope
- merging multiple sentences into one block by default
- breaking one sentence into multiple sentences by default
- large-scale paragraph reordering without explicit user approval

## Boundary Planning Triggers

Use boundary planning before classification or rewriting when sentence-boundary changes are being considered.

### Allow automatic merge of adjacent simple sentences only when:

- the adjacent sentences share the same topic or subject chain
- the second sentence directly supplements the first rather than opening a new contrast, claim, or scope
- the merge preserves hedge strength
- the merge preserves local causal, contrastive, and conditional relations
- the merged output remains clear as a single sentence

### Allow automatic split of an overloaded sentence only when:

- the source contains two or more clearly separable clause layers
- the sentence carries multiple heavy functions such as method, result, or implication in a way that harms readability
- the split preserves the original logic links explicitly
- the split does not create dangling references or scope drift

### Block merge or split when:

- the source is a dense method sentence
- the sentence is a hedge-sensitive scope sentence containing `may`, `could`, `can`, `likely`, or similar qualifiers
- protected spans cross the likely boundary point
- figure, table, or citation anchors depend strongly on the current sentence structure
- the task requires strict sentence-by-sentence alignment and the user has not allowed boundary changes
- the sentence-count change does not produce a meaningful clarity gain

## Word Choice Guidance

- prefer the smallest change that makes the sentence clearer
- avoid unnecessary jargon if a simpler technical expression is equally precise
- keep scientific rigor
- avoid editorial grandstanding

## Local Flow Guidance

- prefer clause-level smoothing to heavy transition insertion
- if the logic is already visible, do not add `however`, `therefore`, or `moreover` just to sound academic
- if a connection is needed, choose the weakest connective that accurately expresses the relation

## Default Feedback Expectation

For each rewritten sentence or sentence row, `editor_feedback` should state:

- the main edit type, such as tightening, clarification, or protected-span preservation
- whether the sentence stayed close to the source or was structurally reorganized

Keep the feedback short.
