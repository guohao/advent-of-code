from util import *

t = 0
for part in PS:
    t = max(t, sum(map(int, part.splitlines())))
print(t)

ts = []
for part in PS:
    ts.append(sum(map(int, part.splitlines())))
print(sum(sorted(ts)[-3:]))
