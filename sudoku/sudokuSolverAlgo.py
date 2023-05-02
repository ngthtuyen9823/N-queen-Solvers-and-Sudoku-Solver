import copy
from sudoku import Sudoku
from sudokuGenerator import *


# -------- Global board ----------------

Board = [
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

solvedBoard = copy.deepcopy(Board)


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
    sudoku.printBoard()
    # Solve Sudoku with a min-conflicts algorithm
    success = sudoku.min_conflicts(var_rate, val_rate, max_steps)
    print('\nPuzzle solution:') if success == True else print('\nNo solution was found!!!\nEnd state:')
    sudoku.printBoard()
    print()
    board = initial_state
    
def mainSolver(level):
    sudokuGenerate(Board, level)
    solvedBoard = copy.deepcopy(Board) # solved board luc nay la ma tran sau khi da them cac so 0 vao
    solve(solvedBoard) #solved board luc nay la ma tran sau khi solve 
    return solvedBoard
   