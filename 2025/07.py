import sys
from functools import cache

g = {}
s = (0, 0)
for i, l in enumerate(sys.stdin.readlines()):
    for j, c in enumerate(l.strip()):
        g[i, j] = c
        if c == "S":
            s = i, j


@cache
def downward(p):
    np = p[0] + 1, p[1]
    if np not in g:
        return set()
    r = set()
    if g[np] == "^":
        r |= downward((np[0] + 1, np[1] - 1))
        r |= downward((np[0] + 1, np[1] + 1))
        r.add(np)
    else:
        r = downward(np)
    return r


@cache
def downward2(p):
    if p not in g:
        return 0
    r = 0
    if g[p] == "^":
        r += downward2((p[0] + 1, p[1] - 1))
        r += downward2((p[0] + 1, p[1] + 1))
    else:
        r = max(1, downward2((p[0] + 1, p[1])))
    return r


print(len(downward(s)))
print(downward2(s))
