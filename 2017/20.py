import sys
import re
from collections import defaultdict

NS = [list(map(int, re.findall(r"-?\d+", line))) for line in sys.stdin.readlines()]
R = len(NS)


def move(particle):
    p, v, a = particle[:3], particle[3:6], particle[6:]
    v = [v[j] + a[j] for j in range(3)]
    p = [p[j] + v[j] for j in range(3)]
    return p + v + a


particles = [move(p) for p in NS]
for _ in range(349):
    particles = [move(p) for p in particles]
print(min(range(R), key=lambda i: sum(map(abs, particles[i][:3]))))

particles = [p.copy() for p in NS]
for k in range(100):
    collisions = defaultdict(list)
    for ptc in particles:
        ptc = move(ptc)
        collisions[tuple(ptc[:3])].append(ptc)
    particles = [v[0] for v in collisions.values() if len(v) == 1]
print(len(particles))
