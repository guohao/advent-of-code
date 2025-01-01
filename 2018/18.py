from util import *

N = 10
G = {(i, j): c for i, line in enumerate(L) for j, c in enumerate(line.strip())}

X = max([x for x, _ in G.keys()]) + 1
Y = max([y for _, y in G.keys()]) + 1

for _ in range(N):
    ng = {}
    for i in range(X):
        for j in range(Y):
            c = Counter()
            for dx, dy in product(range(-1, 2), range(-1, 2)):
                k = i + dx, j + dy
                if k in G:
                    c[G[k]] += 1
            c[G[i, j]] -= 1

            match G[i, j]:
                case '.':
                    if c['|'] >= 3:
                        ng[i, j] = '|'
                case '|':
                    if c['#'] >= 3:
                        ng[i, j] = '#'
                case '#':
                    if not (c['#'] >= 1 and c['|'] >= 1):
                        ng[i, j] = '.'
                case _:
                    assert False
            if (i, j) not in ng:
                ng[i, j] = G[i, j]
    G = ng
print(sum(v == '|' for v in G.values()) * sum(v == '#' for v in G.values()))

N = 1000000000
G = {(i, j): c for i, line in enumerate(L) for j, c in enumerate(line.strip())}

X = max([x for x, _ in G.keys()]) + 1
Y = max([y for _, y in G.keys()]) + 1


def gen(g):
    ng = {}
    for i, j in g:
        c = Counter()
        for dx, dy in product(range(-1, 2), range(-1, 2)):
            k = i + dx, j + dy
            if k in g:
                c[g[k]] += 1
        c[g[i, j]] -= 1
        match g[i, j]:
            case '.':
                if c['|'] >= 3:
                    ng[i, j] = '|'
            case '|':
                if c['#'] >= 3:
                    ng[i, j] = '#'
            case '#':
                if not (c['#'] >= 1 and c['|'] >= 1):
                    ng[i, j] = '.'
        if (i, j) not in ng:
            ng[i, j] = g[i, j]
    return ng


t = 0
seen = {}
while t < N:
    key = tuple(G.values())
    if key in seen:
        t += (N - t) // (t - seen[key]) * (t - seen[key])
    else:
        seen[key] = t
    G = gen(G)
    t += 1

print(sum(v == '|' for v in G.values()) * sum(v == '#' for v in G.values()))
