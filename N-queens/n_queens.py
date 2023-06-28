from constant import *
import random
import sys

class NQueens:
    def __init__(self, size:int):
        self.size = size
        self.state = [[0 for j in range(self.size)] for i in range(self.size)]
        self.vectors = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        self.create_initial_solution()

    # Check if a queen is consistent (no conflicts)
    def is_consistent(self, position) -> bool:
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
    
