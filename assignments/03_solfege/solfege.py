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

    # make sure your arguments are always lowercase Solfege -> solfege
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

    # be sure to use the argument you created above.
    # texts = args.texts   ->  texts = args.solfege
    texts = args.solfege

    # needed to correct the spacing, Python requires 4 spaces after the 
    # dictionary is defined
    syllable = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread',
    }

    # I changed this to "texts" that you assigned it to above
    # you can also use "for text in args.solfege:" It just needed to match
    # what you assigned in the get_args above
    for text in texts:
        # You need to check that the text is in syllable first
        #print(syllable.get(text, text), end='')
        if text in syllable:
            print(f'{text}, {syllable.get(text)}')
        else:
            # tell the user you don't have the note to print
            print("Check out the README.md to see what to print here")


# --------------------------------------------------
if __name__ == '__main__':
    main()
