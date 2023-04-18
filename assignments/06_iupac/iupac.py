#!/usr/bin/env python
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-04-18
Purpose: A Python program to translate IUPAC-encoded
        string of DNA into regular expression that
        will match all the possible strings of DNA
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        'SEQ',
        metavar='SEQ',
        nargs='+',
        help='Input sequence(s)'
    )

    parser.add_argument(
        '-o',
        '--outfile',
        metavar='FILE',
        type=argparse.FileType(mode='w', encoding='UTF-8'),
        help='Output filename'
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to run the program"""

    args = get_args()
    SEQ = args.SEQ
    if args.outfile:
        fh = open(args.out, 'wt', encoding='UTF-8')
    else:
        fh = sys.stdout
    filename = fh.name

    codes = {}
    codes['A'] = 'A'
    codes['C'] = 'C'
    codes['G'] = 'G'
    codes['T'] = 'T'
    codes['U'] = 'U'
    codes['R'] = '[AG]'
    codes['Y'] = '[CT]'
    codes['S'] = '[GC]'
    codes['W'] = '[AT]'
    codes['K'] = '[GT]'
    codes['M'] = '[AC]'
    codes['B'] = '[CGT]'
    codes['D'] = '[AGT]'
    codes['H'] = '[ACT]'
    codes['V'] = '[ACG]'
    codes['N'] = '[ACGT]'

    for dna in SEQ:
        text = [dna]
        text.append('')
        text += [codes.get(dna_char, dna_char) for dna_char in dna]
        fh.write(''.join(text))
        fh.write('\n')

    if filename != '<stdout>':
        print(f'Done, see output in "{filename}"')
    fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
