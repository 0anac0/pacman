from helper import *


class Player:
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

    def move(self, direction):
        self.stored_direction = direction

    def update_direction(self):
        if self.stored_direction == self.direction or self.stored_direction is None:
            return

        x_alignment = (self.pixel_pos.x - MARGIN // 2 - GRID_DIMENSION//2 ) % GRID_DIMENSION
        y_alignment = (self.pixel_pos.y - MARGIN // 2 - GRID_DIMENSION//2) % GRID_DIMENSION

        # só atualizar a direção caso o pacman esteja no quadradinho correto
        if completed_current_square(x_alignment) and completed_current_square(y_alignment):
            self.direction = self.stored_direction

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
        return aux_grid_pos not in GRID.walls

    def draw(self):
        pygame.draw.circle(self.app.screen, YELLOW, self.pixel_pos,  GRID_DIMENSION//2)
        #self.draw_grid_pos()
        pygame.display.update()

    def draw_grid_pos(self):
        g_pos = (
            self.grid_pos.x * GRID_DIMENSION + MARGIN // 2,
            self.grid_pos.y * GRID_DIMENSION + MARGIN // 2,
            GRID_DIMENSION,
            GRID_DIMENSION
        )
        pygame.draw.rect(self.app.screen, RED, g_pos, 1)
