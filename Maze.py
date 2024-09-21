# Maze.py
import numpy as np
import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.grid = np.full((size, size), ' ')
        self.grid[0, 0] = 'A'  # Start position
        self.grid[size - 1, size - 1] = 'G'  # Goal position
        self.energy = size * size
        self.place_walls_obstacles()

    def place_walls_obstacles(self):
        for _ in range(int(self.size * self.size * 0.2)):  # 20% of cells are obstacles
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in [(0, 0), (self.size - 1, self.size - 1)]:
                self.grid[x, y] = random.choice(['-', 'O'])

    def display(self):
        for row in self.grid:
            print(' '.join(row))
