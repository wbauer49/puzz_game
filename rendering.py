
import pygame

from constants import *
import levels


class Renderer:

    curr_level = None
    layout_render = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def render(self):
        self.screen.blit(self.layout_render, (0, 0))
        for obj in self.curr_level.objects:
            self.render_object(obj)
        pygame.display.flip()

    def render_layout(self, layout):
        self.layout_render = pygame.Surface((WIDTH, HEIGHT))
        self.layout_render.fill(BACKGROUND_COLOR)
        for row, row_list in enumerate(layout):
            for col, block_type in enumerate(row_list):
                if block_type == 1:
                    wall_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
                    wall_surface.fill(WALL_COLOR)
                    x = col * BLOCK_SIZE
                    y = row * BLOCK_SIZE
                    self.layout_render.blit(wall_surface, (x, y))

    def render_object(self, object):
        pass

    def go_to_level(self, level_num):
        self.curr_level = levels.get_level(level_num)
        self.render_layout(self.curr_level.layout)
