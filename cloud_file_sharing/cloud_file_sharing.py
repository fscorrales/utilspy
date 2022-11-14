#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/2535DhGy0oE
Purpose: Cloud file sharing
Require package: gofile
"""

import argparse

import gofile as go

# --------------------------------------------------
def get_args():
    """Get file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Cloud file sharing',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', 
        metavar = 'Filename',
        default = None,
        help = "file name with extension",
        type=str)

    return parser.parse_args()

# -------------------------------------------
def store_file(file: str):
    """Upload file to gofile and get url"""
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    return url

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    url = store_file(args.filename)
    print("Download Link: ", url["downloadPage"])

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python cloud_file_sharing.py file.extension