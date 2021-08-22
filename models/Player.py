from settings import *


class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos

    def pixel_pos(self):
        return vec(
            self.grid_pos.x*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2,
            self.grid_pos.y*GRID_DIMENSION + MARGIN//2 + GRID_DIMENSION//2
        )

    def move(self, movement):
        self.grid_pos.x += movement.x
        self.grid_pos.y += movement.y

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, YELLOW, self.pixel_pos(),  GRID_DIMENSION//2)
        pygame.display.update()
