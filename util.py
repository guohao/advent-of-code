import hashlib
import heapq
import math
import re
import sys
from collections import defaultdict, deque, Counter
from itertools import count, permutations, combinations, product, combinations_with_replacement,chain
from typing import Tuple

# (r,c)
_arrow_dirs = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
LRDU = 'LRDU'
LDRU_DIRS = {'L': (0, -1), 'D': (1, 0), 'R': (0, 1), 'U': (-1, 0)}


def _holder():
    defaultdict()
    deque()
    Counter()
    heapq.heapify([])
    math.prod([])
    combinations_with_replacement([], 2)
    permutations([])
    combinations([], 2)
    product([])
    chain()


def ints(l: str):
    return list(map(int, re.findall(r'-?\d+', l)))


def nums(l: list[str]):
    return list(map(ints, l))


def lines(s: str,strip=True):
    if strip:
        return [l.strip() for l in s.splitlines()]
    else:
        return s.splitlines()


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


def nb9(p, _g=None):
    if not _g:
        _g = IG
    for i in range(p[0] - 1, p[0] + 2):
        for j in range(p[1] - 1, p[1] + 2):
            if (i, j) != p and (i, j) in _g:
                yield i, j


def nb4(p):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yield p[0] + i, p[1] + j


def nb9_v(p, _g=None):
    if not _g:
        _g = IG
    return list(map(_g.get, nb9(p)))


def nb4_v(p, _g=None):
    if not _g:
        _g = IG
    return list(map(_g.get, nb4(p)))


def count_9(p, value, _g=None):
    return sum(v == value for v in nb9_v(p, _g))


def count_4(p, value, _g=None):
    return sum(v == value for v in nb4_v(p, _g))


def pairs(ls: list[str], sep: str, reverse=False):
    ps = [(l.strip(), r.strip()) for l, r in [line.split(sep) for line in ls]]
    if reverse:
        return [(r, l) for l, r in ps]
    else:
        return ps


def move(p, d):
    if d in _arrow_dirs:
        return tuple_add(p, _arrow_dirs[d])
    elif d in LDRU_DIRS:
        return tuple_add(p, LDRU_DIRS[d])


def parts(s: str):
    return s.split('\n\n')


def turn(d: tuple[int, int], t: str) -> tuple[int, int]:
    if t == 'L':
        return turn_left(d)
    elif t == 'R':
        return turn_right(d)
    else:
        raise ValueError(f"Invalid turn: {t}")


def turn_left(d: tuple[int, int]) -> tuple[int, int]:
    return -d[1], d[0]


def turn_right(d: tuple[int, int]) -> tuple[int, int]:
    return d[1], -d[0]

def grid(s:str):
    return {(i, j): c for i, line in enumerate(lines(s,False)) for j, c in enumerate(line)}


class Graph2D:

    def __init__(self, from_input=False, rows: int = None, cols: int = None, default_val=None, start=(0, 0)):
        self.start = start
        self.grid = {}
        if from_input:
            self.grid = {(i, j): c for i, line in enumerate(lines(D)) for j, c in enumerate(line)}
            self.rows = len(L)
            self.cols = len(L[0])
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


class UnorderedDict:
    def __init__(self):
        self.g = {}

    def __setitem__(self, key, value):
        self.g[tuple(sorted(key))] = value

    def __getitem__(self, item):
        return self.g[tuple(sorted(item))]


input_file = 'input.txt'
if len(sys.argv) > 1:
    input_file = sys.argv[1]
D = open(input_file).read().strip()
L = lines(D)
I = ints(D)
NS = nums(L)
R = len(L)
C = len(L[0])
N = len(NS[0])
IG = grid(D)
PS = parts(D)

counts = lambda f: sum(map(f, L))
count_nums = lambda f: sum(map(f, NS))
max_nums = lambda f: max(map(f, NS))
