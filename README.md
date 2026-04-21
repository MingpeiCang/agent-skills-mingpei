# agent-skills-mingpei

> Reusable skills, prompts, references, and workflow scaffolds for AI agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/agent-runtime-portable-blue.svg)](https://github.com/MingpeiCang/agent-skills-mingpei)

`agent-skills-mingpei` is a personal but shareable collection of **agent-friendly skill packages**.
Each skill is designed to be as portable as possible across different agent runtimes — including **OpenClaw**, **Claude Code-style workflows**, and custom agent setups.

## Why this repository exists

Most useful agent workflows end up scattered across chats, notes, shell history, and half-finished prompts.
This repository is meant to keep them in one clean place:

- **Reusable** — skills should be easy to copy into another setup
- **Readable** — plain Markdown first, minimal lock-in
- **Self-contained** — references, assets, and helper scripts live with the skill
- **Portable** — avoid assuming one specific orchestration framework whenever possible

## What is a skill?

In this repository, a **skill** is a small, reusable task package for an AI agent.
A skill usually contains:

- a `SKILL.md` instruction file
- optional `references/` for background rules or mappings
- optional `scripts/` for helper automation
- optional `assets/` for bundled templates or static resources

## Repository structure

```text
skills/
  <skill-name>/
    SKILL.md          # main instructions for the agent
    references/       # domain rules, mappings, examples
    scripts/          # helper scripts or automation scaffolds
    assets/           # templates, sample files, static resources
```

## Included skills

### `invoice-reimbursement-docx`
Fill a reimbursement Word template from one or more invoices and output a completed DOCX.

**Use cases**
- invoice PDFs or scanned invoices
- multiple invoices in one run
- zip archives containing invoices
- workflows that must preserve invoice order and map invoice fields into a fixed reimbursement template

**Highlights**
- bundles the blank reimbursement template
- keeps field mapping rules explicit
- supports helper-script-based automation
- designed for document-heavy agent workflows

## Design principles

When adding new skills, this repository prefers:

1. **Clear task boundaries** — one skill should solve one class of problem well
2. **Local context over hidden magic** — important assumptions should live inside the skill folder
3. **Portable formats** — Markdown, simple scripts, and explicit assets beat opaque tooling
4. **Composable workflows** — skills should be easy to combine with other agent systems
5. **Human readability** — the repository should still make sense without a custom runtime

## Compatibility

This repository is written to stay broadly usable across multiple agent environments.

### Expected to work well with
- OpenClaw-style skill systems
- Claude Code / coding-agent workflows
- custom local agent runners
- prompt+script hybrid automations

### What may still vary by environment
- tool names and invocation methods
- file mounting / working-directory behavior
- available models and memory systems
- sandbox and network permissions

When a skill depends on environment-specific behavior, that dependency should be documented inside the skill itself.

## How to use this repo

### Option 1 — Browse and copy a skill
If you only need one skill, open its folder and copy the parts you need into your own agent setup.

### Option 2 — Clone the repository
```bash
git clone https://github.com/MingpeiCang/agent-skills-mingpei.git
```

Then inspect the `skills/` directory and adapt any skill to your own runtime.

### Option 3 — Treat it as a pattern library
Even if your agent framework uses a different format, the instruction structure, references, and helper scripts can still serve as a starting point.

## Roadmap

Planned directions for this repository:

- add more general-purpose reusable skills
- improve cross-agent compatibility notes
- add usage examples for different agent runtimes
- document packaging conventions for portable skills
- separate runtime-specific glue from skill logic where useful

## Contributing

This started as a personal repository, but the goal is to keep it **clean enough to share**.
If you want to reuse ideas from here, feel free to fork, adapt, and remix under the MIT license.

## License

MIT — see [LICENSE](./LICENSE).
