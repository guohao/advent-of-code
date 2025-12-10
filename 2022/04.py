import re
import sys

L = sys.stdin.readlines()


def ints(l: str, neg=True):
    if neg:
        return list(map(int, re.findall(r"-?\d+", l)))
    else:
        return list(map(int, re.findall(r"\d+", l)))


t0 = 0
t1 = 0
for line in L:
    a, b, c, d = ints(line, False)
    t0 += (c - a) * (d - b) <= 0
    t1 += (d - a) * (c - b) <= 0
print(t0)
print(t1)
