from sudoku_solver_algo import *
from choose_level import *
import time

# Define colors
BLACK = (58, 58, 64)
WHITE = (232, 221, 205)
GREEN = (144, 154, 116)
L_GREEN = (135, 174, 166)
RED = (193, 134, 127)
L_RED = (255, 204, 203)
GRAY =  (136, 119, 144)
L_GRAY = (192, 164, 160)
YELLOW = (221, 194, 151)


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = HEIGHT = 50

# This sets the margin between each cell
MARGIN = 5
numbers_1to9 = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
                pygame.K_9]

# Set the width and height of the screen [width, height]
pygame.init()
size = (500, 600)
font = pygame.font.Font('freesansbold.ttf', 32)

# Loop until the user clicks the close button.
done = False

def cheating_all_the_way():
    for row in range(len(board)):
        for column in range(len(board[row])):
            board[row][column] = solved_board[row][column]
            add_num_to_board(board[row][column], row, column, L_GREEN)
            time.sleep(0.05) # allow the user to see the change in the game board
            pygame.display.flip() # updates the screen to reflect the changes made to the board
    finish()


def add_num_to_board(number, row, column, color):
    add_new_rect(row, column, WHITE, 5)
    add_new_rect(row, column, color, None)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), True, BLACK, )
    text_rect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
    text_rect.center = ((MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
    screen.blit(text, text_rect)
    draw_the_border()


def finish():
    if solved_board == board:
        print("The solution is good")
    else:
        print("The solution is not good")


def add_new_rect(row, col, color, width):
    rect_size = pygame.Rect((MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                           HEIGHT)
    if width is not None:
        pygame.draw.rect(screen, color, rect_size, width)  # coloring only the border
    else:
        pygame.draw.rect(screen, color, rect_size)  # coloring the whole rectangle


def flickering(timeFlickering, color):  # flickering with color on-off
    add_new_rect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    add_new_rect(row, column, WHITE, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    add_new_rect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    add_new_rect(row, column, WHITE, 5)
    pygame.display.flip()


def draw_the_border():
    dif = 500 // 9
    for i in range(10):
        thick = 5
        pygame.draw.line(screen, GRAY, (0, i * dif + 2), (500, i * dif + 2), thick)
        pygame.draw.line(screen, GRAY, (i * dif + 2, 0), (i * dif + 2, 500), thick)
    for i in range(10):
        if i % 3 == 0:
            thick = 8
            pygame.draw.line(screen, BLACK, (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, BLACK, (i * dif, 0), (i * dif, 500), thick)


def draw_init_board(table):
    for row in range(len(table)):
        for column in range(len(table[row])):
            color = L_GRAY
            if table[row][column] == 0:  # if we want to change to background of the empty cells
                color = WHITE
                # drawing the rect 
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # show nothing if the number is 0
            font = pygame.font.Font('freesansbold.ttf', 32)
            if table[row][column] == 0:
                text = font.render(" ", True, BLACK, )  # render(text, anti-alias[True], color, background=None)
            else:
                text = font.render(str(table[row][column]), True, BLACK, )

            text_rect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
            text_rect.center = (
                (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
            screen.blit(text, text_rect)
            draw_the_border()


def draw_button(left, top, color, textInButton):
    rect_size = pygame.Rect(left, top, 120, 50)
    pygame.draw.rect(screen, color, rect_size)  # left, top, width, height
    pygame.draw.rect(screen, BLACK, rect_size, 4)
    font_button = pygame.font.Font('freesansbold.ttf', 20)
    text_button = font_button.render(textInButton, True, BLACK, )
    text_rect_button = text_button.get_rect()
    text_rect_button.center = (left + 60, top + 25)
    screen.blit(text_button, text_rect_button)
    

# -- Main Program Loop -----
if __name__ == "__main__":
    flag1 = True
    while flag1:
        level = choose_level()
        if level == 1 or level == 2 or level == 3:
            print(level)
            flag1 = False
            
    pygame.display.set_caption("Sudoku Puzzle")
    screen = pygame.display.set_mode(size)
    
    sol = main_solver(level)  
    
    pygame.init()
    screen.fill(BLACK)
    draw_init_board(board)
    draw_button(70, 520, GRAY, "Refresh")
    draw_button(190, 520, GRAY, "Clear")      
    draw_button(310, 520, GRAY, "Solve")

    ready_for_input = False
    key = None
    while not done:
        is_outside_table = False
        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in numbers_1to9:
                    key = chr(event.key)
                if event.key == pygame.K_RETURN:
                    finish()
                if event.key == pygame.K_c:
                    cheating_all_the_way()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (70 <= pos[0] <= 190) and (520 <= pos[1] <= 570):
                    sol = main_solver(level)  # first at all the script solve the sudoku by itself
                    draw_init_board(board)
                    is_outside_table = True
                if (190 <= pos[0] <= 310) and (520 <= pos[1] <= 570):
                    draw_init_board(board)
                    is_outside_table = True
                if (310 <= pos[0] <= 430) and (520 <= pos[1] <= 570):
                    draw_init_board(sol);
                    is_outside_table = True
                if is_outside_table == False:
                    #  if clicked on a cell get his row and column 
                    if ready_for_input is True:
                        add_new_rect(row, column, WHITE, None)
                        draw_the_border()
                        ready_for_input = False
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (WIDTH + MARGIN)
                    #  checking if it is a empty (0 inside) 
                    if board[row][column] == 0:
                        #  coloring the border of the clicked cell 
                        add_new_rect(row, column, YELLOW, 5)
                        ready_for_input = True
                        #  now only wait for input from the user 
        if ready_for_input and key is not None:
            #  checking if the key is good at it's place 
            if int(key) == sol[row][column]:
                board[row][column] = key
                flickering(0.1, GREEN)  # flickering at a 0.2 seconds with the color green
                add_num_to_board(key, row, column, L_GREEN)
            else:
                flickering(0.1, RED)  # flickering at a 0.2 seconds with the color red
                add_num_to_board(key, row, column, L_RED)

            draw_the_border()
            ready_for_input = False
        key = None
        pygame.display.flip()
        pygame.display.update()


# Close the window and quit.
pygame.quit()
