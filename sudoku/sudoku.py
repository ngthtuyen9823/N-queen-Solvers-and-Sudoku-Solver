import sys
import copy
import random
from typing import List

# This class represent a Sudoku
class Sudoku():

    # Create a new Sudoku
    def __init__(self, state:List, size:int, sub_column_size:int, sub_row_size:int):

        # Set values for instance variables
        self.state = state
        self.size = size
        self.sub_column_size = sub_column_size
        self.sub_row_size = sub_row_size
        self.domains = {}
        self.update_domains()

    # Update domains for cells 
    def update_domains(self):
        # Reset domains
        self.domains = {}
        # Create an array with numbers
        numbers = []
        for y in range(self.size):
            for x in range(self.size):
                # Check if a cell is empty
                if (self.state[y][x] == 0):
                    # Loop all possible numbers
                    numbers = []
                    for number in range(1, self.size + 1):
                        # Check if the number is consistent
                        if(self.is_consistent(number, y, x) == True):
                            numbers.append(number)
                    # Add numbers to a domain
                    if(len(numbers) > 0):
                        self.domains[(y, x)] = numbers
                        
    # Check if a number can be put in a cell
    def is_consistent(self, number:int, row:int, column:int) -> bool:
        # Check a row
        for x in range(self.size):
            # Return false if the number exists in the row
            if (x != column and self.state[row][x] == number):
                return False
        # Check a column
        for y in range(self.size):
            # Return false if the number exists in the column
            if (y != row and self.state[y][column] == number):
                return False
        # Calculate row start and column start
        row_start = (row//self.sub_row_size)*self.sub_row_size
        col_start = (column//self.sub_column_size)*self.sub_column_size;
        # Check sub matrix
        for y in range(row_start, row_start+self.sub_row_size):
            for x in range(col_start, col_start+self.sub_column_size):
                # Return false if the number exists in the submatrix
                if (y != row and x != column and self.state[y][x]== number):
                    return False
        # Return true if no conflicts has been found
        return True
    
    # Calculate number of conflicts
    def number_of_conflicts(self, number:int, row:int, column:int) -> int:
        # Number of conflicts
        number_of_conflicts = 0
        # Check a row
        for x in range(self.size):
            # Check if a conflict is found in a row
            if (x != column and self.state[row][x] == number):
                number_of_conflicts += 1
        # Check a column
        for y in range(self.size):
            # Check if a conflict is found in a column
            if (y != row and self.state[y][column] == number):
                number_of_conflicts += 1
        # Calculate row start and column start
        row_start = (row//self.sub_row_size)*self.sub_row_size
        col_start = (column//self.sub_column_size)*self.sub_column_size;
        # Check sub matrix
        for y in range(row_start, row_start+self.sub_row_size):
            for x in range(col_start, col_start+self.sub_column_size):
                # Check if a conflict is found in a submatrix
                if (y != row and x != column and self.state[y][x]== number):
                    number_of_conflicts += 1
        # Return the number of conflicts
        return number_of_conflicts
    
    # Create an initial solution
    def create_initial_solution(self):
        # Generate an initial solution (probably with conflicts)
        for (y,x), numbers in self.domains.items():
            # A dictionary to store numbers and the number of conflicts for each number
            scores = {}
            # Loop numbers
            for number in numbers:
                # Add to conflicts dictionary
                scores[number] = self.number_of_conflicts(number, y, x)
            # Sort scores on number of conflicts
            scores = {key: value for key, value in sorted(scores.items(), key=lambda item: item[1])}
            # Get best numbers
            best_numbers = []
            min = sys.maxsize
            for key, value in scores.items():
                # Add a number if it is less or equal to current minimum
                if(value <= min):
                    best_numbers.append(key)
                    min = value
            # Assign a number at random (one of the best numbers)
            self.state[y][x] = random.choice(best_numbers)
        # Print initial solution
        print('\nInitial solution:')
        self.print_board()
        print()
        
    # Print the current state
    def print_board(self):
        for i in range(len(self.state)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(len(self.state[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:  # end of the row
                    print(self.state[i][j])
                else:
                    print(str(self.state[i][j]) + " ", end="")
                    
    # Min-conflicts algorithm
    def min_conflicts(self, var_rate:float=0.04, val_rate:float=0.02, max_steps:int=100000) -> bool:
        # Generate an initial solution (probably with conflicts)
        self.create_initial_solution()
        # Now repeatedly choose a random variable in conflict and change it
        for i in range(max_steps):
            # Variables
            conflicts = []
            conflict_count = 0
            # Get all variables that are in conflict
            for (y,x), numbers in self.domains.items():
                # Check if the number is consistent
                if(self.is_consistent(self.state[y][x], y, x) == False):
                    # Add the cell
                    conflicts.append((y,x))
                    # Add to the conflict count
                    conflict_count += 1
                # Add at random to be able to jump out from a local minimum
                elif (random.random() < var_rate):
                    # Add the cell
                    conflicts.append((y,x))
            # Check if we have a valid solution
            if(conflict_count <= 0):
                return True
            # Select a cell in conflict at random
            y, x = random.choice(conflicts)
            # Get numbers to chose from
            numbers = self.domains.get((y, x))
            # Loop numbers
            scores = {}
            for number in numbers:
                # Add the number of conflicts as a score
                scores[number] = self.number_of_conflicts(number, y, x)
            # Sort scores on value
            scores = {key: value for key, value in sorted(scores.items(), key=lambda item: item[1])}
            # Get best numbers
            best_numbers = []
            min = sys.maxsize
            for key, value in scores.items():
                # Add a number if it is less or equal to current minimum
                if (value <= min):
                    best_numbers.append(key)
                    min = value
                # Add at random to be able to jump out from local minimum
                elif (random.random() < val_rate):
                    best_numbers.append(key)
            # Assign a number
            self.state[y][x] = random.choice(best_numbers)
        # No solution was found, return false
        return False


