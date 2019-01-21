#!/usr/bin/env python
import argparse
import json
from sgml_parser import parse as parse_sgml
from serialize_datetime import serialize


def main():
    input, output = get_input_output_args()
    json.dump(parse_sgml(input), output, default=serialize)


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
