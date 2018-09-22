
class Strategy():
    me = None
    game = None

    def __init__(self, game):
        self.game = game
        me = game.get_self()
