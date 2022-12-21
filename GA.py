import random
from Strategy import Strategy
import PrisonersDilemma as pd

def proportionalSelection(objects, C):
    # stochastically select strategies for next generation based on their fitness
    sortedObj = sorted(objects, key = lambda x:x.fitness)
    selected = []
    for c in range(C):
        incSum = 0
        r = random.random()
        for i, obj in enumerate(sortedObj):
            incSum += obj.propFitness
            if incSum > r:
                selected.append(obj)
                break

    return selected

# ==========================================
# ==========================================


def crossover(parents):
    locus = random.randint(0, len(parents[0].string)-1)

    childstrs = [
        parents[0].string[:locus] + parents[1].string[locus:],
        parents[1].string[:locus] + parents[0].string[locus:]
    ]

    children = []
    for i in range(2):
        child = Strategy([parents[0].label, parents[1].label])
        child.string = childstrs[i]
        child.setup()
        children.append(child)

    return children

# ==========================================
# ==========================================

def mutation(children, Pm):
    for child in children:
        for bit in child.string:
            if random.random() < Pm:
                locus = random.randint(0, len(child.string)-1)
                child.string[locus] = "c" if child.string[locus] == "d" else "d"

    return children

# ==========================================
# ==========================================

def generation(strategies, Pc, Pm):

    numParents = round(len(strategies) / 2)

    for i, A in enumerate(strategies):
        for j, B in enumerate(strategies):
            if j < i:
                continue
            scoreAB = pd.prisonersDilemma(A, B)
            A.scores[j] = scoreAB[0]
            B.scores[i] = scoreAB[1]

    totalFitness = 0
    for s in strategies:
        s.fitness = sum(s.scores) / len(s.scores)
        totalFitness += s.fitness

    for s in strategies:
        s.propFitness = s.fitness / totalFitness

    fittest = proportionalSelection(strategies, numParents)

    nextGeneration = []
    nextGeneration.extend(fittest)

    while(len(nextGeneration) < len(strategies)):
        couple = proportionalSelection(strategies, 2)
        print(f"Couple selected: {couple[0].label, couple[1].label}")
        children = []
        if random.random() < Pc:
            children = crossover(couple)
        else:
            children = couple
            for child in children:
                child.parents = [couple[0].label, couple[1].label]

        children = mutation(children, Pm)

        nextGeneration.extend(children)

    for i, s in enumerate(nextGeneration):
        s.label = i

    print(f"Fitness for generation: {totalFitness}")
    # printNextGenerationDetails(nextGeneration)
    return nextGeneration
