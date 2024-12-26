from util import *

import networkx as nx

g = nx.Graph()

for line in lines():
    f, t, d = line.split()[0::2]
    g.add_edge(f, t, weight=int(d))

min_cost = math.inf
max_cost = -math.inf

for path in permutations(g):
    cost = sum(g[u][v]['weight'] for u, v in nb_pair(path))
    min_cost = min(min_cost, cost)
    max_cost = max(max_cost, cost)

print(min_cost)
print(max_cost)
