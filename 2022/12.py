from util import *


def f(p2=None):
    data = D
    q = deque()
    g = {}
    start = 0, 0
    goal = 0, 0
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line.strip()):
            if c == 'E':
                if p2:
                    start = i,j
                else:
                    goal = i, j
                c = 'z'
            if c == 'S':
                if not p2:
                    start = i, j
                c = 'a'
            g[i, j] = ord(c)
    q.append((start, 0))
    visited = set()
    while q:
        (x, y), s = q.popleft()
        if p2:
            if g[x, y] == ord('a'):
                print(s)
                return
        else:
            if (x, y) == goal:
                print(s)
                return
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nb in nb4((x, y)):
            if nb not in g:
                continue
            if p2:
                if g[nb] - g[x, y] >= -1:
                    q.append((nb, s + 1))
            else:
                if g[nb] - g[x, y] <= 1:
                    q.append((nb, s + 1))


f()
f(1)
