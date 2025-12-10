import networkx as nx
import re

import sys

NS = [list(map(int, re.findall(r"-?\d+", l))) for l in sys.stdin.readlines()]


def nb4(p):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yield p[0] + i, p[1] + j


t = 0
nodes = {}
for nums in NS[2:]:
    nodes[nums[0], nums[1]] = (nums[-1], nums[-2])

for a in nodes:
    for b in nodes:
        if a == b:
            continue
        if nodes[b][0]:
            t += nodes[a][1] >= nodes[b][0]

print(t)

g = nx.Graph()

t = 0
nodes = {}
X = Y = 0
for nums in NS[2:]:
    if nums[-1] > 95:
        continue
    nodes[nums[0], nums[1]] = nums[-4:]
    X = max(X, nums[0])
    Y = max(Y, nums[1])

cap = max(x[2] for x in nodes.values())
start = None
for p in nodes:
    if nodes[p][2] == cap:
        start = p
    for nb in nb4(p):
        if nb in nodes:
            g.add_edge(p, nb)
stl = nx.shortest_path_length(g, start, (0, 0))
ltr = nx.shortest_path_length(g, (0, 0), (X, 0))
print(stl + (ltr - 1) * 5 + ltr)
