from strategy.strategy import *
import random, math

def rotate(l, n):
    return l[n:] + l[:n]

def response_type(opp, me):
    return (stance_num(opp) - stance_num(me)) % 3

""" Returns a stance to counter the player """
class StanceCombo(StanceStrategy):
    DECAY = 0.8
    THRESHOLD = 0

    def update_data(self):
        self.update_response()
        self.update_memory()

    # 0 is for same as prev, 1 is for counters prev, 2 is for prev counters
    response = [.001, .001, .001]
    duels = .003

    def update_response(self):
        type = response_type(self.opp.stance, self.last_stance)
        self.response = [x * self.DECAY for x in self.response]
        self.response[type] += 1
        self.duels *= self.DECAY

    memory = {}

    def update_memory(self):
        if self.get_turn_num() > 1:
            key = self.me_last_stance + self.opp_last_stance
            self.memory[key] = get_winning_stance(self.opp.stance)

        self.opp_last_stance = self.opp.stance
        self.me_last_stance = self.me.stance


    def probs_stance(self):
        probs = [x / self.duels for x in self.response]
        probs = rotate(probs, -stance_num(self.me.stance))
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

            scores[s] = probs[g] * get_stat_for_stance(self.me, STANCES[s]) - probs[b] * get_stat_for_stance(self.opp, STANCES[b])

        return scores

    def combo_stance(self):
        scores = self.score_stances()
        var = sum((max(scores) - x) ** 2 for x in scores) / len(scores)

        if var < self.THRESHOLD:
            return self.memo_stance()
        else:
            return STANCES[scores.index(max(scores))]

    def best_stance(self):
        scores = self.score_stances()
        return STANCES[scores.index(max(scores))]

    def memo_stance(self):
        current_key = self.me.stance + self.opp.stance
        if current_key in self.memory:
            return self.memory[current_key]
        else:
            return STANCES[random.randint(0, 2)]

    # Whether the opponent can be hit next turn
    def can_attack(self):
        return self.next_location() == self.opp.location

    def select_stance(self):
        if self.me.location == self.opp.location:
            self.update_response()
            self.duels += 1

        if self.can_attack():
            return self.combo_stance()
        else:
            if self.game.has_monster(self.next_location()):
                return get_winning_stance(self.game.get_monster(self.next_location()).stance)
            else:
                return STANCES[0]
