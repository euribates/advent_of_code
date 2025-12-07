#!/usr/bin/env python3

from core import get_options, load_input_part_2
from operator import mul
from functools import reduce, partial


def get_cols_widths(lines: list[str]) -> list[int]:
    widths = []
    line = [' '] * len(lines[0])
    print(line)
    for l in lines:
        for i, char in enumerate(l):
            if char.isdigit():
                line[i] = '9'
    print(''.join(line))
    in_digits = True
    prev_index = 0
    for i, char in enumerate(line):
        if char.isdigit():
            if not in_digits:
                widths.append(i - prev_index)
                prev_index = i
                in_digits = True
        else:
            in_digits = False
    if prev_index < len(line):
        widths.append(len(line) - prev_index)
    return widths

def multiply(values):
    return reduce(mul, values, 1)


def batch(line, size=3):
    parts = (len(line) + 1) // (size + 1)
    for i in range(parts):
        pos = i * size + i
        yield line[pos: pos + size]


def unverticalize(nums: list[list[str]]) -> int:
    print('\tunverticalize')
    print('\t', nums, 'nums')
    num_cols = len(nums[0])
    print(f'\tnum_cols: {num_cols}')
    for index in range(num_cols):
        result = []
        print(f'\t\tindex: {index}')
        buff = [num[index] for num in nums]
        print(f'\t\tbuff: {buff!r}')
        for j in range(3):
            acc = []
            for value in buff:
                if value[j] != ' ':
                    acc.append(value[j])
            print(f'\t\tacc: {acc!r}')
            if acc:
                result.append(int(''.join(acc)))
        print(f"\t\tresult: {result}")
        yield result


def main(options):
    '''Day 6, part 1'''
    verbose = options.verbose
    *nums, ops = load_input_part_2(options.filename)
    widths = get_cols_widths(nums)
    print(widths)
    return
    print(f"ops: {ops} nums: {nums!r}")
    nums = [list(batch(l, 3)) for l in nums]
    print(f"ops: {ops} nums: {nums!r}")
    nums = list(unverticalize(nums)) 
    print(f"ops: {ops} nums: {nums!r}")
    print()
    acc = 0
    for op, num in zip(ops, nums):
        print(f"- ops: {ops!r}")
        print(f"- nums: {num!r}")
        match op:
            case '+':
                sol = sum(num)
            case '*':
                sol = multiply(num)
            case _:
                raise ValueError(f"What the f*&^ing hell is {op}?")
        acc += sol
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
