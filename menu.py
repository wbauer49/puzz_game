
import env
import level_grid
from levels import world1


ALL_LEVELS = [
    world1.level_list
]


class Menu:

    world_num = 1
    level_num = 1

    def go_to_next_level(self):
        self.level_num += 1

        if self.level_num >= len(ALL_LEVELS[self.world_num - 1]):
            self.go_to_world(self.world_num + 1)
        else:
            self.go_to_level(self.level_num)

    def go_to_world(self, world_num):
        self.world_num = world_num
        self.go_to_level(1)

    def go_to_level(self, level_num):
        self.level_num = level_num
        level = ALL_LEVELS[self.world_num - 1][level_num - 1]
        env.renderer.set_text(None)
        env.renderer.render_layout(level)
        env.grid = level_grid.LevelGrid(level)
