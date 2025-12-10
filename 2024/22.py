from collections import defaultdict
import re
import sys

sys.path.insert(0, "..")
from util import *

ls = L


def f(s: int, n=2000):
    for _ in range(n):
        s = (s * 64) ^ s
        s %= 16777216
        s = (s // 32) ^ s
        s %= 16777216
        s = (s * 2048) ^ s
        s %= 16777216
    return s


t = 0
for line in ls:
    t += f(next(map(int, re.findall(r"-?\d+", line))))
print(t)


def f2(s: int):
    seq = [s]
    for _ in range(2000):
        s = (s * 64) ^ s
        s %= 16777216
        s = (s // 32) ^ s
        s %= 16777216
        s = (s * 2048) ^ s
        s %= 16777216
        seq.append(s)
    return seq


profits = defaultdict(int)
for line in ls:
    ps = [x % 10 for x in f2(next(map(int, re.findall(r"-?\d+", line))))]
    cs = [ps[i + 1] - ps[i] for i in range(len(ps) - 1)]
    seen = {}
    for i in range(len(cs) - 3):
        s4 = tuple(cs[i : i + 4])
        if s4 not in seen:
            seen[s4] = ps[i + 4]
    for s4, price in seen.items():
        profits[s4] += price

print(max(profits.values()))
