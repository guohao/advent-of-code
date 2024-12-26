from util import *

n = 2503

dist = [[] for _ in range(n)]

for ns in NS:
    s, d, r = ns
    for i in range(n):
        dist[i].append(((i + 1) // (d + r) * d + min(d, (i + 1) % (d + r))) * s)

print(max(dist[n - 1]))

c = Counter()
for i in range(n):
    for j in range(len(dist[i])):
        if dist[i][j] == max(dist[i]):
            c[j] += 1
print(c.most_common()[0][1])
