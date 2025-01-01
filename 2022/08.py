from util import *

g = {k: int(v) for k, v in IG.items()}
x_max, y_max = max((x, y) for x, y in g)
ans = 0


def visible():
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        if all((i + dx * k, j + dy * k) not in g or g[i + dx * k, j + dy * k] < g[i, j] for k in
               range(1, max(x_max, y_max))):
            return True
    return False


for i in range(x_max + 1):
    for j in range(y_max + 1):
        ans += visible()
print(ans)

ans = 0


def scenic_score():
    ss = 1
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        c = 0
        k = i, j
        while True:
            k = dx + k[0], dy + k[1]
            if k not in g:
                break
            c += 1
            if g[k] >= g[i, j]:
                break
        ss *= c
    return ss


for i in range(x_max + 1):
    for j in range(y_max + 1):
        ans = max(ans, scenic_score())
print(ans)
