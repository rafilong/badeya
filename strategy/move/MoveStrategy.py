from abc import ABC, abstractmethod

class StanceStrategy(ABC):
    game = None;

    def __init__(self, game):
        self.game = game;

    @abstractmethod
    def whichMove(self):
        pass
