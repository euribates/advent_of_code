#!/usr/bin/env python3

from dataclasses import dataclass
from collections import Counter

import pygame

from core import get_options, load_input
from world import World
from colors import red, green

TachyonMap = Counter()

@dataclass(frozen=True)
class Tachyon:

    x: int = 0
    y: int = 0
    path: int = 0

    def __post_init__(self):
        TachyonMap[(self.x, self.y)] += 1

    def __del__(self):
        if (self.x, self.y) in TachyonMap:
            TachyonMap[(self.x, self.y)] -= 1

    def move(self, world):
        landing = world[(self.x, self.y + 1)]
        if landing == '.':
            yield Tachyon(self.x, self.y + 1, self.path)
        else:
            assert landing == '^', "WTF!"
            yield Tachyon(self.x-1, self.y + 1, self.path << 1)
            yield Tachyon(self.x+1, self.y + 1, self.path << 1 | 1)


def draw_world(screen, world, scale, size, font):
    screen.fill("black")
    text_surface = font.render(str(size), True, 'white')
    screen.blit(text_surface, (2, 2))
    for y in range(world.height):
        for x in range(world.width):
            if tachyons := TachyonMap[(x, y)] > 0:
                color = 'red' if tachyons > 10 else 'green'
                pygame.draw.rect(screen, color, pygame.Rect(
                    x * scale,
                    y * scale,
                    scale,
                    scale,
                    ))
    pygame.display.flip()


def main(options):
    '''Day 7, part 2'''
    scale = 4 
    acc = 0
    start_x, start_y, lines = load_input(options.filename)
    rows = len(lines)
    cols = len(lines[0])
    pygame.init()
    font = pygame.font.SysFont('Serif', 20)
    screen = pygame.display.set_mode((cols * scale, rows * scale))
    clock = pygame.time.Clock()

    world = World(lines)
    tachyones = set([Tachyon(start_x, start_y)])
    for _ in range(rows - 1):
        draw_world(screen, world, scale, len(tachyones), font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        tachyons_to_delete = set([])
        for parent in list(tachyones):
            for son in parent.move(world):
                tachyones.add(son)
            tachyons_to_delete.add(parent)
        for tachyon in list(tachyons_to_delete):
            tachyones.discard(tachyon)
            del tachyon
        clock.tick(24)

    acc = len(tachyones)
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
     main(get_options())
