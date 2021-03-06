from strategy.strategy import *
import random

""" Moves to the closest monster """
class MoveBasic(MoveStrategy):

    def select_move(self):
        if not self.is_moving() and not has_alive_monster(self.game, self.me.location):
            monsters = self.game.nearest_monsters(self.next_location(), 1)
            paths = self.game.shortest_paths(self.me.location, monsters[random.randint(0, len(monsters) - 1)].location)
            if len(paths) != 0:
                return paths[0][0]
        return self.me.destination
