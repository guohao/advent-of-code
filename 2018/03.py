from collections import defaultdict
from itertools import product
import re
import sys

g = defaultdict(int)
for line in L:
    i, l, t, w, h = list(map(int, re.findall(r"-?\d+", line)))
    for j in range(l, l + w):
        for k in range(t, t + h):
            g[j, k] += 1
print(sum(v > 1 for v in g.values()))

g = defaultdict(int)
for line in L:
    i, l, t, w, h = list(map(int, re.findall(r"-?\d+", line)))
    for j in range(l, l + w):
        for k in range(t, t + h):
            g[j, k] += 1

for line in L:
    i, l, t, w, h = list(map(int, re.findall(r"-?\d+", line)))
    if all(g[j, k] == 1 for j, k in product(range(l, l + w), range(t, t + h))):
        print(i)
        break
