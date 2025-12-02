#!/usr/bin/env python3

from core import get_options, load_input

def is_invalid(num: int) -> bool:
    s = str(num)
    l = len(s)
    midpoint = l // 2
    for i in range(1, midpoint + 1):
        repeated = s[:i] * (l // i)
        if repeated == s:
            return True
    return False


def main(options):
    '''Day 2, part 2.
    '''
    acc = 0
    for first_num, last_num in load_input(options.filename):
        for num in range(first_num, last_num + 1):
            if is_invalid(num):
                acc += num
    print(f'Solution day 2 part 2: {acc}')


if __name__ == '__main__':
    main(get_options())
