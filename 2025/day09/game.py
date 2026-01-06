#!/usr/bin/env python

import argparse

import pygame

from vectors import V2, V3

MIN_WIDTH = 255
MIN_HEIGHT = 255


def get_options():
    parser = argparse.ArgumentParser(prog='Game demo', add_help=False)
    parser.add_argument('-s', '--scale', type=float, default=1.0)
    parser.add_argument('-w', '--width', type=int, default=MIN_WIDTH)
    parser.add_argument('-h', '--height', type=int, default=MIN_HEIGHT)
    parser.add_argument('-f', '--fps', type=int, default=24)
    return parser.parse_args()


class Game:

    def __init__(self, width=MIN_WIDTH, height=MIN_HEIGHT):
        options = get_options()
        self.width = max(width, options.width)
        self.height = max(height, options.height)
        self.scale = options.scale
        self.size = (
            (self.width + 1) * self.scale,
            (self.height + 1) * self.scale,
            )
        self.fps = options.fps
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont('Serif', 20)
        self.background_color = 'black'

    def label(self, text, x=None, y=None):
        '''Write text in screen.
        '''
        x = self.width / 2 if x is None else x
        y = self.height / 2 if y is None else y
        text = str(text)
        text_surface = self.font.render(text, True, 'white')
        self.screen.blit(text_surface, (x, y))

    def show_fps(self):
        '''Show actual FPS in screen.
        '''
        actual_fps = self.clock.get_fps()
        s_fps = f'{actual_fps:.02f} FPS'
        self.label(s_fps, x=2, y=2)

    def clear(self):
        rect = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(self.screen, self.background_color, rect)

    def project(self, point: V3) -> V2:
        _x = point.x / point.z
        _y = point.y / point.z
        x = (_x + 1) * self.width / 2.0
        y = (1 - ((_y + 1) / 2.0)) * self.height
        return V2(x, y)

    def box(self, x0, y0, x1, y1, color="white", scale=None):
        scale = scale or self.scale
        x = min(x0, x1)
        y = min(y0, y1)
        width = abs(x1 - x0)
        height = abs(y1 - y0)
        rect = pygame.Rect(x*scale, y*scale, width*scale, height*scale)        
        pygame.draw.rect(self.screen, color, rect)

    def point(self, point: V2, color='green', size=10):
        offset = size // 2
        rect = pygame.Rect(
            point.x - offset,
            point.y - offset,
            size,
            size,
            )        
        pygame.draw.rect(self.screen, color, rect)

    def line(self, p0, p1, color='green', width=3):
        pygame.draw.line(
            self.screen,
            color,
            (p0.x, p0.y),
            (p1.x, p1.y),
            width,
            )

    def dot(self, point, color='white', scale=None):
        scale = scale or self.scale
        rect = pygame.Rect(
            point.x * scale - 1,
            point.y * scale - 1,
            3,
            3,
            )
        pygame.draw.rect(self.screen, color, rect)

    def cross(self, point, color='white'):
        x = point.x * self.scale
        y = point.y * self.scale
        box = pygame.Rect(x - 4, y - 1, 8, 3)
        pygame.draw.rect(self.screen, color, box)
        box = pygame.Rect(x - 1, y - 4, 3, 8)
        pygame.draw.rect(self.screen, color, box)

    def run(self, functor):
        running = True
        while running:
            self.screen.fill(self.background_color)
            running = functor(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
            
            pygame.display.flip()
            self.clock.tick(self.fps)  # limits FPS

        


