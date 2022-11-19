#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/JHnEaJbAeMg
Purpose: Fetch pdf text
Require package: pdfplumber
"""

import argparse

import pdfplumber as pdftool

# --------------------------------------------------
def get_args():
    """Get pdf_file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Fetch text from pdf',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = None,
        help = "Complete pdf's name or path",
        type=str)

    return parser.parse_args()

# --------------------------------------------------
def fetch_pdf_text(path: str):
    """Fetch text from pdf by page"""
    pdf_pages = {}
    with pdftool.open(path) as tool:
        for p_no, page in enumerate(tool.pages, 1):
            pdf_pages[p_no] = page.extract_text()
            # There are options to extract table, 
            # tables and words
    return pdf_pages

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    pdf_pages = fetch_pdf_text(args.filename)
    for k, v in pdf_pages.items():
        print('<--- page no', k, '--->')
        print(v)

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python fetch_pdf_text.py pdf_file.pdf