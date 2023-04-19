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
        # this argument to the command line is usually lowercase
        'seqs',
        metavar='SEQ',
        nargs='+',
        help='Input sequence(s)'
    )

    parser.add_argument(
        '-o',
        '--outfile',
        metavar='FILE',
        #type=argparse.FileType(mode='w', encoding='UTF-8'),
        # you can tell argparse to write in text mode
        type=argparse.FileType('wt'),
        # add the deault to std.out here
        default=sys.stdout,
        help='Output filename'
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to run the program"""

    args = get_args()
    seqs = args.seqs
    #SEQ = args.SEQ

    # no need to open the file, because argparse already did for you.
    #if args.outfile:
    #    fh = open(args.out, 'wt', encoding='UTF-8')
    #else:
    #    fh = sys.stdout
    #filename = fh.name

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

    for dna in seqs:
        text = [dna]
        # use a space as part of the join as the separator below
        #text.append('')
        #iupac += [codes.get(dna_char, dna_char) for dna_char in dna]
        # use join to add to a string
        iupac_text = ''.join([codes.get(dna_char, dna_char) for dna_char in dna])  
        text.append(iupac_text)
        
        # add a space in between 
        #fh.write(''.join(text))
        #fh.write(' '.join(text))
        #fh.write('\n')
  
        # use a print statement to print to stdout of outfile
        print(' '.join(text), file=args.outfile)


    #here is a way to write the "done statement 
    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')

    #if filename != '<stdout>':
    #    print(f'Done, see output in "{filename}"')
    #fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
