
import os
import pygame

import blocks
from constants import *
import env


class Renderer:

    layout_render = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

        sprite_path = os.path.join(os.path.dirname(__file__), "sprites", f"step_indicator.png")
        unscaled_sprite = pygame.image.load(sprite_path)
        self.step_sprite = pygame.transform.scale(unscaled_sprite, (BLOCK_SIZE * 2, BLOCK_SIZE * 2))

    def render(self):
        self.screen.blit(self.layout_render, (0, 0))

        for row, row_list in enumerate(env.grid.grid):
            for col, block in enumerate(row_list):
                if block is None or type(block) is blocks.Wall:
                    continue
                self.screen.blit(block.sprite, (col * BLOCK_SIZE, row * BLOCK_SIZE))

        if env.controller.drag_obj is not None:
            self.screen.blit(env.controller.drag_obj.sprite, (env.controller.drag_pos[0], env.controller.drag_pos[1]))

        i = env.grid.current_step % len(env.grid.item_order)
        self.screen.blit(self.step_sprite, (i * BLOCK_SIZE * 2, HEIGHT - BLOCK_SIZE * 2))

        pygame.display.flip()

    def render_layout(self, level):
        self.layout_render = pygame.Surface((WIDTH, HEIGHT))
        self.layout_render.fill(BACKGROUND_COLOR)
        for row, row_list in enumerate(level.layout):
            for col, block_type in enumerate(row_list):
                if block_type == 1:
                    wall_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
                    wall_surface.fill(WALL_COLOR)
                    self.layout_render.blit(wall_surface, (col * BLOCK_SIZE, row * BLOCK_SIZE))
                elif (col, row) == level.end_coords:
                    goal_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
                    goal_surface.fill((225, 255, 127))
                    self.layout_render.blit(goal_surface, (col * BLOCK_SIZE, row * BLOCK_SIZE))

        work_surface = pygame.Surface((BLOCK_SIZE * level.workspace_rect[2], BLOCK_SIZE * level.workspace_rect[3]))
        work_surface.fill((200, 156, 255))
        self.layout_render.blit(work_surface, (level.workspace_rect[0] * BLOCK_SIZE, level.workspace_rect[1] * BLOCK_SIZE))

        for i, item_type in enumerate(level.item_order):
            sprite = pygame.transform.scale2x(item_type().sprite)

            self.layout_render.blit(sprite, (i * BLOCK_SIZE * 2, HEIGHT - BLOCK_SIZE * 2))
