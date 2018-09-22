from utils import *
import json

class MockDeathEffects:
    def __init__(self, speed, rock, paper, scissors, health):
        self.speed = speed
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        self.health = health

class MockGame:
    def __init__(self, nodes, adjacent_nodes, monsters):
        self.player = MockPlayer()
        self.monsters = monsters
        self.nodes = nodes
        self.adjacent_nodes = adjacent_nodes

    def get_adjacent_nodes(self, node):
        return self.adjacent_nodes[node]

    def shortest_paths(self, loc1, loc2):
        return [[1, 3, 4], [1, 2, 3, 4]];

    def get_self(self):
        return self.player

    def has_monster(self, location):
        if location in self.monsters:
            return True
        return False

    def get_monster(self, location):
        return self.monsters[location];

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

j = {}
with open('./Map.json', 'r') as f:
    j = json.loads(f.read())

nodes = [n['Number'] for n in j['Nodes']]
edges = [(e['Adjacents'][0], e['Adjacents'][1]) for e in j['Edges']]
adjacent_nodes = []
for n in nodes:
    adj = []
    for e in edges:
        if e[0] == n:
            adj.append(e[1])
        elif e[1] == n:
            adj.append(e[0])
    adjacent_nodes.append(adj)
monsters = {}
for m in j['Monsters']:
    md = m['Death Effects'];
    death_effects = MockDeathEffects(md['Speed'], md['Rock'], md['Paper'], md['Scissors'], md['Health'])
    monsters[m['Location']] = (MockEnemy(m['Health'], m['Attack'], m['Stance'], death_effects))

game = MockGame(nodes, adjacent_nodes, monsters)

best_hp = None
best_stats = None
best_stats_st = 0
best_spd = None
walks = generate_walks(game, 0, 4)
for walk in walks:

    ts = get_travel_stats(game, 0, walk)

    if best_hp is None or ts.stats.health > best_hp.stats.health:
        best_hp = ts

    st = ts.stats.rock + ts.stats.paper + ts.stats.scissors
    if best_stats is None or st > best_stats_st:
        best_stats = ts
        best_stats_st = st
    if best_spd is None or ts.stats.speed > best_spd.stats.speed:
        best_spd = ts

print(best_hp)
print()
print(best_stats)
print()
print(best_spd)
