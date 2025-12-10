from collections import defaultdict
from itertools import product
import math
import re
import sys

L = sys.stdin.readlines()
R = len(L)
C = len(L[0].strip())
t = 0
for i in range(R):
    for m in re.finditer(r"\d+", L[i]):
        for j, k in product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
            if 0 <= j < R and 0 <= k < C and L[j][k] != "." and not L[j][k].isdigit():
                t += int(m.group())
                break
print(t)

gears = defaultdict(list)
for i in range(len(L)):
    for m in re.finditer(r"\d+", L[i]):
        for j, k in product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
            if 0 <= j < len(L) and 0 <= k < len(L[0]) and L[j][k] == "*":
                gears[j, k].append(int(m.group()))

print(sum(math.prod(v) for k, v in gears.items() if len(v) == 2))
