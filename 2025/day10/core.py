#!/usr/bin/env python3

import argparse

from machines import Machine

def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 4')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            yield Machine(line)
