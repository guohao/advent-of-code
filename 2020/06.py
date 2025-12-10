import sys

import re

data = D

ans = 0
for part in data.split("\n\n"):
    s = set()
    for line in part.splitlines():
        for x in line:
            s.add(x)
    ans += len(s)
print(ans)

ans = 0
for part in data.split("\n\n"):
    s = {x for x in part}
    for line in part.splitlines():
        s1 = set()
        for x in line:
            s1.add(x)
        s = s & s1
    ans += len(s)
print(ans)
