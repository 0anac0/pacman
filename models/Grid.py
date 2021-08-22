from pygame.math import Vector2 as vec


class Grid:
    def __init__(self, base_file):
        self.walls = []
        self.load_walls(base_file)

    def load_walls(self, base_file):
        with open(file=base_file, mode='r') as file:
            for y_ind, line in enumerate(file):
                for x_ind, char in enumerate(line):
                    if char == '1':
                        self.walls.append(vec(x_ind, y_ind))
