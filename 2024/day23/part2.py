import sys

import networkx as nx

ls = [l.strip() for l in sys.stdin.readlines()]
G = nx.Graph()
for l in ls:
    G.add_edge(*l.split('-'))
print(','.join(sorted(max(nx.find_cliques(G), key=len))))
