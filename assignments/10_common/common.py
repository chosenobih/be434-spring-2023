#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-05-02
Purpose: A Python program to finf common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    parser.add_argument("file1",
                        metavar="FILE1",
                        help="Input file 1")

    parser.add_argument("file2",
                        metavar="FILE2",
                        help="Input file 2")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Use sets to output commone words between two input files"""

    args = get_args()
    ofh = args.outfile

    try:
        fh1 = open(args.file1, "rt", encoding="utf-8")
    except IOError:
        ofh.close()
        sys.exit(f"No such file or directory: '{args.file1}'")

    try:
        fh2 = open(args.file2, "rt", encoding="utf-8")
    except IOError:
        ofh.close()
        sys.exit(f"No such file or directory: '{args.file2}'")

    def read_words_into_set(fh):
        """read all white space delimited text into a set from a file"""
        my_set = set()
        for line in fh:
            for word in line.split():
                my_set.add(word)
        return my_set

    set1 = set()
    set2 = set()
    set1 = read_words_into_set(fh1)
    set2 = read_words_into_set(fh2)
    common = [ofh.write(f"{item}\n") for item in sorted(set1.intersection(set2))]
    print(common)
    fh1.close()
    fh2.close()
    ofh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
