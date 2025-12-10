from itertools import count
import sys
import re

NS = [list(map(int, re.findall(r"\d+", line))) for line in sys.stdin.readlines()]

print(sum(d * r for d, r in NS if d % (2 * r - 2) == 0))

for i in count():
    if all((i + d) % (2 * r - 2) for d, r in NS):
        print(i)
        break
