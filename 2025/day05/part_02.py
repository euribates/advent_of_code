#!/usr/bin/env python3

from core import get_options, load_input

def add_range(fresh_ranges: list, new_range: tuple) -> list:
    if len(fresh_ranges) > 0: # Trere are at least one
        last_range = fresh_ranges[-1]
        if last_range[1] >= (new_range[0] - 1): # Overlap
            fresh_ranges.pop()
            fresh_ranges.append((
                last_range[0], max([last_range[1], new_range[1]])
                ))
            return fresh_ranges
    fresh_ranges.append(new_range)
    return fresh_ranges


def main(options):
    '''Day 5, part 2'''
    verbose = options.verbose
    fresh_ranges, _item_ids = load_input(options.filename)
    merged_ranges = []
    while fresh_ranges:
        if verbose:
            print(f'merged_ranges before: {merged_ranges!r}')
        merged_ranges = add_range(merged_ranges, fresh_ranges.pop(0))
        if verbose:
            print(f'merged_ranges after: {merged_ranges!r}')
    if verbose:
        for a,b in merged_ranges:
            print(a, b, sep='-')

    acc = 0
    for (min_value, max_value) in merged_ranges:
        acc += max_value - min_value + 1
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
