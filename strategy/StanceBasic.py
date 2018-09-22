from .Strategy import StanceStrategy
import random

class StanceBasic(StanceStrategy):

    def whichStance(self):
        return StanceStrategy.STANCES[random.randint(0, 2)]
