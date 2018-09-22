from strategy.strategy import *
import random

""" Returns a stance to counter the monster """
class StanceDuel(StanceStrategy):

    stance_dic = {}
    last_enemy_stance = ""
    first_duel = True

    def select_stance(self):

        stances = self.me.stance + self.op.stance

        # if we have already seen it
        if stances in self.stance_dic:
            return self.stance_dic[stances]

        else:
        # add this to our memory
        if not first_duel:
            key = self.me.stance + self.last_enemy_stance
            if key not in self.stance_dic:
                stance_dic[] = get_winning_stance(self.op.stance)
                return StanceStrategy.STANCES[random.randint(0, 2)]

            # contradiction in memory
            elif self.stance_dic[k] != get_winning_stance(self.op.stance):
                self.second_mode()

            last_enemy_stance = self.op.stance
        else:
            first_duel = False

    def second_mode(self):

        # play something else every round.
        other_stances = StanceStrategy.STANCES
        other_stances.remove(self.me.stance)

        if self.me.other_stances[0] > self.me.other_stances[1]:
            return self.me.other_stances[0]
        else
            return self.me.other_stances[1]








            

