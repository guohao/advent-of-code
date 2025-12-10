import re
import sys
from itertools import count

from functools import reduce

from itertools import count, cycle
import math

PS = sys.stdin.read().split("\n\n")
parts = PS
ins = cycle(parts[0])
d = {}
for line in parts[1].splitlines():
    f, l, r = re.findall(r"\w{3}", line)
    d[f] = {"L": l, "R": r}
node = "AAA"
for t in count():
    if node == "ZZZ":
        print(t)
        break
    node = d[node][next(ins)]

cycles = []

for node in [x for x in d.keys() if x[-1] == "A"]:
    for t in count():
        if node[-1] == "Z":
            cycles.append(t)
            break
        node = d[node][next(ins)]
print(reduce(math.lcm, cycles))
