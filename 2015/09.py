import sys
import heapq
from functools import cache
ls = sys.stdin.readlines()
edges= {}
nodes = set()
for l in ls:
    l=l.strip()
    f,_,t,_,d = l.split()
    d = int(d)
    edges[f,t] = d
    edges[t,f] = d
    nodes.add(f)
    nodes.add(t)

@cache
def dfs(visited):
    if len(visited) == len(nodes):
        return 0,0
    min_cost = 2**63-1
    max_cost = -1
    for n in nodes - set(visited):
        smin,smax = dfs(visited + (n,))
        if visited:
            smin += edges[visited[-1],n]
            smax += edges[visited[-1],n]
        min_cost = min(min_cost,smin)
        max_cost = max(max_cost,smax)
    return min_cost,max_cost

print(dfs(tuple()))
