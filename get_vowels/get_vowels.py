#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/ZkLks_wO3dk
Purpose: Get vowels from string
Require package: None
"""
import argparse

# --------------------------------------------------
def get_args():
    """Get sentence or word from user input"""
    parser = argparse.ArgumentParser(
        description = 'Get vowels from string',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'words', 
        metavar = 'Words',
        nargs='+',
        default = [],
        help = "Word or sentence",
        type=str)

    return parser.parse_args()

# --------------------------------------------------
def sentence_to_words(string: str) -> list:
    """String to list of strings"""
    li = list(string.split())
    return li

# --------------------------------------------------
def get_vowels(words: list) -> list:
    """Get vowels from a list of strings"""
    vowels = []
    for i in words:
        vowels.append([each for each in i if each in 'aeiou'])
    return vowels

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print(get_vowels(args.words))

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python get_vowels.py hello world