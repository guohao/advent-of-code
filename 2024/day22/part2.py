import re
import sys
from collections import defaultdict

ls = [l.strip() for l in sys.stdin.readlines()]


def f(s: int):
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
    ps = [x % 10 for x in f(next(map(int, re.findall(r'-?\d+', line))))]
    changes = [ps[i + 1] - ps[i] for i in range(len(ps) - 1)]
    seen = {}
    for i in range(len(changes) - 3):
        s4 = tuple(changes[i:i + 4])
        if s4 not in seen:
            current_price = ps[i + 4]
            seen[s4] = current_price
    for s4, price in seen.items():
        profits[s4] += price

print(max(profits.values()))
