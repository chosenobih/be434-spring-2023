#!/usr/bin/env python
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-04-18
Purpose: A Python program to translate DNA/RNA to amino acid
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        'sequence',
        metavar='str',
        help='DNA/RNA sequence'
    )

    parser.add_argument(
        '-c',
        '--codons',
        required=True,
        metavar='FILE',
        type=argparse.FileType('rt'),
        help='A file with codon translations'
    )

    parser.add_argument(
        '-o',
        '--outfile',
        metavar='FILE',
        default='out.txt',
        type=argparse.FileType('wt'),
        help='Output filename'
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to run the program"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        codon_table[line.rstrip().split()[0]] = line.rstrip().split()[1]

    k = 3
    seq = args.sequence
    for codon in [seq[i: i + k].upper() for i in range(0, len(seq), k)]:
        if codon_table.get(codon) is None:
            args.outfile.write('-')
        else:
            args.outfile.write(f'{codon_table.get(codon)}')
    args.outfile.write('\n')
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
