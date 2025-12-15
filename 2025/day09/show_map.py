#!/usr/bin/env python3

import math
import random
from itertools import combinations, pairwise
from functools import cache
from collections import defaultdict

from game import Game
from vectors import V2, area
from colors import red, green, yellow
from core import get_options, load_input
from frontiers import Frontiers


def get_all_points(width, height):
    for y in range(height + 1):
        for x in range(width + 1):
            yield V2(x, y)


def main(options):
    '''Show map
    '''
    options = get_options()
    points = list(load_input(options.filename))
    width = max(p.x for p in points)
    height = max(p.y for p in points)
    game = Game(width, height, options)
    frontiers = Frontiers()
    min_x_step = math.inf
    for v1, v2 in pairwise(points):
        x_step = math.abs(v1.x, v2.x) + 1
        if x_step < min_x_step:
            min_x_step = x_step
        frontiers.add(v1, v2)
    frontiers.add(points[-1], points[0])  # Join last point with first one

    def show_map(game: Game):
        game.show_fps()
        for p in get_all_points(width, height):
            if frontiers.is_inside(p):
                game.cross(p, color='white')
        for p in frontiers.perimeter:
            game.dot(p, color='green')
        for p in frontiers.vertexs:
            game.dot(p, color='red')
        return True

    game.run(show_map)


if __name__ == '__main__':
    main(get_options())
