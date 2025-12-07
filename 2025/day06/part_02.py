#!/usr/bin/env python3

from core import get_options, load_input_part_2
from operator import mul
from functools import reduce


def get_cols_widths(lines: list[str]) -> list[int]:
    widths = []
    line = [' '] * len(lines[0])
    for _l in lines:
        for i, char in enumerate(_l):
            if char.isdigit():
                line[i] = '9'
    in_digits = True
    prev_index = 0
    for i, char in enumerate(line):
        if char.isdigit():
            if not in_digits:
                widths.append(i - prev_index - 1)
                prev_index = i
                in_digits = True
        else:
            in_digits = False
    if prev_index < len(line):
        widths.append(len(line) - prev_index)
    return widths


def multiply(values):
    return reduce(mul, values, 1)


def print_world(world):
    for row in world:
        for num in row:
            print(num, end=' ')
        print()


def transpose(matriz):
    return list(map(list, zip(*matriz)))


def main(options):
    '''Day 6, part 1'''
    verbose = options.verbose
    *lines, ops = load_input_part_2(options.filename)
    widths = get_cols_widths(lines)
    world = []
    for line in lines:
        buff = []
        index = 0
        for width in widths:
            buff.append(line[index:index + width])
            index += width + 1
        world.append(buff)
    cols = len(world[0])
    rows = len(world)
    if verbose:
        print_world(world)
    if verbose:
        print(f'cols: {cols}')
        print(f'rows: {rows}')
    acc = 0
    for col in range(cols):
        op = ops[col]
        matrix = [list(world[row][col]) for row in range(rows)]
        operands = [int(''.join(_l)) for _l in transpose(matrix)]
        match op:
            case '+':
                sol = sum(operands)
            case '*':
                sol = multiply(operands)
            case _:
                raise ValueError(f"What the f*&^ing hell is {op}?")
        acc += sol
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
