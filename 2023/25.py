from itertools import combinations
import sys

import re

import networkx as nx

sys.path.insert(0, "..")
from util import *

graph = nx.DiGraph()
for line in L:
    left, right = line.split(":")
    for y in right.split():
        graph.add_edge(left, y, capacity=1)
        graph.add_edge(y, left, capacity=1)

for a, b in combinations(graph.nodes, 2):
    cut_c, (left, right) = nx.minimum_cut(graph, a, b)
    if cut_c == 3:
        print(len(left) * len(right))
        break
