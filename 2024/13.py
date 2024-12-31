from util import *

from z3 import *


def run(p2=None):
    t = 0
    for p in PS:
        a, b, c = p.splitlines()
        ax, ay = list(map(int, re.findall(r'-?\d+', a)))
        bx, by = list(map(int, re.findall(r'-?\d+', b)))
        tx, ty = list(map(int, re.findall(r'-?\d+', c)))
        if p2:
            tx += 10000000000000
            ty += 10000000000000
        s = Optimize()
        pa = Int("pa")
        pb = Int("pb")
        mv = Int("sum")
        s.add(tx == ax * pa + bx * pb)
        s.add(ty == ay * pa + by * pb)
        s.add(mv == pa * 3 + pb)
        h = s.minimize(mv)
        s.check()
        g = s.lower(h)
        if hasattr(g, 'as_long'):
            t += g.as_long()

    print(t)


run()
run(1)
