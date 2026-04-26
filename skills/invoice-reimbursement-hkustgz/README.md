# invoice-reimbursement-hkustgz

Fill a HKUST(GZ) reimbursement Word template from one or more invoices and output a completed DOCX.

## What this skill is for

This skill handles reimbursement workflows where invoice contents must be mapped into a fixed Word template instead of returned as raw extracted data.

## Use cases

- multiple invoice PDFs or scanned invoices in one run
- zip archives that contain invoice files
- reimbursement workflows that must preserve invoice order
- document-heavy tasks that require a completed DOCX output

## Inputs

- one or more invoice PDFs or images
- optional zip archive that contains invoice files
- bundled template at `assets/reimbursement-template.docx`

## Outputs

- a completed reimbursement DOCX saved as a new file

## Dependencies

- `minimax-docx` for opening, editing, validating, and saving the Word document

## Structure

```text
invoice-reimbursement-hkustgz/
  SKILL.md
  README.md
  references/
  scripts/
  assets/
```

## Folder guidance

- `references/workflow.md`: field mapping and output rules.
- `scripts/fill_reimbursement.py`: helper scaffold for automation.
- `assets/reimbursement-template.docx`: bundled blank reimbursement template.

## Notes

- Keep one output row per invoice line item.
- Preserve invoice order in both the table and photo-caption placeholders.
- Use this skill when the target deliverable is the finished reimbursement document, not just invoice extraction.
