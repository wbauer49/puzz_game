
import pygame

import blocks
from constants import *
import env


class Controller:

    drag_obj = None
    drag_pos = None

    start_coords = None

    def check_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                self.start_coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
                if env.grid.coords_in_range(self.start_coords):
                    self.drag_obj = env.grid.get_grid_block(self.start_coords)
                    self.drag_pos = (event.pos[0] - BLOCK_SIZE // 2, event.pos[1] - BLOCK_SIZE // 2)

            else:  # right click
                if self.drag_obj is not None:
                    self.drag_obj.rotate()
                else:
                    coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
                    if env.grid.coords_in_range(coords):
                        block = env.grid.get_grid_block(coords)
                        if isinstance(block, blocks.Item):
                            block.rotate()

        elif event.type == pygame.MOUSEMOTION:
            if self.drag_obj is not None:
                self.drag_pos = (event.pos[0] - BLOCK_SIZE // 2, event.pos[1] - BLOCK_SIZE // 2)

        elif event.type == pygame.MOUSEBUTTONUP:  # snap back to grid
            if self.drag_obj is not None:
                if event.button == 1:
                    end_coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
                    if env.grid.coords_in_workspace(end_coords):
                        end_block = env.grid.get_grid_block(end_coords)
                        if end_block is None:  # if empty, drop the block here
                            env.grid.set_grid_block(end_coords, self.drag_obj)
                            env.grid.set_grid_block(self.start_coords, None)

                    self.drag_obj = None

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                env.grid.step_forward()
