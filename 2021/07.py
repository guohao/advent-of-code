from util import *

data = D
ns = list(map(int, data.split(",")))

ans = math.inf
for n in range(min(ns), max(ns) + 1):
    ans = min(ans, sum(abs(x - n) for x in ns))
print(ans)

ans = math.inf
for n in range(min(ns), max(ns) + 1):
    ans = min(ans, sum((1 + abs(x - n)) * (abs(x - n)) // 2 for x in ns))
print(ans)
