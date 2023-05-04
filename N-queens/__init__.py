import n_queens_gui
from n_queens import NQueens
from constant import *

class Game:
    # This class represents the N-Queens problem.
    # There is no UI, but its methods and attributes can be used by a GUself.sizeI.

    def __init__(self, solver: NQueens):
        self.solver = solver

    def get_size(self):
        # Get size of board (square so only one value)
        return self.solver.size

    def reset_new_size(self, value):
        # Resets the board with new dimensions (square so only one value).
        self.solver.size = value
        self.reset_board()

    def get_board(self):
        # Get game board.
        return self.solver.state

    def reset_board(self):
        # Restores board to empty, with current dimensions.
        state = []
        for y in range(self.solver.size):
            row = []
            for x in range(self.solver.size):
                row.append(EMPTY_SPOT)
            state.append(row)
        self.solver.state = state

    def is_winning_position(self):
        # Checks whether all queens are placed by counting them. There should be as many as the board size.
        num_queens = sum(row.count(QUEEN) for row in self.solver.state)
        return num_queens >= self.solver.size

    def is_queen(self, pos):
        # Check whether given position contains a queen.
        i, j = pos
        return self.solver.state[i][j] == QUEEN

    def place_queen(self, pos):
        # Add a queen (represented by 1) at a given (row, col).
        if self.solver.is_consistent(pos):
            self.solver.state[pos[0]][pos[1]] = QUEEN
            return True  # Return value is useful for GUI - e.g trigger sound.
        return False

    def remove_queen(self, pos):
        # Set position on board to EMPTY value
        self.solver.state[pos[0]][pos[1]] = EMPTY_SPOT

    def create_initial_solution(self):
        # Create a random initial solution.
        self.solver.create_initial_solution()

    def solve(self):
        try:
            var_rate = 0.02
            max_steps = 200000
            success = self.solver.min_conflicts(var_rate, max_steps)
            if success == False:
                print('\nNo solution was found!!!\nEnd state:')
        except:
            print("No solution found")

    
if __name__ == "__main__":
    n_queens = NQueens(BOARD_SIZE)
    game = Game(n_queens)
    n_queens_gui.run_gui(game)