from util import *

cubes = NS
ans = 6 * len(cubes)
for i, a in enumerate(cubes):
    for b in cubes[:i]:
        if sum(abs(a[k] - b[k]) for k in range(3)) == 1:
            ans -= 2
print(ans)

lower_bound = [min(c[i] - 1 for c in cubes) for i in range(3)]
upper_bound = [max(c[i] + 1 for c in cubes) for i in range(3)]

ans = 0
dq = deque()
dq.append(lower_bound)
seen = set()
while dq:
    v = dq.popleft()
    if v in cubes:
        ans += 1
        continue
    if tuple(v) not in seen:
        seen.add(tuple(v))
        for i, j in product(range(0, 3), (-1, 1)):
            nv = v.copy()
            nv[i] += j
            if all(lower_bound[i] <= nv[i] <= upper_bound[i] for i in range(3)):
                dq.append(nv)

print(ans)
