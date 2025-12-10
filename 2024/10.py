from collections import defaultdict, deque
import sys

L = sys.stdin.readlines()
IG = {(i, j): L[i][j] for i in range(len(L)) for j in range(len(L[i].strip()))}

g = defaultdict(str) | IG
q = deque()
starts = [x for x in g if g[x] == "0"]
seen = set()
for s in starts:
    q.append((s, s))
while q:
    s, p = q.popleft()
    if g[p] == "9":
        seen.add((s, p))
        continue
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if g[nx, ny] == str(int(g[p]) + 1):
            q.append((s, (nx, ny)))

print(len(seen))

t = 0
for s in starts:
    q = deque([(s, s)])
    while q:
        s, p = q.popleft()
        if g[p] == "9":
            t += 1
            continue
        x, y = p
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if g[nx, ny] == str(int(g[p]) + 1):
                q.append((s, (nx, ny)))
print(t)
