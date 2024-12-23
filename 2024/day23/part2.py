import sys

import networkx as nx

print(','.join(sorted(max(nx.find_cliques(nx.Graph(l.strip().split('-') for l in sys.stdin.readlines())), key=len))))
