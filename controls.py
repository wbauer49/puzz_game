
import pygame

import blocks
import map_grid
from constants import *

drag_obj = None
drag_pos = None

start_coords = None


def check_event(event):

    global drag_obj
    global drag_pos
    global start_coords

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # left click
            start_coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
            drag_obj = map_grid.get_grid_block(start_coords)
            drag_pos = (event.pos[0] - BLOCK_SIZE // 2, event.pos[1] - BLOCK_SIZE // 2)

        else:  # right click
            print("loool")
            if drag_obj is not None:
                drag_obj.rotate()

            else:
                coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
                block = map_grid.get_grid_block(coords)
                if isinstance(block, blocks.Item):
                    block.rotate()

    elif event.type == pygame.MOUSEMOTION:
        if drag_obj is not None:
            drag_pos = (event.pos[0] - BLOCK_SIZE // 2, event.pos[1] - BLOCK_SIZE // 2)

    elif event.type == pygame.MOUSEBUTTONUP:  # snap back to grid
        if drag_obj is not None:
            if event.button == 1:
                end_coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
                end_block = map_grid.get_grid_block(end_coords)
                if end_block is None:  # if empty, drop the block here
                    map_grid.set_grid_block(end_coords, drag_obj)
                    map_grid.set_grid_block(start_coords, None)

                drag_obj = None
