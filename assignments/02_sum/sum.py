#!/usr/bin/env python3
"""
Author : Chosen Obih
Email : chosenobih@arizona.edu
Date   : 2023-02-05
Purpose: A Python program that will sum one or more required integer values
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='A program that sums one or more integer values',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbs',
                        metavar='int',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main function to run the program"""

    args = get_args()
    numbs = args.numbs
    numbers = []
    total = 0
    for numb in args.numbs:
        total += numb
        numbers.append(str(numb))
    print('{} = {}'.format(' + '.join(numbers), total))
# --------------------------------------------------
if __name__ == '__main__':
    main()
