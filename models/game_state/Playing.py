from models.game_state.State import State
from helper import *
import pygame


class Playing(State):
    def __init__(self, app):
        super().__init__(app=app)
        self.player = self.app.player

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.update_running(False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                elif event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                elif event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(BACKGROUND, (MARGIN//2, MARGIN//2))
        draw_grid(self.screen, (GRID_DIMENSION, GRID_DIMENSION))
        draw_text('CURRENT SCORE: 0', self.screen, GUI_TEXT_SIZE, WHITE, START_FONT, (WIDTH//3, 14), True)
        draw_text('HIGH SCORE: 0', self.screen, GUI_TEXT_SIZE, WHITE, START_FONT, (2*WIDTH//3 - 24, 6), False)
        self.player.draw()
        pygame.display.update()

