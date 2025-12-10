import re
import sys

import networkx as nx

G = nx.DiGraph(l.split(")") for l in L)
# for line in L:
#     a, b = line.split(')')
#     G.add_edge(a, b)

print(sum(len(nx.descendants(G, n)) for n in G.nodes()))
G = G.to_undirected()
print(nx.shortest_path_length(G, "YOU", "SAN") - 2)
