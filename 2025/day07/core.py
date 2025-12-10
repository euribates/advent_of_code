#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 4')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    lines = []
    y = 0
    with open(filename) as f_input:
        for line in f_input:
            lines.append(list(line.strip()))
            if 'S' in line:
                start_y = y
                start_x = line.index('S')
        y += 1
    return start_x, start_y, lines
