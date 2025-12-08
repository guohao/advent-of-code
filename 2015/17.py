import sys
from itertools import combinations

cs = list(map(int, sys.stdin.readlines()))
print(sum(sum(c) == 150 for i in range(1, len(cs) + 1) for c in combinations(cs, i)))
for i in range(1, len(cs) + 1):
    s = sum(sum(c) == 150 for c in combinations(cs, i))
    if s:
        print(s)
        break
