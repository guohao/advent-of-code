import sys


def nb4(p):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yield p[0] + i, p[1] + j


import re


def nb4(p):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yield p[0] + i, p[1] + j


sys.setrecursionlimit(10000000)

L = sys.stdin.readlines()
IG = {(i, j): c for i, line in enumerate(L) for j, c in enumerate(line.strip())}
DIRECTIONS = {
    ">": [(0, 1)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    "^": [(-1, 0)],
    ".": [(0, 1), (1, 0), (0, -1), (-1, 0)],
}
ls = L
g = IG

start = (0, [c for _, c in g if g[0, c] == "."][0])
R = len(ls)
goal = (R - 1, [c for _, c in g if g[R - 1, c] == "."][0])

seen = set()


def dfs(p):
    if p == goal:
        return 0
    seen.add(p)
    path_len = 0
    for dr, dc in DIRECTIONS[g[p]]:
        nb = dr + p[0], dc + p[1]
        if nb in g and g[nb] != "#" and nb not in seen:
            path_len = max(1 + dfs(nb), path_len)
    seen.remove(p)
    return path_len


print(dfs(start))
g = {k for k, v in g.items() if v != "#"}
start = (0, [c for _, c in g if (0, c) in g][0])
R = len(ls)
goal = (R - 1, [c for _, c in g if (R - 1, c) in g][0])


def nb4(_x, _y):
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        yield _x + dx, _y + dy


seen = set()
adj = {p: {q: 1 for q in nb4(*p) if q in g} for p in g}
while True:
    for p, qs in adj.items():
        if len(qs) != 2:
            continue
        q1, q2 = qs
        adj[q1][q2] = adj[p][q1] + adj[p][q2]
        adj[q2][q1] = adj[p][q1] + adj[p][q2]
        del adj[p], adj[q1][p], adj[q2][p]
        break
    else:
        break


def dfs2(p):
    if p == goal:
        return 0
    seen.add(p)
    ans = float("-inf")
    for nb, d in adj[p].items():
        if nb in seen:
            continue
        ans = max(d + dfs2(nb), ans)
    seen.remove(p)
    return ans


print(dfs2(start))
