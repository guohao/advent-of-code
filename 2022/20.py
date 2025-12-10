from collections import deque
import sys


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


I = [int(line.strip()) for line in sys.stdin.readlines()]


def f(k, p2=None):
    ns = I
    if p2:
        ns = [811589153 * x for x in ns]
    N = len(ns)
    move = deque(range(N))
    for _ in range(k):
        for i, di in enumerate(ns):
            src = move.index(i)
            move.rotate(-src)
            move.popleft()
            move.rotate(-di)
            move.appendleft(i)
    move.rotate(-move.index(ns.index(0)))
    ans = sum([ns[move[i % N]] for i in (1000, 2000, 3000)])
    print(ans)


f(1)
f(10, 1)
