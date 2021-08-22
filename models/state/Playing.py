from models.state.State import State
from helper import *
from settings import *
import pygame


class Playing(State):
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

        return running, state

    def update(self):
        pass

    def draw(self):
        self.screen.fill(RED)

        pygame.display.update()
