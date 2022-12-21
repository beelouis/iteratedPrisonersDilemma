def prisonersDilemma(A, B, runs):
    scoreA = 0
    scoreB = 0

    for i in range(runs):
#         print(f"Past Game: {A.memory}")

        moveA = A.lookup.get(A.memory, A.firstMove)
        moveB = B.lookup.get(B.memory, B.firstMove)
        A.memory = str(moveA + moveB)
        B.memory = str(moveA + moveB)

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

#         print(f"Moves: {moveA}, {moveB} => Scores: {newScoreA}\n")
    A.memory = ""
    B.memory = ""
    return scoreA / runs
