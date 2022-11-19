#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/ZgBeec1ClSc
Purpose: Extract text from pdf (NOT WORKING)
Require package: pdfminer
"""

import argparse
import io

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

# --------------------------------------------------
def get_args():
    """Get pdf_file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Extract text from pdf (NOT WORKING)',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = None,
        help = "pdf's file name with extension",
        type=str)

    return parser.parse_args()

# --------------------------------------------------
def convert_pdf_to_txt(path: str):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8' #Where should it go?
    laparams = LAParams()
    with io.StringIO() as retstr:
        with TextConverter(rsrcmgr, retstr, laparams=laparams) as device:
            with open(path, 'rb') as fp:
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                password = ''
                maxpages = 0
                caching = True
                pagenos = set()

                for page in PDFPage.get_pages(fp, pagenos, 
                maxpages=maxpages, password=password, 
                caching=caching, check_extractable=True):
                    interpreter.process_page(page)
                return retstr.getvalue()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print(convert_pdf_to_txt(args.filename))

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python pdf_extract_text.py pdf_file.pdf


