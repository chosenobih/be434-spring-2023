#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-04-18
Purpose: A Python program to create synthetic DNA/RNA sequences
"""

import argparse
import random


# --------------------------------------------------
def get_args():

    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return parser.parse_args()


# --------------------------------------------------
def main():
    "main function to run the program"

    args = get_args()
    random.seed(args.seed)

    def create_pool(pctgc, max_len, seq_type):
        """ Create the pool of bases """

        t_or_u = 'T' if seq_type == 'dna' else 'U'
        num_gc = int((pctgc / 2) * max_len)
        num_at = int(((1 - pctgc) / 2) * max_len)
        pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

        for _ in range(max_len - len(pool)):
            pool += random.choice(pool)

        return ''.join(sorted(pool))

    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    for i in range(0, args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, seq_len)
        new_seq = args.outfile.write(f'">{i+1}\n", "{seq}\n"')

    print(new_seq)


# --------------------------------------------------
if __name__ == '__main__':
    main()
