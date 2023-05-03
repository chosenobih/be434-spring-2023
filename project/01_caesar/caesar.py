#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-05-03
Purpose: A Python program to implement the caesar shift
"""

import argparse
import string
import sys


# --------------------------------------------------
def get_args():
    """Caesar Shift"""

    parser = argparse.ArgumentParser(
        description="Caesar Shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "infile",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=sys.stdin
    )

    parser.add_argument(
        "-n",
        "--number",
        help="A number to shift",
        metavar="NUMBER",
        type=int,
        default=3
    )

    parser.add_argument(
        "-d", "--decode",
        help="A boolean flag",
        action="store_true",
        default=False
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def test_shift():
    """test the common cases of error"""

    assert shift_forward("A", 3) == "D"
    assert shift_forward("H", 3) == "K"
    assert shift_forward("K", -3) == "H"
    assert shift_forward("Z", 1) == "A"
    assert shift_forward("Z", 3) == "C"


def shift_forward(inchar, steps):
    """Make a loud noise"""

    if inchar not in string.ascii_uppercase:
        return inchar

    start = ord("A") if inchar.isupper() else ord('a')

    inc = (((ord(inchar) - start) + steps) % 26) + start
    newchar = chr(inc)
    return newchar


def main():
    """caesar shift basic encryption"""

    args = get_args()

    shift = (-1 * abs(args.number)) if args.decode else abs(args.number)
    for line in args.infile:
        args.outfile.write(''.join([shift_forward(c.upper(), shift).upper()
                                    for c in line]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
