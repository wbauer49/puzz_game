
from blocks import *


class Level:
    item_order = None

    def create_items(self):
        item_list = []
        item_counts = {}
        for item_type in self.item_order:
            if item_type not in item_counts:
                item_counts[item_type] = 0
            item_counts[item_type] += 1
            item_list.append(item_type(index=item_counts[item_type] - 1))

        return item_list


class Level1(Level):
    layout = [
        "00000000011111111111",
        "00000000000011111111",
        "00000000000000001111",
        "00000000000000000001",
        "00000000000000000001",
        "00000000000000000001",
    ]
    workspace_rect = (0, 0, 2, 6)
    end_coords = (17, 4)
    item_order = [Mover]


class Level2(Level):
    layout = [
        "0000000000111111",
        "0000000000111111",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
    ]
    workspace_rect = (1, 1, 3, 4)
    end_coords = (12, 5)
    item_order = [Piston, Mover]


class Level3(Level):
    layout = [
        "0000000111111111",
        "0000000111111111",
        "0000000111111111",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
    ]
    workspace_rect = (1, 1, 3, 4)
    end_coords = (12, 5)
    item_order = [Mover, Piston]


class Level4(Level):
    layout = [
        "111111000000",
        "111111000000",
        "111111000000",
        "111111000000",
        "000000000000",
        "000000000000",
        "000000000000",
        "000000000000",
        "000000000000",
        "000000000000",
    ]
    workspace_rect = (6, 0, 6, 4)
    end_coords = (5, 9)
    item_order = [Piston, Mover, Swapper]


class Level5(Level):
    layout = [
        "111111111111111111",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "111111111111111111",
    ]
    workspace_rect = (2, 2, 2, 2)
    end_coords = (11, 4)
    item_order = [Swapper, Turner]


class Level6(Level):
    layout = [
        "111111111111111111",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "100000000000000001",
        "111111111111111111",
    ]
    workspace_rect = (2, 2, 2, 2)
    end_coords = (5, 4)
    item_order = [Swapper, HardTurner]


class Level7(Level):
    layout = [
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000100000",
        "00000000000000100000",
        "00000000000000100000",
        "00000000000000100000",
        "00000000000000100000",
        "00000000000000100000",
    ]
    workspace_rect = (1, 1, 7, 3)
    end_coords = (17, 7)
    item_order = [Turner, HardTurner, Mover]


class Level8(Level):
    layout = [
        "11111111110000000000",
        "00000000000000000000",
        "00000000000000000000",
        "11111000000000000000",
        "10000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "11111111000000000000",
    ]
    workspace_rect = (10, 1, 5, 5)
    end_coords = (2, 8)
    item_order = [Mover, Piston, Turner]


class Level9(Level):
    layout = [
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
    ]
    workspace_rect = (1, 1, 5, 5)
    end_coords = (11, 8)
    item_order = [Mover, Piston, Turner, HardTurner, Swapper, Piston, Turner, HardTurner, Swapper, Mover, Mover]


level_list = [
    Level1,
    Level2,
    Level3,
    Level4,
    Level5,
    Level6,
    Level7,
    Level8,
    Level9,
]
