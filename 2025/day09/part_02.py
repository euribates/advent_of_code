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
from frontiers import Frontiers, bonded

# SCALE = .01
SCALE = 10
FONT = None
SCREEN = None
CLOCK = None
FPS = 1

    
def dot(screen, p, color='white', scale=SCALE):
    rect = pygame.Rect(p.x * scale, p.y * scale, 3, 3)
    pygame.draw.rect(screen, color, rect)


def get_all_points(width, height):
    for y in range(height + 1):
        for x in range(width + 1):
            yield V2(x, y)


def main(options):
    '''Day 9, part 2.
    '''
    global SCREEN, FONT, SCALE

    options = get_options()
    SCALE = options.scale
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
    FPS = options.fps
    SCREEN = pygame.display.set_mode(((max_width + 1) * SCALE, (max_height + 1) * SCALE))
    FONT = pygame.font.SysFont('Serif', 20)
    clock = pygame.time.Clock()
    running = True

    candidates = frontiers.get_candidates()
    perimeter = {
        V2(int(p.x * SCALE), int(p.y * SCALE))
        for p in frontiers.perimeter
        }
    vertexs = {
        V2(int(p.x * SCALE), int(p.y * SCALE))
        for p in frontiers.vertexs
        }
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        SCREEN.fill("black")
        s_fps = str(clock.get_fps())
        text_surface = FONT.render(s_fps, True, 'white')
        SCREEN.blit(text_surface, (2, 2))

        for p in perimeter:
            dot(SCREEN, p, 'yellow', scale=1.0)
        for p in vertexs:
            dot(SCREEN, p, 'green', scale=1.0)

        try:
            (p1, p2, area) = next(candidates)
        except StopIteration:
            running = False

        if area > acc:
            dot(SCREEN, p1, color='purple', scale=SCALE)
            dot(SCREEN, p2, color='purple', scale=SCALE)
            is_inside = True
            y0, y1 = bonded(p1.y, p2.y)
            x0, x1 = bonded(p1.x, p2.x)
            for y in range(y0, y1 + 1):
                for x in range(x0, x1 + 1):
                    if not frontiers.is_inside(V2(x, y)):
                        is_inside = False
                        break
                if is_inside is False:
                    break
            rect = pygame.Rect(
                x0 * SCALE,
                y0 * SCALE,
                (x1 - x0) * SCALE,
                (y1 - y0) * SCALE,
                )
            if is_inside:
                pygame.draw.rect(SCREEN, 'green', rect)
                acc = max(acc, area)
            else:
                pygame.draw.rect(SCREEN, 'red', rect)
        pygame.display.flip()
        clock.tick(FPS)  # limits FPS


    print(f'Solution day 2 part 1: {acc}')


if __name__ == '__main__':
    main(get_options())
