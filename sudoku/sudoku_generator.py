import random
import copy

# searches for an empty cell on a Sudoku board
def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return y, x  # y = row , x = column
    # if we got here it mean that we finish the sudoku, so return none
    return None

# checks if a given number is valid to be placed in a given cell of a Sudoku board
def valid_check(board, number, coordinates):
    # checking row
    for x in range(len(board[0])):
        if number == board[coordinates[0]][x] and coordinates[1] != x:  
            return False

    # checking column
    for y in range(len(board)):
        if number == board[y][coordinates[1]] and coordinates[0] != y:
            return False

    # checking the box
    box_x = coordinates[1] // 3
    box_y = coordinates[0] // 3

    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if number == board[y][x] and (y, x) != coordinates:
                return False

    return True

# checks if a given number is valid to be placed in a given cell of a Sudoku board
def generate_random_board(board):
    # end condition:- getting to the end of the board - the function find_empty return NONE
    find = find_empty(board)
    if find is None:  
        return True
    # If there is no empty cell left, the function returns True, indicating that the board is completed.
    else:
        row, col = find # found the empty position
    for number in range(1, 10):
        random_number = random.randint(1, 9) 
        if valid_check(board, random_number, (row, col)):
            board[row][col] = random_number
            if generate_random_board(board):
                return True
            board[row][col] = 0
    return False


def delete_cells(first_board, number):
    while number:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if first_board[row][col] != 0:
            first_board[row][col] = 0
            number = number - 1


def sudoku_generate(first_board, level):
    generate_random_board(first_board)
    if level == 1:
        delete_cells(first_board, 30)
    if level == 2:
        delete_cells(first_board, 40)
    if level == 3:
        delete_cells(first_board, 50)
