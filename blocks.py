
from constants import BLOCK_SIZE

import os.path
import pygame


class Block(pygame.sprite.Sprite):
    is_directional = False
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
    pass


class Item(Block):
    is_directional = True


class Box(Item):
    sprite_name = "box"
    is_directional = False


class Mover(Item):
    sprite_name = "mover"

