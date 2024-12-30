import networkx as nx

from util import *

g = nx.Graph()
for nums in NS:
    for b in nums[1:]:
        g.add_edge(nums[0], b)

print(len(nx.node_connected_component(g,0)))
print(len(list(nx.connected_components(g))))
