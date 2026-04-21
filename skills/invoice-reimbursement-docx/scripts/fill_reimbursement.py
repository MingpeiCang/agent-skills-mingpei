#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.oxml.ns import qn

NUM_RE = re.compile(r'[-+]?(?:\d+\.\d+|\d+)')


def extract_inputs(inputs):
    files = []
    tmpdirs = []
    for item in inputs:
        p = Path(item)
        if p.suffix.lower() == '.zip':
            td = tempfile.mkdtemp(prefix='reimb_')
            tmpdirs.append(td)
            with zipfile.ZipFile(p) as zf:
                zf.extractall(td)
            for child in sorted(Path(td).rglob('*')):
                if child.suffix.lower() in {'.pdf', '.png', '.jpg', '.jpeg', '.webp'}:
                    files.append(str(child))
        else:
            files.append(str(p))
    return files, tmpdirs


def set_cell(cell, text):
    cell.text = ''
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(str(text))
    r.font.name = 'Arial'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), 'SimSun')
    r.font.size = Pt(10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--template', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('inputs', nargs='+')
    args = ap.parse_args()

    # This script expects invoice extraction to be done upstream by the agent.
    # It only fills a structured table when the agent has already computed rows.
    raise SystemExit('Use the skill workflow to extract invoice rows, then patch this script with row data before execution.')


if __name__ == '__main__':
    main()
