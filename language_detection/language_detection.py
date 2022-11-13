#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/BCfoj2sZpXY
Purpose: Language detection using Python
Require package: langdetect
"""
import argparse

from langdetect import detect

# --------------------------------------------------
def get_args():
    """Get sentence from user input"""
    parser = argparse.ArgumentParser(
        description = 'Language detection using Python',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'sentence', 
        metavar = 'Sentence',
        default = None,
        help = "A quoted sentence")

    return parser.parse_args()

# --------------------------------------------------
def detect_lang(string: str) -> str:
    """Detect language from string"""
    lang = detect(string)
    return lang

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print(detect_lang(args.sentence))

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python language_detection.py "hola buenas tardes"