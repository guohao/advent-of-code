import operator
from functools import reduce

from util import *


def move(particle):
    p, v, a = particle[:3], particle[3:6], particle[6:]
    v = [v[j] + a[j] for j in range(3)]
    p = [p[j] + v[j] for j in range(3)]
    return p + v + a


particles = NS.copy()
collisions = defaultdict(list)
for _ in range(350):
    particles = map(move, particles)
print(min(zip(range(R), particles), key=lambda x: sum(map(abs, x[1][:3])))[0])

ans = 0
particles = NS.copy()
for k in range(100):
    nps = []
    collisions = defaultdict(list)
    for ptc in particles:
        ptc = move(ptc)
        collisions[tuple(ptc[:3])].append(ptc)
    particles = reduce(
        operator.add, [v for v in collisions.values() if len(v) == 1], []
    )
    ans = len(particles)
print(ans)
