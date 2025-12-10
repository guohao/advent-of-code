from collections import deque
import re
import sys


def ints(l: str, neg=True):
    if neg:
        return list(map(int, re.findall(r"-?\d+", l)))
    else:
        return list(map(int, re.findall(r"\d+", l)))


parts = RAW.split("\n\n")

qs = {}
for c in zip(*parts[0].splitlines()):
    if c[-1].isdigit():
        qs[int(c[-1])] = deque([x for x in c[:-1][::-1] if x.isalpha()])

for m in parts[1].splitlines():
    n, f, t = ints(m)
    for _ in range(n):
        qs[t].append(qs[f].pop())
print("".join(q.pop() for q in qs.values()))

qs = {}
for c in zip(*parts[0].splitlines()):
    if c[-1].isdigit():
        qs[int(c[-1])] = deque([x for x in c[:-1][::-1] if x.isalpha()])

for m in parts[1].splitlines():
    n, f, t = ints(m)
    qs[f].rotate(n)
    for _ in range(n):
        qs[t].append(qs[f].popleft())
print("".join(q.pop() for q in qs.values()))
