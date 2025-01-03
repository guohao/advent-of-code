from util import *


def f(p2=None):
    lines = L
    grid = set()
    for line in lines:
        parts = line.split(' -> ')
        for i in range(1, len(parts)):
            xs, ys = (int(x) for x in parts[i - 1].split(','))
            xe, ye = (int(x) for x in parts[i].split(','))
            for x in range(min(xs, xe), max(xe, xs) + 1):
                for y in range(min(ys, ye), max(ys, ye) + 1):
                    grid.add((x, y))
    y_abyss = max(y for x, y in grid)
    if p2:
        y_abyss += 2

    ss = len(grid)

    def dfs(x, y, grid):
        point = (x, y)
        if p2:
            if y == y_abyss - 1:
                grid.add(point)
                return
        else:
            if y == y_abyss:
                return
        if point in grid:
            return
        dfs(x, y + 1, grid)
        if (x, y + 1) not in grid:
            return
        dfs(x - 1, y + 1, grid)
        if (x - 1, y + 1) not in grid:
            return
        dfs(x + 1, y + 1, grid)
        if (x + 1, y + 1) not in grid:
            return
        grid.add(point)

    dfs(500, 0, grid)
    print(len(grid) - ss)


f()
f(1)
