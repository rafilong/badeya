# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import strategy.Config as config

first_line = True # DO NOT REMOVE
init = True

# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game
    if init:
        move_strategy = config.STRATEGY['move'](game)
        stance_strategy = config.STRATEGY['stance'](game)
        init = False

    destination = move_strategy.get_move()
    stance = stance_strategy.get_stance()

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination, stance)
