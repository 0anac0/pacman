from pygame.math import Vector2 as vec


class Grid:
    def __init__(self, base_file):
        self.walls = []
        self.coins = []
        self.load_grid(base_file)

    def load_grid(self, base_file):
        with open(file=base_file, mode='r') as file:
            for y_ind, line in enumerate(file):
                for x_ind, char in enumerate(line):
                    if char == '1':
                        self.walls.append(vec(x_ind, y_ind))
                    elif char == 'C':
                        self.coins.append(vec(x_ind, y_ind))

    def check_coins(self, pos):
        coin_consumed = False
        if pos in self.coins:
            self.coins.remove(pos)
            coin_consumed = True
        return coin_consumed
