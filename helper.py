import pygame.font
from settings import *
from models.Grid import Grid

# grid
GRID = Grid('grid.txt')


def draw_text(text, screen, size, color, font_name, pos, centered=True):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(text, False, color)
    pos_x, pos_y = pos
    if centered:
        text_size = text.get_size()
        pos_x = pos[0] - text_size[0]/2
        pos_y = pos[1] - text_size[1]/2

    screen.blit(text, (pos_x, pos_y))


def draw_grid_debug(screen):
    for x in range(WIDTH//GRID_DIMENSION):
        pygame.draw.line(
            screen,
            GRAY,
            (x*GRID_DIMENSION + MARGIN//2, MARGIN//2),
            (x*GRID_DIMENSION + MARGIN//2, HEIGHT + MARGIN//2)
        )
    for y in range(HEIGHT//GRID_DIMENSION):
        pygame.draw.line(
            screen,
            GRAY,
            (MARGIN//2, y * GRID_DIMENSION + MARGIN//2),
            (WIDTH+ MARGIN//2, y * GRID_DIMENSION + MARGIN//2)
        )


def draw_grid_cells():
    for i in range(GRID.cols):
        for j in range(GRID.rows):
            GRID.cells[i][j].draw()
