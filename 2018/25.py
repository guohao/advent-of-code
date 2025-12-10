import re
import sys

sys.path.insert(0, "..")
from util import *


def ints(l: str, neg=True):
    if neg:
        return list(map(int, re.findall(r"-?\d+", l)))
    else:
        return list(map(int, re.findall(r"\d+", l)))


import networkx as nx


def is_same(a, b):
    return sum(abs(a[i] - b[i]) for i in range(4)) <= 3


G = nx.Graph()
for line in L:
    G.add_node(tuple(ints(line)))
for a in G.nodes():
    for b in G.nodes():
        if a == b:
            continue
        if is_same(a, b):
            G.add_edge(a, b)
print(len(list(nx.connected_components(G))))
