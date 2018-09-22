import math

STANCES = ["Rock", "Paper", "Scissors"]

def stance_num(stance):
    if stance == "Rock":
        return 0
    elif stance == "Scissors":
        return 1
    elif stance == "Paper":
        return 2
    else:
        return -1

""" Stats information for finding best walks """

class Stats:
    def __init__(self, speed, rock, paper, scissors, health):
        self.speed = speed
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        self.health = health

    def copy(self):
        return copy.copy(self)

    def with_damage(self, amount):
        return Stats(self.speed, self.rock, self.paper, self.scissors, self.health - amount)

    def after_kill(self, monster):
        return Stats(self.speed + monster.death_effects.speed, self.rock + monster.death_effects.rock, self.paper + monster.death_effects.paper, self.scissors + monster.death_effects.scissors, self.health + monster.death_effects.health)

def generate_walks(game, current_location, n):
    if n == 0:
        return [[]]
    to_return = []
    adj = game.get_adjacent_nodes(current_location) + [current_location]
    for node in adj:
        subres = generate_walks(game, node, n - 1)
        for result in subres:
            to_return.append([node] + result)
    return to_return


def get_current_stats(game, player):
    return Stats(player.speed, player.rock, player.paper, player.scissors, player.health)

class TravelInfo:
    def __init__(self, duration, stats):
        self.duration = duration
        self.stats = stats

    def __str__(self):
        return 'Time: ' + str(self.duration) + '\nSpeed: ' + str(self.stats.speed) + '\nRock: ' + str(self.stats.rock) + '\nPaper: ' + str(self.stats.paper) + '\nScissors: ' + str(self.stats.scissors) + '\nHP: ' + str(self.stats.health)

def get_respawn_status(game):
    resp_status = {}
    for monster in game.get_all_monsters():
        resp_status[monster.location] = monster.respawn_counter
    return resp_status

# Gets the player's estimated stats after following a given path
def get_travel_stats(game, current_location, path, must_kill = False):
    me = game.get_self()
    stats = get_current_stats(game, me)
    resp_status = get_respawn_status(game)
    (t, st) = ttl_helper(game, stats, resp_status, current_location, path, 0, 0, must_kill)
    return TravelInfo(t, st)

# See above
def ttl_helper(game, stats, resp_status, current_location, path, idx, time_in_future, must_kill):
    if idx == len(path):
        return (0, stats)

    # Time it will take to leave this location
    time_for_this_loc = (7 - stats.speed)

    # If we're fighting, we do more calculations
    if will_monster_be_alive(game, resp_status, current_location, time_in_future):
        monster = game.get_monster(current_location)
        time_to_kill = get_time_to_kill(game, stats, monster)
        if must_kill:
            time_for_this_loc = max(time_for_this_loc, time_to_kill)
        # Take damage
        stats = stats.with_damage(time_to_kill * monster.attack)
        # If we kill the monster
        if time_to_kill <= time_for_this_loc:
            # Update stats
            stats = stats.after_kill(monster)
            # If we improve speed stat, and we killed monster fast enough, we
            # get to leave earlier
            time_for_this_loc = max(time_to_kill, 7 - stats.speed)
            resp_status[current_location] = 7 - monster.respawn_rate + time_in_future

    next_location = path[idx]

    (time, end_stats) = ttl_helper(game, stats, resp_status, next_location, path, idx + 1, time_in_future + time_for_this_loc, must_kill)
    return (time_for_this_loc + time, end_stats)


def has_alive_monster(game, location):
    if game.has_monster(location):
        return not game.get_monster(location).dead
    else:
        return False

# Guesses whether a monster will be alive, a given number of turns from now
def will_monster_be_alive(game, resp_status, location, time_from_now):
    if not game.has_monster(location):
        return False
    return time_from_now >= resp_status[location]

# Determines the time-to-kill the current monster, assuming winning stance
def get_time_to_kill(game, stats, monster):
    hp = monster.health
    fighting_stat = get_stat_for_stance(stats, get_winning_stance(monster.stance))
    return math.ceil(hp / fighting_stat)

# How much damage the player will take while killing a monster
def damage_to_kill(stats, monster):
    damage_taken = 0
    turns_to_kill = get_time_to_kill(monster, self.me)
    damage_taken += monster.attack * turns_to_kill

    return damage_taken

# Damage the player will take moving along the given path
def path_damage(game, stats, path):
    damage_taken = 0;
    for i in range(len(path)):
        monster = game.get_monster(node[i])

        # check if enemy respawns by the time i get there
        if monster.respawn_counter <  (7 - stats.speed) * (i+1):
            damage_taken += damage_to_kill(monster)

    return damage_taken

# Whether or not we can steal a nearby kill
def can_steal(game, stats, opp):
    if game.shortest_paths(stats.location, opp.location)[0] == 1:
        monster = self.game.get_monster(opp.location)

        if get_time_to_kill(monster, opp) > (7 - self.speed):
            return True


# Gives the winning stance given another one
def get_winning_stance(stance):
    if stance == 'Rock':
        return 'Paper'
    elif stance == 'Paper':
        return 'Scissors'
    elif stance == 'Scissors':
        return 'Rock'

# Grabs the relevant stat for a stance by name
def get_stat_for_stance(stats, name):
    if name == 'Rock':
        return stats.rock
    elif name == 'Paper':
        return stats.paper
    else:
        return stats.scissors
