from strategy.strategy import MoveStrategy
import random

""" Moves to the closest monster, but moves to hp monster if health is below threshold """
class MoveSudoku(MoveStrategy):
    BUFFER = 20

    def select_move(self):
        # assums there is always a path between two points
        hp_monster = self.game.get_monster(0)
        hp_paths = self.game.shortest_paths(self.me.location, hp_monster.location)

        if self.path_damage(hp_paths[0]) + self.damage_to_kill(hp_monster) + MoveSudoku.BUFFER > self.me.health:
            return hp_paths[0][0]

        elif not self.moving() and not self.has_alive_monster():
            monsters = self.game.nearest_monsters(self.next_location(), 1)
            paths = self.game.shortest_paths(self.me.location, monsters[random.randint(0, len(monsters) - 1)].location)
            return paths[0][0]

        return self.me.destination
