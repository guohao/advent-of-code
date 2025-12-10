import sys

import re

import networkx as nx

sys.path.insert(0, "..")
from util import *

G = nx.grid_2d_graph(71, 71)
for ns in NS[:1024]:
    G.remove_node(tuple(ns))
print(nx.shortest_path_length(G, min(G), max(G)))

G = nx.grid_2d_graph(71, 71)
for i, ns in enumerate(NS):
    G.remove_node(tuple(ns))
    try:
        nx.shortest_path_length(G, min(G), max(G))
    except:
        print(L[i])
        break
