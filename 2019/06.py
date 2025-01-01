import networkx as nx

from util import *

data = D 

G = nx.DiGraph()
for line in data.splitlines():
    a, b = line.split(')')
    G.add_edge(a, b)

print(sum(len(nx.descendants(G, n)) for n in G.nodes()))
print(nx.shortest_path_length(G, 'YOU', 'SAN') - 2)
