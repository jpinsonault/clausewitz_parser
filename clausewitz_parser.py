#!/usr/bin/env python
 
"""

""" 

import sys
import pyparsing

from save_file_syntax import SaveFile
from save_file_syntax import Dictionary

import argparse
import re
from pprint import pprint

from SaveFileParser import SaveFileParser


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('save_file', help='EU4 Save File')
    args = parser.parse_args()

    return args


def main(args):
    parser = SaveFileParser(args.save_file)

    nation_size_stats = parser.nation_size_stats


if __name__ == '__main__':
    sys.exit(main(parse_args()))
