#!/usr/bin/env python3

import math
#!/usr/bin/env python3

import random
from itertools import combinations, pairwise
from functools import cache
from collections import defaultdict

from vectors import V2, area
from colors import red, green, yellow
from core import get_options, load_input
from frontiers import Frontiers, bonded




def get_all_points(min_width, max_width, min_height, max_height):
    for y in range(min_height, max_height + 1):
        for x in range(min_width, max_width + 1):
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
    num_points = (
        (max_width - min_width + 1)
        * (max_height - min_height + 1)
        )
    height = max_height - min_height + 1
    frontiers = Frontiers()
    min_x_step = math.inf
    min_y_step = math.inf
    for v1, v2 in pairwise(points):
        if v1.y == v2.y:
            x_step = abs(v1.x - v2.x) + 1
            if x_step < min_x_step:
                min_x_step = x_step
        elif v1.x == v2.x:
            y_step = abs(v1.y - v2.y) + 1
            if y_step < min_y_step:
                min_y_step = y_step
        frontiers.add(v1, v2)
    frontiers.add(points[-1], points[0])  # Join last point with first one
    print(f'Points: {len(points)}')
    print(f'Perimeter: {len(frontiers.perimeter)}')
    print(f'Total num. of points: {num_points}')
    print(f'Width: {min_width} ~ {max_width}')
    print(f'Height: {min_height} ~ {max_height}')
    print(f'Min. X step: {min_x_step}')
    print(f'Min. Y step: {min_y_step}')
    print(f'Space is: {width} × {height}')
    print(f'Líneas horizontales: {len(frontiers.horizontal)}')
    print(f'Líneas verticales: {len(frontiers.vertical)}')
    if frontiers.is_inside(V2(7, 2), verbose=True):
        print('It\'s inside')
    else:
        print('It\'s outside')


if __name__ == '__main__':
    main(get_options())
