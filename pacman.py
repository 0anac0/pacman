import sys
import random
from helper import *
from models.game_state.Start import Start
from models.characters.Player import Player
from models.characters.Enemy import Enemy
from models.characters.EnemyFrightened import EnemyFrightened
from models.characters.EnemyRegular import EnemyRegular
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH + MARGIN, HEIGHT + MARGIN))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = Start(self)
        self.player = Player(self, PLAYER_START_POS)
        self.enemies = [Enemy(self, vec(14, 11)), EnemyFrightened(self, vec(10, 11)), EnemyRegular(self, vec(10, 17))]

        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 20000)
        self.mode = 'scatter'
        self.current_score = 0
        self.high_score = 0

    def reset_high_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score

    def reset_game(self):
        self.current_score = 0
        self.reset_mode()
        self.reset_enemies_positions()
        self.player.lifes = 3

        for enemy in self.enemies:
            enemy.lifes = 1

    def reset_enemies_positions(self):
        for enemy in self.enemies:
            enemy.reset_initial_position()

    def reset_mode(self):
        possible_modes = ['scatter', 'chase']
        if self.mode in possible_modes:
            possible_modes.remove(self.mode)

        chosen_index = random.randint(0, len(possible_modes)-1)
        self.mode = possible_modes[chosen_index]

    def increase_score(self, score):
        self.current_score += score

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
