from collections import defaultdict, deque
import sys
import re

NS = [list(map(int, re.findall(r"\d+", line))) for line in sys.stdin.readlines()]

comps = defaultdict(list)
for a, b in NS:
    comps[a].append(b)
    comps[b].append(a)

q = deque([(0, frozenset())])
ans = 0
while q:
    u, visited = q.popleft()
    has_next = False
    for v in comps[u]:
        if (u, v) not in visited and (v, u) not in visited:
            q.append((v, visited | {(u, v)}))
            has_next = True
    if not has_next:
        ans = max(ans, sum(sum(x) for x in visited))
print(ans)

q = deque([(0, frozenset())])
ans = 0
max_len = 0
while q:
    u, visited = q.popleft()
    has_next = False
    for v in comps[u]:
        if (u, v) not in visited and (v, u) not in visited:
            q.append((v, visited | {(u, v)}))
            has_next = True
    if not has_next:
        if len(visited) > max_len:
            max_len = len(visited)
            ans = sum(sum(x) for x in visited)
        elif len(visited) == max_len:
            ans = max(ans, sum(sum(x) for x in visited))
print(ans)
