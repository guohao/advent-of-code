import sys
from collections import deque

import networkx as nx

g = nx.DiGraph()
for line in sys.stdin.read().split('\n'):
    if ':' in line:
        l, r = line.split(':')
        g.add_node(l, v=int(r.strip()))
    elif '->' in line:
        a, op, b, _, c = line.split()
        g.add_edge(a, c, op=op)
        g.add_edge(b, c, op=op)

vals = nx.get_node_attributes(g, 'v')
q = deque(vals)
while q:
    k = q.popleft()
    for s in g.successors(k):
        if s in vals:
            continue
        a, b = g.predecessors(s)
        op = g[a][s]['op']
        if a in vals and b in vals:
            a = vals[a]
            b = vals[b]
            match op:
                case 'XOR':
                    vals[s] = a ^ b
                case 'OR':
                    vals[s] = a | b
                case 'AND':
                    vals[s] = a & b
            q.append(s)
print(int(''.join(map(lambda k: str(vals[k]), sorted([x for x in vals if x[0] == 'z'], reverse=True))), 2))
