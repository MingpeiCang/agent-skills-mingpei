# agent-skills-mingpei

Mingpei Cang's personal Codex skill repository.

## Included skills

### `invoice-reimbursement-hkustgz`
Fill a HKUST(GZ) reimbursement Word template from one or more invoices and output a completed DOCX.

Use cases:
- invoice PDFs or scanned invoices
- multiple invoices in one run
- zip archives containing invoices
- workflows that must preserve invoice order and map invoice fields into a fixed reimbursement template

Highlights:
- bundles the blank reimbursement template
- keeps field mapping rules explicit
- requires `minimax-docx` for Word processing

### `rewrite-as-ns`
Rewrite scientific or technical text in a distilled manuscript style while preserving technical meaning and scope.

Use cases:
- sentence-level manuscript polishing
- short batch rewriting for papers, reviews, or response letters
- technical prose cleanup with strict meaning preservation
- style-guided repair of minor citation debris or formatting noise

Highlights:
- emphasizes meaning preservation over aggressive rewriting
- separates core style imitation from editorial overlay
- bundles references for quality gate, protected spans, and line-edit discipline

## Compatibility

These skills are intended to stay usable across multiple agent environments, including Codex-style and OpenClaw-style workflows.

## Structure

```text
skills/
  invoice-reimbursement-hkustgz/
  rewrite-as-ns/
```
