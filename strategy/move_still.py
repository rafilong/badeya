from strategy.strategy import *
import random

class MoveStill(MoveStrategy):

    def select_move(self):
        return self.me.location
