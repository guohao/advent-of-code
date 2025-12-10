import itertools
import re
import sys
from itertools import product

sys.path.insert(0, "..")
from util import *


def tuple_add(_a, _b) -> tuple[int, ...]:
    """Adds two tuples of the same length"""
    assert len(_a) == len(_b)
    return tuple(_a[i] + _b[i] for i in range(len(_a)))


def move(p, d):
    _arrow_dirs = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    LDRU_DIRS = {"L": (0, -1), "D": (1, 0), "R": (0, 1), "U": (-1, 0)}
    if d in _arrow_dirs:
        return tuple_add(p, _arrow_dirs[d])
    elif d in LDRU_DIRS:
        return tuple_add(p, LDRU_DIRS[d])


def dest_of_hex_walk(
    path: list[str], start: tuple[int, int, int] = (0, 0, 0)
) -> tuple[int, int, int]:
    return list(hex_walk(path, start))[-1]


def hex_walk(
    path,
    start=(0, 0, 0),
):
    directions = {
        "n": (1, 1, 0),
        "s": (-1, -1, 0),
        "e": (1, -1, 0),
        "w": (-1, 1, 0),
        "ne": (1, 0, -1),
        "sw": (-1, 0, 1),
        "nw": (0, 1, -1),
        "se": (0, -1, 1),
    }
    x, y, z = start
    for move in path:
        dx, dy, dz = directions[move]
        x, y, z = x + dx, y + dy, z + dz
        yield x, y, z


data = D


def build_black_grid(data: str):
    tiles = set()
    for line in data.splitlines():
        path = re.findall(r"se|sw|ne|nw|e|w", line)
        dest = dest_of_hex_walk(path)
        if dest in tiles:
            tiles.remove(dest)
        else:
            tiles.add(dest)
    return tiles


tiles = build_black_grid(data)
print(len(tiles))


def range_of_grid_3(g):
    rx = min(x for x, _, _ in g), max(x for x, _, _ in g)
    ry = min(y for _, y, _ in g), max(y for _, y, _ in g)
    rz = min(z for _, _, z in g), max(z for _, _, z in g)
    return rx, ry, rz


def hex_neighbors_without_ns(x, y, z):
    directions = {
        "e": (1, -1, 0),
        "w": (-1, 1, 0),
        "ne": (1, 0, -1),
        "sw": (-1, 0, 1),
        "nw": (0, 1, -1),
        "se": (0, -1, 1),
    }
    for dx, dy, dz in directions.values():
        yield x + dx, y + dy, z + dz


def gen_next(g):
    ng = set()
    rx, ry, rz = list(map(lambda r: range(r[0] - 1, r[1] + 2), range_of_grid_3(g)))
    for p in itertools.product(rx, ry, rz):
        blacks = sum(nb in g for nb in hex_neighbors_without_ns(*p))
        if p in g and not (blacks == 0 or blacks > 2):
            ng.add(p)
        if p not in g and blacks == 2:
            ng.add(p)
    return ng


for i in range(100):
    tiles = gen_next(tiles)
print(len(tiles))
