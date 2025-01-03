from util import *


def p1():
    data = D

    g = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            g[i, j] = c
    while True:
        gs = {}
        changed = False
        for i, j in g:
            gs[i, j] = g[i, j]
            if g[i, j] == '.':
                continue
            cnt = 0
            for di, dj in product(range(-1, 2), repeat=2):
                if di == dj == 0:
                    continue
                nb = i + di, j + dj
                if nb in g and g[nb] == '#':
                    cnt += 1
            if cnt == 0 and g[i, j] == 'L':
                changed = True
                gs[i, j] = '#'
            if cnt >= 4 and g[i, j] == '#':
                changed = True
                gs[i, j] = 'L'
        g = gs
        if not changed:
            print(sum(v == '#' for v in g.values()))
            return


def p2():
    data = D

    g = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            g[i, j] = c
    while True:
        gs = {}
        changed = False
        for i, j in g:
            gs[i, j] = g[i, j]
            if g[i, j] == '.':
                continue
            cnt = 0
            for di, dj in product(range(-1, 2), repeat=2):
                if di == dj == 0:
                    continue
                nb = i + di, j + dj
                while nb in g and g[nb] == '.':
                    nb = nb[0] + di, nb[1] + dj
                if nb in g and g[nb] == '#':
                    cnt += 1
            if cnt == 0 and g[i, j] == 'L':
                changed = True
                gs[i, j] = '#'
            if cnt >= 5 and g[i, j] == '#':
                changed = True
                gs[i, j] = 'L'
        g = gs
        if not changed:
            print(sum(v == '#' for v in g.values()))
            break


p1()
p2()
