from itertools import count
import math
import sys
import re

L = sys.stdin.readlines()
NS = [list(map(int, re.findall(r"-?\d+", line))) for line in L]

X = 101
Y = 103
rs = []
for ns in NS:
    p0, p1, v0, v1 = ns
    rs.append(((p0, p1), (v0, v1)))

for _ in range(100):
    ns = []
    for (x, y), (dx, dy) in rs:
        nx = (x + dx) % X
        ny = (y + dy) % Y
        ns.append(((nx, ny), (dx, dy)))
    rs = ns

ans = [0] * 4
MX = X // 2
MY = Y // 2
for (x, y), _ in rs:
    if x > MX and y > MY:
        ans[0] += 1
    elif x > MX and y < MY:
        ans[1] += 1
    elif x < MX and y > MY:
        ans[2] += 1
    elif x < MX and y < MY:
        ans[3] += 1

print(math.prod(ans))

for t in count(101):
    ns = []
    for (x, y), (dx, dy) in rs:
        nx = (x + dx) % X
        ny = (y + dy) % Y
        ns.append(((nx, ny), (dx, dy)))
    rs = ns
    g = set(r for r, v in rs)
    for j in range(Y):
        line = ""
        for i in range(X):
            if (i, j) in g:
                line += "#"
            else:
                line += "."
        if "#########" in line:
            print(t)
            exit()
