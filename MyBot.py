# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random
from strategy.MoveBasic import MoveBasic
from strategy.StanceBasic import StanceBasic

first_line = True # DO NOT REMOVE
init = True

# global variables or other functions can go here
STANCES = ["Rock", "Paper", "Scissors"]

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

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
        move_strategy = MoveBasic(game)
        stance_strategy = StanceBasic(game)
        init = False

    destination = move_strategy.whichMove()
    stance = stance_strategy.whichStance()

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination, stance)
