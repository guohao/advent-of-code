import functools
import math
import re
import sys
from collections import defaultdict

valves = {}
dist = defaultdict(lambda: defaultdict(lambda: math.inf))
for i, line in enumerate(sys.stdin.readlines()):
    cells = line.split()
    r = list(map(int, re.findall(r'-?\d+', line)))[0]
    c, ov = cells[1],cells[9:]
    valves[c] = r
    for j in [x.replace(',', '') for x in ov]:
        dist[c][j] = 1

for k in valves:
    for i in valves:
        for j in valves:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


@functools.cache
def dfs(v: str, closed: frozenset, t, isE) -> int:
    if t <= 1:
        return 0
    if len(closed) == 0:
        return 0
    # elephant helps
    ret = dfs('AA', closed, 26, False) if isE else 0
    for c in closed:
        if (nt := t - dist[v][c] - 1) >= 0:
            ret = max(ret, valves[c] * nt + dfs(c, closed - {c}, nt, isE))
    return ret


print(dfs('AA', frozenset(v[0] for v in valves.items() if v[1] != 0), 26, True))
