from util import *

C4 = {(0, 0), (0, C - 1), (R - 1, 0), (R - 1, C - 1)}


def f(p2=None):
    g = IG.copy()
    if p2:
        for p in C4:
            g[p] = "#"
    for _ in range(100):
        ng = {}
        for p in g:
            if p2 and p in C4:
                ng[p] = "#"
                continue
            o = count_9(p, "#", g)
            if g[p] == "#":
                ng[p] = "#" if o in {2, 3} else "."
            else:
                ng[p] = "#" if o == 3 else "."
        g = ng
    print(Counter(g.values())["#"])


f()
f(True)
