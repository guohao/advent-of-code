from util import *

R = 6
C = 50
g = [["."] * C for _ in range(R)]
for line in L:
    pos, offset = ints(line)
    if "rect" in line:
        for i, j in product(range(offset), range(pos)):
            g[i][j] = "#"
    elif "row" in line:
        pos %= R
        g[pos] = g[pos][-offset:] + g[pos][:-offset]
    elif "column" in line:
        pos %= C
        col = [g[i][pos] for i in range(R)]
        col = col[-offset:] + col[:-offset]
        for i in range(R):
            g[i][pos] = col[i]

print(sum(a.count("#") for a in g))

for i in range(R):
    print("".join(g[i][j] for j in range(C)))
