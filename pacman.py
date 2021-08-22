import pygame
import sys
from settings import *
from helper import *
from models.game_state.Start import Start
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = Start(self.screen)

    def update_state(self, new_state):
        self.state = new_state

    def update_running(self, new_running=False):
        self.running = new_running

    def run(self):
        while self.running:
            if self.state:
                self.running, self.state = self.state.events()
                self.state.draw()
                self.state.update()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
