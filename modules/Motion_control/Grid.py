import numpy as np
from helpers.BaseClass import BaseClass


class Grid(BaseClass):
    """Grid where robot operates."""

    def __init__(self):
        self.grid_size = 50
        self.grid = np.zeros((self.grid_size, self.grid_size))

    def change_position(self, old_position, new_position):
        self.grid[position] = 1
