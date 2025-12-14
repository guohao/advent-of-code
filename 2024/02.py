import sys
from itertools import combinations

L = list(list(map(int, l.split())) for l in sys.stdin.readlines())

r1 = 0
for l in L:
    s = sorted(l)
    if s != l and s[::-1] != l:
        continue
    for i in range(1, len(l)):
        if not 1 <= abs(l[i] - l[i - 1]) <= 3:
            break
    else:
        r1 += 1
print(r1)

r2 = 0
for l in L:
    valid = False
    for l in combinations(l, len(l) - 1):
        l = list(l)
        s = sorted(l)
        if s != l and s[::-1] != l:
            continue
        for i in range(1, len(l)):
            if not 1 <= abs(l[i] - l[i - 1]) <= 3:
                break
        else:
            valid = True
    if valid:
        r2 += 1
print(r2)
