#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-05-05
Purpose: A python vigenere cipher program
"""

import argparse
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Vigenere Ciphers",
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
        "-k",
        "--keyword",
        help="A keyword",
        metavar="KEYWORD",
        type=str,
        default="CIPHER",
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
def main():
    """Main function to run the program"""

    args = get_args()

    for line in args.infile:
        line = line.upper()
        line_cipher = ""
        character_position = 0
        for word in re.split(r"(\W+)", line):
            for c in word:
                cipher_character = args.keyword[character_position % len(args.keyword)]
                mapped, inc = map_char(c.upper(), cipher_character, args.decode)
                character_position += inc
                line_cipher = line_cipher + mapped
        args.outfile.write(line_cipher)


# --------------------------------------------------
def map_char(input_character, cipher_charater, decode):
    """translate inchar with its cipher character
    using base 26"""

    if input_character not in string.ascii_uppercase:
        return input_character, 0

    in_value = ord(input_character) - 65
    cipher_value = ord(cipher_charater) - 65

    if decode:
        final_character = chr(((in_value - cipher_value) % 26) + 65)
    else:
        final_character = chr(((in_value + cipher_value) % 26) + 65)

    return final_character, 1


# --------------------------------------------------
if __name__ == "__main__":
    main()
