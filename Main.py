import random
import Moves as m
import GA
import PrisonersDilemma as pd
from Strategy import Strategy

def printStrategies(strategies):
    for s in strategies:
        print("===============================================")
        print("===============================================")
        print(s.label)
        print("initial memory:")
        for i in s.string[:6]:
            print(i)
        for i, game in enumerate(m.memorySpace):
            print(game , "->", s.string[i+6])

# =========================================
# =========================================

def initialPopulation(N, lenString, string = []):
    population = []
    for i in range(N):
        s = Strategy(N)
        s.label = i
        if string == []:
            s.setRanString(lenString)
        else:
            s.string = string
        s.setup()
        population.append(s)
    return population

# =========================================
# =========================================

N = 20
memoryGames = 3
lenString = 2** ( (memoryGames*len(m.moves)) + (memoryGames*len(m.moves)) )
Nopp = 1
G = 50
ABruns = 100
Pm = 0.001
Pc = 0.7

P = initialPopulation(N, lenString)
for p in P:
    print(p.label)
    for i, g in enumerate(m.games):
        print(f"{g} -> {p.string[i+1]}", end = " | ")
    print("\n")

Opps = initialPopulation(Nopp, lenString, ["c" for i in range(lenString)])

print("==========================================================")
print("==========================================================")
print("==========================================================")

finalPopulation = GA.generation(P, Opps, 0, G, Pc, Pm, ABruns)
for p in finalPopulation:
    print(f"label: {p.label} => {p.score} => {p.fitness} => {p.propFitness}")
    for i, g in enumerate(m.games):
        print(f"{g} -> {p.string[i+1]}", end = " | ")
    print("\n")
