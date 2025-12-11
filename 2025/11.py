import networkx as nx
from collections import deque
import sys
import math

G = nx.DiGraph()
for l in sys.stdin.readlines():
    left,r = l.split(":")
    for e in r.split():
        G.add_edge(left,e)
print(len(list(nx.all_shortest_paths(G,'you','out'))))

def path_count(fr,to):
    q = deque([fr])
    d = {}
    desc = nx.descendants(G,fr)
    while q:
        node = q.popleft()
        if to in d:
            return d[to]
        pred = set(G.predecessors(node)) & desc
        if not any(x not in d for x in pred):
            d[node] = max(1,sum(d[x] for x in pred))
        for v in G.successors(node):
            if v not in d:
                q.append(v)

must = ['svr','fft','dac','out']
print(math.prod(path_count(must[i-1],must[i]) for i in range(1,len(must))))



