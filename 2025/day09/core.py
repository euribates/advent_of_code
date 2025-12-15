#!/usr/bin/env python3

import argparse

from vectors import V2

def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 4')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-s', '--scale', type=float, default=1.0)
    parser.add_argument('-f', '--fps', type=int, default=24)
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            x, y = line.split(',')
            yield V2(int(x), int(y))
