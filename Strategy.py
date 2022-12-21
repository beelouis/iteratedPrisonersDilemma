import random
import Moves as m

class Strategy:
    def __init__(self, N):
        self.label = ""
        self.string = []
        self.memory = ""
        self.firstMove = ""
        self.score = 0
        self.fitness = 0
        self.propFitness = 0.0

    def setRanString(self):
        for i in range(len(m.games) + 1):
            self.string.append(m.moves[random.randint(0, 1)])

    def setString(self, string):
        self.string = string

    def setup(self):
        self.lookup = dict({game : self.string[i+1] for i, game in enumerate(m.games)})
        self.firstMove = self.string[0]
