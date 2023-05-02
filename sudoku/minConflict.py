def min_conflict(problem, numIter=10000):

    state = problem.getStartState()

    for i in range(numIter):

        var = problem.getVar(state)  # Get the next conflicted variable randomly

        # No conflict, i.e. We have solved the problem
        if var == -1:
            return state

        val = problem.getValue(state, var)
        state = problem.updateBoard(state, var, val)

    return []
