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

def initialPopulation(N):
    strategies = []
    for i in range(N):
        s = Strategy([])
        s.label = i
        s.randomString()
        s.setup()
        strategies.append(s)

    return strategies

# =========================================
# =========================================

numRuns = 1
numGenerations = 50
Pc = 0.7
Pm = 0.001

for run in range(numRuns):
    N = 20
    strategies = initialPopulation(N)
    printStrategies(strategies)
    print(f"Run {run}")

    for gen in range(numGenerations):
        print(f"Generation {gen}")
        strategies = GA.generation(strategies, Pc, Pm)
