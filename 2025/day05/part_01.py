#!/usr/bin/env python3

from core import get_options, load_input


def main(options):
    '''Day 5, part 1'''
    verbose = options.verbose
    fresh_ranges, item_ids = load_input(options.filename)
    acc = 0
    if verbose:
        for a,b in fresh_ranges:
            print(a, b, sep='-')
        print()
        for item_id in item_ids:
            print(item_id)
    for item_id in item_ids:
        for (min_value, max_value) in fresh_ranges:
            if min_value <= item_id <= max_value:
                acc += 1
                break
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
