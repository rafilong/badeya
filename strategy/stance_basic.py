from strategy.strategy import *
import random

""" Returns a stance to counter the monster """
class StanceBasic(StanceStrategy):

    def select_stance(self):
        if self.opp.location == self.next_location:
            return get_winning_stance(self.opp.stance)
        elif self.game.has_monster(self.next_location()):
            return get_winning_stance(self.game.get_monster(self.next_location()).stance)
        else:
            return STANCES[random.randint(0, 2)]
