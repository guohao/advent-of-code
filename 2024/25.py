import sys

sys.path.insert(0, "..")
from util import *

ls = []
ks = []
for p in PS:
    lines = [l.strip() for l in p.splitlines()]
    g = {(i, j): c for i, line in enumerate(lines) for j, c in enumerate(line)}
    hs = []
    if p[0] == "#":
        for j in range(len(lines[0])):
            for i in range(len(lines)):
                if g[i, j] != "#":
                    hs.append(i - 1)
                    break

        ls.append((hs, len(lines) - 1))
    else:
        for j in range(len(lines[0])):
            for i in range(len(lines)):
                if g[i, j] != ".":
                    hs.append(len(lines) - i - 1)
                    break
        ks.append((hs, len(lines) - 1))

t = 0
for l, h0 in ls:
    for k, h1 in ks:
        if len(k) != len(l):
            continue
        s = max(k[i] + l[i] for i in range(len(k)))
        if s < h0 and s < h1:
            t += 1
print(t)
