import sys
import re
from itertools import combinations, product, permutations
from collections import deque, defaultdict
import heapq
import math


def turn(d, udlr):
    dx, dy = d
    match udlr:
        case "R":
            dx, dy = dy, -dx
        case "L":
            dx, dy = -dy, dx
    return dx, dy


r2 = None
x = y = 0
d = (1, 0)
visited = {(x, y)}
for step in input().strip().split(", "):
    d = turn(d, step[0])
    moves = int(step[1:])
    for i in range(moves):
        x += d[0]
        y += d[1]
        if (x, y) in visited:
            if not r2:
                r2 = abs(x) + abs(y)
        visited.add((x, y))
print(abs(x) + abs(y))
print(r2)
