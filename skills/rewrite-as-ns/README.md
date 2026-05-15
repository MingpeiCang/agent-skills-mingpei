# rewrite-as-ns

Rewrite scientific or technical text in a distilled manuscript style while preserving technical meaning and claim scope.

## What this skill is for

This skill is for sentence-level, paragraph-level, or section-level rewriting where style should improve but the scientific content, polarity, modality, and scope must remain intact.

## Use cases

- manuscript sentence polishing
- paragraph- and section-level restructuring
- short batch rewriting for papers, rebuttals, or review sheets
- technical prose cleanup with strict meaning preservation
- repair of minor citation debris or formatting noise when the intended wording is recoverable
- Chinese-to-English academic translation with logic reconstruction

## Inputs

- source scientific or technical text
- bundled style guidance in `references/`

## Outputs

- rewritten text in the target style
- concise `editor_feedback` by default unless the caller asks for another format

## Dependencies

- no external skill dependency is required

## Structure

```text
rewrite-as-ns/
  SKILL.md
  README.md
  references/
    writing-strategy.md    # paper type, reader workflow, diagnosis, claim-evidence-boundary
    section-moves.md       # section move orders, evidence strength, phrase families
    style-spec.md          # quantitative style targets, lexical tendencies
    lexicon-bank.md        # frequency-ranked vocabulary, collocations, transitions
    template-bank.md       # structural templates by function and section
    variation-playbook.md  # controlled variation for long texts
    exemplars.md           # before/after examples by function and section
    function-map.md        # sentence rhetorical classification
    quality-gate.md        # validation rules, overclaim checks
    editorial-layer.md     # editorial overlay, editor_feedback format
    protected-spans.md     # content that must be preserved exactly
    line-edit-playbook.md  # sentence-level editing discipline, boundary planning
  agents/
    openai.yaml
```

## Folder guidance

- `references/writing-strategy.md`: writing strategy layer — paper type identification, reader workflow, hourglass structure, claim-evidence-boundary, diagnosis-before-edit, section responsibilities, overclaim control, Chinese-to-English mode.
- `references/section-moves.md`: section-specific move orders and phrase families derived from Academic Phrasebank, with evidence strength hierarchy (strong/moderate/speculative).
- `references/style-spec.md`: primary target style definition. Includes sentence length targets, passive voice ratios, verb/adjective/adverb frequency rankings, section-specific voice and tense guidance.
- `references/quality-gate.md`: final validation rules including hard constraints, quantitative style checks, overclaim checklist, and self-check questions.
- `references/editorial-layer.md`: sentence-level editing discipline and `editor_feedback` format.
- `references/lexicon-bank.md`: frequency-ranked vocabulary, section-specific verb selection, high-frequency bigrams/trigrams, transition word frequency by section.
- `references/template-bank.md`: structural templates organized by rhetorical function (contribution/result/method/scope/transition), with section-specific variants (Abstract signatures, Methods passive, Results hedged/contrast).
- `references/variation-playbook.md`: controlled variation strategies for long texts — transition economy, voice/tense by section, rotation by function, paragraph-level alternation.
- `references/exemplars.md`: before/after rewrite examples by function and section, with analysis of why each change works.
- `references/function-map.md`: sentence rhetorical classification (contribution, method, result, scope, transition) with typical cues and preferred moves.
- `references/protected-spans.md`: content protection rules for `[[...]]` spans, equations, code identifiers, chemical formulas.
- `references/line-edit-playbook.md`: allowed/restricted editing moves, boundary planning triggers for sentence merge/split.
- `agents/openai.yaml`: provider-specific config shipped with the skill.

## Acknowledgments

The writing strategy layer (`writing-strategy.md`, `section-moves.md`) and the strategic concepts in `SKILL.md` (paper type identification, reader workflow model, claim-evidence-boundary framework, diagnosis-before-edit priority, section responsibilities, overclaim control, Chinese-to-English mode) are adapted from the `nature-polishing` skill by Yuan1z, which itself is built from academic writing course notes and the Academic Phrasebank.

## Notes

- Prefer the lightest rewrite that materially improves the sentence.
- Do not invent missing content when the source is meaning-critical and unrecoverable.
- This skill is the primary rewrite path and should not fall back to the older rule-based baseline.
- The 9-step workflow includes diagnosis before editing: identify the failure mode before rewriting.
- Use `writing-strategy.md` for paragraph/section-level tasks and `section-moves.md` for section-specific guidance.
