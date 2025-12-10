from collections import deque
from itertools import combinations
import sys

import re

data = D

seq = deque()
for n in map(int, data.splitlines()):
    if len(seq) < 25:
        seq.append(n)
    else:
        if not any(a + b == n for a, b in combinations(seq, 2)):
            print(n)
            break
        seq.append(n)
        seq.popleft()

data = D

seq = deque()
target = -1
for n in map(int, data.splitlines()):
    if len(seq) < 25:
        seq.append(n)
    else:
        if not any(a + b == n for a, b in combinations(seq, 2)):
            target = n
            break
        seq.append(n)
        seq.popleft()

ns = list(map(int, data.splitlines()))
ns = ns[: ns.index(target)]
for i in range(len(ns)):
    for j in range(1, len(ns) - i):
        if sum(ns[i : i + j + 1]) == target:
            ans = sorted(ns[i : i + 1 + j])
            print(ans[0] + ans[-1])
            exit()
