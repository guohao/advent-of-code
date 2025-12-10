import re
import sys
from itertools import combinations

L = sys.stdin.readlines()
NS = [list(map(int, re.findall(r"\d+", line))) for line in L]


def f(ns):
    if ns == sorted(ns) or ns == sorted(ns, reverse=True):
        for i in range(1, len(ns)):
            if not (1 <= abs(ns[i] - ns[i - 1]) <= 3):
                break
        else:
            return 1
    return 0


def f2(ns):
    for c in combinations(ns, len(ns) - 1):
        c = list(c)
        if c == sorted(c) or c == sorted(c, reverse=True):
            for i in range(1, len(c)):
                if not (1 <= abs(c[i] - c[i - 1]) <= 3):
                    break
            else:
                return 1
    return 0


print(sum(f(ns) for ns in NS))
print(sum(f2(ns) for ns in NS))
