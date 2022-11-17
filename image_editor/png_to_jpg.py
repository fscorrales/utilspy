#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/CAdOKTTbBxM
Purpose: png_to_jpg
Require package:
"""

import argparse

from PIL import Image

# --------------------------------------------------
def get_args():
    """Get Filename and Output name from user input"""
    parser = argparse.ArgumentParser(
        description = 'png_to_jpg',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = [],
        help = 'Complete png filename or path',
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'jpg_name', 
        default = 'output.jpg',
        help = "jpg file's name or path",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def png_to_jpg(filename:str, 
                output_name:str = 'output.jpg'):
    """png_to_jpg"""
    img = Image.open(filename)
    rgb_img = img.convert('RGB')
    rgb_img.save(output_name)
    #png_to_jpg("image.png")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    png_to_jpg(args.filename, args.output)
    print('Complete')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python png_to_jpg.py image.png