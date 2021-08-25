from models.characters.Enemy import Enemy
from helper import *
import random


class EnemyRegular(Enemy):
    def __init__(self, app, pos, color=CYAN, speed=1):
        super().__init__(app=app, pos=pos, speed=speed, color=color, eye_color=BLACK)
        self._scatter_target = vec(1, 1)
        self.calculate_scatter_target()

    def calculate_scatter_target(self):
        quadrant = random.randint(0, 3)
        if quadrant == 0:
            target = vec(1, 1)
        elif quadrant == 1:
            target = vec(1, GRID.cols - 2)
        elif quadrant == 2:
            target = vec(GRID.rows - 2, GRID.cols - 2)
        else:
            target = vec(GRID.rows - 2, 1)
        self._scatter_target = target

    # alvo em modo scatter é o quadrante gerado aleatoriamente
    def scatter_target(self):
        return self._scatter_target

    def chase_target(self):
        return self.flee_target()

    def check_if_target_out_of_path(self, target):
        target_cell = GRID.cells[int(target.y)][int(target.x)]
        if self.app.mode == 'scatter':
            self_cell = GRID.cells[int(self.grid_pos.y)][int(self.grid_pos.x)]
            if self_cell == target_cell:
                self.calculate_scatter_target()
                target_cell = GRID.cells[int(target.y)][int(target.x)]

        if target_cell not in self.path:
            self.calculate_path(target)
