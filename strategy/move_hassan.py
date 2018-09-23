from strategy.strategy import *
import random
""" Moves to the closest monster """
class MoveHassan(MoveStrategy):

    first_turn = True
    last_node = 10
    def select_move(self):

        if self.game.turn_number == 295:
            self.game.log(str(self.me.rock) + "  " + str(self.me.scissors) + "  " + str(self.me.paper) + "   " + str(self.me.speed) + "   " + str(self.me.health))
        if self.me.destination != self.me.location:
            return self.me.destination

        if self.first_turn:
            self.first_turn = False
            self.last_node = 1
            return 1

        else:
            if self.me.location == 0:
                options = [1, 6, 10]
                random.shuffle(options)
                if self.last_node != 0:
                    options.remove(self.last_node)

                if self.game.get_monster(0).respawn_counter <= 12:
                    return 0
                elif not self.game.get_monster(options[0]).dead:
                    self.last_node = options[0]
                    return options[0]
                else:
                    self.last_node = options[1]
                    return options[1]
            elif self.me.location == 1 and self.me.scissors >= 4 and not self.game.get_monster(3).dead:
                    return 3
            elif self.me.location == 3:
                return 1
            else:
                return 0

        if not self.is_moving() and not has_alive_monster(self.game, self.me.location):
            monsters = self.game.nearest_monsters(self.next_location(), 1)
            paths = self.game.shortest_paths(self.me.location, monsters[random.randint(0, len(monsters) - 1)].location)
            if len(paths) != 0:
                return paths[0][0]
        return self.me.destination
