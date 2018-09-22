from strategy.strategy import *
import random

""" Moves to the closest monster """
class MoveWalks(MoveStrategy):
    walk = []
    idx = 0

    def score(travel_info):
        stats = travel_info.stats
        return stat

    def select_move(self):
        if self.just_moved():
            self.idx += 1;

        if has_alive_monster(self.game, self.me.location):
            ttk = get_time_to_kill(self.game, self.me, self.game.get_monster(self.me.location))
            if ttk >= 7 - self.me.speed:
                return self.me.location

        if self.idx >= len(self.walk):
            '''walks = generate_walks(self.game, self.me.location, 5)
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
            self.walk = best_stats_walk'''
            self.walk = [10, 16, 10, 0]
            self.idx = 0

        return self.walk[self.idx]
