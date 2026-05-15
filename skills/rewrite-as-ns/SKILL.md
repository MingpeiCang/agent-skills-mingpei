---
name: rewrite-as-ns
description: Use when the user wants scientific or technical text rewritten in a distilled target style with strict meaning preservation, sentence-level editorial control, and concise editor feedback, especially for manuscript-style rewriting without rule-based fallback or external API use.
---

# Rewrite as NS

Use this skill for scientific and technical style imitation when the rewrite must preserve the full technical meaning while following a bundled target style specification.

This skill is the primary rewrite path. Do not rely on the old rule-based baseline as a fallback.

## Two Layers

This skill operates through two tightly coupled layers:

1. `core_style_imitation`
   - preserve the distilled voice
   - preserve scientific meaning
   - choose the lightest rewrite that produces a better sentence
2. `editorial_overlay`
   - preserve protected spans
   - enforce sentence-level editing discipline
   - reduce unnecessary jargon and repetition
   - append concise `editor_feedback` after the rewrite by default

## Read Order

1. Read [references/style-spec.md](references/style-spec.md) and [references/quality-gate.md](references/quality-gate.md) for any rewrite task.
2. Read [references/writing-strategy.md](references/writing-strategy.md) when the task involves paragraph- or section-level rewriting, argument restructuring, or Chinese-to-English translation.
3. Read [references/section-moves.md](references/section-moves.md) when rewriting a specific section (Introduction, Results, Discussion, Methods, Conclusion, Abstract, or Title).
4. Read [references/editorial-layer.md](references/editorial-layer.md), [references/protected-spans.md](references/protected-spans.md), and [references/line-edit-playbook.md](references/line-edit-playbook.md) for any rewrite task that resembles manuscript editing.
5. Read [references/function-map.md](references/function-map.md) if the sentence function is unclear or the batch mixes several function types.
6. For long-form writing or repeated sentence-by-sentence rewriting, read:
   - [references/lexicon-bank.md](references/lexicon-bank.md)
   - [references/template-bank.md](references/template-bank.md)
   - [references/variation-playbook.md](references/variation-playbook.md)
7. Read [references/exemplars.md](references/exemplars.md) when the user wants examples, batch consistency, or closer imitation of the distilled style.

## Scope

- single scientific sentence rewrite
- short batch rewrite
- sentence-by-sentence rewriting inside a paragraph, table, or review sheet
- style-guided repair of minor citation debris or encoding noise when the intended wording is still recoverable

## Core Workflow

1. Determine the unit of work and the requested output format.
2. Identify the paper type (research / methods / hypothesis / algorithmic). This governs narrative logic.
3. Diagnose the failure mode before editing:
   - wrong paper type logic
   - missing gap or poor positioning
   - claim without evidence
   - evidence without a clear claim
   - missing boundary or limitation
   - Results and Discussion mixed together
   - weak title or abstract signal
   - sentence-level clutter only
   Prioritize: `paper type → section job → paragraph logic → claim/evidence/boundary → sentence polish`
4. Plan sentence boundaries for the current unit.
5. Classify the resulting unit by rhetorical function.
6. Choose the rewrite mode:
   - `minimal_polish`
   - `structural_rewrite`
   - `repair_rewrite`
7. Rewrite the unit. Apply the two layers (core style imitation + editorial overlay).
8. Run the quality gate before returning the result.
9. Return the rewritten text followed by concise `editor_feedback`, unless the user explicitly asks for a different review or table format.

## Boundary Planning

- preserve source sentence boundaries by default
- allow automatic merge or split only when the user has not forbidden boundary changes and the clarity gain is clear
- make boundary decisions before rhetorical classification and rewrite-mode selection
- preserve source-to-output mapping whenever a merge or split occurs so batch output and feedback can report it

## Rewrite Modes

- `minimal_polish`: The source is already close to the target style. Fix punctuation, redundancy, small grammar issues, citation debris, or minor formatting noise only.
- `structural_rewrite`: The meaning is intact but the sentence becomes clearer if its evidence, method, result, contrast, or implication structure is made more explicit.
- `repair_rewrite`: The source contains small, recoverable corruption such as broken spacing, merged fragments, or citation residue. Repair only what is clearly inferable from the source.

If the damage is meaning-critical and not reconstructable, say so briefly instead of inventing content.

## Batch Rules

- Keep one row per source sentence by default.
- If boundary planning approves a merge or split, allow `many-to-one` or `one-to-many` output only when the source-to-output mapping is preserved.
- Preserve source order unless the user explicitly asks for reorganization.
- For tabular output, default columns are:
  - `id`
  - `source_ids`
  - `boundary_action`
  - `function_group`
  - `source_text`
  - `rewritten_text`
  - `editor_feedback`
- Use `boundary_action` values such as `preserved`, `merged`, or `split`, and use `source_ids` to show which source sentence(s) feed each output unit.
- For paragraph tasks, preserve local discourse markers and adjacency logic across neighboring sentences.
- For long articles, vary opener families and reporting verbs across nearby sentences unless the source discourse requires repetition.

## Non-Negotiables

- Preserve numbers, named entities, polarity, modality, causality, and claim scope.
- Do not import topic nouns from examples or from unrelated source sentences.
- Do not force a template when the source sentence is already strong.
- Do not inflate claims.
- Allow sentence merges or splits only when boundary planning approves them under explicit safety rules.
- Do not let a boundary change alter hedge strength, causal relation, contrast relation, protected spans, or claim scope.

## When To Stay Conservative

- dense method sentences
- transition sentences that already have the right opener
- scope sentences containing `may`, `could`, `can`, `likely`, or similar hedges
- already polished contribution sentences that only need local cleanup

## Claim-Evidence-Boundary

Every important scientific statement should have three parts:

1. **Claim**: what is being said
2. **Evidence**: what supports it
3. **Boundary**: where the claim stops, or what uncertainty remains

When polishing, repair these failures before polishing rhythm:
- claim without evidence → add data, citation, or mechanism
- data without an explicit point → surface the finding
- implication without a scope condition → add boundary language

## Chinese-to-English Mode

When the source is Chinese or strongly Chinese-influenced English:

1. Extract core propositions first — do not translate clause-by-clause
2. Reconstruct explicit logical links: contrast, cause, implication, limitation
3. Verify terminology, causality, hedging, and disciplinary nuance
4. Keep key technical terms stable
5. Remove Chinese discourse patterns (e.g., excessive `With the development of...`, `In recent years, more and more...`)

## Deliverables

- Direct rewrite request: output the rewritten text first, then append a concise `editor_feedback` block.
- Review or evaluation request: include clear pairwise fields and short failure notes.
- When a merge or split occurs, note the `boundary_action` and the reason briefly in `editor_feedback` unless the user explicitly asks for output without feedback.
- Default `editor_feedback` should be brief and concrete:
  - what changed
  - why the change improves clarity or style
  - any residual caution about scope, hedge strength, or technical precision
