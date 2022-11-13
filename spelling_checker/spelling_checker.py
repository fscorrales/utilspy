#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/RQMrtwEjqAg
Purpose: Spelling checker with Python (NOT WORKING)
Require package: textblob
"""
import argparse

from textblob import TextBlob

# --------------------------------------------------
def get_args():
    """Get sentence or word from user input"""
    parser = argparse.ArgumentParser(
        description = 'Spelling checker with Python (NOT WORKING)',
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
def correct(words: list) -> list:
    """Correct spelling mistakes from a list of strings"""
    corrected_words = []
    for i in words:
        corrected_words.append(TextBlob(i))
    print("Wrong words: ", words)
    print("Corrected words are: ")
    for i in corrected_words:
        print(i.correct(), end=' ')
    return corrected_words

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    correct(args.words)

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python spelling_checker.py helo wort