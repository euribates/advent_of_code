#!/usr/bin/env python3

import argparse
import re

pat_spaces = re.compile(r'\s+')

def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 6')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    lines = []
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            lines.append(pat_spaces.split(line))
    for *nums, op in zip(*lines):
        yield [int(_) for _ in nums], op


def load_input_part_2(filename: str):
    with open(filename) as f_input:
        lines = [
            line.strip('\n') for line in f_input
            ]
    lines[-1] = [
        _.strip()
        for _ in pat_spaces.split(lines[-1])
        if _.strip()
        ]
    return lines
