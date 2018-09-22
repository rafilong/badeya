from strategy.strategy import MoveStrategy
import random

class MoveBasic(MoveStrategy):

    def select_move(self):
        if (self.game.get_self().location == self.game.get_self().destination):
            paths = self.game.get_adjacent_nodes(self.game.get_self().location)
            return paths[random.randint(0, len(paths)-1)]
        else:
            return self.game.get_self().destination
