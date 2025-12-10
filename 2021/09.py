import math
import sys

import re

g = {(i, j): int(c) for i, line in enumerate(L) for j, c in enumerate(line)}
ans = 0
for x, y in g:
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nb = x + dx, y + dy
        if nb in g and g[nb] <= g[x, y]:
            break
    else:
        ans += g[x, y] + 1
print(ans)

mx = max(x for x, _ in g)
my = max(y for _, y in g)
seen = set()
basins = []


def bfs(x, y):
    if (x, y) not in g:
        return
    if (x, y) in seen:
        return
    if g[x, y] == 9:
        return
    seen.add((x, y))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        bfs(x + dx, y + dy)


for i in range(mx + 1):
    for j in range(my + 1):
        pre_size = len(seen)
        bfs(i, j)
        basins.append(len(seen) - pre_size)

print(math.prod(sorted(basins)[-3:]))
