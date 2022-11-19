#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/lY40rpBtmrE
Purpose: Convert pdf to any (NOT WORKING)
Require package: aspose_words
"""

import argparse

import aspose.words as aw

# --------------------------------------------------
def get_args():
    """Get pdf_file and output file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Convert pdf to any (NOT WORKING)',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = None,
        help = "Complete pdf's name or path",
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'output_name', 
        default = 'output.tiff',
        help = "Output file's name with desire extension",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def pdf_to_any(pdf_file: str, 
                output_file: str = 'output.tiff'):
    """Convert pdf to any"""
    pdf = aw.Document(pdf_file)
    pdf.save(output_file)
    #pdf_to_any('pdf_file.pdf', 'tiff_file.tiff')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    pdf_to_any(args.filename, args.output)
    print('Complete')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python pdf_to_any.py test.pdf