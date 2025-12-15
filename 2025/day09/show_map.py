#!/usr/bin/env python3

import math
import random
from itertools import combinations, pairwise
from functools import cache
from collections import defaultdict

import pygame

from vectors import V2, area
from colors import red, green, yellow
from core import get_options, load_input
from frontiers import Frontiers


# SCALE = .01
SCALE = 10
FONT = None
SCREEN = None
CLOCK = None
FPS = 1


def box(screen, p, color='white', scale=SCALE):
    box = pygame.Rect(p.x * scale, p.y * scale, 3, 3)
    pygame.draw.rect(screen, color, box)


def cross(screen, p, color='white', scale=SCALE):
    x = p.x * scale
    y = p.y * scale
    box = pygame.Rect(x - 3, y - 1, 6, 3)
    pygame.draw.rect(screen, color, box)
    box = pygame.Rect(x - 1, y - 3, 3, 6)
    pygame.draw.rect(screen, color, box)


def get_all_points(width, height):
    for y in range(height + 1):
        for x in range(width + 1):
            yield V2(x, y)


def main(options):
    '''Day 9, part 2.
    '''
    global SCREEN, FONT, SCALE, FPS

    options = get_options()
    SCALE = options.scale
    FPS = options.fps
    points = list(load_input(options.filename))
    min_width = min(p.x for p in points)
    max_width = max(p.x for p in points) + 1
    width = max_width - min_width + 1
    min_height = min(p.y for p in points) + 1
    max_height = max(p.y for p in points)
    height = max_height - min_height + 1
    acc = 0
    frontiers = Frontiers()
    for v1, v2 in pairwise(points):
        frontiers.add(v1, v2)
    frontiers.add(points[-1], points[0])  # Join last point with first one
    if options.verbose:
        print(f'Points: {len(points)}')
        print(f'Perimeter: {len(frontiers.perimeter)}')
        print(f'Width: {min_width} ~ {max_width}')
        print(f'Height: {min_height} ~ {max_height}')
        print(f'Space is: {width} × {height}')
        print(f'Líneas horizontales: {len(frontiers.horizontal)}')
        print(f'Líneas verticales: {len(frontiers.vertical)}')
        if frontiers.is_inside(V2(7, 2), verbose=True):
            print('It\'s inside')
        else:
            print('It\'s outside')
        return

    pygame.init()
    SCREEN = pygame.display.set_mode(((max_width + 1) * SCALE, (max_height + 1) * SCALE))
    FONT = pygame.font.SysFont('Serif', 20)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        SCREEN.fill("black")
        s_fps = str(clock.get_fps())
        text_surface = FONT.render(s_fps, True, 'white')
        SCREEN.blit(text_surface, (2, 2))

        for p in get_all_points(max_width, max_height):
            if frontiers.is_inside(p):
                cross(SCREEN, p, 'white', scale=SCALE)
        for p in frontiers.perimeter:
            box(SCREEN, p, 'green', scale=SCALE)
        for p in frontiers.vertexs:
            box(SCREEN, p, 'red', scale=SCALE)

        pygame.display.flip()
        clock.tick(FPS)  # limits FPS
        print('clock')


    print(f'Solution day 2 part 1: {acc}')


if __name__ == '__main__':
    main(get_options())
