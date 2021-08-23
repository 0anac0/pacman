from helper import *


class Character:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.direction = vec(0, 0)
        self.stored_direction = self.direction
        self.pixel_pos = self.get_pixel_pos()

    def get_pixel_pos(self):
        return vec(
            self.grid_pos.x*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2,
            self.grid_pos.y*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2
        )

    def update_direction(self):
        pass

    def update(self):
        self.update_direction()
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

    def time_to_move(self):
        x_alignment = (self.pixel_pos.x - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION
        y_alignment = (self.pixel_pos.y - MARGIN / 2 - GRID_DIMENSION/2) % GRID_DIMENSION

        # só atualizar a direção caso o pacman esteja no quadradinho correto
        return completed_current_square(x_alignment) and completed_current_square(y_alignment)

    def almost_time_to_move(self):
        x_alignment = (self.pixel_pos.x - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION
        y_alignment = (self.pixel_pos.y - MARGIN / 2 - GRID_DIMENSION/2) % GRID_DIMENSION

        # só atualizar a direção caso o pacman esteja no quadradinho correto
        return completed_current_square(x_alignment, 1) and completed_current_square(y_alignment, 1)
