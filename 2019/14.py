import math
import sys

D = sys.stdin.read()
import re
from collections import defaultdict, deque

data = D

G = defaultdict(list)
in_degree = defaultdict(int)
for line in data.splitlines():
    f, t = line.split(" => ")
    tc, tn = t.split()
    tc = int(tc)
    for cell in f.split(", "):
        fc, fn = cell.split()
        fc = int(fc)
        G[tn].append((fn, fc, tc))
        in_degree[fn] += 1
    if tn not in in_degree:
        in_degree[tn] = 0


def topological_sort():
    q = deque([n for n in G.keys() if in_degree[n] == 0])
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for fn, _, _ in G[node]:
            in_degree[fn] -= 1
            if in_degree[fn] == 0:
                q.append(fn)
    return result


needs = {"FUEL": 1}
for tn in topological_sort():
    if tn not in needs:
        continue
    need = needs[tn]
    for fn, fc, tc in G[tn]:
        if fn not in needs:
            needs[fn] = 0
        needs[fn] += math.ceil(need / tc) * fc
print(needs["ORE"])

data = D

in_degree = defaultdict(int)
for line in data.splitlines():
    f, t = line.split(" => ")
    tc, tn = t.split()
    for cell in f.split(", "):
        fc, fn = cell.split()
        in_degree[fn] += 1
    if tn not in in_degree:
        in_degree[tn] = 0


def topological_sort():
    q = deque([n for n in G.keys() if in_degree[n] == 0])
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for fn, _, _ in G[node]:
            in_degree[fn] -= 1
            if in_degree[fn] == 0:
                q.append(fn)
    return result


needs = {"FUEL": 1}
for tn in topological_sort():
    if tn not in needs:
        continue
    need = needs[tn]
    for fn, fc, tc in G[tn]:
        if fn not in needs:
            needs[fn] = 0
        needs[fn] += need / tc * fc
print(int(1000000000000 // needs["ORE"]))
