import Strategy

class StanceStrategy(Strategy):

    @abstractmethod
    def whichMove(self):
        pass
