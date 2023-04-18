#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-04-04
Purpose: A Python program to concatenate files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        nargs='+',
                        metavar='file',
                        type=argparse.FileType("rt"),
                        help='Input files(s)',
                        default=False)

    parser.add_argument('-n', '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to run the program"""

    args = get_args()
# file = args.file
# number = args.number

    line_number = 0
    for file_name in args.files:
        with open(file_name, encoding="utf8") as f:
            for line in f:
                if args.number:
                    print(f'{line_number:>6} {line}', end='')
                    line_number += 1
                else:
                    print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
