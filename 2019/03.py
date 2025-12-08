from util import *

D = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}


def visited(cmds):
    seen = set()
    p = 0, 0
    for cmd in cmds.split(","):
        n = int(cmd[1:])
        d = D[cmd[0]]
        for _ in range(n):
            p = p[0] + d[0], p[1] + d[1]
            seen.add(p)
    return seen


sa, sb = map(visited, L)

print(min(sum(map(abs, x)) for x in sa if x in sb))


def visited2(cmds):
    seen = {}
    p = 0, 0
    s = 0
    for cmd in cmds.split(","):
        n = int(cmd[1:])
        d = D[cmd[0]]
        for _ in range(n):
            p = p[0] + d[0], p[1] + d[1]
            s += 1
            if p not in seen:
                seen[p] = s
    return seen


sa, sb = map(visited2, L)

print(min(sa[x] + sb[x] for x in sa if x in sb))
