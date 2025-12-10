import sys
import heapq
import networkx as nx

L = sys.stdin.readlines()
g = nx.DiGraph()
for line in L:
    a = line.split()[1]
    b = line.split()[-3]
    g.add_edge(a, b)
print("".join(nx.lexicographical_topological_sort(g)))

g = nx.DiGraph()
for line in L:
    a = ord(line.split()[1]) - ord("A") + 61
    b = ord(line.split()[-3]) - ord("A") + 61
    g.add_edge(a, b)

indegree = {v: d for v, d in g.in_degree() if d > 0}
zero_indegree = [v for v, d in g.in_degree() if d == 0]
heapq.heapify(zero_indegree)

workers = []

t = 0
while indegree:
    while not zero_indegree or len(workers) == 5:
        t, node = heapq.heappop(workers)
        for child in g[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                heapq.heappush(zero_indegree, child)
                del indegree[child]
    node = heapq.heappop(zero_indegree)
    heapq.heappush(workers, (t + node, node))

worker = heapq.heappop(workers)
print(worker[0])
