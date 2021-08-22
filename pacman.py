import pygame
import sys
from helper import *
from models.game_state.Start import Start
from models.Player import Player
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH + MARGIN, HEIGHT + MARGIN))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = Start(self)
        self.player = Player(self, PLAYER_START_POS)
        print(GRID.walls)

    def update_state(self, new_state):
        self.state = new_state

    def update_running(self, new_running=False):
        self.running = new_running

    def run(self):
        while self.running:
            if self.state:
                self.state.events()
                self.state.draw()
                self.state.update()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
