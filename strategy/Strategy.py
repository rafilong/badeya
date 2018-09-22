from abc import ABC, abstractmethod

class Strategy(ABC):

    def __init__(self, game):
        self.game = game

class MoveStrategy(Strategy):

    @abstractmethod
    def whichMove(self):
        pass

class StanceStrategy(Strategy):
    STANCES = ["Rock", "Paper", "Scissors"]

    @abstractmethod
    def whichStance(self):
        pass
