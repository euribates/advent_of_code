#!/usr/bin/env python3

from core import get_options, load_input

def is_invalid(num: int) -> bool:
    s = str(num)
    l = len(s)
    if l % 2:
        return False
    midpoint = l // 2
    return s[:midpoint] == s[midpoint:]


def main(options):
    '''Day 2, part 1.
    '''
    acc = 0
    for first_num, last_num in load_input(options.filename):
        for num in range(first_num, last_num + 1):
            if is_invalid(num):
                acc += num
    print(f'Solution day 2 part 1: {acc}')


if __name__ == '__main__':
    main(get_options())
