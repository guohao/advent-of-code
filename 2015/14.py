import sys
import re
from collections import defaultdict

ls = sys.stdin.readlines()
r1 = 0
sec = 2503
records = []
for l in ls:
    s, d, r = map(int, re.findall(r"\d+", l))
    r1 = max(r1, (sec // (d + r) * d + min(sec % (d + r), d)) * s)
    record = []
    for i in range(1, sec + 1):
        record.append((i // (d + r) * d + min(i % (d + r), d)) * s)
    records.append(record)
points = defaultdict(int)
for i in range(sec):
    dis = {j: records[j][i] for j in range(len(ls))}
    longest = max(dis.values())
    for j in dis:
        if dis[j] == longest:
            points[j] += 1

print(r1)
print(max(points.values()))
