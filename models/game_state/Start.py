from models.game_state.State import State
from models.game_state.Playing import Playing
from helper import *
from settings import *
import pygame


class Start(State):
    def __init__(self, screen):
        super().__init__(screen=screen)

    def events(self):
        state = self
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = Playing(self.screen)

        return (running, state)

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        texts = [
            ['INTELIGENCIA ARTIFICIAL PARA JOGOS', (30, 100, 130), (WIDTH / 2, HEIGHT / 2 - 200)],
            ['ANA CLAUDIA', (30, 100, 130), (WIDTH / 2, HEIGHT / 2 - 170)],
            ['2021.1', (30, 100, 130), (WIDTH / 2, HEIGHT / 2 - 150)],
            ['APERTE ESPAÇO PARA INICIAR', (170, 130, 80), (WIDTH / 2, HEIGHT / 2)],
            ['SOMENTE 1 JOGADOR', (30, 70, 130), (WIDTH / 2, HEIGHT / 2 + 50)],
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
