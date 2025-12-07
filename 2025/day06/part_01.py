#!/usr/bin/env python3

from core import get_options, load_input
from operator import mul
from functools import reduce

def multiply(values):
    return reduce(mul, values, 1)


def main(options):
    '''Day 6, part 1'''
    verbose = options.verbose
    acc = 0
    for nums, op in load_input(options.filename):
        match op:
            case '+':
                sol = sum(nums)
            case '*':
                sol = multiply(nums)
            case _:
                raise ValueError(f"What the f*&^ing hell is {op}?")
        if verbose:
            print(*nums, sep=op, end=' = ')
            print(sol)
        acc += sol
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
