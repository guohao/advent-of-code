from util import *

DS = {0: ("U", (-1, 0)), 1: ("D", (1, 0)), 2: ("L", (0, -1)), 3: ("R", (0, 1))}

hp = [(0, "", 1, 1)]
min_len_path = None
max_len = -math.inf
while hp:
    l, p, x, y = heapq.heappop(hp)
    if x == y == 4:
        if not min_len_path:
            min_len_path = p
        max_len = max(max_len, l)
        continue
    if x <= 0 or x > 4:
        continue
    if y <= 0 or y > 4:
        continue
    for i, c in enumerate(md5(f"{D}{p}")[:4]):
        if int(c, 16) > int("a", 16):
            dl, (dx, dy) = DS[i]
            heapq.heappush(hp, (l + 1, p + dl, x + dx, y + dy))

print(min_len_path)
print(max_len)
