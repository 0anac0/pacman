from models.GridCell import GridCell
from settings import *


class Grid:
    def __init__(self, base_file):
        self.coins = []
        self.cells = []
        self.load_grid(base_file)

        self.cols = len(self.cells)
        self.rows = len(self.cells[0])
        self.load_cells_neighbors()

    def draw(self, screen):
        self.draw_coins(3, screen)

    def draw_coins(self, coin_radio, screen):
        for coin in self.coins:
            pygame.draw.circle(
                screen, WHITE,
                (coin.x * GRID_DIMENSION + MARGIN//2 + coin_radio / 2 + GRID_DIMENSION // 2,
                 coin.y * GRID_DIMENSION + MARGIN//2 + coin_radio / 2 + GRID_DIMENSION // 2),
                coin_radio
            )

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

    def reset_cell_heuristics(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.cells[i][j].reset_values()

    def a_estrela(self, start_pos, end_pos):
        openSet, closeSet, path = [], [], []
        finished = False
        self.reset_cell_heuristics()
        start = self.cells[int(start_pos.y)][int(start_pos.x)]
        end = self.cells[int(end_pos.y)][int(end_pos.x)]

        start.h = start.heuristics(end)
        start.f = start.h + start.g

        openSet.append(start)

        while not finished:
            if len(openSet) <= 0:
                print('não há caminho :(')
                finished = True
                break

            winner = 0
            # para todos os abertos na ultima rodada, escolher o de menor custo
            for i in range(len(openSet)):
                if openSet[i].f < openSet[winner].f:
                    winner = i
                elif openSet[i].f == openSet[winner].f:
                    if openSet[i].h < openSet[winner].h:
                        winner = i

            current = openSet[winner]
            # checagem se o nó é o destino
            if current == end:
                temp = current
                while temp.prev:
                    path.append(temp.prev)
                    temp = temp.prev
                    finished = True

            # testar outros caminhos
            if not finished:
                openSet.remove(current)
                closeSet.append(current)

                for neighbor in current.neighbors:
                    if neighbor in closeSet or neighbor.wall:
                        continue

                    newPath = False
                    if neighbor in openSet:
                        tempG = current.g + neighbor.heuristics(current)
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                            newPath = True
                    else:
                        neighbor.g = current.g + neighbor.heuristics(current)
                        newPath = True
                        openSet.append(neighbor)

                    if newPath:
                        neighbor.h = neighbor.heuristics(end)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.prev = current
        return path