
import blocks
import copy
import env


class LevelGrid:

    curr_level = None
    curr_step = 0
    grid = []
    saved_position = None

    def __init__(self, level):
        self.curr_level = level
        self.reset_level()

    def reset_level(self):
        item_list = self.curr_level.create_items()

        self.grid = []
        for row, row_list in enumerate(self.curr_level.layout):
            self.grid.append([])
            for col, block_type in enumerate(row_list):
                self.grid[row].append(None)
                if block_type == "1":
                    self.grid[row][col] = blocks.Wall()
                elif self.coords_in_workspace((col, row)) and item_list:
                    if self.saved_position is not None:
                        saved_block = self.saved_position.get((col, row), None)
                        if saved_block:
                            self.grid[row][col] = saved_block
                    else:
                        self.grid[row][col] = item_list.pop()

        self.curr_step = 0

    def coords_in_range(self, coords):
        return 0 <= coords[0] < len(self.grid[0]) and 0 <= coords[1] < len(self.grid)

    def coords_in_workspace(self, coords):
        rect = self.curr_level.workspace_rect
        return rect[0] <= coords[0] < rect[0] + rect[2] and rect[1] <= coords[1] < rect[1] + rect[3]

    def step_forward(self):
        if self.curr_step == 0:
            self.saved_position = {}

        modded_step = self.curr_step % len(self.curr_level.item_order)
        item_type = self.curr_level.item_order[modded_step]

        actioned_items = []
        for row, row_list in enumerate(self.grid):
            for col, block in enumerate(row_list):
                if type(block) is item_type and block not in actioned_items:
                    if block.index == self.curr_level.item_order[:modded_step].count(type(block)):
                        block.perform_action((col, row))
                        actioned_items.append(block)
                if self.curr_step == 0 and block and block.is_item:
                    self.saved_position[(col, row)] = copy.copy(block)

        self.curr_step += 1
        print(f"step: {self.curr_step}")

        if self.get_grid_block(self.curr_level.end_coords) is not None:
            env.renderer.set_text("Success! Press C to continue.")
            env.controller.in_win_screen = True

    def get_grid_block(self, coords):
        return self.grid[coords[1]][coords[0]]

    def set_grid_block(self, coords, block):
        self.grid[coords[1]][coords[0]] = block

    def get_width(self):
        return len(self.grid[0])

    def get_height(self):
        return len(self.grid)
