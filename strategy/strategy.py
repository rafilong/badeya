from abc import ABC, abstractmethod
from strategy.utils import *

class Strategy(ABC):

    def __init__(self):
        self.game = None

    def __init__(self, game):
        self.game = game
        self.me = game.get_self()
        self.opp = game.get_opponent()

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

    def get_stance(self):
        self.update()
        return self.select_stance()

    @abstractmethod
    def select_stance(self):
        pass
