from collections import deque
import sys

sys.path.insert(0, "..")
from util import *


def join(l):
    return "".join(map(str, l))


import re


def join(l):
    return "".join(map(str, l))


import networkx as nx

g = nx.DiGraph()
for line in L:
    if ":" in line:
        l, r = line.split(":")
        g.add_node(l, v=int(r.strip()))
    elif "->" in line:
        a, op, b, _, c = line.split()
        g.add_edge(a, c, op=op)
        g.add_edge(b, c, op=op)

vals = nx.get_node_attributes(g, "v")
q = deque(vals)
while q:
    k = q.popleft()
    for s in g.successors(k):
        if s in vals:
            continue
        a, b = g.predecessors(s)
        op = g[a][s]["op"]
        if a in vals and b in vals:
            a = vals[a]
            b = vals[b]
            match op:
                case "XOR":
                    vals[s] = a ^ b
                case "OR":
                    vals[s] = a | b
                case "AND":
                    vals[s] = a & b
            q.append(s)
print(
    int(
        "".join(
            map(
                lambda k: str(vals[k]),
                sorted([x for x in vals if x[0] == "z"], reverse=True),
            )
        ),
        2,
    )
)

XOR = "XOR"
AND = "AND"
OR = "OR"

g = {}
rg = {}
minmax = lambda _a, _b: (_a, _b) if _a <= _b else (_b, _a)
for line in PS[1].splitlines():
    a, op, b, _, c = line.split()
    a, b = minmax(a, b)
    g[a, b, op] = c
    rg[c] = a, b, op


def swap(_a, _b):
    rg[_a], rg[_b] = rg[_b], rg[_a]
    g[rg[_a]], g[rg[_b]] = g[rg[_b]], g[rg[_a]]


output = set()
c = ""
for i in range(int(max(rg)[1:])):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"
    zn = f"z{i + 1:02}"
    xxy = g[x, y, XOR]
    xay = g[x, y, AND]
    if not c:
        c = xay
    else:
        a, b = minmax(c, xxy)
        k = a, b, XOR
        if k not in g:
            a, b = list(set(rg[z][:2]) ^ set(k[:2]))
            output.add(a)
            output.add(b)
            swap(a, b)
        elif g[k] != z:
            output.add(g[k])
            output.add(z)
            swap(z, g[k])
        k = rg[z]
        xxy = g[x, y, XOR]
        xay = g[x, y, AND]
        c = g[*minmax(c, xxy), AND]
        c = g[*minmax(c, xay), OR]

print(",".join(sorted(output)))
