from strategy.strategy import MoveStrategy
import random

class MoveBasic(MoveStrategy):

    def select_move(self):
        if not self.moving() and not self.has_alive_monster():
            monsters = self.game.nearest_monsters(next_location, 1)
            return monsters[random.randint(0, len(monsters))].location
        else:
            return self.me.destination
