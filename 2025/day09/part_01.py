#!/usr/bin/env python3

import math
from itertools import combinations

from tqdm import tqdm

from colors import red
from vectors import V2, area
from core import get_options, load_input


def main(options):
    '''Day 9, part 1.
    '''
    options = get_options()
    points = list(load_input(options.filename))
    acc = 0
    for p1, p2 in tqdm(list(combinations(points, 2))):
        a = area(p1, p2)
        if a > acc:
            acc = a
    print(f'Solution day 2 part 1: {acc}')


if __name__ == '__main__':
    main(get_options())
