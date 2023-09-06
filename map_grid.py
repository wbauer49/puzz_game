
import blocks


GRID = [[]]
ITEM_ORDER = []
CURRENT_STEP = 0


def init_grid(level):
    global GRID
    global ITEM_ORDER

    ITEM_ORDER = level.item_order

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


def coords_in_range(coords):
    return 0 <= coords[0] < len(GRID[0]) and 0 <= coords[1] < len(GRID)


def get_grid_block(coords):
    return GRID[coords[1]][coords[0]]


def set_grid_block(coords, block):
    GRID[coords[1]][coords[0]] = block


def get_width():
    return len(GRID[0])


def get_height():
    return len(GRID)


def step_forward():
    global CURRENT_STEP
    global ITEM_ORDER

    item_type = ITEM_ORDER[CURRENT_STEP % len(ITEM_ORDER)]

    actioned_items = []
    for row, row_list in enumerate(GRID):
        for col, block in enumerate(row_list):
            if type(block) is item_type and block not in actioned_items:
                block.perform_action((col, row))
                actioned_items.append(block)

    CURRENT_STEP += 1
    print(f"step: {CURRENT_STEP}")

