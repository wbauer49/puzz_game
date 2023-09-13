
import os
import pygame

from constants import *
import env


class Renderer:

    layout_render = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.flip()

        sprite_path = os.path.join(os.path.dirname(__file__), "sprites", f"step_indicator.png")
        unscaled_sprite = pygame.image.load(sprite_path)
        self.step_sprite = pygame.transform.scale(unscaled_sprite, (PIX * 2, PIX * 2))

    def render(self):
        self.screen.blit(self.layout_render, (0, 0))

        for row, row_list in enumerate(env.grid.grid):
            for col, block in enumerate(row_list):
                if block is None or block.is_wall:
                    continue
                self.screen.blit(block.sprite, (col * PIX, row * PIX))

        if env.controller.drag_obj is not None:
            self.screen.blit(env.controller.drag_obj.sprite, (env.controller.drag_pos[0], env.controller.drag_pos[1]))

        i = env.grid.curr_step % len(env.grid.curr_level.item_order)
        self.screen.blit(self.step_sprite, (i * PIX * 2, HEIGHT - PIX * 2))

        pygame.display.flip()

    def render_layout(self, level):
        self.layout_render = pygame.Surface((WIDTH, HEIGHT))
        self.layout_render.fill(COLORS.BORDERS)

        grid_surface = pygame.Surface((len(level.layout[0]) * PIX, len(level.layout) * PIX))
        grid_surface.fill(COLORS.BACKGROUND)
        self.layout_render.blit(grid_surface, (0, 0))

        for row, row_list in enumerate(level.layout):
            for col, block_type in enumerate(row_list):
                if block_type == "1":
                    wall_surface = pygame.Surface((PIX, PIX))
                    wall_surface.fill(COLORS.WALL)
                    self.layout_render.blit(wall_surface, (col * PIX, row * PIX))
                elif (col, row) == level.end_coords:
                    goal_surface = pygame.Surface((PIX, PIX))
                    goal_surface.fill(COLORS.GOAL)
                    self.layout_render.blit(goal_surface, (col * PIX, row * PIX))

        work_surface = pygame.Surface((PIX * level.workspace_rect[2], PIX * level.workspace_rect[3]))
        work_surface.fill(COLORS.WORKSPACE)
        self.layout_render.blit(work_surface, (level.workspace_rect[0] * PIX, level.workspace_rect[1] * PIX))

        for i, item_type in enumerate(level.item_order):
            sprite = pygame.transform.scale2x(item_type().sprite)
            self.layout_render.blit(sprite, (i * PIX * 2, HEIGHT - PIX * 2))
