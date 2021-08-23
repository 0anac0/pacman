import pygame
from pygame.math import Vector2 as vec

# tamanho da tela
WIDTH, HEIGHT = 560, 620
FPS = 60
GRID_DIMENSION = 20
MARGIN = 50

# posicoes
PLAYER_START_POS = vec(1, 1)

# cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (110, 110, 110)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# fontes
START_FONT = 'arial black'
GUI_TEXT_SIZE = 24
START_TEXT_SIZE = 28

# background
BACKGROUND = pygame.transform.scale(pygame.image.load('maze.png'), (WIDTH, HEIGHT))
