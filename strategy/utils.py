import math

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

def get_current_stats(game, player):
    return Stats(player.speed, player.rock, player.paper, player.scissors, player.health)

class TravelInfo:
    def __init__(self, duration, stats):
        self.duration = duration
        self.stats = stats

    def __str__(self):
        return 'Time: ' + str(self.duration) + '\nSpeed: ' + str(self.stats.speed) + '\nRock: ' + str(self.stats.rock) + '\nPaper: ' + str(self.stats.paper) + '\nScissors: ' + str(self.stats.scissors) + '\nHP: ' + str(self.stats.health)

def get_travel_stats(game, target_location):
    me = game.get_self()
    stats = get_current_stats(game, me)
    paths = game.shortest_paths(me.location, target_location)

    min_time = -1
    min_time_stats = None
    for path in paths:
        (time_using_path, end_stats) = ttl_helper(game, stats, me.location, path, 0, 0)
        if min_time == -1 or time_using_path < min_time:
            min_time = time_using_path
            min_time_stats = end_stats
    return TravelInfo(min_time, min_time_stats)

def ttl_helper(game, stats, current_location, path, idx, time_in_future):
    if idx == len(path):
        return (0, stats)

    time_for_this_loc = (7 - stats.speed)
    if will_monster_be_alive(game, current_location, time_in_future):
        monster = game.get_monster(current_location)
        time_to_kill = get_time_to_kill(game, stats, monster)
        stats = stats.with_damage(time_to_kill * monster.attack)
        if time_to_kill <= time_for_this_loc:
            stats = stats.after_kill(monster)
            time_for_this_loc = max(time_to_kill, 7 - stats.speed)

    next_location = path[idx]

    (time, end_stats) = ttl_helper(game, stats, next_location, path, idx + 1, time_in_future + time_for_this_loc)
    return (time_for_this_loc + time, end_stats)


def will_monster_be_alive(game, location, time_from_now):
    if not game.has_monster(location):
        return False
    monster = game.get_monster(location)
    if not monster.dead:
        return True
    return time_from_now >= monster.respawn_counter

def get_time_to_kill(game, stats, monster):
    me = game.get_self()
    hp = monster.health
    fighting_stat = get_stat_for_stance(me, get_winning_stance(monster.stance))
    return math.ceil(hp / fighting_stat)

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

def get_stat_for_stance(entity, name):
    if name == 'Rock':
        return entity.rock
    elif name == 'Paper':
        return entity.paper
    else:
        return entity.scissors
