#!/usr/bin/env python3

import argparse
from vectors import V3


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 8')
    parser.add_argument('filename')
    parser.add_argument('limit', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            x, y, z = line.strip().split(',')
            yield V3(int(x), int(y), int(z))
