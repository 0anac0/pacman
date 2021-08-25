from models.characters.Enemy import Enemy
from helper import *


class EnemyFrightened(Enemy):
    def __init__(self, app, pos, color=LIGHT_YELLOW, speed=1):
        super().__init__(app=app, pos=pos, speed=speed, color=color, eye_color=BLACK)

    # alvo do assustado quando em modo scatter é o quadrante mais longe do jogador
    def scatter_target(self):
        return self.flee_target()

    def chase_target(self):
        return self.flee_target()
