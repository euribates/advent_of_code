#!/usr/bin/env python3


class World:

    def __init__(self, matrix):
        self.rows = matrix.copy()
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def copy(self):
        return World(self.rows)

    def __str__(self):
        buff = [
            f'World {self.width} x {self.height}',
            '------------------------------------------',
            ]
        for row in self.rows:
            line = []
            for char in row:
                line.append(char)
            buff.append(''.join(line))
        buff.append('------------------------------------------')
        return '\n'.join(buff)

    def is_empty(self, x: int, y: int) -> bool:
        if 0 <= x < self.width:
            if 0 <= y < self.height:
                row = self.rows[y]
                if row[x] == '@':
                    return False
        return True

    def __iter__(self):
        self._x = 0
        self._y = 0
        return self

    def __next__(self):
        result = (self._x, self._y, self.rows[self._y][self._x])
        self._x = (self._x + 1) % self.width
        if self._x == 0:
            self._y = (self._y + 1) % self.height
            if self._y == 0:
                raise StopIteration
        return result

    def neighbours(self, x, y):
        for delta_x in [-1, 0, 1]:
            for delta_y in [-1, 0, 1]:
                if delta_x == delta_y == 0:
                    continue
                yield (x + delta_x, y + delta_y)
