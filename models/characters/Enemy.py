from models.characters.Character import Character
from helper import *


class Enemy(Character):
    def __init__(self, app, pos, color=RED, speed=1, eye_color=WHITE):
        super().__init__(app=app, pos=pos, speed=speed)
        self.color = color
        self.path = []
        self.eye_color = eye_color

    def target(self):
        if self.app.mode == 'scatter':
            return self.scatter_target()
        elif self.app.mode == 'chase':
            return self.chase_target()
        else:
            return self.flee_target()

    def chase_target(self):
        return self.app.player.grid_pos

    # inimigo é um perseguidor por default
    def scatter_target(self):
        return self.chase_target()

    def flee_target(self):
        x = self.app.player.grid_pos.x
        y = self.app.player.grid_pos.y

        if y < GRID.cols/2:
            quadrant_y = GRID.cols - 2
        else:
            quadrant_y = 1
        if x < GRID.rows/2:
            quadrant_x = GRID.rows - 2
        else:
            quadrant_x = 1
        return vec(
            quadrant_x,
            quadrant_y,
        )

    def calculate_path(self, target):
        self.path = GRID.a_estrela(target, self.grid_pos)

    def draw_eyes(self, color):
        pygame.draw.circle(self.app.screen, color, (self.pixel_pos.x - 3, self.pixel_pos.y),  3)
        pygame.draw.circle(self.app.screen, color, (self.pixel_pos.x + 3, self.pixel_pos.y),  3)

    def draw(self):
        if self.app.mode == 'flee':
            self.draw_eyes(WHITE)
        else:
            pygame.draw.circle(self.app.screen, self.color, self.pixel_pos,  GRID_DIMENSION*1.4//3)
            self.draw_eyes(self.eye_color)
            pygame.draw.rect(
                self.app.screen, self.color,
                (self.pixel_pos.x - (GRID_DIMENSION*1.4//3), self.pixel_pos.y, GRID_DIMENSION/1.1,  GRID_DIMENSION//2)
            )
        pygame.display.update()

    def update_direction(self):
        if self.time_to_move():
            self.check_if_target_out_of_path(self.target())
            self.calculate_direction()

    def check_if_target_out_of_path(self, target):
        target_cell = GRID.cells[int(target.y)][int(target.x)]
        if target_cell not in self.path:
            self.calculate_path(target)

    def calculate_direction(self):
        if len(self.path) <= 0:
            return
        next_pos = self.path[0]
        self.path.pop(0)
        dir_x = next_pos.x - self.grid_pos.x
        dir_y = next_pos.y - self.grid_pos.y
        if dir_x != 0:
            dir_x = dir_x/abs(dir_x)
        if dir_y != 0:
            dir_y = dir_y/abs(dir_y)

        self.direction = vec(dir_x, dir_y)
