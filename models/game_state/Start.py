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

        draw_text(
            'INTELIGENCIA ARTIFICIAL PARA JOGOS',
            self.screen,
            START_TEXT_SIZE,
            (30, 100, 130),
            START_FONT,
            (WIDTH / 2, HEIGHT / 2 - 200)
        )

        draw_text(
            'ANA CLAUDIA',
            self.screen,
            START_TEXT_SIZE,
            (30, 100, 130),
            START_FONT,
            (WIDTH / 2, HEIGHT / 2 - 170)
        )

        draw_text(
            '2021.1',
            self.screen,
            START_TEXT_SIZE,
            (30, 100, 130),
            START_FONT,
            (WIDTH / 2, HEIGHT / 2 - 150)
        )
        draw_text(
            'APERTE ESPAÇO PARA INICIAR',
            self.screen,
            START_TEXT_SIZE,
            (170, 130, 80),
            START_FONT,
            (WIDTH / 2, HEIGHT / 2)
        )

        draw_text(
            'SOMENTE 1 JOGADOR',
            self.screen,
            START_TEXT_SIZE,
            (30, 70, 130),
            START_FONT,
            (WIDTH / 2, HEIGHT / 2 + 50)
        )
        pygame.display.update()