#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 5')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    fresh_ranges = []
    item_ids = []
    first_section = True
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            if not line and first_section:
                first_section = False
                continue
            if first_section:
                (low_id, high_id) = line.split('-')
                fresh_ranges.append((int(low_id), int(high_id)))
            else:
                id_item = int(line)
                item_ids.append(id_item)

    return sorted(fresh_ranges), item_ids
