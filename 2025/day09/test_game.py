#!/usr/bin/env python

from vectors import V2
from vectors import V3
from game import Game

WIDTH = 512
HEIGHT = 512



def main():
    '''Game lib demo.
    '''
    game = Game()
    points = [
        V3(-0.5, 0.5, 0.5),
        V3(0.5, 0.5, 0.5),
        V3(0.5, -0.5, 0.5),
        V3(-0.5, -0.5, 0.5),

        V3(-0.5, 0.5, -0.5),
        V3(0.5, 0.5, -0.5),
        V3(0.5, -0.5, -0.5),
        V3(-0.5, -0.5, -0.5),
        ]
    edges = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7],
        ]
    dt = 0.5 / game.fps
    dz = 1.0

    def loop(game: Game):
        nonlocal points, dz    
        game.clear()
        game.show_fps()
        # for p in points:
            # game.point(
                # game.project(p.rotate_on_y(dz) + V3(0, 0, dz))
                # )
        for indexes in edges:
            for index in range(len(indexes)):
                p0 = points[indexes[index]]
                p1 = points[indexes[(index + 1) % len(indexes)]]
                game.line(
                    game.project(p0.rotate_on_y(dz) + V3(0, 0, dz)),
                    game.project(p1.rotate_on_y(dz) + V3(0, 0, dz)),
                    )
        dz += dt

        if dz > 10:
            return False
        return True
    
    game.run(loop)

    print(f'Game lib demo')


if __name__ == '__main__':
    main()
