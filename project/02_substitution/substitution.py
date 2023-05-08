#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-05-05
Purpose: A python substitution cipher program
"""

import argparse
import random
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Substitution Cipher",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "infile",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )

    parser.add_argument(
        "-s", "--seed",
        help="A random seed",
        metavar="SEED",
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
        "-o", "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to run the substitution cipher"""

    args = get_args()
    random.seed(args.seed)
    substitution = build_dictionary()

    for line in args.infile:
        args.outfile.write(
            "".join([substitution_cypher(c.upper(), substitution, args.decode)
                    for c in line])
        )


# --------------------------------------------------
def build_dictionary():
    """Function to create a dictionary and
    a list to hold the alphabetes"""

    substitution = {}
    alphabetes = []

    alphabetes = list(string.ascii_uppercase)
    substitution = dict(zip(list(alphabetes), random.sample(alphabetes, 26)))

    return substitution


# --------------------------------------------------
def substitution_cypher(inchar, subdict, decode):
    """Function to convert character in each line of input file
    to substituted value"""

    if inchar not in string.ascii_uppercase:
        return inchar

    if decode:
        newchar = "".join([key for key, value in subdict.items()
                           if value == inchar])
    else:
        mychar = subdict.get(inchar)
        newchar = inchar if mychar is None else mychar

    return newchar


# --------------------------------------------------
if __name__ == "__main__":
    main()
