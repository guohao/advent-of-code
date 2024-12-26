from util import *

g = Graph2D(rows=1000, cols=1000, default_val=0)

for line in lines():
    xs, ys, xe, ye = map(int, re.findall(r'\d+', line))
    for i in range(xs, xe + 1):
        for j in range(ys, ye + 1):
            if 'turn on' in line:
                g[i, j] = 1
            elif 'turn off' in line:
                g[i, j] = 0
            elif 'toggle' in line:
                g[i, j] ^= 1

print(sum(g.values()))

g = Graph2D(rows=1000, cols=1000, default_val=0)

for line in lines():
    xs, ys, xe, ye = map(int, re.findall(r'\d+', line))
    for i in range(xs, xe + 1):
        for j in range(ys, ye + 1):
            if 'turn on' in line:
                g[i, j] += 1
            elif 'turn off' in line:
                g[i, j] = max(0, g[i, j] - 1)
            elif 'toggle' in line:
                g[i, j] += 2

print(sum(g.values()))
