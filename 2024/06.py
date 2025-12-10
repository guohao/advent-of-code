from collections import deque
import sys

L = sys.stdin.readlines()
IG = {(i, j): L[i][j] for i in range(len(L)) for j in range(len(L[i].strip()))}

g = IG
q = deque()
start = [k for k, v in g.items() if v == "^"][0]
q.append([start, (-1, 0)])
seen = set()
while q:
    (x, y), (dx, dy) = q.popleft()
    seen.add((x, y))
    nx, ny = x + dx, y + dy
    if (nx, ny) not in g:
        break
    if g[nx, ny] == "#":
        dx, dy = dy, -dx
        nx, ny = x + dx, y + dy
        if (nx, ny) not in g:
            break
        elif g[nx, ny] == "#":
            dx, dy = dy, -dx
            nx, ny = x + dx, y + dy
            if (nx, ny) not in g:
                break
    q.append(((nx, ny), (dx, dy)))
print(len(seen))

og = IG
t = 0
for k in og:
    if og[k] in "^#":
        continue
    g = og.copy()
    g[k] = "#"
    start = [k for k, v in g.items() if v == "^"][0]
    q = deque()
    q.append([start, (-1, 0)])
    seen = set()
    while q:
        (x, y), (dx, dy) = q.popleft()
        k = ((x, y), (dx, dy))
        if k in seen:
            t += 1
            break
        seen.add(k)
        nx, ny = x + dx, y + dy
        if (nx, ny) not in g:
            break
        if g[nx, ny] == "#":
            dx, dy = dy, -dx
            nx, ny = x + dx, y + dy
            if (nx, ny) not in g:
                break
            elif g[nx, ny] == "#":
                dx, dy = dy, -dx
                nx, ny = x + dx, y + dy
                if (nx, ny) not in g:
                    break
        q.append(((nx, ny), (dx, dy)))
print(t)
