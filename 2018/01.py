from itertools import cycle
import sys

L = sys.stdin.readlines()
t = 0
for line in L:
    t += int(line.strip())
print(t)

t = 0
seen = set()
for line in cycle(L):
    seen.add(t)
    t += int(line.strip())
    if t in seen:
        print(t)
        break
