import MoveStrategy

class MoveBasic(MoveStrategy):

    def whichMove(self):
        if (me.location == me.destination):
            return game.get_adjacent_nodes(me.location)[random.randint(0, len(paths)-1)][0]
        else:
            return me.destination
