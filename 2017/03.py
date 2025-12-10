from itertools import count
import sys

goal = int(input().strip())


def nb9_v(p, g):
    return sum(
        g.get((i, j), 0)
        for i in range(p[0] - 1, p[0] + 2)
        for j in range(p[1] - 1, p[1] + 2)
        if (i, j) != p
    )


x = y = 0
dx, dy = 1, 0
g = {(0, 0): 1}
for i in range(goal - 1):
    x, y = x + dx, y + dy
    g[x, y] = nb9_v((x, y), g)
    lx, ly = x - dy, y + dx
    if (lx, ly) not in g:
        dx, dy = -dy, dx

print(abs(x) + abs(y))

g = {(0, 0): 1}
x = y = 0
dx, dy = 1, 0

for _ in count():
    x, y = x + dx, y + dy
    g[x, y] = nb9_v((x, y), g)
    if g[x, y] > goal:
        print(g[x, y])
        break
    lx, ly = x - dy, y + dx
    if (lx, ly) not in g:
        dx, dy = -dy, dx
