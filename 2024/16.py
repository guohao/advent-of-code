import heapq
import math
import sys

L = sys.stdin.readlines()
IG = {(i, j): L[i][j] for i in range(len(L)) for j in range(len(L[i].strip()))}

g = IG

start = next(x for x in g if g[x] == "S")
target = next(x for x in g if g[x] == "E")
tv = [(0, start, (0, 1))]
SEEN = set()
while tv:
    s, p, d = heapq.heappop(tv)
    if g.get(p, "#") == "#":
        continue
    if (p, d) in SEEN:
        continue
    SEEN.add((p, d))
    if p == target:
        print(s)
        break
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        sa = 1 if (dx, dy) == d else 1001
        heapq.heappush(tv, (s + sa, (dx + x, dy + y), (dx, dy)))

start = next(x for x in g if g[x] == "S")
target = next(x for x in g if g[x] == "E")
tv = [(0, [start], (0, 1))]
SEEN = {}
best = math.inf
ans = set()
while tv:
    s, path, d = heapq.heappop(tv)
    if s > best:
        continue
    p = path[-1]
    if g.get(p, "#") == "#":
        continue
    if (p, d) in SEEN and SEEN[p, d] < s:
        continue
    SEEN[p, d] = s
    if p == target:
        best = min(best, s)
        if best == s:
            ans |= set(path)
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        sa = 1 if (dx, dy) == d else 1001
        np = path + [(dx + x, dy + y)]
        heapq.heappush(tv, (s + sa, np, (dx, dy)))

print(len(ans))
