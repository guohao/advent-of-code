from collections import defaultdict
import math
import re
import sys

import functools

sys.path.insert(0, "..")
from util import *

D = {}
for i, line in enumerate(L):
    cells = line.split()
    r = list(map(int, re.findall(r"-?\d+", line)))[0]
    c, ov = cells[1], cells[9:]
    ov = [x.replace(",", "") for x in ov]
    D[c] = (r, ov)


@functools.cache
def dfs(current, ov: str, time_left) -> int:
    if time_left == 1:
        return 0
    time_left = time_left - 1
    if current in ov or D[current][0] == 0:
        return max(dfs(c, ov, time_left) for c in D[current][1])
    else:
        return time_left * D[current][0] + dfs(current, ov + "," + current, time_left)


ret = dfs("AA", "", 30)
print(ret)

valves = {}
dist = defaultdict(lambda: defaultdict(lambda: math.inf))
for i, line in enumerate(L):
    cells = line.split()
    r = list(map(int, re.findall(r"-?\d+", line)))[0]
    c, ov = cells[1], cells[9:]
    valves[c] = r
    for j in [x.replace(",", "") for x in ov]:
        dist[c][j] = 1

for k in valves:
    for i in valves:
        for j in valves:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


@functools.cache
def dfs2(v: str, closed: frozenset, t, isE) -> int:
    if t <= 1:
        return 0
    if len(closed) == 0:
        return 0
    # elephant helps
    ret = dfs2("AA", closed, 26, False) if isE else 0
    for c in closed:
        if (nt := t - dist[v][c] - 1) >= 0:
            ret = max(ret, valves[c] * nt + dfs2(c, closed - {c}, nt, isE))
    return ret


print(dfs2("AA", frozenset(v[0] for v in valves.items() if v[1] != 0), 26, True))
