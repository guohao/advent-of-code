from itertools import count
import sys

L = [line.strip() for line in sys.stdin.readlines() if line.strip()]
initial = L[0].split()[-1]
d = {i: "#" for i, c in enumerate(initial) if c == "#"}
rules = {l: r for l, r in map(lambda x: x.split(" => "), L[1:]) if r == "#"}

for _ in range(20):
    nd = {}
    for i in range(min(d) - 2, max(d) + 3):
        p = "".join("#" if j in d else "." for j in range(i - 2, i + 3))
        if p in rules:
            nd[i] = "#"
    d = nd

print(sum(d))

d = {i: "#" for i, c in enumerate(initial) if c == "#"}
prev_pattern = None
prev_min = None
prev_sum = None

for gen in range(1, 50000000001):
    nd = {}
    for i in range(min(d) - 2, max(d) + 3):
        p = "".join("#" if j in d else "." for j in range(i - 2, i + 3))
        if p in rules:
            nd[i] = "#"
    if not nd:
        break
    curr_min = min(nd)
    curr_sum = sum(nd)
    curr_pattern = sorted([k - curr_min for k in nd])

    if prev_pattern is not None and prev_pattern == curr_pattern:
        delta = curr_min - prev_min
        remaining = 50000000000 - gen
        print(curr_sum + delta * len(nd) * remaining)
        break

    prev_pattern = curr_pattern
    prev_min = curr_min
    prev_sum = curr_sum
    d = nd
