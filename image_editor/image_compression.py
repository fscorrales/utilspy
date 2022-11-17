#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/U4Ysonp7xq8
Purpose: Image compression
Require package:
"""

import argparse

from PIL import Image

# --------------------------------------------------
def get_args():
    """Get Filename and Output name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Image compression',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = [],
        help = 'Complete filename or path',
        type=str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'jpg_name', 
        default = 'output.jpg',
        help = "jpg file's name or path",
        type = str)

    parser.add_argument(
        '-q', '--quality', 
        metavar = "JPEG's quality", 
        default = 10,
        help = "jpeg file's quality",
        type = int)

    return parser.parse_args()

# --------------------------------------------------
def image_compression(filename:str, 
                    output_name:str = 'output.jpg',
                    quality:int = 10):
    """Image compression"""
    img = Image.open(filename)
    img.save(output_name, 'JPEG', optimize = True, quality = quality)
    #image_compression("image.jpg")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    image_compression(args.filename, args.output, args.quality)
    print('Complete')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python image_compression.py image.jpg