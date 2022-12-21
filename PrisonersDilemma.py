def prisonersDilemma(A, B, runs):
    scoreA = 0

    for i in range(runs):

        moveA = A.lookup.get(A.memory)
        moveB = B.lookup.get(B.memory)
        A.memory = A.memory[2:] + str(moveA + moveB)
        B.memory = B.memory[2:] + str(moveA + moveB)

        if moveA == moveB:
            if moveA == "c":
                newScoreA = 3
            else:
                newScoreA = 1
        else:
            if moveA == "c":
                newScoreA = 0
            else:
                newScoreA = 5

        scoreA += newScoreA

    A.resetMemory()
    B.resetMemory()
    return scoreA / runs
