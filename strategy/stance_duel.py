from strategy.strategy import *
import random

""" Returns a stance to counter the monster """
class StanceDuel(StanceStrategy):

    stance_dic = {}
    last_enemy_stance = ""
    first_duel = True

    def select_stance(self):
        stances = self.me.stance + self.opp.stance

        if self.opp.stance == "Invalid Stance":
            return STANCES[random.randint(0, 2)]
        # if we have already seen it
        if stances in self.stance_dic:
            # contradiction in memory
            if self.stance_dic[stances] != get_winning_stance(self.opp.stance):
                self.second_mode()
            else:
                self.last_enemy_stance = self.opp.stance
                return self.stance_dic[stances]

        # add this to our memory
        if not self.first_duel:
            key = self.me.stance + self.last_enemy_stance
            if key not in self.stance_dic:
                self.stance_dic[key] = get_winning_stance(self.opp.stance)
                self.last_enemy_stance = self.opp.stance
                return STANCES[random.randint(0, 2)]

        else:
            self.first_duel = False
                    
        self.last_enemy_stance = self.opp.stance
        return STANCES[random.randint(0, 2)]
    def second_mode(self):

        # play something else every round.
        other_stances = STANCES
        other_stances.remove(self.me.stance)

        if other_stances[0] > other_stances[1]:
            return other_stances[0]
        else:
            return other_stances[1]








            

