from collections import Counter
import sys
import re

NS = [list(map(int, re.findall(r"\d+", line))) for line in sys.stdin.readlines()]
print(sum(abs(a - b) for a, b in zip(*map(sorted, zip(*NS)))))

a, b = zip(*NS)
b = Counter(b)
print(sum(x * b[x] for x in a))
