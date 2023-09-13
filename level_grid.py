
import blocks


class LevelGrid:

    curr_level = None
    curr_step = 0
    grid = []

    def __init__(self, level):
        self.curr_level = level
        self.reset_level()

    def reset_level(self):
        self.grid = []
        items = list(self.curr_level.items)

        for row, row_list in enumerate(self.curr_level.layout):
            self.grid.append([])
            for col, block_type in enumerate(row_list):
                self.grid[row].append(None)
                if block_type == "1":
                    self.grid[row][col] = blocks.Wall()
                elif self.coords_in_workspace((col, row)) and items:
                    self.grid[row][col] = (items.pop())()  # level.items is a list of types

        self.curr_step = 0

    def coords_in_range(self, coords):
        return 0 <= coords[0] < len(self.grid[0]) and 0 <= coords[1] < len(self.grid)

    def coords_in_workspace(self, coords):
        rect = self.curr_level.workspace_rect
        return rect[0] <= coords[0] < rect[0] + rect[2] and rect[1] <= coords[1] < rect[1] + rect[3]

    def step_forward(self):
        item_type = self.curr_level.item_order[self.curr_step % len(self.curr_level.item_order)]

        actioned_items = []
        for row, row_list in enumerate(self.grid):
            for col, block in enumerate(row_list):
                if type(block) is item_type and block not in actioned_items:
                    block.perform_action((col, row))
                    actioned_items.append(block)

        self.curr_step += 1
        print(f"step: {self.curr_step}")

        if self.get_grid_block(self.curr_level.end_coords) is not None:
            print(f"WIN!")

    def get_grid_block(self, coords):
        return self.grid[coords[1]][coords[0]]

    def set_grid_block(self, coords, block):
        self.grid[coords[1]][coords[0]] = block

    def get_width(self):
        return len(self.grid[0])

    def get_height(self):
        return len(self.grid)
