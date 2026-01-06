#!/usr/bin/env python3

from collections import deque
from collections import Counter

from tqdm import tqdm

from core import get_options, load_input


def bfs(machine, verbose=False):
    q = deque([(machine, 0)])
    count = 0
    explored = set()
    while q:
        if verbose:
            print(f'Loop count: {count}')
            print(f'  - Explored: {explored!r}')
            print(f'  - Size of queue: {len(q)}')
        machine, result = q.popleft()
        if verbose:
            print(f'  - current machine is {machine.label} [{result}]')
        if machine.is_ready():
            return result
        for index in range(len(machine.buttons)):
            new_machine = machine.press_button(index)
            if new_machine.is_ready():
                return result + 1
            if new_machine.label not in explored:
                q.append((new_machine, result + 1))
        explored.add(machine.label)
        count += 1
        if verbose:
            input('next?')
    raise ValueError('Esta máquina no se puede resolver.')


def main(options):
    '''Day 10, part 1.
    '''
    options = get_options()
    machines = list(load_input(options.filename))
    acc = 0
    for machine in tqdm(machines):
        acc += bfs(machine)
    label = main.__doc__.strip()
    print(f'Solution {label}: {acc}')


if __name__ == '__main__':
    main(get_options())
