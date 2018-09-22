from strategy.strategy import StanceStrategy
import random

class StanceRandom(StanceStrategy):

    def select_stance(self):
        return StanceStrategy.STANCES[random.randint(0, 2)]