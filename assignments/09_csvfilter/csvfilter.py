#!/usr/bin/env python3
"""
Author: Chosen Obih
Email: chosenobih@arizona.edu
Date: 2023-04-22
Purpose: A Python program to filter csv
"""

import argparse
import re
import sys
import pandas as pd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Filter delimited records",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        required=True,
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "-v",
        "--val",
        help="Value for filter",
        metavar="val",
        required=True,
        type=str,
        default=None,
    )

    parser.add_argument(
        "-c",
        "--col",
        help="Column for filter",
        metavar="col", type=str,
        default=""
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="OUTFILE",
        type=str,
        default="out.csv",
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        help="Input delimiter",
        metavar="delim",
        type=str,
        default=",",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    dataframe = pd.read_csv(args.file.name, sep=args.delimiter, dtype=str, engine="python")

    if args.col and (args.col not in dataframe.columns):
        args.file.close()
        print(f'--col "{args.col}" not a valid column!')
        mylist = ", ".join(dataframe.columns.tolist())
        sys.exit(f"Choose from {mylist}")

    if args.col:
        pattern = re.compile(".*" + args.val + ".*", re.IGNORECASE)

        mask = (
            dataframe[[args.col]]
            .apply(lambda x: x.str.contains(pattern, regex=True))
            .any(axis=1)
        )

        outdf = dataframe[mask]
    else:
        outdf = dataframe[
            dataframe.apply(lambda row: row.str.contains(args.val, case=False).any(), axis=1)
        ]

    if outdf.shape[0] == 0:
        args.file.close()
        sys.exit(f'No usable data in --file "{args.file.name}"')
    else:
        outdf.to_csv(args.outfile, header=True, index=False, mode="wt")
        print(f'Done, wrote {outdf.shape[0]} to "{args.outfile}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
