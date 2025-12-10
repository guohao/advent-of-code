import re
import sys

lines = L
ans = 0
for line in lines:
    f, t, c, s = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    if int(f) <= s.count(c) <= int(t):
        ans += 1
print(ans)

ans = 0
for line in lines:
    f, t, c, s = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    f = int(f) - 1
    t = int(t) - 1
    mc = 0
    if 0 <= t < len(s) and s[t] == c:
        mc += 1
    if 0 <= f < len(s) and s[f] == c:
        mc += 1
    if mc == 1:
        ans += 1
print(ans)
