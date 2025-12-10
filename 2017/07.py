import sys
from functools import cache
import networkx as nx

L = sys.stdin.readlines()
g = nx.DiGraph()
for line in L:
    cells = line.replace(",", "").split()
    g.add_node(cells[0], v=int(cells[1][1:-1]))
    if "->" in line:
        for c in cells[3:]:
            g.add_edge(cells[0], c)
print(next(nx.topological_sort(g)))


@cache
def tw(n: str) -> int:
    return nx.get_node_attributes(g, "v")[n] + sum(map(tw, g[n]))


def need_to_be(es: int, root: str) -> int:
    if len(set(map(tw, g[root]))) == 1:
        return es - tw(root) + nx.get_node_attributes(g, "v")[root]
    ue = (es - nx.get_node_attributes(g, "v")[root]) // len(g[root])
    for up in g[root]:
        if ue != tw(up):
            return need_to_be(ue, up)


bottom = next(nx.topological_sort(g))
vs = list(g[bottom])
for i, v in enumerate(vs):
    l, m, r = [tw(vs[(i + j) % len(vs)]) for j in range(-1, 2)]
    if l == r != m:
        print(need_to_be(l, v))
        break
