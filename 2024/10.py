from util import *

t = 0

g = IG | defaultdict(int)
q = deque()
starts = [x for x in g if g[x] == "0"]
for s in starts:
    q.append((s, s))
seen = set()
while q:
    s, p = q.popleft()
    if g[p] == "9":
        t += 1
        seen.add((s, p))
        continue
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if g[nx, ny] == str(int(g[p]) + 1):
            q.append((s, (nx, ny)))

print(len(seen))
print(t)
