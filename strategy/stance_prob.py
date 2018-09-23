from strategy.strategy import *
import random, math

""" Returns a stance to counter the player """
class StanceProb(StanceStrategy):
    DECAY = 0.8

    # 0 is for same as prev, 1 is for counters prev, 2 is for prev counters
    response = [[0.001, 0.001, 0.001], [0.001, 0.001, 0.001], [0.001, 0.001, 0.001]]
    duels = .009

    def update_response(self):
        self.response = [[x * self.DECAY for x in y] for y in self.response]
        self.response[stance_num(self.last_stance)][stance_num(self.opp.stance)] += 1
        self.duels *= self.DECAY
        self.duels += 1

    def probs_stance(self):
        probs = [[x / self.duels for x in y] for y in self.response]
        return probs

    def score_stances(self):
        probs = self.probs_stance()
        scores = [0, 0, 0]

        for s in range(len(STANCES)):
            stance = STANCES[s]

            # the stance that counters stance
            b = (s + 1) % 3
            # the stance that stance counters
            g = (s + 2) % 3

            scores[s] = probs[stance_num(self.me.stance)][g] * get_stat_for_stance(self.me, STANCES[s]) - probs[stance_num(self.me.stance)][b] * get_stat_for_stance(self.opp, STANCES[b])

        return scores

    def best_stance(self):
        scores = self.score_stances()
        return STANCES[scores.index(max(scores))]

    # Whether the opponent can be hit next turn
    def can_attack(self):
        return self.next_location() == self.opp.location

    def select_stance(self):
        if self.me.location == self.opp.location:
            self.update_response()

        if self.can_attack():
            return self.best_stance()
        else:
            if self.game.has_monster(self.next_location()):
                return get_winning_stance(self.game.get_monster(self.next_location()).stance)
            else:
                return STANCES[0]
