from util import *

g = [0] * 1000

for line in L:
    xs, ys, xe, ye = ints(line)
    v = int('1' * (xe - xs + 1), 2) << xs
    if 'turn on' in line:
        f = lambda x: x | v
    elif 'turn off' in line:
        f = lambda x: ~(~x | v)
    else:
        f = lambda x: x ^ v
    for i in range(ys, ye + 1):
        g[i] = f(g[i])

print(sum(x.bit_count() for x in g))

g = defaultdict(int)
for line in L:
    xs, ys, xe, ye = ints(line)
    for i in range(xs, xe + 1):
        for j in range(ys, ye + 1):
            if 'turn on' in line:
                g[i, j] += 1
            elif 'turn off' in line:
                g[i, j] = max(0, g[i, j] - 1)
            elif 'toggle' in line:
                g[i, j] += 2

print(sum(g.values()))
