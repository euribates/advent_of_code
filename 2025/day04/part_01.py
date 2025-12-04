#!/usr/bin/env python3

from core import get_options, load_input
from world import World
from colors import green, red, yellow


def has_access(world: World, x: int, y: int) -> bool:
    counter = 0
    if world.rows[y][x] == '.':
        return False
    for n_x, n_y in world.neighbours(x, y):
        if not world.is_empty(n_x, n_y):
            counter += 1
    return counter < 4


def dump(world):
    buff = []
    for x, y, char in world:
        if has_access(world, x, y):
            buff.append(yellow('x'))
        else:
            if world.is_empty(x, y):
                buff.append(green(char))
            else:
                buff.append(red(char))
        if x == (world.width - 1):
            buff.append('\n')
    return ''.join(buff)


def main(options):
    '''Day 4, part 1'''
    verbose = options.verbose
    acc = 0
    world = World(load_input(options.filename))
    if verbose:
        print(dump(world))
    for (x, y, _char) in world:
        if has_access(world, x, y):
            acc += 1
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
    main(get_options())
