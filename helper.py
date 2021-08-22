import pygame.font
from settings import *


def draw_text(text, screen, size, color, font_name, pos, centered=True):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(text, False, color)
    pos_x, pos_y = pos
    if centered:
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
            (x*cell_width + MARGIN//2, MARGIN//2),
            (x*cell_width + MARGIN//2, HEIGHT + MARGIN//2)
        )
    for y in range(HEIGHT//cell_height):
        pygame.draw.line(
            screen,
            GRAY,
            (MARGIN//2, y * cell_height + MARGIN//2),
            (WIDTH+ MARGIN//2, y * cell_height + MARGIN//2)
        )