import sys
import re
from itertools import combinations, product, permutations, chain
from collections import deque, defaultdict
from functools import cache
import heapq
import math

g = []
for l in sys.stdin.readlines():
    x, y = map(int, l.strip().split(","))
    g.append((x, y))

h_edges = []
v_edges = []
for i in range(len(g)):
    a = g[i - 1]
    b = g[i]
    a, b = sorted([a, b])
    if a[0] == b[0]:
        v_edges.append((a, b))
    else:
        h_edges.append((a, b))
g = set(g)


def p_in(x, y):
    if (x, y) in g:
        return True
    udlr = set()
    for (x0, hy), (x1, _) in h_edges:
        if x0 <= x <= x1:
            if y == hy:
                return True
            elif y < hy:
                udlr.add("U")
            else:
                udlr.add("D")
    for (vx, y0), (_, y1) in v_edges:
        if y0 <= y <= y1:
            if x == vx:
                return True
            elif x < vx:
                udlr.add("L")
            else:
                udlr.add("R")
    return len(udlr) == 4


def line_in(x, y1, y2):
    y1, y2 = sorted([y1, y2])
    for (x0, y), (x1, _) in h_edges:
        if x0 < x < x1 and y1 < y < y2:
            return False
    return True


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


print(max(area(a,b) for a, b in combinations(g, 2)))

r2 = 0
for a, b in combinations(g, 2):
    (ax, ay), (bx, by) = sorted([a, b])
    cx, cy = ax, by
    dx, dy = bx, ay
    if p_in(cx, cy) and p_in(dx, dy):
        if line_in(ax, ay, by):
            r2 = max(area(a, b), r2)
print(r2)
