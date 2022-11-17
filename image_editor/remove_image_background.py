#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/RkdFkhfMK2k
Purpose: Remove image background
Require package: rembg
"""

import argparse

from rembg import remove
from PIL import Image

# --------------------------------------------------
def get_args():
    """Get Filename and Output name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Remove image background',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = [],
        help = 'Complete filename or path',
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'png_name', 
        default = 'output.png',
        help = "png's file name or path",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def remove_background(filename:str, 
                    output_name:str = 'output.png'):
    """Remove background"""
    input = Image.open(filename)
    output = remove(input)
    output.save(output_name)
    #remove_background("image.jpg")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    remove_background(args.filename, args.output)
    print('Complete')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python remove_image_background.py image.jpg