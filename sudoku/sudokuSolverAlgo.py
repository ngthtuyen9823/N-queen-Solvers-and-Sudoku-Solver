import copy
from sudokuGenerator import *
from minConflict import *
import sudoku_problem
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
    prob = sudoku_problem.Sudoku(board)
    board = min_conflict(prob)
    print(board)
def mainSolver(level):
    sudokuGenerate(Board, level)
    solvedBoard = copy.deepcopy(Board) # solved board luc nay la ma tran sau khi da them cac so 0 vao
    solve(solvedBoard) #solved board luc nay la ma tran sau khi solve 
    return solvedBoard
   