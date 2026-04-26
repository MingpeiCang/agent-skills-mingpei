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
2. Read [references/editorial-layer.md](references/editorial-layer.md), [references/protected-spans.md](references/protected-spans.md), and [references/line-edit-playbook.md](references/line-edit-playbook.md) for any rewrite task that resembles manuscript editing.
3. Read [references/function-map.md](references/function-map.md) if the sentence function is unclear or the batch mixes several function types.
4. For long-form writing or repeated sentence-by-sentence rewriting, read:
   - [references/lexicon-bank.md](references/lexicon-bank.md)
   - [references/template-bank.md](references/template-bank.md)
   - [references/variation-playbook.md](references/variation-playbook.md)
5. Read [references/exemplars.md](references/exemplars.md) when the user wants examples, batch consistency, or closer imitation of the distilled style.

## Scope

- single scientific sentence rewrite
- short batch rewrite
- sentence-by-sentence rewriting inside a paragraph, table, or review sheet
- style-guided repair of minor citation debris or encoding noise when the intended wording is still recoverable

## Core Workflow

1. Determine the unit of work and the requested output format.
2. Classify the source sentence by rhetorical function.
3. Choose the rewrite mode:
   - `minimal_polish`
   - `structural_rewrite`
   - `repair_rewrite`
4. Rewrite the sentence.
5. Run the quality gate before returning the result.
6. Return the rewritten text followed by concise `editor_feedback`, unless the user explicitly asks for a different review or table format.

## Rewrite Modes

- `minimal_polish`: The source is already close to the target style. Fix punctuation, redundancy, small grammar issues, citation debris, or minor formatting noise only.
- `structural_rewrite`: The meaning is intact but the sentence becomes clearer if its evidence, method, result, contrast, or implication structure is made more explicit.
- `repair_rewrite`: The source contains small, recoverable corruption such as broken spacing, merged fragments, or citation residue. Repair only what is clearly inferable from the source.

If the damage is meaning-critical and not reconstructable, say so briefly instead of inventing content.

## Batch Rules

- Keep one row per source sentence unless the user explicitly asks for merged prose.
- Preserve source order unless the user explicitly asks for reorganization.
- For tabular output, default columns are:
  - `id`
  - `function_group`
  - `source_text`
  - `rewritten_text`
  - `editor_feedback`
- For paragraph tasks, preserve local discourse markers and adjacency logic across neighboring sentences.
- For long articles, vary opener families and reporting verbs across nearby sentences unless the source discourse requires repetition.

## Non-Negotiables

- Preserve numbers, named entities, polarity, modality, causality, and claim scope.
- Do not import topic nouns from examples or from unrelated source sentences.
- Do not force a template when the source sentence is already strong.
- Do not inflate claims.
- Do not split one sentence into two unless the source already requires semicolon-scale structure.

## When To Stay Conservative

- dense method sentences
- transition sentences that already have the right opener
- scope sentences containing `may`, `could`, `can`, `likely`, or similar hedges
- already polished contribution sentences that only need local cleanup

## Deliverables

- Direct rewrite request: output the rewritten text first, then append a concise `editor_feedback` block.
- Review or evaluation request: include clear pairwise fields and short failure notes.
- Default `editor_feedback` should be brief and concrete:
  - what changed
  - why the change improves clarity or style
  - any residual caution about scope, hedge strength, or technical precision
