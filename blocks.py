import map_grid
from constants import BLOCK_SIZE

import os.path
import pygame


class Block(pygame.sprite.Sprite):
    is_directional = False
    is_wall = False

    direction = 0
    sprite_name = "unassigned"

    def __init__(self):
        super().__init__()

        sprite_path = os.path.join(os.path.dirname(__file__), "sprites", f"{self.sprite_name}.png")
        unscaled_sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(unscaled_sprite, (BLOCK_SIZE, BLOCK_SIZE))

    def rotate(self):
        if self.is_directional:
            self.direction = (self.direction + 1) % 4
            self.sprite = pygame.transform.rotate(self.sprite, -90)


class Wall(Block):
    is_wall = True


class Item(Block):
    is_directional = True

    def perform_action(self, self_coords):
        pass


class Box(Item):
    sprite_name = "box"
    is_directional = False


def get_all_coords_in_direction(start_coords, direction):
    x, y = start_coords

    if direction == 0:
        ret_coords = [(x, i) for i in range(y - 1, -1, -1)]
    elif direction == 1:
        ret_coords = [(i, y) for i in range(x + 1, map_grid.get_width())]
    elif direction == 2:
        ret_coords = [(x, i) for i in range(y + 1, map_grid.get_height())]
    elif direction == 3:
        ret_coords = [(i, y) for i in range(x - 1, -1, -1)]
    else:
        raise ValueError

    return ret_coords


class Piston(Item):
    sprite_name = "piston"
    move_self = False

    def perform_action(self, self_coords):
        coords_list = get_all_coords_in_direction(self_coords, self.direction)
        for i, coords in enumerate(coords_list):
            block = map_grid.get_grid_block(coords)
            if block is None:
                for j in range(i - 1, -1, -1):
                    move_block = map_grid.get_grid_block(coords_list[j])
                    map_grid.set_grid_block(coords_list[j + 1], move_block)

                if self.move_self:
                    map_grid.set_grid_block(coords_list[0], self)
                    map_grid.set_grid_block(self_coords, None)
                else:
                    map_grid.set_grid_block(coords_list[0], None)

                return

            elif block.is_wall:
                return


class Mover(Piston):
    sprite_name = "mover"
    move_self = True


class Turner(Item):
    sprite_name = "turner"
    clockwise = True
    rotate_others = False

    def perform_action(self, self_coords):
        x, y = self_coords

        if self.clockwise:
            coords_list = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        else:
            coords_list = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]

        for coords in coords_list:
            if map_grid.get_grid_block(coords).is_wall:
                return

        temp_block = map_grid.get_grid_block(coords_list[3])
        for i in range(2, -1, -1):
            move_block = map_grid.get_grid_block(coords_list[i])
            map_grid.set_grid_block(coords_list[i + 1], move_block)
            if self.rotate_others:
                move_block.rotate()
        map_grid.set_grid_block(coords_list[0], temp_block)
        if self.rotate_others:
            temp_block.rotate()

        self.rotate()


class HardTurner(Turner):
    sprite_name = "hard_turner"
    rotate_others = True
