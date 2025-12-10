from collections import Counter
import sys

import re

print(sum(abs(a - b) for a, b in zip(*map(sorted, zip(*NS)))))
a, b = zip(*NS)
b = Counter(b)
print(sum((x * b[x]) for x in a))
