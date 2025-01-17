#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-02-05
Purpose: A Python program to demonstrate the concept of dictionary in python
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('solfege',
                        nargs='+',
                        metavar='str',
                        type=str,
                        help='solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to run the program"""

    args = get_args()

    texts = args.solfege

    syllable = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread',
    }

    for text in texts:
        if text in syllable:
            print(f'{text}, {syllable.get(text)}')
        else:
            print(f'I don\'t know "{text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
