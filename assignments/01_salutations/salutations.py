#!/usr/bin/env python3
"""
Author : Chosen Obih
Email : chosenobih@arizona.edu
Date   : 2023-01-27
Purpose: A salutation script to greet user
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greeting and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main function to run the program"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = args.excited

    salutaion = f"{greeting} {name}"
    if excited: salutaion += "!"
    print(salutaion)
# --------------------------------------------------
if __name__ == '__main__':
    main()
