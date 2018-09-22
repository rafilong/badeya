from strategy.strategy import *
import random
""" Moves to the closest monster """
class MoveWalks(MoveStrategy):
    walk = []
    idx = 0

    def score(self, walk):
        score = 0
        ts = get_travel_stats(self.game, self.me.location, walk + [0], True)
        if (walk[0] == self.me.location):
            score -= 10
        if ts.stats.health <= 30:
            return ts.stats.health ** 3 - 27000
        return score + (ts.stats.rock + ts.stats.paper + ts.stats.scissors) * 7 + ts.stats.health

    def select_move(self):
        if self.just_moved():
            walks = generate_walks(self.game, self.me.location, 5)

            walks = sorted(walks, key=self.score)
            self.walk = walks[-1]
            self.game.log(str(self.walk))
            self.game.log(str(self.score(self.walk)))
            self.game.log(str(get_travel_stats(self.game, self.me.location, self.walk + [0], True)))
            self.idx = 0

        if has_alive_monster(self.game, self.me.location):
            ttk = get_time_to_kill(self.game, self.me, self.game.get_monster(self.me.location))
            if ttk >= 7 - self.me.speed:
            # if ttk >= self.me.movement_counter:
                return self.me.location
        elif self.game.has_monster(self.me.location):
            monster = self.game.get_monster(self.me.location)
            if monster.respawn_counter < 10 and monster.respawn_counter >= 7 - self.me.speed:
                return self.me.location

        if self.idx >= len(self.walk):
            walks = generate_walks(self.game, self.me.location, 5)

            walks = sorted(walks, key=self.score)
            self.walk = walks[-1]
            self.game.log(str(self.walk))
            self.game.log(str(self.score(self.walk)))
            self.game.log(str(get_travel_stats(self.game, self.me.location, self.walk + [0], True)))
            self.idx = 0

        return self.walk[self.idx]
