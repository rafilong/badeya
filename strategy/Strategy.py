from abc import ABC, abstractmethod

class Strategy(ABC):

    def __init__(self):
        self.game = None

    def __init__(self, game):
        self.game = game
        self.me = game.get_self()
        self.op = game.get_opponent()

    def update(self):
        pass

class MoveStrategy(Strategy):

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
