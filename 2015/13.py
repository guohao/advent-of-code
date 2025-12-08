import sys
from itertools import permutations
from collections import defaultdict

ls = sys.stdin.readlines()
g = defaultdict(int)
ps = set()
for l in ls:
    cells = l.split()
    a, b = cells[0], cells[-1][:-1]
    v = int(cells[3])
    if "lose" in l:
        v = -v
    g[a, b] = v
    ps.add(a)


def neighbors(lst, i):
    n = len(lst)
    return lst[i - 1], lst[(i + 1) % n]


def run():
    r1 = 0
    for p in permutations(ps):
        adder = 0
        for i in range(len(p)):
            adder += sum(g[p[i], x] for x in neighbors(p, i))
        r1 = max(adder, r1)
    print(r1)


run()
ps.add("me")
run()
