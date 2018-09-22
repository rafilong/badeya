from strategy.strategy import *
import random

""" Returns a stance to counter the monster """
class StanceDuel(StanceStrategy):

    memory = {}
    start_counter = 0;
    opp_last_stance = ""
    me_last_stance = ""

    def select_stance(self):
        current_key = self.me.stance + self.opp.stance
        if current_key in self.memory:
            return self.memory[current_key]


        if self.start_counter > 1:
            key = self.me_last_stance + self.opp_last_stance
            self.memory[key] = get_winning_stance(self.opp.stance)

        else:
            self.start_counter += 1

        self.opp_last_stance = self.opp.stance
        self.me_last_stance = self.me.stance
        return STANCES[random.randint(0, 2)]
