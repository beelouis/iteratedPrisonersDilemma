import random
import Moves as m

class Strategy:
    def __init__(self, parents):
        self.parents = parents
        self.label = 0
        self.string = list([])
        self.lookup = dict({})
        self.memory = ""
        self.fitness = 0
        self.propFitness = 0.0
        self.scores = [0 for i in range(20)]

    def randomString(self):
        for i in range(70):
            self.string.append(m.moves[random.randint(0, 1)])

    def setup(self):
        self.lookup = dict({game : self.string[i+6] for i, game in enumerate(m.memorySpace)})
        self.memory = "".join(self.string[:6])
