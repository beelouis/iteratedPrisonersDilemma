def prisonersDilemma(A, B):
    scoreA = 0
    scoreB = 0

    for i in range(100):
        moveA = A.lookup[A.memory]
        moveB = B.lookup[B.memory]
        A.memory = str(A.memory[2:] + moveA + moveB)
        B.memory = str(B.memory[2:] + moveA + moveB)

        if moveA == moveB:
            if moveA == "c":
                scoreA += 3
                scoreB += 3
            else:
                scoreA += 1
                scoreB += 1
        else:
            if moveA == "c":
                scoreB += 5
            else:
                scoreA += 5

        # printPDDetails(moveA, moveB, A, B, scoreA, scoreB)

    return [scoreA/100, scoreB/100]
