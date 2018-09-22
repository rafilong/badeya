import StanceStrategy

class StanceBasic(StanceStrategy):

    def whichStance(self):
        return STANCES[random.randit(0, 2)]
