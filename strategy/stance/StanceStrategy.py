import Strategy

class StanceStrategy(Strategy):

    @abstractmethod
    def whichStance(self):
        pass
