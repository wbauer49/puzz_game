
import blocks
import env


class LevelGrid:

    current_step = 0

    def __init__(self, level):
        self.item_order = level.item_order
        self.workspace_rect = level.workspace_rect
        self.end_coords = level.end_coords

        self.grid = []
        for row, row_list in enumerate(level.layout):
            self.grid.append([])
            for col, block_type in enumerate(row_list):
                self.grid[row].append(None)
                if block_type == 1:
                    self.grid[row][col] = blocks.Wall()
                elif self.coords_in_workspace((col, row)) and level.items:
                    self.grid[row][col] = (level.items.pop())()  # level.items is a list of types

    def coords_in_range(self, coords):
        return 0 <= coords[0] < len(self.grid[0]) and 0 <= coords[1] < len(self.grid)

    def coords_in_workspace(self, coords):
        return self.workspace_rect[0] <= coords[0] < self.workspace_rect[0] + self.workspace_rect[2] and \
            self.workspace_rect[1] <= coords[1] < self.workspace_rect[1] + self.workspace_rect[3]

    def step_forward(self):
        item_type = self.item_order[self.current_step % len(self.item_order)]

        actioned_items = []
        for row, row_list in enumerate(self.grid):
            for col, block in enumerate(row_list):
                if type(block) is item_type and block not in actioned_items:
                    block.perform_action((col, row))
                    actioned_items.append(block)

        self.current_step += 1
        print(f"step: {self.current_step}")

        if self.get_grid_block(self.end_coords) is not None:
            print(f"WIN!")

    def get_grid_block(self, coords):
        return self.grid[coords[1]][coords[0]]

    def set_grid_block(self, coords, block):
        self.grid[coords[1]][coords[0]] = block

    def get_width(self):
        return len(self.grid[0])

    def get_height(self):
        return len(self.grid)
