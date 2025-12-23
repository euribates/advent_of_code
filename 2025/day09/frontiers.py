#!/usr/bin/env python3

from collections import defaultdict
from functools import cache
from itertools import combinations
from vectors import V2, area


class Frontiers:

    def __init__(self):
        self.vertexs = list()
        self.perimeter = set([])
        self.horizontal = defaultdict(list)
        self.vertical = defaultdict(list)

    def add(self, v1: V2, v2: V2):
        if len(self.vertexs) == 0: 
            self.vertexs.append(v1)
        else:
            assert self.vertexs[-1] == v1
        self.vertexs.append(v2)
        if v1.x == v2.x: # Vertical
            y0, y1 = (v1.y, v2.y) if v1.y <= v2.y else (v2.y, v1.y)
            self.vertical[v1.x].append((y0, y1))
            for y in range(y0 + 1, y1):
                self.perimeter.add(V2(v1.x, y))
        elif v1.y == v2.y:  # Horizontal
            x0, x1 = (v1.x, v2.x) if v1.x <= v2.x else (v2.x, v1.x)
            self.horizontal[v1.y].append((x0, x1))
            for x in range(x0 + 1, x1):
                self.perimeter.add(V2(x, v1.y))
        else:
            raise ValueError(f'Something is wrong, {v1}, {v2} not in the same axis')

    def get_candidates(self):
        for p1, p2 in combinations(self.vertexs[0:-1], 2):
            yield p1, p2, area(p1, p2)

    @cache
    def is_inside(self, p: V2, verbose=False) -> True:
        # count horizontal lines
        if verbose: print(f'\t- Check if {p} is in vertex set')
        if p in self.vertexs:
            if verbose: print('\tyes, it is.')
            return True
        if verbose: print(f'\t- Check if {p} is in perimeter')
        if p in self.perimeter:
            if verbose: print('\tyes, it is.')
            return True
        if verbose:
            print(f'\t- Check if {p} is inside')
        x = p.x + 0.5
        y = p.y + 0.5
        x_is_inside = False
        for _y in sorted(self.horizontal.keys()):
            if verbose:
                print(f'\t\tChecking horizontal lines in y = {y}')
            if _y > y:
                if verbose:
                    print(f'\t\t\tBreak, _y {_y} > {y} y')
                break
            lines = self.horizontal[_y]
            for line in lines:
                if verbose:
                    print(f'\t\t\t{line[0]} <= {p.x} <= {line[1]} {line[0] <= p.x <= line[1]}')
                x_is_inside ^= bool(line[0] <= x <= line[1])
        if verbose:
            print(f'\t\tx_is_inside is {x_is_inside}')
        y_is_inside = False
        for _x in sorted(self.vertical.keys()):
            if verbose:
                print(f'\t\tChecking vertical lines in x = {_x}')
            if _x > x:
                if verbose:
                    print(f'\t\t\tBreak, _x {_x} > {x} x')
                break
            lines = self.vertical[_x]
            for line in lines:
                if verbose:
                    print(f'\t\t\t{line[0]} <= {p.y} <= {line[1]} {line[0] <= p.y <= line[1]}')
                y_is_inside ^= bool(line[0] <= y <= line[1])
        if verbose:
            print(f'\t\ty_is_inside is {y_is_inside}')
        return x_is_inside and y_is_inside
