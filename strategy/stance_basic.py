from strategy.strategy import StanceStrategy
import random

""" Returns a stance to counter the monster """
class StanceBasic(StanceStrategy):

    def select_stance(self):
        if self.game.has_monster(self.next_location):
            return self.get_winning_stance(self.game.get_monster(self.next_location))
        else:
            return self.stance
