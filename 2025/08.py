import sys
from collections import deque, defaultdict
from itertools import combinations

ls = sys.stdin.readlines()
boxes = sorted(list(tuple(map(int, l.split(","))) for l in ls))
dist = []
for a, b in combinations(boxes, 2):
    dis = sum((a[i] - b[i]) ** 2 for i in range(3))
    dist.append((dis, (a, b)))
dist.sort()
q = deque(dist)
groups = []
b2g = defaultdict(lambda: -1)
i = 0
while q:
    (_, (a, b)) = q.popleft()
    ga = b2g[a]
    gb = b2g[b]
    if ga == gb == -1:
        groups.append({a, b})
        b2g[a] = len(groups) - 1
        b2g[b] = len(groups) - 1
    elif ga == -1:
        groups[gb].add(a)
        b2g[a] = gb
    elif gb == -1:
        groups[ga].add(b)
        b2g[b] = ga
    elif ga == gb:
        pass
    else:
        groups.append(groups[ga] | groups[gb])
        if len(groups[-1]) == len(boxes):
            print(a[0] * b[0])
            break
        for c in groups[-1]:
            b2g[c] = len(groups) - 1
    i += 1
    if i == 1000:
        r1 = []
        valid = set()
        for a in b2g:
            valid.add(b2g[a])
        for c in valid:
            r1.append(len(groups[c]))
        r1.sort()
        a, b, c = r1[::-1][:3]
        print(a * b * c)
