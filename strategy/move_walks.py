from strategy.strategy import *
import random

""" Moves to the closest monster """
class MoveWalks(MoveStrategy):

    def score(travel_info):
        stats = travel_info.stats
        return stat

    def select_move(self):
        self.walk = []
        self.idx = 0

        if self.just_moved():
            ttk = 0
            if self.game.has_monster(self.me.location):
                ttk = get_time_to_kill(self.game, self.me, self.game.get_monster(self.me.location))
            self.game.log(str(ttk))
            if ttk <= 7:
                self.idx += 1
                if self.idx < len(self.walk):
                    return self.walk[self.idx]

        if self.idx >= len(self.walk):
            walks = generate_walks(self.game, self.me.location, 5)
            best_stats = None
            best_stats_walk = walks[0]
            best_stats_st = 0

            for walk in walks:
                ts = get_travel_stats(self.game, self.me.location, walk + [0], True)

                st = ts.stats.rock + ts.stats.paper + ts.stats.scissors
                if ts.stats.health > 30 and (best_stats is None or (st > best_stats_st or (st == best_stats_st and ts.duration < best_stats.duration))):
                    best_stats = ts
                    best_stats_st = st
                    best_stats_walk = walk
            self.walk = best_stats_walk
            self.idx = 0
            return self.walk[self.idx]

        return self.me.destination
