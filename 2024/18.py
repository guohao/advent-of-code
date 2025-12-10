import sys
import re
import networkx as nx

L = sys.stdin.readlines()
NS = [list(map(int, re.findall(r"\d+", line))) for line in L]

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
        print(L[i].strip())
        break
