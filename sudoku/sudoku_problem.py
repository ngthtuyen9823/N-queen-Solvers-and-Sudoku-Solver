from random import random,sample,choice, shuffle

class Sudoku:
    def __init__(self, board):
        """Initializes sudoku board. Values describe the predefined values in board: It is set containing tuples (position, value)"""

        # Initialize the board positions
        self.board = board
        self.fixedPos = set()
        for x in range(9):
            for y in range(9):
                if board[x][y] != 0:
                    pos = (x,y)
                    self.fixedPos.add(pos)

        self.valDomain = {}
        for x in range(9):
            for y in range(9):
                pos = (x, y)
                if pos not in self.fixedPos:
                    self.valDomain[pos] = [i for i in range(1, 9 + 1)]

        self.region = lambda pos: (int(pos[0] / 9 ** 0.5), int(pos[1] / 9 ** 0.5))

    def getStartState(self):
        """Initializes the board, and returns starting configuration"""

        return self.board


    def isConflicted(self, state, position):
        """Tells whether given position is conflicted"""

        return self.numConflicts(state, position) > 0


    def getVar(self, state):
        """Returns randomnly selected conflicted variable"""

        Range = [(a, b) for a in range(9) for b in range(9)]

        while Range:
            position = choice(Range)

            if position in self.fixedPos:
                Range.remove(position)
                continue

            if self.isConflicted(state, position):
                return position
                break
            else:
                Range.remove(position)

        return -1


    def numConflicts(self, state, position):
        """Returns the number of conflicts in given state with respect to given Position"""

        x, y = position
        val = state[x][y]
        # same row
        result = [True for i in range(9) if (i != y and state[x][i] == val)]
        # same column
        result.extend([True for i in range(9) if (i != x and state[i][y] == val)])

        # same region
        region = self.region(position)
        start = region[0] * int(9 ** 0.5), region[1] * int(9 ** 0.5)
        stop = start[0] + int(9 ** 0.5), start[1] + int(9 ** 0.5)
        result.extend([True for i in range(start[0], stop[0]) for j in range(start[1], stop[1]) if
                       (i, j) != position and state[i][j] == val])

        return len(result)


    def getValue(self, state, var):
        """ Find the Least Conflicted value of var"""

        conflicts = {}
        newState = list(state)
        currConflicts = self.numConflicts(state, var)

        # For all possible values of var, find the number of conflicts that happen with it.
        for val in self.valDomain[var]:
            newState = self.updateBoard(state, var, val)
            conflicts[val] = self.numConflicts(newState, var)

        # Find the minimum conflict values
        minConflictVal = conflicts[min(conflicts, key=conflicts.get)]  # Sort the conflicts by values

        # If there are more than one value, with same minimum number, we need to break the tie randomly, or code might get stuck in wrong solution
        allMinVal = [val for val, numConflicts in conflicts.items() if numConflicts == minConflictVal]

        minVal = choice(allMinVal)

        return minVal
    def updateBoard(self, state, var, val):
        state[var[0]][var[1]] = val
        return state




