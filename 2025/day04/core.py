#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 4')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    world = []
    with open(filename) as f_input:
        for line in f_input:
            world.append(list(line.strip()))
    return world
