#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 2')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        lines = f_input.read().split(',')
        for line in lines:
            first_num, last_num = line.split('-')
            yield int(first_num), int(last_num)
