from util import *

g = {k: int(v) for k, v in IG.items()}
hp = [(0, (1, 0), (1, 0), 1), (0, (0, 1), (0, 1), 1)]
seen = set()
target = max(g)
while hp:
    cost, (x, y), (dx, dy), moved = heapq.heappop(hp)
    if moved == 4:
        continue
    if (x, y) not in g:
        continue
    cost += g[x, y]
    k = ((x, y), (dx, dy), moved)
    if k in seen:
        continue
    seen.add(k)
    if (x, y) == target:
        print(cost)
        break
    for nx, ny in [(-dy, dx), (dy, -dx), (dx, dy)]:
        n_move = 1 if (nx, ny) != (dx, dy) else (moved + 1)
        heapq.heappush(hp, (cost, (x + nx, y + ny), (nx, ny), n_move))

hp = [(0, (1, 0), (1, 0), 1), (0, (0, 1), (0, 1), 1)]
seen = set()
target = max(g)
while hp:
    cost, (x, y), (dx, dy), moved = heapq.heappop(hp)
    if moved == 11:
        continue
    if (x, y) not in g:
        continue
    cost += g[x, y]
    k = ((x, y), (dx, dy), moved)
    if k in seen:
        continue
    seen.add(k)
    if (x, y) == target:
        print(cost)
        break
    if moved < 4:
        heapq.heappush(hp, (cost, (x + dx, y + dy), (dx, dy), moved + 1))
    else:
        for nx, ny in [(-dy, dx), (dy, -dx), (dx, dy)]:
            n_move = 1 if (nx, ny) != (dx, dy) else (moved + 1)
            heapq.heappush(hp, (cost, (x + nx, y + ny), (nx, ny), n_move))
