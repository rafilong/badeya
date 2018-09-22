from strategy.strategy import *
import random

def rotate(l, n):
    return l[n:] + l[:n]

def response_type(opp, me):
    return (stance_num(opp) - stance_num(me)) % 3

""" Returns a stance to counter the player """
class StanceDynamic(StanceStrategy):
    DECAY = 1

    # 0 is for same as prev, 1 is for counters prev, 2 is for prev counters
    response = [.001, .001, .001]
    duels = .003

    def update_response(self):
        type = response_type(self.opp.stance, self.last_stance)
        self.response = [x * self.DECAY for x in self.response]
        self.response[type] += 1
        self.duels *= self.DECAY

    def probs_stance(self):
        probs = [x / self.duels for x in self.response]
        probs = rotate(probs, -stance_num(self.last_stance))
        return probs

    def best_stance(self):
        probs = self.probs_stance()
        scores = [0, 0, 0]

        for s in range(len(STANCES)):
            stance = STANCES[s]

            # the stance that counters stance
            b = (s + 1) % 3
            # the stance that stance counters
            g = (s + 2) % 3

            scores[s] = probs[g] * get_stat_for_stance(self.me, STANCES[s]) - probs[b] * get_stat_for_stance(self.opp, STANCES[b])

        return STANCES[scores.index(max(scores))]

    def select_stance(self):
        # Update bookkeeper
        if self.me.location == self.opp.location:
            self.update_response()
            self.duels += 1

        return self.best_stance()