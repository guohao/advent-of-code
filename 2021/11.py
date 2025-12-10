from itertools import count, product
import sys

L = sys.stdin.readlines()
g = {(i, j): int(c) for i, line in enumerate(L) for j, c in enumerate(line.strip())}
ans = 0
for _ in range(100):
    flashed = set()
    g = {k: v + 1 for k, v in g.items()}
    while any(v > 9 and k not in flashed for k, v in g.items()):
        for x, y in g:
            if g[x, y] > 9 and (x, y) not in flashed:
                for dx, dy in product(range(-1, 2), repeat=2):
                    if dx == dy == 0:
                        continue
                    nb = x + dx, y + dy
                    if nb in g:
                        g[nb] += 1
                flashed.add((x, y))
    for n in flashed:
        g[n] = 0
    ans += len(flashed)
print(ans)

g = {(i, j): int(c) for i, line in enumerate(L) for j, c in enumerate(line.strip())}
ans = 0
for t in count(1):
    flashed = set()
    g = {k: v + 1 for k, v in g.items()}
    while any(v > 9 and k not in flashed for k, v in g.items()):
        for n in g:
            x, y = n
            if g[n] > 9 and n not in flashed:
                for dx, dy in product(range(-1, 2), repeat=2):
                    if dx == dy == 0:
                        continue
                    nb = x + dx, y + dy
                    if nb in g:
                        g[nb] += 1
                flashed.add(n)
    for n in flashed:
        g[n] = 0
    if len(flashed) == len(g):
        print(t)
        break
