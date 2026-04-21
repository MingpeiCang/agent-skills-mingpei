# agent-skills-mingpei

A personal collection of reusable skills, prompts, references, and workflow scaffolds for AI agents.

## Goals
- Keep skills reusable across different agent runtimes
- Store each skill in a self-contained folder
- Bundle references, assets, and helper scripts when useful
- Prefer plain Markdown and simple folder conventions over platform lock-in

## Suggested layout

```text
skills/
  <skill-name>/
    SKILL.md
    references/
    scripts/
    assets/
```

## Included skills
- `invoice-reimbursement-docx` — fill a reimbursement Word template from invoice files and output a completed DOCX.

## Portability notes
This repository is intended to stay broadly usable across agent systems such as OpenClaw, Claude Code workflows, and other custom agent setups. Some skills may still rely on local tools or environment-specific dependencies; those should be documented inside each skill folder.
