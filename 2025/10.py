import sys
from z3 import *

def solve(l, part2=False):
    cells = l.split()
    btns = [list(map(int, x[1:-1].split(","))) for x in cells[1:-1]]
    o = Optimize()
    x = IntVector("x", len(btns))
    for xi in x:
        o.add(xi >= 0)
    if part2:
        jls = list(map(int, cells[-1][1:-1].split(",")))
        for i, s in enumerate(jls):
            o.add(Sum(x[j] for j, btn in enumerate(btns) if i in btn) == s)
    else:
        lts = cells[0][1:-1]
        for i, c in enumerate(lts):
            s = 1 if c == "#" else 0
            o.add(Sum(x[j] for j, btn in enumerate(btns) if i in btn) % 2 == s)
    o.minimize(Sum(x))
    return o.model().eval(Sum(x)).as_long() if o.check() == sat else 0

ls = sys.stdin.readlines()
print(sum(map(solve,ls)))
print(sum(solve(l, True) for l in ls))
