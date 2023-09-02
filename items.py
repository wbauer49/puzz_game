
import os.path
import pygame


class Item(pygame.sprite.Sprite):

    sprite_name = "unassigned"

    dir = 0

    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(__file__), "sprites", f"{self.sprite_name}.png")
        pygame.image.load(image_path)


class Box(Item):
    sprite_name = "box"


class Mover(Item):
    sprite_name = "mover"

