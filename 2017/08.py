from collections import defaultdict
import sys

import re


def join(l):
    return "".join(map(str, l))


rs = defaultdict(int)
ans = 0
for line in L:
    line = line.replace("dec", "-=")
    line = line.replace("inc", "+=")
    cells = line.split()
    cells[0] = f'rs["{cells[0]}"]'
    cells[-3] = f'rs["{cells[-3]}"]'
    line = " ".join(cells) + " else 0"
    exec(line)
    ans = max(ans, max(rs.values()))
print(max(rs.values()))
print(ans)
