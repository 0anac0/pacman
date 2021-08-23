from models.characters.Character import Character
from settings import *


class Enemy(Character):
    def __init__(self, app, pos):
        super().__init__(app=app, pos=pos)

    def draw(self):
        pygame.draw.circle(self.app.screen, RED, self.pixel_pos,  GRID_DIMENSION//3)
        pygame.draw.rect(
            self.app.screen, RED,
            (self.pixel_pos.x - (GRID_DIMENSION/3), self.pixel_pos.y, GRID_DIMENSION/1.5,  GRID_DIMENSION//2)
        )
        pygame.display.update()