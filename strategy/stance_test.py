from strategy.strategy import *
import random

""" Returns a stance to counter the monster """
class StanceTest(StanceStrategy):

    def select_stance(self):
        # return get_winning_stance(self.game.get_monster(self.next_location()).stance)
        return STANCES[0]
