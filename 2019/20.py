from collections import defaultdict, deque
import heapq
import sys

import re


def join(l):
    return "".join(map(str, l))


def bfs_shortest_path(G, start, end):
    if start not in G or end not in G:
        return None
    q = deque([(start, 0)])
    visited = {start}
    while q:
        node, dist = q.popleft()
        if node == end:
            return dist
        for neighbor in G[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
    return None


def p1(data: str):
    g = {}
    l2p = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == "." or c.isupper():
                g[i, j] = c
    G = defaultdict(list)
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == ".":
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nb = (i + dx, j + dy)
                    if nb in g and g[nb] == ".":
                        G[(i, j)].append(nb)
                        G[nb].append((i, j))
            elif c.isupper():
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nb = (i + dx, j + dy)
                    if nb in g and g[nb].isupper():
                        p = (nb[0] + dx, nb[1] + dy)
                        if p in g:
                            pair = "".join(sorted(c + data.splitlines()[nb[0]][nb[1]]))
                            if pair in l2p:
                                G[l2p[pair]].append(p)
                                G[p].append(l2p[pair])
                            else:
                                l2p[pair] = p
                            break
    return bfs_shortest_path(G, l2p["AA"], l2p["ZZ"])


def p2(data: str):
    g = {}
    X = len(data.splitlines())
    Y = len(data.splitlines()[0])
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == "." or c.isupper():
                g[i, j] = c
    G = defaultdict(list)
    outs = {}
    ins = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == ".":
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nb = (i + dx, j + dy)
                    if nb in g and g[nb] == ".":
                        G[(i, j)].append(nb)
                        G[nb].append((i, j))
            elif c.isupper():
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nb = (i + dx, j + dy)
                    if nb in g and g[nb].isupper():
                        p = (nb[0] + dx, nb[1] + dy)
                        if p in g:
                            pair = "".join(sorted(c + data.splitlines()[nb[0]][nb[1]]))
                            if 1 < i - dx < X - 1 and 1 < j - dy < Y - 1:
                                ins[pair] = p
                            else:
                                outs[pair] = p
                            break
    trans = {}
    for o in ins:
        trans[outs[o]] = (ins[o], -1)
        trans[ins[o]] = (outs[o], 1)
    paths = defaultdict(dict)

    for a in list(outs.values()) + list(ins.values()):
        for b in list(outs.values()) + list(ins.values()):
            if a == b:
                continue
            dist = bfs_shortest_path(G, a, b)
            if dist is not None:
                paths[a][b] = dist
                paths[b][a] = dist
    q = []
    heapq.heapify(q)

    start = outs["AA"]
    target = outs["ZZ"]

    del paths[target]
    for p in paths:
        if start in paths[p]:
            del paths[p][start]

    q.append((0, 0, start))
    while q:
        steps, lvl, node = heapq.heappop(q)
        reaches = paths[node].copy()
        if lvl == 0:
            if target in reaches:
                return steps + paths[node][target]
            for o in outs.values():
                if o in reaches:
                    del reaches[o]
        else:
            if target in reaches:
                del reaches[target]
        steps += 1
        for n in reaches:
            p, diff = trans[n]
            heapq.heappush(q, (steps + reaches[n], lvl + diff, p))


D = sys.stdin.read()
print(p1(D))
print(p2(D))
