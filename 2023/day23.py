import sys
from collections import defaultdict

from helper import *
from heapq import *

sys.setrecursionlimit(1000000)

data = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""
# data = raw_data(2023, 23)
lines = lines(data)
start = (0, lines[0].index('.'))
goal = (len(lines) - 1, lines[-1].index('.'))
g = {(i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}


def neighbors(p, ignore_direction=False):
    if g[p] == '#':
        return
    if g[p] == '.' or ignore_direction:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = p[0] + dx, p[1] + dy
            np = (nx, ny)
            if np in g and g[np] != '#':
                yield np
    else:
        dx, dy = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[g[p]]
        nx, ny = p[0] + dx, p[1] + dy
        np = (nx, ny)
        if np in g and g[np] != '#':
            yield np


def transitive_closure(ignore_direction=False):
    adjacency = defaultdict(set)
    weight = defaultdict(int)
    for p in g:
        for neighbor in neighbors(p, ignore_direction):
            adjacency[p].add(neighbor)
            weight[p, neighbor] = 1
    while True:
        changed = False
        for v, e in adjacency.copy().items():
            if len(e) == 2:
                changed = True
                a, b = e
                adjacency[a].add(b)
                adjacency[b].add(a)
                weight[a, b] = weight[a, v] + weight[v, b]
                del adjacency[v]
        if not changed:
            break
    return adjacency, weight


def dfs(p, path, ignore_direction=False):
    if p not in g:
        return 0
    if p == goal:
        return len(path)
    if g[p] == '#':
        return 0
    if p in path:
        return 0

    path = path.union({p})
    ret = 0
    for neighbor in neighbors(p, ignore_direction):
        ret = max(ret, dfs(neighbor, path, ignore_direction))
    return ret


# def solve(ignore_direction=False):


# transitive_closure()
print(dfs(start, set()))
# print(dfs(start, set(), True))
