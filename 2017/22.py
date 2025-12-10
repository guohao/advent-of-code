import sys

import re

sys.path.insert(0, "..")
from util import *

x, y = R // 2, R // 2
dx, dy = -1, 0

ans = 0
for _ in range(10000):
    u = x, y
    s = IG.get(u, ".")
    if s == "#":
        dx, dy = dy, -dx
        IG[u] = "."
    else:
        dx, dy = -dy, dx
        IG[u] = "#"
        ans += 1
    x, y = x + dx, y + dy

print(ans)

nodes = {}
n = len(L)
for i in range(n):
    for j in range(n):
        nodes[i, j] = "infected" if L[i][j] == "#" else "clean"

x, y = n // 2, n // 2
dx, dy = -1, 0

ans = 0
for _ in range(10000000):
    u = x, y
    s = nodes.get(u, "clean")
    if s == "clean":
        dx, dy = -dy, dx
        nodes[u] = "weakened"
    elif s == "weakened":
        nodes[u] = "infected"
        ans += 1
    elif s == "infected":
        dx, dy = dy, -dx
        nodes[u] = "flagged"
    else:
        dx, dy = -dx, -dy
        nodes[u] = "clean"
    x, y = x + dx, y + dy

print(ans)
