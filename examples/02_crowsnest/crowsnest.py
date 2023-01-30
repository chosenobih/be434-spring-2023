#!/usr/bin/env python3
"""
Author : chosen <chosen@localhost>
Date   : 2023-01-27
Purpose: crowsnest_practice
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='crowsnest_practice',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")
    #print("Ahoy, Captain, {} {} off the larboard bow!".format(article, word))
# --------------------------------------------------
if __name__ == '__main__':
    main()
