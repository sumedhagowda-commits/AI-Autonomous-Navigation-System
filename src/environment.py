import numpy as np
import random

class GridEnvironment:
    def __init__(self, size=20):
        self.size = size
        self.grid = np.zeros((size, size))

    def add_obstacles(self, num=20):
        for _ in range(num):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.grid[x][y] = 1

    def is_obstacle(self, pos):
        return self.grid[pos[0]][pos[1]] == 1