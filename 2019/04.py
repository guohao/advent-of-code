import re
import sys

l, r = map(int, D.split("-"))
t = 0
for i in range(l, r + 1):
    s = str(i)
    for j in range(1, len(s)):
        if s[j] == s[j - 1]:
            break
    else:
        continue
    if sorted(s) != list(s):
        continue
    t += 1

print(t)

t = 0

for i in range(l, r + 1):
    s = str(i)
    if sorted(s) != list(s):
        continue
    if any(len(m.group()) == 2 for m in re.finditer(r"(\d)\1+", s)):
        t += 1

print(t)
