import sys
from itertools import cycle

lines = sys.stdin.readlines()
nodes = {}
carts = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        nodes[i, j] = lines[i][j]

for n in nodes:
    if nodes[n] not in 'v><^':
        continue
    s2d = {'>': (0, 1),
           '<': (0, -1),
           '^': (-1, 0),
           'v': (1, 0)}
    c = cycle([lambda dx, dy: (-dy, dx), lambda dx, dy: (dx, dy), lambda dx, dy: (dy, -dx)])
    carts[n] = (s2d[nodes[n]], c)
while True:
    n_carts = {}
    for x, y in sorted(carts):
        d, c = carts[x, y]
        del carts[x, y]
        if nodes[x, y] == '+':
            d = next(c)(*d)
        elif nodes[x, y] == '\\':
            d = (d[1], d[0])
        elif nodes[x, y] == '/':
            d = (-d[1], -d[0])
        nx, ny = d[0] + x, d[1] + y
        if (nx, ny) in n_carts or (nx, ny) in carts:
            print(ny, nx)
            exit()
        else:
            n_carts[nx, ny] = d, c
    carts = n_carts
