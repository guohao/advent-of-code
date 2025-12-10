from collections import defaultdict
from itertools import product
import sys

L = sys.stdin.readlines()
R = len(L)
C = len(L[0].strip())

gd = defaultdict(list)
for i in range(R):
    for j in range(C):
        v = L[i][j]
        if v != ".":
            gd[v].append((i, j))
ans = set()
for v in gd.values():
    for a, b in product(v, repeat=2):
        if a == b:
            continue
        x = 2 * a[0] - b[0]
        y = 2 * a[1] - b[1]
        if 0 <= x < R and 0 <= y < C:
            ans.add((x, y))

print(len(ans))

ans = set()
for v in gd.values():
    for a, b in product(v, repeat=2):
        if a == b:
            continue
        x = 2 * a[0] - b[0]
        y = 2 * a[1] - b[1]
        ans.add(a)
        while 0 <= x < R and 0 <= y < C:
            ans.add((x, y))
            x += a[0] - b[0]
            y += a[1] - b[1]

print(len(ans))
