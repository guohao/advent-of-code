from collections import defaultdict
import math
import sys

L = sys.stdin.readlines()
IG = {(i, j): L[i][j] for i in range(len(L)) for j in range(len(L[i].strip()))}


def nb4(p):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yield p[0] + i, p[1] + j


g = defaultdict(str) | IG
seen = set()


def dfs(curr):
    if curr in seen:
        return 0, 0
    seen.add(curr)
    a, p = 1, 0
    for nb in nb4(curr):
        if g[nb] == g[curr]:
            a0, p0 = dfs(nb)
            a += a0
            p += p0
        else:
            p += 1
    return a, p


print(sum(math.prod(dfs(k)) for k in list(g.keys())))

seen.clear()

inner = defaultdict(set)
outer = defaultdict(set)


def dfs2(frm, curr):
    if curr in seen:
        return
    seen.add(curr)
    inner[frm].add(curr)
    for nb in nb4(curr):
        if nb in g:
            if g[nb] == g[curr]:
                dfs2(frm, nb)
            else:
                outer[frm].add(nb)


for k in g:
    dfs2(k, k)

t = 0
for k in g:
    c = 0
    for x, y in inner[k]:
        for c0, c1 in [
            [(-1, 0), (0, -1)],
            [(1, 0), (0, 1)],
            [(-1, 0), (0, 1)],
            [(1, 0), (0, -1)],
        ]:
            if (x + c0[0], y + c0[1]) in outer[k] and (x + c1[0], y + c1[1]) in outer[
                k
            ]:
                c += 1
            elif (
                (x + c0[0], y + c0[1]) in inner[k]
                and (x + c1[0], y + c1[1]) in inner[k]
                and (x + c0[0] + c1[0], y + c0[1] + c1[1]) in outer[k]
            ):
                c += 1
    t += len(inner[k]) * c

print(t)
