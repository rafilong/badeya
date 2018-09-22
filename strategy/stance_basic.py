from strategy.strategy import StanceStrategy
import random

""" Returns a stance to counter the monster """
class StanceBasic(StanceStrategy):

    def select_stance(self):
        if self.op.location == self.next_location:
            return StanceStrategy.get_winning_stance(self.op.stance)
        elif self.game.has_monster(self.next_location()):
            return StanceStrategy.get_winning_stance(self.game.get_monster(self.next_location()).stance)
        else:
            return StanceStrategy.STANCES[random.randint(0, 2)]
