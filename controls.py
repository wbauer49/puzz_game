
import pygame

from constants import *


drag_obj = None

def check_event(event, objects):

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            start_coords = (event.pos[0] // BLOCK_SIZE, event.pos[1] // BLOCK_SIZE)
            drag_obj = objects.get(start_coords, None)
            if drag_obj is not None:
                pass

    elif event.type == pygame.MOUSEMOTION:
        if drag_obj is not None:
            mouse_x, mouse_y = event.pos

            rectangle.x = mouse_x + offset_x
            rectangle.y = mouse_y + offset_y

    elif event.type == pygame.MOUSEBUTTONUP:  # snap back to grid
        if event.button == 1: