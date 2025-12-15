import pygame

from vectors import V2


class Game:

    def __init__(self, width, height, options):
        self.width = max(width, 255)
        self.height = max(height, 255)
        self.scale = options.scale
        self.size = (
            (width + 1) * self.scale,
            (height + 1) * self.scale,
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

    def dot(self, point, color='white'):
        rect = pygame.Rect(
            point.x * self.scale - 1,
            point.y * self.scale - 1,
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

        


