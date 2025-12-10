from collections import deque
import sys


def tuple_add(_a, _b) -> tuple[int, ...]:
    """Adds two tuples of the same length"""
    assert len(_a) == len(_b)
    return tuple(_a[i] + _b[i] for i in range(len(_a)))


grid = [l for l in RAW.split("\n")]
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
    np = tuple_add(p, d)
    if np in g:
        q.append((np, d))
    else:
        for nd in [(d[1], d[0]), (-d[1], -d[0])]:
            np = tuple_add(p, nd)
            if np in g:
                q.append((np, nd))
                break

print(ans)
print(ans2)
