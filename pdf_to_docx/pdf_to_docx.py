#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/iWei0Yptcog
Purpose: Convert pdf to docx
Require package: pdf2docx
"""

import argparse

from pdf2docx import Converter

# --------------------------------------------------
def get_args():
    """Get pdf_file and docx_file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Convert pdf to docx',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = None,
        help = "pdf's file name with extension",
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'docx_name', 
        default = 'output.docx',
        help = "docx's file name with extension",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def convert_pdf_to_docx(pdf_file: str, docx_file: str):
    """Convert pdf to docx"""
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close
    #convert_pdf_to_docx('pdf_file.pdf', 'docx_file.docx')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    convert_pdf_to_docx(args.filename, args.output)

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python pdf_to_docx.py test.pdf