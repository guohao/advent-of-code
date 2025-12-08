from util import *

ps = []
for line in L:
    line = line.strip()
    digits = tuple(map(int, re.findall(r"-?\d+", line)))
    ps.append(digits)
minX = min(x[0] for x in ps)
minY = min(x[1] for x in ps)
maxX = max(x[0] for x in ps)
maxY = max(x[1] for x in ps)

g = {}
invalid = set()
for i, j in product(range(minX, maxX + 1), range(minY, maxY + 1)):
    dist_to = {k: abs(k[0] - i) + abs(k[1] - j) for k in ps}
    nearest = min(dist_to.values())
    if list(dist_to.values()).count(nearest) == 1:
        for k, v in dist_to.items():
            if v == nearest:
                g[i, j] = k
                break
    else:
        g[i, j] = "."
    if i in (minX, maxX) or j in (minY, maxY):
        invalid.add(g[i, j])

c = Counter(g.values())
for x in invalid:
    del c[x]
print(c.most_common()[0][1])

t = 0
for i, j in product(range(minX, maxX + 1), range(minY, maxY + 1)):
    t += sum((abs(k[0] - i) + abs(k[1] - j)) for k in ps) < 10000

print(t)
