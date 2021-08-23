from helper import *


class Character:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.direction = vec(1, 0)
        self.stored_direction = self.direction
        self.pixel_pos = self.get_pixel_pos()

    def get_pixel_pos(self):
        return vec(
            self.grid_pos.x*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2,
            self.grid_pos.y*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2
        )

    def update(self):
        aux_pixel_pos = self.pixel_pos + self.direction
        aux_grid_pos = vec(
            (aux_pixel_pos.x - MARGIN//2)//GRID_DIMENSION,
            (aux_pixel_pos.y - MARGIN//2)//GRID_DIMENSION
        )
        if self.allowed_movement():
            self.pixel_pos = aux_pixel_pos
            self.grid_pos = aux_grid_pos

    def allowed_movement(self):
        aux_pixel_pos = self.pixel_pos + self.direction
        aux_grid_pos = vec(
            (aux_pixel_pos.x - MARGIN//2 + (GRID_DIMENSION*self.direction.x)//2)//GRID_DIMENSION,
            (aux_pixel_pos.y - MARGIN//2 + (GRID_DIMENSION*self.direction.y)//2)//GRID_DIMENSION
        )
        return not GRID.cells[int(aux_grid_pos.y)][int(aux_grid_pos.x)].wall

    def draw(self):
        pass