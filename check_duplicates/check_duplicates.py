#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/ZkLks_wO3dk?t=18
Purpose: Check duplicates elements from list
Require package: None
"""
import argparse

# --------------------------------------------------
def get_args():
    """Get list from user input"""
    parser = argparse.ArgumentParser(
        description = 'Check duplicates elements from list',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'list', 
        metavar = 'List',
        nargs='+',
        default = [],
        help = "List of elements")

    return parser.parse_args()

# --------------------------------------------------
def check_duplicates(lst: list) -> bool:
    """Check if there are duplicates in a list"""
    duplicates = len(lst) != len(set(lst))
    return duplicates

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print(check_duplicates(args.list))

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python check_duplicates.py 1 2 3 4 1