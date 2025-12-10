import sys
import re
from itertools import count

NS = [list(map(int, re.findall(r"-?\d+", l))) for l in sys.stdin.readlines()]


def first(f) -> int:
    for i in count():
        if f(i):
            return i


ans = 1
ps = [(ns[1], ns[-1]) for ns in NS]


def f():
    print(
        first(
            lambda i: all((i + b + j) % a == 0 for j, (a, b) in enumerate(ps, start=1))
        )
    )


f()
ps.append((11, 0))
f()
