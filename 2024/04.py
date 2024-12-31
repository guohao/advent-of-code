from util import *

t = 0
for i, j in product(range(R), range(C)):
    for dx, dy in product(range(-1, 2), repeat=2):
        t += 'XMAS' == ''.join(IG.get((i + k * dx, j + k * dy), '.') for k in range(4))
print(t)

t = 0
for i, j in product(range(R), range(C)):
    if IG[i, j] != 'A':
        continue
    nbs = {(a, b): IG.get((i + a, j + b), '') for a, b in [(-1, -1), (-1, 1), (1, 1), (1, -1)]}
    c = Counter(nbs.values())
    if c['S'] == c['M'] == 2 and nbs[-1, -1] != nbs[1, 1]:
        t += 1
print(t)
