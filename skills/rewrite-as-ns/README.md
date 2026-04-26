# rewrite-as-ns

Rewrite scientific or technical text in a distilled manuscript style while preserving technical meaning and claim scope.

## What this skill is for

This skill is for sentence-level or short-batch rewriting where style should improve but the scientific content, polarity, modality, and scope must remain intact.

## Use cases

- manuscript sentence polishing
- short batch rewriting for papers, rebuttals, or review sheets
- technical prose cleanup with strict meaning preservation
- repair of minor citation debris or formatting noise when the intended wording is recoverable

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
  agents/
```

## Folder guidance

- `references/style-spec.md`: primary target style definition.
- `references/quality-gate.md`: final validation rules.
- `references/editorial-layer.md`: sentence-level editing discipline.
- `agents/openai.yaml`: provider-specific config shipped with the skill.

## Notes

- Prefer the lightest rewrite that materially improves the sentence.
- Do not invent missing content when the source is meaning-critical and unrecoverable.
- This skill is the primary rewrite path and should not fall back to the older rule-based baseline.
