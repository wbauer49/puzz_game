
import blocks
import env
import level_grid


class Level1:
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
    end_coords = (17, 8)
    items = [
        blocks.Mover,
        blocks.Turner,
        blocks.HardTurner,
    ]
    item_order = [
        blocks.Turner,
        blocks.HardTurner,
        blocks.Mover,
    ]


class Level2:
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
    items = [
        blocks.Mover,
        blocks.Piston,
        blocks.Turner,
    ]
    item_order = [
        blocks.Mover,
        blocks.Piston,
        blocks.Turner,
    ]


all_levels = [

    Level1(),
    Level2(),
]


def get_level(level_num):
    return all_levels[level_num - 1]


def go_to_level(level_num):
    level = get_level(level_num)
    env.renderer.render_layout(level)
    env.grid = level_grid.LevelGrid(level)
