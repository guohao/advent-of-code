from collections import deque
import sys

RAW = sys.stdin.read()
grid = RAW.splitlines()
g = {(i, j): c for i, line in enumerate(grid) for j, c in enumerate(line) if c != " "}
start = next((0, j) for j in range(len(grid[0])) if (0, j) in g)
q = deque([(start, (1, 0))])
ans = ""
ans2 = 0
while q:
    p, d = q.popleft()
    ans2 += 1
    if g[p].isalpha():
        ans += g[p]
    np = (p[0] + d[0], p[1] + d[1])
    if np in g:
        q.append((np, d))
    else:
        for nd in [(d[1], d[0]), (-d[1], -d[0])]:
            np = (p[0] + nd[0], p[1] + nd[1])
            if np in g:
                q.append((np, nd))
                break

print(ans)
print(ans2)
