from strategy.strategy import MoveStrategy
import random

class MoveRandom(MoveStrategy):

    def select_move(self):
        if (self.me.location == self.me.destination):
            paths = self.game.get_adjacent_nodes(self.me.location)
            return paths[random.randint(0, len(paths)-1)]
        else:
            return self.me.destination
