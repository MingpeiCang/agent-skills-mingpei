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
- breaking one sentence into multiple sentences unless the original structure genuinely requires it
- large-scale paragraph reordering without explicit user approval

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
