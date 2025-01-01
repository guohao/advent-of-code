from util import *

t = 0
for line in L:
    line = line.strip()
    t += int(line)
print(t)

t = 0
seen = set()
for line in cycle(L):
    seen.add(t)
    t += int(line)
    if t in seen:
        print(t)
        exit()
