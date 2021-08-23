import pdb

from pygame.math import Vector2 as vec
from models.GridCell import GridCell


class Grid:
    def __init__(self, base_file):
        self.coins = []
        self.cells = []
        self.load_grid(base_file)

        self.cols = len(self.cells)
        self.rows = len(self.cells[0])
        self.load_cells_neighbors()

    def load_grid(self, base_file):
        with open(file=base_file, mode='r') as file:
            for y_ind, line in enumerate(file):
                arr = []
                for x_ind, char in enumerate(line):
                    wall = False
                    if char == '1':
                        wall = True
                    elif char == 'C':
                        self.coins.append(vec(x_ind, y_ind))
                    if char != '\n':
                        arr.append(GridCell(x_ind, y_ind, wall))
                self.cells.append(arr)

    def load_cells_neighbors(self):
       for i in range(self.cols):
            for j in range(self.rows):
                self.cells[i][j].add_neighbors(self.cells)

    def check_coins(self, pos):
        coin_consumed = False
        if pos in self.coins:
            self.coins.remove(pos)
            coin_consumed = True
        return coin_consumed
