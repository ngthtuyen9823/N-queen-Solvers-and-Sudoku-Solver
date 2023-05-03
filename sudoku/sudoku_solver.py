import copy
from sudoku import Sudoku
from sudoku_generator import *


# -------- Global board ----------------

board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

solved_board = copy.deepcopy(board)


def solve(board):
    size = 9 # 9 columns and 9 rows
    sub_column_size = 3 # 3 columns in each submatrix
    sub_row_size = 3 # 3 rows in each submatrix
    var_rate = 0.02
    val_rate = 0.03
    max_steps = 200000
    initial_state = board
    sudoku = Sudoku(initial_state, size, sub_column_size, sub_row_size)
    print('Puzzle input:')
    sudoku.print_board()
    # Solve Sudoku with a min-conflicts algorithm
    success = sudoku.min_conflicts(var_rate, val_rate, max_steps)
    print('\nPuzzle solution:') if success == True else print('\nNo solution was found!!!\nEnd state:')
    sudoku.print_board()
    print()
    board = initial_state 
    
def main_solver(level):
    sudoku_generate(board, level)
    solved_board = copy.deepcopy(board) 
    solve(solved_board) 
    return solved_board
   