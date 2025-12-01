#!/usr/bin/env python3

from core import get_options, load_input

INITIAL = 50

def main(options):
    '''Day 1, part 1.
    '''
    counter = 0
    position = INITIAL
    for cmd, steps in load_input(options.filename):
        if cmd == 'R':
            position = (position + steps) % 100
        elif cmd == 'L':
            position = (position - steps) % 100
        if position == 0:
            counter += 1
    print(f'[Day 1] Sol. part one is: {counter}')


if __name__ == '__main__':
    main(get_options())
