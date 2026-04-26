# <skill-name>

One-line summary of what the skill does and when it should be used.

## What this skill is for

Describe the core problem the skill solves.

## Use cases

- concrete workflow or request pattern
- concrete workflow or request pattern
- concrete workflow or request pattern

## Inputs

- primary user inputs or source files
- required bundled resources, if any

## Outputs

- expected deliverable
- optional side outputs such as logs, tables, or intermediate files

## Dependencies

- required skill, tool, or runtime
- optional dependency, if relevant

## Structure

```text
<skill-name>/
  SKILL.md
  README.md
  references/
  scripts/
  assets/
  agents/
```

## Folder guidance

- `SKILL.md`: required entry point and behavior contract.
- `README.md`: human-facing summary for the repository.
- `references/`: reusable guidance, style rules, mappings, or workflow notes.
- `scripts/`: helper automation used by the skill.
- `assets/`: bundled templates, examples, or other binary resources.
- `agents/`: provider-specific config only when needed.

## Notes

- Keep the README short. Put detailed operating rules in `SKILL.md` or `references/`.
- If a folder is unused, omit it instead of keeping empty placeholders.
