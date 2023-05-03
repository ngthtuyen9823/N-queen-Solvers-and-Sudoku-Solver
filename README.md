# AI-final-project

# How to start project
```
1. mkdir .venv
2. python -m venv .venv
3. .venv\Scripts\activate
4. pip install -r requirements.txt
5. python __init__.py
```
----------------------------------------------------------------------------
Sudoku generator and solver with simple GUI created in Python using PyGame.

About the game
In the beginning the player chooses a level of difficulty (easy, normal or hard). Afterwards, the first script generates a random sudoku map according to the chosen level of difficulty and another script solves the sudoku for comparison with the player input after the player submits their answers. The player can then play sudoku with a simple GUI

The program contains 4 scripts .
1️⃣ sudokuGenerator - script that generates a 9X9 sudoku board according to the sudoku puzzle rules - using the backtracking algorithm
2️⃣ sudokuSolverAlgo - script that solves the sudoku puzzle - using the backtracking algorithm
3️⃣ chooseLevel - simple script for the level difficulty GUI
4️⃣ GUI - the main script, the player runs this script to play the game
