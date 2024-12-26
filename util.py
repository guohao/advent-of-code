import re
from typing import Tuple

import math
import hashlib
import sys
from itertools import combinations, count, product, permutations
from collections import deque

_raw = open('input.txt').read().strip()
# (r,c)
_arrow_dirs = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}


def raw():
    return _raw


def ints(l: str):
    return list(map(int, re.findall(r'-?\d+', l)))


def nums():
    return list(map(ints, lines()))


def lines(s=None):
    if not s:
        s = _raw
    return [l.strip() for l in s.splitlines()]


def list_add(_a, _b):
    assert len(_a) == len(_b)
    return list(_a[i] + _b[i] for i in range(len(_a)))


def tuple_add(_a, _b) -> tuple[int, ...]:
    """
    Adds two tuples of the same length
    """
    assert len(_a) == len(_b)
    return tuple(_a[i] + _b[i] for i in range(len(_a)))


def tuple_add_2(_a, _b) -> tuple[int, int]:
    """
    Adds two tuples of length 2
    """
    assert len(_a) == len(_b) == 2
    return _a[0] + _b[0], _a[1] + _b[1]


counts = lambda f: sum(map(f, lines()))
count_nums = lambda f: sum(map(f, nums()))


def md5(s: str):
    return hashlib.md5(s.encode()).hexdigest()


def first(f) -> int:
    for i in count():
        if f(i):
            return i


def nb_pair(l):
    return zip(l[:-1], l[1:])

def c2i(c: str):
    return ord(c) - ord('a')

def i2c(i: int):
    return chr(i + ord('a'))

def join(l):
    return ''.join(map(str, l))

class Graph2D:

    def __init__(self, rows: int = None, cols: int = None, default_val=None, start=(0, 0)):
        self.start = start
        self.grid = {}
        if any([rows, cols]) and not all([rows, cols]):
            raise ValueError("Rows and cols must be provided")
        if rows and cols:
            self.rows = rows
            self.cols = cols
            for r in range(rows):
                for c in range(cols):
                    self.grid[(r, c)] = default_val

        self.pos: Tuple[int, int] = self.start
        self.visited: set[Tuple[int, int]] = set()
        self.visited.add(self.pos)

    def move(self, dir_or_pos):
        """
        Move to a direction or position
        """
        target_pos = None
        if dir_or_pos in _arrow_dirs:
            target_pos = tuple_add_2(_arrow_dirs[dir_or_pos], self.pos)
        elif isinstance(dir_or_pos, tuple) and len(dir_or_pos) == 2:
            target_pos = dir_or_pos
        if not target_pos:
            raise ValueError(f"Invalid direction or pos: {dir_or_pos}")
        self.pos = target_pos
        self.visited.add(self.pos)
        return self

    def set(self, pos, value):
        self.grid[pos] = value
        return self

    def moves(self, directions):
        for d in directions:
            self.move(d)
        return self

    def visited_num(self):
        return len(self.visited)

    def visited(self):
        return self.visited

    def pos(self):
        return self.pos

    def reset_pos(self):
        self.pos = self.start
        return self

    def values(self):
        return self.grid.values()

    def __contains__(self, item):
        return item in self.grid

    def __getitem__(self, item):
        return self.grid[item]

    def __len__(self):
        return len(self.grid)

    def __setitem__(self, key, value):
        self.grid[key] = value


def graph2d():
    return Graph2D()
