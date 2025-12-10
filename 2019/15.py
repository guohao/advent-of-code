import sys
from collections import deque
import networkx as nx
from intcode import IntCodeVM

sys.path.insert(0, "..")
from util import *

data = D


def p1():
    q = deque([[]])
    seen = set()
    D = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    while q:
        path = q.popleft()
        vm = IntCodeVM(data)
        x, y = 0, 0
        for move in path:
            vm.rq.append(move)
            vm.run()
            s = vm.sq.popleft()
            if s == 2:
                print(len(path))
                return
            elif s == 1:
                d = D[move]
                x, y = x + d[0], y + d[1]
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i in range(1, 5):
            q.append(path + [i])


def p2():
    q = deque([[]])
    seen = set()
    D = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    oxygen = 0, 0
    while q:
        path = q.popleft()
        vm = IntCodeVM(data)
        x, y = 0, 0
        for move in path:
            vm.rq.append(move)
            vm.run()
            s = vm.sq.popleft()
            if s == 0:
                continue
            d = D[move]
            x, y = x + d[0], y + d[1]
            if s == 2:
                oxygen = x, y
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i in range(1, 5):
            q.append(path + [i])
    G = nx.Graph()
    for x, y in seen:
        for d in D.values():
            nb = (x + d[0], y + d[1])
            if nb in seen:
                G.add_edge(nb, (x, y))
    print(max(nx.shortest_path_length(G, oxygen).values()))


p1()
p2()
