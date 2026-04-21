# Workflow

## Input
- One or more invoice PDFs/images, optionally inside a zip archive.
- The bundled blank template at `assets/reimbursement-template.docx`.
- `minimax-docx` must be used to process the Word document.

## Required mapping
- 物品名称 = 发票项目名称
- 品牌型号 = 发票规格型号, blank if the invoice spec/model is blank
- 单价 = (金额 + 税额) / 数量
- 数量 = 发票数量
- 总价 = 金额 + 税额 - 折让或减价
- 备注 = 留空

## Rules
- Keep one table row per invoice line item.
- Use invoice line items exactly as shown, including leading category text such as `*塑料制品*`.
- If an invoice has discount/reduction lines, include them in the total.
- Preserve invoice order for table rows and image captions.
- Create one photo-caption placeholder per invoice, labeled `图1`, `图2`, ... and named by the invoice item name.
- Do not duplicate a single invoice into multiple photo captions.
- Use `minimax-docx` to edit, validate, and save the Word output.

## Output
- Save the completed DOCX as a new file.
- If the user provided a zip archive, unpack it first, then process the contained invoices.
