import re
import sys
from itertools import permutations

import networkx as nx

L = sys.stdin.readlines()
R = len(L)
C = len(L[0].strip())

g = nx.Graph()
nodes = {}

d2p = {}
for i in range(R):
    for j in range(C):
        nodes[i, j] = L[i][j]
        if L[i][j].isnumeric():
            d2p[int(L[i][j])] = i, j

for n in nodes:
    if nodes[n] == "#":
        continue
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nb = n[0] + i, n[1] + j
        if nb in nodes and nodes[nb] != "#":
            g.add_edge(n, nb)

simplified_g = nx.Graph()
target_nodes = list(d2p.values())
for i, u in enumerate(target_nodes):
    for v in target_nodes[i + 1 :]:
        if nx.has_path(g, u, v):
            shortest_path_length = nx.shortest_path_length(g, u, v)
            simplified_g.add_edge(u, v, weight=shortest_path_length)

start = d2p[0]
del d2p[0]
print(
    min(
        nx.path_weight(simplified_g, [start] + list(c), weight="weight")
        for c in permutations(d2p.values())
    )
)
print(
    min(
        nx.path_weight(simplified_g, [start] + list(c) + [start], weight="weight")
        for c in permutations(d2p.values())
    )
)
