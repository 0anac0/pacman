import pdb

from models.characters.Character import Character
from helper import *


class Enemy(Character):
    def __init__(self, app, pos):
        super().__init__(app=app, pos=pos)
        self.calculate_path()

    def calculate_path(self):
        self.path = GRID.a_estrela(self.app.player.grid_pos, self.grid_pos)

    def draw(self):
        pygame.draw.circle(self.app.screen, RED, self.pixel_pos,  GRID_DIMENSION//3)
        pygame.draw.rect(
            self.app.screen, RED,
            (self.pixel_pos.x - (GRID_DIMENSION/3), self.pixel_pos.y, GRID_DIMENSION/1.5,  GRID_DIMENSION//2)
        )
        pygame.display.update()

    def update_direction(self):
        if self.time_to_move():
            self.calculate_direction()
        elif self.almost_time_to_move() and not self.allowed_movement():
            self.calculate_direction()

    def calculate_direction(self):
        #pdb.set_trace()
        #print(len(self.path))
        if len(self.path) <= 0:
            return
        next_pos = self.path[0]
        self.path.pop(0)
        dir_x = next_pos.x - self.grid_pos.x
        dir_y = next_pos.y - self.grid_pos.y
        self.direction = vec(dir_x, dir_y)
