#!/usr/bin/env python3

from functools import cache
import pygame

from core import get_options, load_input
from world import World

SCALE = 4
FONT = None
SCREEN = None
CLOCK = None

def draw_world(world, x, y):
    SCREEN.fill("black")
    label = f'{x}×{y}'
    text_surface = FONT.render(label, True, 'white')
    SCREEN.blit(text_surface, (2, 2))
    box = pygame.Rect(x * SCALE, y * SCALE, SCALE, SCALE)
    pygame.draw.rect(SCREEN, 'green', box)
    pygame.display.flip()
    CLOCK.tick(24)


@cache
def move_and_split(world, x, y):
    if y >= world.height - 1:
        return 1
    landing = world[(x, y + 1)]
    if landing == '.':
        return move_and_split(world, x, y + 1)
    draw_world(world, x, y)
    assert landing == '^', "WTF!"
    left = move_and_split(world, x - 1, y + 1)
    right = move_and_split(world, x + 1, y + 1)
    return left + right


def main(options):
    '''Day 7, part 2'''
    global FONT, SCREEN, CLOCK
    pygame.init()
    SCALE = 4
    FONT = pygame.font.SysFont('Serif', 20)
    CLOCK = pygame.time.Clock()
    start_x, start_y, lines = load_input(options.filename)
    world = World(lines)
    SCREEN = pygame.display.set_mode((world.width * SCALE, world.height * SCALE))

    acc = move_and_split(world, start_x, start_y)
    print(f'Solution for {main.__doc__}: {acc}')


if __name__ == '__main__':
     main(get_options())
