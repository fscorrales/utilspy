#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/Pv6ioGZeouI
Purpose: Convert images to pdf
Require package: pillow
"""

import argparse

from PIL import Image

# --------------------------------------------------
def get_args():
    """Get Filename and Output name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Convert images to pdf',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filenames',
        nargs= '+', 
        default = [],
        help = 'Filenmanes with extension as list',
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'pdf_name', 
        default = 'output.pdf',
        help = "pdf's file name",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def image_pdf(filename:str, output:str):
    """Convert list of images to pdf"""
    images = []
    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)

        images[0].save(output, save_all = True, append_images = images[1:])
    #image_pdf(["image1.jpg", "image2.png"], "output.pdf")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    image_pdf(args.filename, args.output)

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python images_to_pdf.py test.png test2.jpg