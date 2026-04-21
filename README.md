# invoice-reimbursement-hkustgz

A portable skill for filling HKUST(GZ) reimbursement Word templates from invoice files.

## Included skill

### `invoice-reimbursement-hkustgz`
Fill a reimbursement Word template from one or more invoices and output a completed DOCX.

**Use cases**
- invoice PDFs or scanned invoices
- multiple invoices in one run
- zip archives containing invoices
- requests like “帮我填写以下报销单”
- workflows that must preserve invoice order and map invoice fields into a fixed reimbursement template

**Highlights**
- bundles the blank reimbursement template
- keeps field mapping rules explicit
- requires `minimax-docx` for Word processing
- designed for document-heavy agent workflows

## Compatibility

This skill is intended to stay usable across multiple agent environments, including OpenClaw and Claude Code-style workflows.

## Structure

```text
invoice-reimbursement-hkustgz/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```
