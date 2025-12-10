import sys
from collections import deque
from intcode import IntCodeVM

D = input().strip()
data = D


def p1():
    q = deque([[]])
    seen = set()
    D_map = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
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
                d = D_map[move]
                x, y = x + d[0], y + d[1]
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i in range(1, 5):
            q.append(path + [i])


def p2():
    q = deque([[]])
    seen = set()
    D_map = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
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
            d = D_map[move]
            x, y = x + d[0], y + d[1]
            if s == 2:
                oxygen = x, y
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i in range(1, 5):
            q.append(path + [i])

    def bfs_max_distance(start):
        q = deque([(start, 0)])
        visited = {start}
        max_dist = 0
        while q:
            pos, dist = q.popleft()
            max_dist = max(max_dist, dist)
            x, y = pos
            for d in D_map.values():
                nb = (x + d[0], y + d[1])
                if nb in seen and nb not in visited:
                    visited.add(nb)
                    q.append((nb, dist + 1))
        return max_dist

    print(bfs_max_distance(oxygen))


p1()
p2()
