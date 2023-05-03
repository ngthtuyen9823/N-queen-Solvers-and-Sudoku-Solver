import n_queens_gui
import random
import sys

QUEEN = 1
EMPTY_SPOT = 0
BOARD_SIZE = 5


class NQueens:
    """
    This class represents the N-Queens problem.
    There is no UI, but its methods and attributes can be used by a GUself.sizeI.
    """

    def __init__(self, n):
        self.size = n
        self.state = []
        self.state = []
        self.reset_board()
        self.create_initial_solution()
        self.vectors = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


    def get_size(self):
        """
        Get size of board (square so only one value)
        """
        return self.size

    def reset_new_size(self, value):
        """
        Resets the board with new dimensions (square so only one value).
        """
        self.size = value
        self.reset_board()

    def get_board(self):
        """
        Get game board.
        """
        return self.state

    def reset_board(self):
        """
        Restores board to empty, with current dimensions.
        """
        self.state = []
        for y in range(self.size):
            row = []
            for x in range(self.size):
                row.append(EMPTY_SPOT)
            self.state.append(row)

    def is_winning_position(self):
        """
        Checks whether all queens are placed by counting them. There should be as many as the board size.
        """
        num_queens = sum(row.count(QUEEN) for row in self.state)
        return num_queens >= self.size

    def is_queen(self, pos):
        """
        Check whether given position contains a queen.
        """
        i, j = pos
        return self.state[i][j] == QUEEN

    def place_queen(self, pos):
        """
        Add a queen (represented by 1) at a given (row, col).
        """
        if self.is_legal_move(pos):
            self.state[pos[0]][pos[1]] = QUEEN
            return True  # Return value is useful for GUI - e.g trigger sound.
        return False

    def remove_queen(self, pos):
        """
        Set position on board to EMPTY value
        """
        self.state[pos[0]][pos[1]] = EMPTY_SPOT

    def is_legal_move(self, pos):
        """
        Check if position is on board and there are no clashes with existing queens
        """
        return self.check_row(pos[EMPTY_SPOT]) and self.check_cols(pos[1]) and self.check_diagonals(pos)

    def check_row(self, row_num):
        """
        Check a given row for collisions. Returns True if move is legal
        """
        return not QUEEN in self.state[row_num]

    def check_cols(self, pos):
        """
        Check columns and return True if move is legal, False otherwise
        """
        legal = True
        for row in self.state:
            if row[pos] == QUEEN:
                legal = False
        return legal

    def check_diagonals(self, pos):
        """
        Checks all 4 diagonals from given position in a 2d list separately, to determine
        if there is a collision with another queen.
        Returns True if move is legal, else False.
        """
        num_rows, num_cols = len(self.state), len(self.state[0])
        row_num, col_num = pos

        # Lower-right diagonal from (row_num, col_num)
        i, j = row_num, col_num  # This covers case where spot is already occupied.
        while i < num_rows and j < num_cols:
            if self.state[i][j] == QUEEN:
                return False
            i, j = i + 1, j + 1

        # Upper-left diagonal from (row_num, col_num)
        i, j = row_num - 1, col_num - 1
        while i >= 0 and j >= 0:
            if self.state[i][j] == QUEEN:
                return False
            i, j = i - 1, j - 1

        # Upper-right diagonal from (row_num, col_num)
        i, j = row_num - 1, col_num + 1
        while i >= 0 and j < num_cols:
            if self.state[i][j] == QUEEN:
                return False
            i, j = i - 1, j + 1

        # Lower-left diagonal from (row_num, col_num)
        i, j = row_num + 1, col_num - 1
        while i < num_cols and j >= 0:
            if self.state[i][j] == QUEEN:
                return False
            i, j = i + 1, j - 1

        return True

    def solve(self):
        self.min_conflicts()
        success = self.min_conflicts()
        if success == False: 
            print('\nNo solution was found!!!\nEnd state:')
        
    # Check if a queen is consistent (no conflicts)
    def is_consistent(self, position:()) -> bool:
        # Get the row and column for the queen
        row, column = position
        # Check a row
        for x in range(self.size):
            # Return false if another queen exists in the row
            if (x != column and self.state[row][x] == QUEEN):
                return False
        # Check a column
        for y in range(self.size):
            
            # Return false if another queen exists in the column
            if (y != row and self.state[y][column] == QUEEN):
                return False
        # Check diagonals
        for vector in self.vectors:
                    
            # Reset the start position
            sy, sx = position
            # Get vector deltas
            dy, dx = vector
            # Loop until we are outside the board or have moved the number of steps in the goal
            while True:
                # Update the position
                sy += dy
                sx += dx
                
                # Check if the loop should terminate
                if(sy < 0 or abs(sy) >= self.size or sx < 0 or abs(sx) >= self.size):
                    break
                # Check if we found another queen
                if (y != sy and x != sx and self.state[sy][sx] == QUEEN):
                    return False
        # Return true if no conflicts has been found
        return True
    # Calculate number of conflicts
    def number_of_conflicts(self, position:int) -> int:
        # Number of conflicts
        number_of_conflicts = 0
        # Get the row and column for the queen
        row, column = position
        # Check a row
        for x in range(self.size):
            # Return false if another queen exists in the row
            if (x != column and self.state[row][x] == QUEEN):
                number_of_conflicts += 1
        # Check a column
        for y in range(self.size):
            
            # Return false if another queen exists in the column
            if (y != row and self.state[y][column] == QUEEN):
                number_of_conflicts += 1
        # Check diagonals
        for vector in self.vectors:
                    
            # Reset the start position
            sy, sx = position
            # Get vector deltas
            dy, dx = vector
            # Loop until we are outside the board or have moved the number of steps in the goal
            while True:
                # Update the position
                sy += dy
                sx += dx
                
                # Check if the loop should terminate
                if(sy < 0 or abs(sy) >= self.size or sx < 0 or abs(sx) >= self.size):
                    break
                # Check if we found another queen
                if (y != sy and x != sx and self.state[sy][sx] == QUEEN):
                    number_of_conflicts += 1
        # Return the number of conflicts
        return number_of_conflicts
    # Create an initial solution at random (probably with conflicts)
    def create_initial_solution(self):
        # Loop rows
        for y in range(self.size):
            # Get a column at random
            x = int(random.random() * self.size) - 1
            # Add a queen
            self.state[y][x] = QUEEN
        # Print initial solution
    # Min-conflicts algorithm
    def min_conflicts(self, val_rate:float=0.02, max_steps:int=100000) -> bool:
        # Now repeatedly choose a random variable in conflict and change it
        for i in range(max_steps):
            # Print remaining steps
            if((i + 1)%10000 == 0):
                print(max_steps - i - 1)
            # Variables
            conflicts = []
            # Get all queens that are in conflict
            for y in range(self.size):
                for x in range(self.size):
                    # Check if we have found a queen
                    if (self.state[y][x] == QUEEN and self.is_consistent((y, x)) == False):
                        # Add as a conflict
                        conflicts.append((y, x))
            # Check if the puzzle is solved
            if (len(conflicts) <= 0):
                return True
            # Select a conflict at random
            y, x = random.choice(conflicts)
            # A dictionary to store numbers and the number of conflicts for each number
            scores = {}
            # Loop each column in the row
            for column in range(self.size):
                
                # Count the number of conflicts
                scores[(y, column)] = self.number_of_conflicts((y, column))
            # Sort scores on number of conflicts
            scores = {key: value for key, value in sorted(scores.items(), key=lambda item: item[1])}
            # Get best positions
            best_positions = []
            min_conflicts = sys.maxsize
            for key, value in scores.items():
                
                # Add a position if it is less than or equal to current minimum
                if(value <= min_conflicts):
                    best_positions.append(key)
                    min_conflicts = value
                 # Add at random to be able to jump out from local minimum
                elif (random.random() < val_rate):
                    best_positions.append(key)
            # Get one of the best positions at random
            by, bx = random.choice(best_positions)
            # Update queen position
            self.state[y][x] = EMPTY_SPOT
            self.state[by][bx] = QUEEN
        # No solution was found, return false
        return False
    


n_queens_gui.run_gui(NQueens(BOARD_SIZE))