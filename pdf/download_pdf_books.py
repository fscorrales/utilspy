#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/UoBhK-BIcBE
Purpose: Download pdf from internet
Require package:
"""

import argparse

import urllib.request

# --------------------------------------------------
def get_args():
    """Get link to download and pdf_file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Download pdf from internet',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'url', 
        metavar = 'Link',
        default = '',
        help = "Website link from where pdf is going to be downloading",
        type=str)

    parser.add_argument(
        '-p', '--pdf_name', 
        metavar = "pdf'name",
        default = 'output',
        help = "pdf's name without extension",
        type=str)

    return parser.parse_args()

# --------------------------------------------------
def download_pdf(url: str,
                pdf_name: str = 'output'):
    """Download pdf from link"""
    output = pdf_name + '.pdf'
    urllib.request.urlretrieve(url, output)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    download_pdf(args.url, args.pdf_name)
    print('Complete')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python download_pdf_books.py url