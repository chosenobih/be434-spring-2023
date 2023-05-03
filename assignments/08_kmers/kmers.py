#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-04-18
Purpose: A Python program to create synthetic DNA/RNA sequences
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find the common k-mers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-k", "--kmer",
        help="K-mer size",
        metavar="int",
        type=int,
        default=3
    )

    parser.add_argument(
        "FILE1",
        help="Input file 1",
        metavar="FILE1",
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "FILE2",
        help="Input file 2",
        metavar="FILE2",
        type=argparse.FileType("rt"),
    )

    args = parser.parse_args()

    if not args.kmer > 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """find the common k-mers between two files"""

    args = get_args()
    user_file_1 = args.FILE1
    user_file_2 = args.FILE2

    def find_kmers(seq, k):
        """Find all k-mers in string"""

        n = len(seq) - k + 1
        return [] if n < 1 else [seq[i: i + k] for i in range(n)]

    def test_find_kmers():
        """Test find_kmers"""

        assert find_kmers("", 1) == []
        assert find_kmers("ACTG", 1) == ["A", "C", "T", "G"]
        assert find_kmers("ACTG", 2) == ["AC", "CT", "TG"]
        assert find_kmers("ACTG", 3) == ["ACT", "CTG"]
        assert find_kmers("ACTG", 4) == ["ACTG"]
        assert find_kmers("ACTG", 5) == []

    def parse_kmers(open_file, k):
        """Get counts of matching kmers"""

        words1 = {}
        for line in open_file:
            for word in line.split():
                for kmer in find_kmers(word, k):
                    words1[kmer] = words1.get(kmer, 0) + 1
        return words1

    def print_kmers(f1_kmers, f2_kmers):
        """Format and print all matching kmers"""

        for key in set(f1_kmers) & set(f2_kmers):
            print(f"{key:10} {f1_kmers[key]:5} {f2_kmers[key]:5}")

    test_find_kmers()
    f1_kmers = parse_kmers(user_file_1, args.kmer)
    f2_kmers = parse_kmers(user_file_2, args.kmer)
    print_kmers(f1_kmers, f2_kmers)


# --------------------------------------------------
if __name__ == "__main__":
    main()
