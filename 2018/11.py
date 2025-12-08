from util import *
from functools import cache

gsn = int(D)


@cache
def power_level(x, y):
    rack_id = x + 10
    return int(f"{(rack_id * y + gsn) * rack_id:03}"[-3]) - 5


n = 300
g = {}
for i in range(n):
    for j in range(n):
        s = 0
        for k in range(3):
            for l in range(3):
                s += power_level(i + k, j + l)
        g[i, j] = s
print(max(g, key=lambda v: g[v]))

N = 301
best = 0
ans = 0, 0, 0

sat = defaultdict(int)
for x in range(1, N):
    for y in range(1, N):
        cid = x + 10
        p = int(f"{(cid * y + gsn) * cid:03}"[-3]) - 5
        sat[x, y] = sat[x - 1, y] - sat[x - 1, y - 1] + sat[x, y - 1] + p

for k in range(1, N):
    for x in range(k, N):
        for y in range(k, N):
            total = sat[x, y] - sat[x, y - k] - sat[x - k, y] + sat[x - k, y - k]
            if total > best:
                best = total
                ans = x - k + 1, y - k + 1, k
print(ans)
