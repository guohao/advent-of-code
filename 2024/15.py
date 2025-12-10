from collections import defaultdict
import sys

sys.path.insert(0, "..")
from util import *


def move(p, d):
    _arrow_dirs = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    LDRU_DIRS = {"L": (0, -1), "D": (1, 0), "R": (0, 1), "U": (-1, 0)}
    if d in _arrow_dirs:
        return tuple_add(p, _arrow_dirs[d])
    elif d in LDRU_DIRS:
        return tuple_add(p, LDRU_DIRS[d])


import re


def tuple_add(_a, _b) -> tuple[int, ...]:
    """Adds two tuples of the same length"""
    assert len(_a) == len(_b)
    return tuple(_a[i] + _b[i] for i in range(len(_a)))


_arrow_dirs = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
LDRU_DIRS = {"L": (0, -1), "D": (1, 0), "R": (0, 1), "U": (-1, 0)}


def move(p, d):
    if d in _arrow_dirs:
        return tuple_add(p, _arrow_dirs[d])
    elif d in LDRU_DIRS:
        return tuple_add(p, LDRU_DIRS[d])


g = defaultdict(lambda: "#") | {
    (i, j): c for i, line in enumerate(PS[0].splitlines()) for j, c in enumerate(line)
}
x, y = next(n for n in g if g[n] == "@")
for d in PS[1].replace("\n", ""):
    assert g[x, y] == "@"
    dx, dy = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}[d]
    nx, ny = x + dx, y + dy
    while g[nx, ny] == "O":
        nx, ny = nx + dx, ny + dy
    if g[nx, ny] == ".":
        while (nx, ny) != (x, y):
            g[nx, ny] = g[nx - dx, ny - dy]
            nx, ny = nx - dx, ny - dy
        g[x, y] = "."
        x, y = x + dx, y + dy
print(sum(p[0] * 100 + p[1] for p in g if g[p] == "O"))

PS[0] = (
    PS[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
)

g = defaultdict(lambda: "#") | {
    (i, j): c for i, line in enumerate(PS[0].splitlines()) for j, c in enumerate(line)
}
x, y = next(n for n in g if g[n] == "@")


def can_move(_x, _y, _dx, _dy):
    target = _x + _dx, _y + _dy
    if g[target] == ".":
        return True
    if g[target] == "#":
        return False
    if _dx == 0:
        return can_move(*target, _dx, _dy)
    else:
        lr = -1 if g[target] == "]" else 1
        return can_move(*target, _dx, _dy) and can_move(
            target[0], target[1] + lr, _dx, _dy
        )


def move(_x, _y, _dx, _dy):
    target = _x + _dx, _y + _dy
    if g[target] != ".":
        if _dx == 0:
            move(*target, _dx, _dy)
        else:
            if g[target] in "[]":
                lr = -1 if g[target] == "]" else 1
                move(_x + _dx, _y + dy + lr, _dx, _dy)
                move(_x + _dx, _y + dy, _dx, _dy)
    g[target] = g[_x, _y]
    g[_x, _y] = "."


for d in PS[1].replace("\n", ""):
    assert g[x, y] == "@"
    dx, dy = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}[d]
    nx, ny = x + dx, y + dy
    if can_move(x, y, dx, dy):
        move(x, y, dx, dy)
        x, y = nx, ny
print(sum(p[0] * 100 + p[1] for p in g if g[p] == "["))
