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

    # note that I updated to "files" here becuase you use that later
    parser.add_argument('files',
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

# note that you already opened the file(s) as file handle(s) 
# with the magic of argparse, no need to open it again
# line_number should start at 1, and start at 1 for each file
# you need to move inside the loop to reset to 1 after each file
    #line_number = 0
    for file_name in args.files:
        #with open(file_name, encoding="utf8") as f:
        # you need to count line numbers here, so you don't start over
        # for each file you are concatenating
        line_number = 1
        for line in file_name:
            if args.number:
                # added the tab \t below and rstrip to remove the \n
                print(f'{line_number:>6}\t{line.rstrip()}')
                line_number += 1
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
