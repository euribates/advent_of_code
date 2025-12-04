#!/usr/bin/env python3

from core import get_options, load_input

def get_max_jolts(line: str, verbose=False) -> int:
    candidates = set([])
    for i, c1 in enumerate(line):
        for c2 in line[i+1:]:
            value = int(f'{c1}{c2}')
            candidates.add(value)
    result = max(candidates)
    if verbose:
        print(f'Line: {line}   result: {result}')
    return result


def main(options):
    '''Day 3, part 1'''
    verbose = options.verbose
    acc = 0
    for line in load_input(options.filename):
        acc += get_max_jolts(line, verbose=verbose)
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
