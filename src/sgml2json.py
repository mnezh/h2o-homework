#!/usr/bin/env python
'''
Since parsing SGML is too slow to be performed each time
API starts, let's convert to something more digestible.
I've decided to use JSON as it is a quick win, although
if I needed to do something more durable, I'd rather ETL
data into database, SQLite or something like this.

However, for a homework JSON a good enough, knowing the
limitations.
'''

import argparse
import json
from sgml_parser import parse as parse_sgml
from serialize_datetime import dump_serialize


def main():
    input, output = get_input_output_args()
    json.dump(parse_sgml(input), output, default=dump_serialize)


def get_input_output_args():
    parser = argparse.ArgumentParser(
        description='Lewis SGML to JSON converter.')
    parser.add_argument(
        'infile',
        type=argparse.FileType('r'),
        nargs=1,
        help='input SGML file')
    parser.add_argument(
        'outfile',
        type=argparse.FileType('w'),
        nargs=1,
        help='output SGML file')
    args = parser.parse_args()
    return (args.infile[0], args.outfile[0])


if __name__ == "__main__":
    main()
