#!/usr/bin/env python3

from dataclasses import dataclass

from core import get_options, load_input
from world import World
from colors import red, green



@dataclass(frozen=True)
class Tachyon:

    x: int = 0
    y: int = 0

    class Meta:
        actives = set([])
        stoped = set([])
        num_splits = 0


    @classmethod
    def actives(cls):
        return sorted(
            [t for t in cls.Meta.actives],
            key=lambda t: t.y,
            )

    def __hash__(self):
        return hash((self.x, self.y))

    def stop(self):
        self.Meta.stoped.add(self)
        self.Meta.actives.discard(self)

    def __post_init__(self):
        Tachyon.Meta.actives.add(self)

    @classmethod
    def at(cls, x, y):
        for tachyon in Tachyon.Meta.actives:
            if tachyon.x == x and tachyon.y == y:
                return tachyon
        for tachyon in Tachyon.Meta.stoped:
            if tachyon.x == x and tachyon.y == y:
                return tachyon
        return None

    @classmethod
    def move(cls, world, step=None):
        # make moves firts
        actives_now = list(cls.actives())
        # print('Move phase')
        # print(f'step: {step}: actives_now={actives_now!r}')
        moved = []
        for t in actives_now:
            t.stop()
            # print(f'Ananalize {t} (move phase):')
            landing = world[(t.x, t.y + 1)]
            # print(f'\t- World at {t.x}, {t.y + 1} is {landing}')
            if world[(t.x, t.y + 1)] == '.':
                # print(f'\t- Move to {t.x}, {t.y + 1}')
                if t.y + 1 < world.height:
                    Tachyon(t.x, t.y + 1)
                moved.append(t)
            # else:
                # print(f'\t- Tachyon {t} can not move')
        # print('Split phase')
        actives_now = [t for t in actives_now if t not in moved]
        # print(f'step: {step}: actives_now={actives_now!r}')
        # Then splits
        for t in actives_now:
            t.stop()
            # print(f'Ananalize {t} (split phase):')
            if world[(t.x, t.y + 1)] == '^':
                t.split(world)

    def split(self, world):
        if self.y <= world.height:
            if world[(self.x - 1, self.y + 1)] == '.':
                if not Tachyon.at(self.x-1, self.y + 1):
                    if self.y + 1 < world.height:
                        Tachyon(self.x-1, self.y + 1)
            if world[(self.x + 1, self.y + 1)] == '.':
                if not Tachyon.at(self.x + 1, self.y + 1):
                    if self.y + 1 < world.height:
                        Tachyon(self.x + 1, self.y + 1)
            Tachyon.Meta.num_splits += 1


def dump(world):
    buff = []
    for (y, row) in enumerate(world.rows):
        line = []
        for x, char in enumerate(row):
            if t := Tachyon.at(x, y):
                if t in Tachyon.Meta.stoped:
                    line.append(red('|'))
                else:
                    line.append(green('|'))
            else:
                line.append(char)
        buff.append(''.join(line))
    num_stoped = len(Tachyon.Meta.stoped)
    num_actives = len(Tachyon.Meta.actives)
    buff.append(f'Tachyons: {num_stoped + num_actives}')
    buff.append(f' actives: {num_actives}')
    buff.append(f'  splits: {Tachyon.Meta.num_splits}')
    return '\n'.join(buff)


def main(options):
    '''Day 7, part 1'''
    verbose = options.verbose
    debug = options.debug
    acc = 0
    start_x, start_y, lines = load_input(options.filename)
    rows = len(lines)
    cols = len(lines[0])
    if verbose:
        print(f'start_x: {start_x}')
        print(f'start_y: {start_y}')
        print(f'size: {cols} x {rows}')
    world = World(lines)
    Tachyon(start_x, start_y)
    if verbose:
        print(dump(world))
        print('move')
    active_tachyons = Tachyon.actives()
    step = 0
    if verbose:
        print(dump(world), f'step: {step}', sep='\n')
        if debug:
            input()
    while Tachyon.actives():
        for t in Tachyon.actives():
            t.move(world, step=step)
        step += 1
        if verbose:
            print("\033[H\033[2J", end="")
            print(dump(world), f'step: {step}', sep='\n')
        if debug:
            input()

    acc = Tachyon.Meta.num_splits
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
     main(get_options())
