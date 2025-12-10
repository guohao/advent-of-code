import sys
import re
import networkx as nx

NS = [list(map(int, re.findall(r"\d+", line))) for line in sys.stdin.readlines()]

g = nx.Graph()
for nums in NS:
    for b in nums[1:]:
        g.add_edge(nums[0], b)

print(len(nx.node_connected_component(g, 0)))
print(len(list(nx.connected_components(g))))
