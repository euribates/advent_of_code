#!/usr/bin/env python3

from collections import deque
from collections import Counter
from itertools import permutations

from tqdm import tqdm

from core import get_options, load_input


def main(options):
    '''Day 10, part 2.
    '''
    options = get_options()
    machines = list(load_input(options.filename))
    acc = 0
    for machine in machines:
        machine.mode = 2
        print(machine)
        commands = list(machine.get_commands())
        for cmds in tqdm(permutations(commands, 4)):
            machine.reset()
            for cmd in cmds:
                machine.apply_command(cmd)
            if machine.is_working():
                print('\t', cmds)
                from icecream import ic; ic(machine)
                from icecream import ic; ic(machine.counters)
                input()
        break
    label = main.__doc__.strip()
    print(f'Solution {label}: {acc}')


if __name__ == '__main__':
    main(get_options())
