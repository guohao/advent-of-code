from collections import deque
from itertools import product
import sys

import re

L = sys.stdin.readlines()


def ints(l: str, neg=True):
    if neg:
        return list(map(int, re.findall(r"-?\d+", l)))
    else:
        return list(map(int, re.findall(r"\d+", l)))


NS = [tuple(ints(line)) for line in L]
cubes = NS
ans = 6 * len(cubes)
for i, a in enumerate(cubes):
    for b in cubes[:i]:
        if sum(abs(a[k] - b[k]) for k in range(3)) == 1:
            ans -= 2
print(ans)

# Part 2: 只计算外部表面积（排除内部空气口袋）
# 使用 BFS 从外部开始遍历，只计算能到达的立方体面
cubes_set = set(cubes)
lower_bound = [min(c[i] - 1 for c in cubes) for i in range(3)]
upper_bound = [max(c[i] + 1 for c in cubes) for i in range(3)]

ans = 0
dq = deque()
dq.append(tuple(lower_bound))
seen = set()
seen.add(tuple(lower_bound))

while dq:
    v = dq.popleft()
    # 检查6个相邻方向
    for i in range(3):
        for j in (-1, 1):
            nv = list(v)
            nv[i] += j
            nv_tuple = tuple(nv)

            # 如果相邻位置是立方体，则这是一个外部面
            if nv_tuple in cubes_set:
                ans += 1
            # 如果相邻位置是空气且在边界内且未访问过，则加入队列
            elif nv_tuple not in seen:
                if all(lower_bound[k] <= nv[k] <= upper_bound[k] for k in range(3)):
                    seen.add(nv_tuple)
                    dq.append(nv_tuple)

print(ans)
