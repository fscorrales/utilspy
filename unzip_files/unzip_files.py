#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/CFFI5cEtopc
Purpose: Unzip files
Require package: 
"""

import argparse

from zipfile import ZipFile

# --------------------------------------------------
def get_args():
    """Get complete filename or path from user input"""
    parser = argparse.ArgumentParser(
        description = 'Unzip files',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'zipfile', 
        metavar = 'Zipfile',
        default = [],
        help = 'Complete filenmane or path',
        type=str)

    return parser.parse_args()

# --------------------------------------------------
def unzip_files(zipfile_name:str):
    """Unzip file"""
    with ZipFile(zipfile_name, 'r') as zip_object:
        zip_object.extractall()
    return zip_object
    #image_pdf(["image1.jpg", "image2.png"], "output.pdf")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    zip = unzip_files(args.zipfile)
    print(zip.namelist())

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python unzip_files.py zip_file.zip