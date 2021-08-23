from helper import *
from models.characters.Character import Character


class Player(Character):
    def __init__(self, app, pos):
        super().__init__(app=app, pos=pos)
        self.stored_direction = self.direction

    def move(self, direction):
        self.stored_direction = direction

    def update_direction(self):
        if self.stored_direction == self.direction or self.stored_direction is None:
            return

        # só atualizar a direção caso o pacman esteja no quadradinho correto
        if self.time_to_move():
            self.direction = self.stored_direction
        elif self.almost_time_to_move() and not self.allowed_movement():
            self.direction = self.stored_direction

    def draw(self):
        pygame.draw.circle(self.app.screen, YELLOW, self.pixel_pos,  GRID_DIMENSION//2)
        # self.draw_grid_pos()
        pygame.display.update()

    def draw_grid_pos(self):
        g_pos = (
            self.grid_pos.x * GRID_DIMENSION + MARGIN // 2,
            self.grid_pos.y * GRID_DIMENSION + MARGIN // 2,
            GRID_DIMENSION,
            GRID_DIMENSION
        )
        pygame.draw.rect(self.app.screen, RED, g_pos, 1)
