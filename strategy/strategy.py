from abc import ABC, abstractmethod
from strategy.utils import *

class Strategy(ABC):

    def __init__(self):
        self.game = None

    def __init__(self, game):
        self.game = game
        self.me = game.get_self()
        self.opp = game.get_opponent()
        self.me.name = "Good Bot"

        # Initialize with dummy values
        self.last_time = 100
        self.last_dest = self.me.location
        self.last_location = self.me.location
        self.last_stance = self.me.stance
        self.delay = 0

    def update(self):
        self.last_time = self.me.movement_counter
        self.last_dest = self.me.destination
        self.last_location = self.me.location
        self.last_stance = self.me.stance
        self.delay -= 1
        if self.me.location == self.me.destination and self.delay == 0:
            self.delay = 7 - self.me.speed
        pass

    """ Movement information for player """
    # Whether the player wil move in the next turn
    def will_move(self):
        if (self.me.movement_counter - 1 == self.me.speed):
            return True
        else:
            return False

    # Where the player will be in the next turn
    def next_location(self):
        if self.will_move():
            return self.me.destination
        else:
            return self.me.location

    # Whether the player is currently moving to a new location
    def is_moving(self):
        return self.me.destination != self.me.location

    # Whether the play just moved last turn
    def just_moved(self):
        if self.last_dest == self.last_location:
            return self.delay == 0
        else:
            return (self.last_dest == self.me.location) and (self.last_time < self.me.movement_counter)

""" Defines an interface for movement strategies """
class MoveStrategy(Strategy):

    def get_move(self):
        move = self.select_move()
        self.update()
        return move

    @abstractmethod
    def select_move(self):
        pass

""" Defines an interface for movement strategies """
class StanceStrategy(Strategy):

    def get_stance(self):
        stance = self.select_stance()
        self.update()
        return stance

    @abstractmethod
    def select_stance(self):
        pass
