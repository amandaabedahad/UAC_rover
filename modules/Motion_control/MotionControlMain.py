import random
import numpy as np
from Grid import Grid
from helpers.BaseClass import BaseClass


class MotionControlMain(BaseClass):
    """Module used to control movements of robot. Robot living in grid."""

    SERIALIZABLE_FIELDS = [
        "position"
    ]

    def __init__(self):
        super().__init__("motion_control_main")
        self.actions = {0: "right", 1: "left", 2: "up", 3: "down"}
        self.position = (0, 0)
        self.grid = Grid()

    def init_pos_random(self):
        new_position = tuple(np.random.randint(low=0, high=self.grid.grid_size-1, size=2))
        self.grid.change_position(old_position=self.position, new_position=new_position)
        self.position = new_position

    def choose_new_action(self):
        random_action = random.randint(0, len(self.actions) - 1)
        selected_action = self.actions[random_action]
