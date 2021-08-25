import sys
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
        self.enemies = [Enemy(self, vec(20, 1)), EnemyFrightened(self, vec(1, 1)), EnemyRegular(self, vec(24, 1))]
        self.mode = 'scatter'
        # self.enemies = []
        self.current_score = 0

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
