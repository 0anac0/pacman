import pygame.font
from settings import *

BACKGROUND = pygame.transform.scale(pygame.image.load('maze.png'), (WIDTH, HEIGHT))


def draw_text(text, screen, size, color, font_name, pos):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(text, False, color)
    text_size = text.get_size()
    pos_x = pos[0] - text_size[0]/2
    pos_y = pos[1] - text_size[1]/2

    screen.blit(text, (pos_x, pos_y))


def draw_grid(screen, cell_dimensions):
    cell_width, cell_height = cell_dimensions
    for x in range(WIDTH//cell_width):
        pygame.draw.line(
            screen,
            GRAY,
            (x*cell_width, 0),
            (x*cell_width, HEIGHT)
        )
    for y in range(HEIGHT//cell_height):
        pygame.draw.line(
            screen,
            GRAY,
            (0, y * cell_height),
            (WIDTH, y * cell_height)
        )