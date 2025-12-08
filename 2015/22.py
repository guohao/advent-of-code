import sys
import re
import math
from itertools import product
import heapq
spells = [
    (53, 4, 0, 0, 0, 0),
    (73, 2, 2, 0, 0, 0),
    (113, 0, 0, 7, 0, 6),
    (173, 3, 0, 0, 0, 6),
    (229, 0, 0, 0, 101, 5),
]

boss_hp, boss_damage = list(map(int,re.findall(r'-?\d+',sys.stdin.read())))

def fight(p2=None):
    b_hp, b_damage = boss_hp,boss_damage
    heap = [(0, 50, 500, (), b_hp, False)]
    while heap:
        cost, hp, mana, effects, b_hp, boss_turn = heapq.heappop(heap)
        if p2 and not boss_turn:
            hp -= 1
        if hp <= 0:
            continue
        armor = 0
        n_effects = []
        for i, heal, add_mana, damage, add_armor, lasts in effects:
            hp += heal
            mana += add_mana
            armor += add_armor
            b_hp -= damage
            if lasts > 1:
                n_effects.append((i, heal, add_mana, damage, add_armor, lasts - 1))
        effects = n_effects
        if b_hp <= 0:
            print(cost)
            break
        if boss_turn:
            heapq.heappush(
                heap,
                (cost, hp - b_damage + armor, mana, tuple(effects), b_hp, False),
            )
        else:
            for j, (cost_mana, damage, heal, add_armor, add_mana, lasts) in enumerate(
                spells
            ):
                if j in {e[0] for e in effects}:
                    continue
                if cost_mana > mana:
                    continue
                new_effects = effects.copy()
                if lasts == 0:
                    new_b_hp = b_hp - damage
                    new_player_hp = hp + heal
                else:
                    new_player_hp = hp
                    new_b_hp = b_hp
                    new_effects += ((j, heal, add_mana, damage, add_armor, lasts),)
                ps = (cost + cost_mana, new_player_hp, mana - cost_mana, new_effects)
                heapq.heappush(heap, (*ps, new_b_hp, True))


fight()
fight(1)
