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

def initialPopulation(N, string = []):
    population = []
    for i in range(N):
        s = Strategy(N)
        s.label = i
        if string == []:
            s.setRanString()
        else:
            s.string = string
        s.setup()
        population.append(s)
    return population

# =========================================
# =========================================

N = 20
Nopp = 1
G = 50
ABruns = 100
Pm = 0.01
Pc = 0.7

P = initialPopulation(N)
for p in P:
    print(p.label)
    print(f"First move: {p.string[0]}")
    for i, g in enumerate(m.games):
        print(f"{g} -> {p.string[i+1]}", end = " | ")
    print("\n")

Opps = initialPopulation(Nopp, ["c", "c", "c", "c", "c"])

print("==========================================================")
print("==========================================================")
print("==========================================================")

finalPopulation = GA.generation(P, Opps, 0, G, Pc, Pm, ABruns)
for p in finalPopulation:
    print(f"label: {p.label} => {p.score} => {p.fitness} => {p.propFitness}")
    print(f"start: {p.string[0]}", end = " | ")
    for i, g in enumerate(m.games):
        print(f"{g} -> {p.string[i+1]}", end = " | ")
    print("\n")
