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
        self.player.update()
        for enemy in self.app.enemies:
            enemy.update()
        coin_gained = GRID.check_coins(self.player.grid_pos)
        if coin_gained:
            self.app.increase_score(10)

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(BACKGROUND, (MARGIN//2, MARGIN//2))
        GRID.draw(self.screen)
        draw_text('CURRENT SCORE: '+str(self.app.current_score), self.screen, GUI_TEXT_SIZE, WHITE, START_FONT, (WIDTH//3, 14), True)
        draw_text('HIGH SCORE: 0', self.screen, GUI_TEXT_SIZE, WHITE, START_FONT, (2*WIDTH//3 - 24, 6), False)
        self.player.draw()
        # draw_grid_cells()
        for enemy in self.app.enemies:
            enemy.draw()
        pygame.display.update()
