from util import *
from functools import reduce

t = 0
for line in L:
    n = len(line) // 2
    a = line[:n]
    b = line[n:]
    c = list(set(a) & set(b))[0]
    t += ord(c) + 1
    if "a" <= c <= "z":
        t -= ord("a")
    else:
        t -= ord("A")
        t += 26
print(t)

t = 0
for i in range(0, len(L), 3):
    tg = L[i : i + 3]
    c = list(reduce(lambda x, y: x & y, map(set, tg)))[0]
    t += ord(c) + 1
    if "a" <= c <= "z":
        t -= ord("a")
    else:
        t -= ord("A")
        t += 26
print(t)
