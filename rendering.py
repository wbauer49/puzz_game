
import pygame

import blocks
from constants import *
import levels
import map_grid
import controls


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

        for row, row_list in enumerate(map_grid.GRID):
            for col, block in enumerate(row_list):
                if block is None or type(block) is blocks.Wall:
                    continue
                self.screen.blit(block.sprite, (col * BLOCK_SIZE, row * BLOCK_SIZE))

        if controls.drag_obj is not None:
            self.screen.blit(controls.drag_obj.sprite, (controls.drag_pos[0], controls.drag_pos[1]))

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

    def go_to_level(self, level_num):
        self.curr_level = levels.get_level(level_num)
        self.render_layout(self.curr_level.layout)

        map_grid.init_grid(self.curr_level)
