import pygame.font


def draw_text(text, screen, size, color, font_name, pos):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(text, False, color)
    text_size = text.get_size()
    pos_x = pos[0] - text_size[0]/2
    pos_y = pos[1] - text_size[1]/2

    screen.blit(text, (pos_x, pos_y))

