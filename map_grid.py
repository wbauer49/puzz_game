
import blocks


GRID = [[]]


def init_grid(level):
    global GRID
    GRID = []

    for row, row_list in enumerate(level.layout):
        GRID.append([])
        for col, block_type in enumerate(row_list):
            GRID[row].append(None)
            if block_type == 1:
                GRID[row][col] = blocks.Wall()
            else:
                if level.items:
                    GRID[row][col] = (level.items.pop())()  # level.items is a list of types


def get_grid_block(coords):
    return GRID[coords[1]][coords[0]]


def set_grid_block(coords, block):
    GRID[coords[1]][coords[0]] = block
