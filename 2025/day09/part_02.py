#!/usr/bin/env python3

from itertools import pairwise

from game import Game
from vectors import V2
from core import get_options, load_input
from frontiers import Frontiers

step = 0
acc = 0
X0 = 0
Y0 = 0
X1 = 0
Y1 = 0

    
def check_is_inside(frontiers, x0, y0, x1, y1) -> bool:
    if not frontiers.is_inside(V2(x0, y1)):
        return False
    if not frontiers.is_inside(V2(x1, y0)):
        return False
    if y0 > y1:
        y0, y1 = y1, y0
    if x0 > x1:
        x0, x1 = x1, x0
    for y in range(y0 + 1, y1):
        if not frontiers.is_inside(V2(x0, y)):
            return False
        if not frontiers.is_inside(V2(x1, y)):
            return False
    for x in range(x0 + 1, x1):
        if not frontiers.is_inside(V2(x, y0)):
            return False
        if not frontiers.is_inside(V2(x, y1)):
            return False
    return True


def main(options):
    '''Day 9, part 2.
    '''
    global acc, step
    options = get_options()
    points = list(load_input(options.filename))
    width = max(p.x for p in points) + 1
    height = max(p.y for p in points) + 1

    frontiers = Frontiers()
    for v1, v2 in pairwise(points):
        frontiers.add(v1, v2)
    frontiers.add(points[-1], points[0])  # Join last point with first one
    size = (len(points) + 1) * len(points)
    candidates = frontiers.get_candidates()
    perimeter = {
        V2(int(p.x * options.scale), int(p.y * options.scale))
        for p in frontiers.perimeter
        }
    vertexs = {
        V2(int(p.x * options.scale), int(p.y * options.scale))
        for p in frontiers.vertexs
        }
    game = Game(width, height, options)
    
    def loop(game: Game):
        global acc, step, X0, Y0, X1, Y1
        game.show_fps()
        step = min(size, step + 1)
        percent = step * 100.0 / size
        game.label(f'{step} / {size} {percent:.02f}%', x=2, y=20)
        for p in perimeter:
            game.dot(p, 'green', scale=1.0)
        for p in vertexs:
            game.dot(p, 'red', scale=1.0)
        try:
            (p1, p2, area) = next(candidates)
            if area > acc:
                game.dot(p1, color='purple')
                game.dot(p2, color='purple')
                is_inside = check_is_inside(frontiers, p1.x, p1.y, p2.x, p2.y)
                if is_inside:
                    X0 = p1.x
                    Y0 = p1.y
                    X1 = p2.x
                    Y1 = p2.y
                    print(X0, Y0, X1, Y1)
                    acc = area
            game.box(X0, Y0, X1, Y1, 'green')
        except StopIteration:
            return False
        return True
    
    game.run(loop)

    print(f'Solution day 2 part 1: {acc}')


if __name__ == '__main__':
    main(get_options())
