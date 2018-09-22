from strategy.strategy import *
import random

walk = []
idx = 0
turns_to_move = -1

""" Moves to the closest monster """
class MoveWalks(MoveStrategy):

    def select_move(self):
        global walk, idx
        if not self.is_moving():
            idx += 1
            if idx < len(walk):
                return walk[idx]
            
        if idx >= len(walk):
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
            walk = best_stats_walk
            idx = 0
            return walk[idx]

        return self.me.destination
