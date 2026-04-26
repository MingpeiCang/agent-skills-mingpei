---
name: invoice-reimbursement-hkustgz
description: Fill a reimbursement Word template from one or more invoices, including PDFs or zip archives of invoices, and output a completed DOCX. Use when the task is to extract invoice line items, map them into the reimbursement template, handle discount lines, preserve invoice order, bundle the blank template into the skill, or when Mingpei asks things like "帮我填写以下报销单".
---

# Invoice Reimbursement HKUST(GZ)

Fill the bundled reimbursement template from invoice contents and return a completed DOCX.

## Use this skill
- Multiple invoices, PDF invoices, scanned invoices, or a zip archive of invoices.
- Need a filled reimbursement DOCX, not just extracted invoice data.
- Need the blank template bundled with the skill.
- Need to process Word files with `minimax-docx`.

## Dependencies
- `minimax-docx` for DOCX creation, editing, and validation. Use it to process Word files for this skill.
- No other skill is required.

## Workflow
1. Use `minimax-docx` to open, edit, and validate the reimbursement Word template.
2. Unpack any zip archive and collect invoice files.
3. Extract each invoice line item, totals, and any discount/reduction lines.
4. Map fields exactly:
   - 物品名称 = 发票项目名称
   - 品牌型号 = 发票规格型号, blank if spec/model is blank
   - 单价 = (金额 + 税额) / 数量
   - 数量 = 发票数量
   - 总价 = 金额 + 税额 - 折让或减价
   - 备注 = 留空
5. Keep one row per invoice line item.
6. Preserve invoice order in both the table and the end-of-file photo captions.
7. Add one caption placeholder per invoice, labeled `图1`, `图2`, ... and named by the invoice item name.
8. Save the completed DOCX as a new file.

## Bundled resources
- `assets/reimbursement-template.docx` , the blank template.
- `references/workflow.md` , field mapping and output rules.
- `scripts/fill_reimbursement.py` , helper scaffold for automation.
