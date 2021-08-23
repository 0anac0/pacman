import math
from settings import *


class GridCell:
    def __init__(self, x, y, wall=False):
        self.x, self.y = x, y
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = wall

    def reset_values(self):
        self.f, self.g, self.h = 0, 0, 0

    def heuristics(self, b):
        return math.sqrt((self.x - b.x) ** 2 + abs(self.y - b.y) ** 2)

    def draw(self):
        color = RED if self.wall else WHITE
        g_pos = (
            self.x * GRID_DIMENSION,
            self.y * GRID_DIMENSION,
            GRID_DIMENSION,
            GRID_DIMENSION
        )
        pygame.draw.rect(BACKGROUND, color, g_pos, 1)

    def add_neighbors(self, grid):
        cols = len(grid)
        rows = len(grid[0])
        if self.x < rows - 1:
            self.neighbors.append(grid[self.y][self.x + 1])
        if self.x > 0:
            self.neighbors.append(grid[self.y][self.x - 1])
        if self.y < cols - 1:
            self.neighbors.append(grid[self.y + 1][self.x])
        if self.y > 0:
            self.neighbors.append(grid[self.y - 1][self.x])

        # Add Diagonals
        # if self.x < cols - 1 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x + 1][self.y + 1])
        # if self.x < cols - 1 and self.y > 0:
        #     self.neighbors.append(grid[self.x + 1][self.y - 1])
        # if self.x > 0 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x - 1][self.y + 1])
        # if self.x > 0 and self.y > 0:
        #     self.neighbors.append(grid[self.x - 1][self.y - 1])

