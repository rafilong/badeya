from utils import *

class MockDeathEffects:
    def __init__(self, speed, rock, paper, scissors, health):
        self.speed = speed
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        self.health = health

class MockGame:
    def __init__(self):
        self.player = MockPlayer()
        self.monster3 = MockEnemy(3, 5, 'Scissors', MockDeathEffects(2,0,1,0,0));

    def shortest_paths(self, loc1, loc2):
        return [[1, 3, 4], [1, 2, 3, 4]];

    def get_self(self):
        return self.player

    def has_monster(self, location):
        if location == 0:
            return True
        return False

    def get_monster(self, location):
        if location == 0:
            return self.monster3
        return None

class MockPlayer:
    def __init__(self):
        self.location = 0
        self.speed = 0
        self.rock = 1
        self.paper = 1
        self.scissors = 1
        self.health = 100

class MockEnemy:
    def __init__(self, health, attack, stance, death_effects):
        self.health = health
        self.attack = attack
        self.stance = stance
        self.death_effects = death_effects
        self.dead = False
        self.respawn_counter = 0

game = MockGame()
ttl = get_travel_stats(game, 4)
print(ttl)
