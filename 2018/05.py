import re
import sys


def join(l):
    return "".join(map(str, l))


import string

d = D
p = []
for i in range(26):
    aA = string.ascii_lowercase[i] + string.ascii_uppercase[i]
    p.append(aA)
    p.append(aA[::-1])

p = "|".join(p)
while True:
    d, n = re.subn(p, "", d)
    if n == 0:
        print(len(d))
        break

ans = len(D)
for i in range(26):
    aA = string.ascii_lowercase[i] + "|" + string.ascii_uppercase[i]
    d = D
    d = re.sub(aA, "", d)
    while True:
        d, n = re.subn(p, "", d)
        if n == 0:
            ans = min(ans, len(d))
            break
print(ans)
