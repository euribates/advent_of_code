#!/usr/bin/env python3

from core import get_options, load_input

INITIAL = 50


def bold(text):
    text = str(text)
    return f'\33[1m{text}\33[0m'


def main(options):
    '''Day 1, part 2.
    '''
    counter = 0
    position = INITIAL
    if options.verbose:
        print(f'The dial starts by pointing at {position};')
    for cmd, steps in load_input(options.filename):
        if steps > 100:
            counter += steps // 100
            steps = steps % 100
        prev_pos = position
        if cmd == 'R':
            position = (position + steps) % 100
        elif cmd == 'L':
            position = (position - steps) % 100
        if options.verbose:
            if position == 0:
                print(f'The dial is rotated {cmd}{steps} to point at {bold(position)};', end=' ')
            else:
                print(f'The dial is rotated {cmd}{steps} to point at {position};', end=' ')
        if position == 0:
            counter += 1
            if options.verbose:
                print()
        elif cmd == 'R' and prev_pos > 0 and prev_pos + steps > 100:
            if options.verbose:
                print(f'during this rotation, it points at 0 {bold("once")}.')
            counter += 1
        elif cmd == 'L' and prev_pos > 0 and prev_pos - steps < 0:
            if options.verbose:
                print(f'during this rotation, it points at 0 {bold("once")}.')
            counter += 1
        else:
            if options.verbose:
                print()


    print(f'[Day 1] Sol. part two is: {counter}')


if __name__ == '__main__':
    main(get_options())
