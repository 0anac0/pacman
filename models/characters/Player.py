from helper import *
from models.characters.Character import Character
from models.game_state.GameOver import GameOver


class Player(Character):
    def __init__(self, app, pos):
        super().__init__(app=app, pos=pos, speed=2, lifes=3)
        self.stored_direction = self.direction

    def move(self, direction):
        self.stored_direction = direction

    def loose_life(self):
        self.lifes -= 1
        if self.lifes <= 0:
            self.lifes = 0
            self.app.update_state(GameOver(self.app, lost=True))

    def update_direction(self):
        if self.stored_direction == self.direction or self.stored_direction is None:
            return

        # só atualizar a direção caso o pacman esteja no quadradinho correto
        if self.time_to_move():
            self.direction = self.stored_direction

    def draw(self):
        draw_pacman(self.app.screen, self.pixel_pos, self.mouth_coords())
        #self.draw_grid_pos()
        pygame.display.update()

    def mouth_coords(self):
        if self.direction == vec(1, 0):
            return [
                self.pixel_pos,
                (self.pixel_pos.x + GRID_DIMENSION//2, self.pixel_pos.y - 10),
                (self.pixel_pos.x + GRID_DIMENSION//2, self.pixel_pos.y + 10)]
        elif self.direction == vec(-1, 0):
            return [
                self.pixel_pos,
                (self.pixel_pos.x - GRID_DIMENSION // 2, self.pixel_pos.y - 10),
                (self.pixel_pos.x - GRID_DIMENSION // 2, self.pixel_pos.y + 10)]
        elif self.direction == vec(0, 1):
            return [
                self.pixel_pos,
                (self.pixel_pos.x - GRID_DIMENSION // 2, self.pixel_pos.y + 10),
                (self.pixel_pos.x + GRID_DIMENSION // 2, self.pixel_pos.y + 10)]
        else:
            return [
                self.pixel_pos,
                (self.pixel_pos.x - GRID_DIMENSION // 2, self.pixel_pos.y - 10),
                (self.pixel_pos.x + GRID_DIMENSION // 2, self.pixel_pos.y - 10)]

    def draw_grid_pos(self):
        g_pos = (
            self.grid_pos.x * GRID_DIMENSION + MARGIN // 2,
            self.grid_pos.y * GRID_DIMENSION + MARGIN // 2,
            GRID_DIMENSION,
            GRID_DIMENSION
        )
        pygame.draw.rect(self.app.screen, RED, g_pos, 1)
