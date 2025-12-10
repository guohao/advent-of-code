from itertools import count
import sys


def nb9_v(p, _g=None):
    if _g is None:
        _g = IG
    return list(map(_g.get, nb9(p, _g)))


import re


def nb9(p, _g=None):
    if _g is None:
        _g = IG
    for i in range(p[0] - 1, p[0] + 2):
        for j in range(p[1] - 1, p[1] + 2):
            if (i, j) != p and (i, j) in _g:
                yield i, j


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
