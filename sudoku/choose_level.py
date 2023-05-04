import pygame
from constant import *

pygame.init()
size = (CELL_X, CELL_Y)
window = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 25)

def draw_button(left, top, color, textInButton):
    rect_size = pygame.Rect(left, top, 60, 30)
    pygame.draw.rect(window, color, rect_size)  
    pygame.draw.rect(window, BLACK, rect_size, 3)
    font_button = pygame.font.Font('freesansbold.ttf', 20)
    text_button = font_button.render(textInButton, True, BLACK, )
    text_rect_button = text_button.get_rect()
    text_rect_button.center = (left + 30, top + 15)
    window.blit(text_button, text_rect_button)


def choose_level():
    level = 0
    text = font.render('Choose game level', True, BLACK, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (CELL_X // 2, CELL_Y // 2 - 40)
    pygame.display.set_caption("Sudoku Puzzle")

    done = True
    while done:
        window.fill(WHITE)
        window.blit(text, text_rect)
        draw_button(40, 100, GRAY, "1")
        draw_button(120, 100, GRAY, "2")
        draw_button(200, 100, GRAY, "3")
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (40 <= pos[0] <= 100) and (100 <= pos[1] <= 130):
                    level = 1
                if (120 <= pos[0] <= 180) and (100 <= pos[1] <= 130):
                    level = 2
                if (200 <= pos[0] <= 260) and (100 <= pos[1] <= 130):
                    level = 3
                if level != 0:
                    pygame.quit()
                    return level

            pygame.display.update()

