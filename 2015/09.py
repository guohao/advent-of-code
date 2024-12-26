from util import *

dist = {}
nodes = set()
for line in lines():
    f, t, d = line.split()[0::2]
    nodes |= {f, t}
    dist[f, t] = int(d)
    dist[t, f] = int(d)

min_cost = math.inf
max_cost = -math.inf

for path in permutations(nodes):
    cost = sum(dist[u, v] for u, v in nb_pair(path))
    min_cost = min(min_cost, cost)
    max_cost = max(max_cost, cost)

print(min_cost)
print(max_cost)
