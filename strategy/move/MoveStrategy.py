import Strategy

class MoveStrategy(Strategy):

    @abstractmethod
    def whichMove(self):
        pass
