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
        return 0

    """Damage the player will take moving along the given path."""
    def path_damage(self, path):
        return 0

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
