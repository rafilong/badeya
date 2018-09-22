from abc import ABC, abstractmethod
from strategy.utils import *

class Strategy(ABC):

    def __init__(self):
        self.game = None

    def __init__(self, game):
        self.game = game
        self.me = game.get_self()
        self.op = game.get_opponent()

    def update(self):
        pass

    def will_move(self):
        if (self.me.movement_counter - 1 == self.me.speed):
            return True
        else:
            return False

    def next_location(self):
        if self.will_move():
            return self.me.destination
        else:
            return self.me.location

class MoveStrategy(Strategy):
    """How much damage the player will take while killing a monster."""
    def damage_to_kill(self, monster):
        damage_taken = 0
        turns_to_kill = self.turns_to_kill(monster, self.me)
        damage_taken += monster.attack * turns_to_kill

        return damage_taken

    """Damage the player will take moving along the given path."""
    # Hassan
    def path_damage(self, path):
        damage_taken = 0;
        for i in range(len(path)):
            monster = self.game.get_monster(node[i])

            # check if enemy respawns by the time i get there
            if monster.respawn_counter <  (7 - self.me.speed) * (i+1):
                damage_taken += damage_to_kill(monster)

        return damage_taken

    """ Whether or not we can steal a nearby kill"""
    def can_steal(self):
        if self.game.shortest_paths(self.me.location, self.op.location)[0] == 1:
            monster = self.game.get_monster(self.op.location)

            if self.turns_to_kill(monster, self.op) > (7 - self.speed):
                return True


    """ How many turns does it take for an entity to kill the given monster"""
    def turns_to_kill(self, monster, entity):
        win_stance_str = get_winning_stance(monster.stance)
        if win_stance_str == "Rock":
            win_stance = entity.paper
        elif win_stance_str == "Paper":
            win_stance = entity.scissors
        else:
            win_stance = entity.rock

        if monster.health // win_stance

    """Whether the current node has a living monster."""
    def has_alive_monster(self):
        return self.game.has_monster(self.me.location) and not self.game.get_monster(self.me.location).dead

    """Whether the player is in the state of moving."""
    def moving(self):
        return self.me.destination != self.me.location

    def get_move(self):
        self.update()
        return self.select_move()

    @abstractmethod
    def select_move(self):
        pass

class StanceStrategy(Strategy):
    STANCES = ["Rock", "Paper", "Scissors"]

    def get_winning_stance(stance):
        if stance == "Rock":
            return "Paper"
        elif stance == "Paper":
            return "Scissors"
        elif stance == "Scissors":
            return "Rock"

    def get_stance(self):
        self.update()
        return self.select_stance()

    @abstractmethod
    def select_stance(self):
        pass
