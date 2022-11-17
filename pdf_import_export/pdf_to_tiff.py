#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/iWei0Yptcog
Purpose: Convert pdf to tiff (NOT WORKING)
Require package: aspose_words
"""

import argparse

import aspose.words as aw

# --------------------------------------------------
def get_args():
    """Get pdf_file and tiff_file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Convert pdf to tiff (NOT WORKING)',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = None,
        help = "Complete pdf's name or path",
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'tiff_name', 
        default = 'output.tiff',
        help = "tiff's file name with extension",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def pdf_to_tiff(pdf_file: str, tiff_file: str):
    """Convert pdf to tiff"""
    pdf = aw.Document(pdf_file)
    pdf.save(tiff_file)
    #pdf_to_tiff('pdf_file.pdf', 'tiff_file.tiff')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    pdf_to_tiff(args.filename, args.output)
    print('Complete')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python pdf_to_tiff.py test.pdf