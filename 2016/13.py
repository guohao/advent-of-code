import networkx as nx

from util import *

fn = int(*I)
g = nx.Graph()


def is_open(x, y):
    if x < 0 or y < 0:
        return False
    return not (x * x + 3 * x + 2 * x * y + y + y * y + fn).bit_count() % 2


for n in product(range(100), repeat=2):
    if is_open(*n):
        for nb in nb4(n):
            if is_open(*nb):
                g.add_edge(n, nb)

print(nx.shortest_path_length(g, (1, 1), (31, 39)))
print(len(nx.single_source_shortest_path_length(g, (1, 1), cutoff=50)))
