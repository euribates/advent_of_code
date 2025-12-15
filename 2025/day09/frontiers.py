#!/usr/bin/env python3

from collections import defaultdict
from functools import cache
from itertools import combinations
from vectors import V2, area


def bonded(v1, v2):
    if v1 <= v2:
        return v1, v2
    else:
        return v2, v1



class FilledBoxes:

    def __init__(self, x, y, width=1, height=1):
        self.p0 = V2(x, y)
        self.p1 = V2(x + width, y + height)

    def __contains__(self, point: V2):
        return (
               self.p0.x <= point.x < self.p1.x
           and self.p0.y <= point.y < self.p1.y
           )

    @property
    def width(self):
        return self.p1.x - self.p0.x

    @property
    def height(self):
        return self.p1.y - self.p0.y

    @property
    def area(self):
        return self.width * self.height

    def expand_right(self):
        return FilledBoxes(self.p0.x, self.p0.y, width=self.width+1, height=self.height)
    
    def expand_left(self):
        return FilledBoxes(self.p0.x - 1, self.p0.y, width=self.width+1, height=self.height)

    def expand_up(self):
        return FilledBoxes(self.p0.x, self.p0.y - 1, width=self.width, height=self.height + 1)
        
    def expand_down(self):
        return FilledBoxes(self.p0.x, self.p0.y, width=self.width, height=self.height + 1)
        

class Frontiers:

    def __init__(self):
        self.vertexs = set([])
        self.perimeter = set([])
        self.horizontal = defaultdict(list)
        self.vertical = defaultdict(list)

    def add(self, v1: V2, v2: V2):
        self.vertexs.add(v1)
        self.vertexs.add(v2)
        if v1.x == v2.x: # Vertical
            _y0, _y1 = bonded(v1.y, v2.y)
            self.vertical[v1.x].append((_y0, _y1))
            for _y in range(_y0 + 1, _y1):
                self.perimeter.add(V2(v1.x, _y))
        elif v1.y == v2.y:  # Horizontal
            _x0, _x1 = bonded(v1.x, v2.x)
            self.horizontal[v1.y].append((_x0, _x1))
            for x in range(_x0 + 1, _x1):
                self.perimeter.add(V2(x, v1.y))
        else:
            raise ValueError(f'Something is wrong, {v1}, {v2} not in the same axis')

    def get_candidates(self):
        for p1, p2 in combinations(self.vertexs, 2):
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
