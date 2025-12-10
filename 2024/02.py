import re
import sys
from itertools import combinations

count_nums = lambda f: sum(map(f, NS))

count_nums = lambda f: sum(map(f, NS))

count_nums = lambda f: sum(map(f, NS))


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


print(count_nums(f))
print(count_nums(f2))
