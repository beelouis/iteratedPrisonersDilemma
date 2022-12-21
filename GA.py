import random
from Strategy import Strategy
import PrisonersDilemma as pd

def proportionalSelection(P):
    sortedP = sorted(P, key = lambda p:p.fitness)

    couples = [[0,0] for i in range(round(len(P)/2))]
    outer = 0
    inner = 0

    for i in range(len(P)):
        incSum = 0
        r = random.random()
        for p in sortedP:
            incSum += p.propFitness
            if incSum > r:
                outer += 1 if (i % 2 == 0 and i != 0) else 0
                inner = i % 2
                couples[outer][inner] = p
                break

    return couples
# ==========================================
# ==========================================


def crossover(couples, Pc):
    P = []
    for couple in couples:
        if random.random() < Pc:
            locus = random.randint(0, len(couple[0].string)-1)
            s1 = couple[0].string
            s2 = couple[1].string
            couple[0].string = s1[:locus] + s2[locus:]
            couple[1].string = s2[:locus] + s1[locus:]
        P.extend(couple)

    return P
# ==========================================
# ==========================================

def mutate(P, Pm):
    for p in P:
        modifier = 1
        for i, gene in enumerate(p.string):
            if random.random() * modifier < Pm:
                p.string[i] = "c" if gene == "d" else "d"
        p.setup()
    return P

# ==========================================
# ==========================================

def generation(P, Opps, genNumber, maxGen, Pc, Pm, ABruns):
    if genNumber == maxGen:
        return P
    print(f"--------------- generation: {genNumber} --------------- ")
    for A in P:
        for Opp in Opps:
            A.score = pd.prisonersDilemma(A, Opp, ABruns)

    totalFitness = 0
    for p in P:
        p.fitness = p.score / len(Opps)
        print(f"{p.label}, {p.fitness}")
        totalFitness += p.fitness

    for p in P:
        p.propFitness = p.fitness / totalFitness

    couples = proportionalSelection(P)
    P = crossover(couples, Pc)
    P = mutate(P, Pm)

    print(f"\nTotal Fitness = {totalFitness}\n")

    genNumber += 1
    return generation(P, Opps, genNumber, maxGen, Pc, Pm, ABruns)
