from strategy.strategy import *
import random

""" Returns a stance to counter the monster """
class StanceTest(StanceStrategy):

    def select_stance(self):
        if self.game.get_turn_num() > 1:
            return get_winning_stance(self.opp.stance)
        else:
            return STANCES[0]
