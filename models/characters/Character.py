from helper import *


class Character:
    def __init__(self, app, pos, speed=0.5, lifes=1):
        self.app = app
        self.grid_pos = pos
        self.initial_pos = self.grid_pos
        self.direction = vec(0, 0)
        self.stored_direction = self.direction
        self.pixel_pos = self.get_pixel_pos()
        self.speed = speed
        self.lifes = lifes

    def reset_initial_position(self):
        self.grid_pos = self.initial_pos
        self.pixel_pos = self.get_pixel_pos()

    def check_collision(self, other_character):
        return self.grid_pos == other_character.grid_pos

    def get_pixel_pos(self):
        return vec(
            self.grid_pos.x*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2,
            self.grid_pos.y*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2
        )

    def update_direction(self):
        pass

    def update(self):
        self.update_direction()
        aux_pixel_pos = self.pixel_pos + self.direction*self.speed
        aux_grid_pos = vec(
            (aux_pixel_pos.x - MARGIN//2)//GRID_DIMENSION,
            (aux_pixel_pos.y - MARGIN//2)//GRID_DIMENSION
        )
        if self.allowed_movement():
            self.pixel_pos = aux_pixel_pos
            self.grid_pos = aux_grid_pos

    def allowed_movement(self):
        aux_pixel_pos = self.pixel_pos + self.direction*self.speed
        aux_grid_pos = vec(
            (aux_pixel_pos.x - MARGIN//2 + (GRID_DIMENSION*self.direction.x)//2)/GRID_DIMENSION,
            (aux_pixel_pos.y - MARGIN//2 + (GRID_DIMENSION*self.direction.y)//2)/GRID_DIMENSION
        )

        x_alignment = (aux_pixel_pos.x - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION
        y_alignment = (aux_pixel_pos.y - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION
        will_be_time_to_move = x_alignment == 0 and y_alignment == 0
        next_pos_wall = GRID.cells[int(aux_grid_pos.y)][int(aux_grid_pos.x)].wall

        return will_be_time_to_move or not next_pos_wall

    def draw(self):
        pass

    def time_to_move(self):
        x_alignment = (self.pixel_pos.x - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION
        y_alignment = (self.pixel_pos.y - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION

        # só atualizar a direção caso o pacman esteja bem central no quadradinho
        return x_alignment == 0 and y_alignment == 0
