from strategy.strategy import *
import random

class StanceRandom(StanceStrategy):

    def select_stance(self):
        return STANCES[random.randint(0, 2)]
