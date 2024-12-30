from util import *

goal = I[0]
x = y = 0
dx, dy = 1, 0
g = {(0, 0): 1}
for i in range(goal - 1):
    x, y = x + dx, y + dy
    g[x, y] = sum(nb9_v((x, y), g))
    lx, ly = x - dy, y + dx
    if (lx, ly) not in g:
        dx, dy = -dy, dx

print(abs(x) + abs(y))

g = {(0, 0): 1}
x, y = 0, 0
dx, dy = 1, 0

for _ in count():
    x, y = x + dx, y + dy
    g[x, y] = sum(nb9_v((x, y), g))
    if g[x, y] > goal:
        print(g[x, y])
        break
    lx, ly = x - dy, y + dx
    if (lx, ly) not in g:
        dx, dy = -dy, dx
