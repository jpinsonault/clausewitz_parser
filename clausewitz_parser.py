#!/usr/bin/env python
 
"""

""" 

import sys
import pyparsing


import argparse
import re
from pprint import pprint

greet = Word( alphas ) + Literal(",").suppress() + Word( alphas ) + Literal("!").suppress()


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('save_file', help='EU4 Save File')
    args = parser.parse_args()

    return args


def main(args):
    with open(args.save_file, 'r') as save_file:
        save_file_string = save_file.read()

    greeting = greet.parseString( "Hello, World!" )
    print greeting


if __name__ == '__main__':
    sys.exit(main(parse_args()))
