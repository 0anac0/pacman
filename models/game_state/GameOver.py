from models.game_state.State import State
from models.game_state.Playing import Playing
from helper import *
from settings import *
import pygame


class GameOver(State):
    def __init__(self, app):
        super().__init__(app=app)
        self.app.reset_high_score()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.update_running(False)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.app.reset_game()
                GRID.load_grid_from_file()
                self.app.update_state(Playing(self.app))

    def update(self):
        pass

    def draw(self):
        self.app.screen.fill(BLACK)

        texts = [
            ['GAME OVER', (200, 100, 130), (WIDTH / 2 + MARGIN//2, HEIGHT / 2 - 200)],
            ['YOUR SCORE: ' + str(self.app.current_score), (30, 70, 130), (WIDTH / 2 + MARGIN//2, HEIGHT / 2 - 170)],
            ['HIGH SCORE: ' + str(self.app.high_score), (30, 70, 130), (WIDTH / 2 + MARGIN//2, HEIGHT / 2 - 150)],
            ['APERTE ESPAÇO PARA INICIAR NOVAMENTE', (170, 130, 80), (WIDTH / 2 + MARGIN//2, HEIGHT / 2)],
            ['SOMENTE 1 JOGADOR', (30, 70, 130), (WIDTH / 2 + MARGIN//2, HEIGHT / 2 + 50)],
        ]

        for text in texts:
            draw_text(
                text[0],
                self.screen,
                START_TEXT_SIZE,
                text[1],
                START_FONT,
                text[2]
            )

        pygame.display.update()
