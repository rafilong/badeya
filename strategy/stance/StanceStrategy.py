from abc import ABC, abstractmethod

class StanceStrategy(ABC):

    @abstractmethod
    def whichStance():
        pass
