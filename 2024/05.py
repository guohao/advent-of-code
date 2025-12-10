import re
import sys

RAW = sys.stdin.read()
PS = RAW.strip().split("\n\n")


def ints(l: str, neg=True):
    if neg:
        return list(map(int, re.findall(r"-?\d+", l)))
    else:
        return list(map(int, re.findall(r"\d+", l)))


t = 0
p0 = []
for l in PS[0].splitlines():
    a, b = map(int, l.split("|"))
    p0.append((a, b))

for l in PS[1].splitlines():
    ns = ints(l)
    for a, b in p0:
        if a in ns and b in ns:
            if ns.index(a) > ns.index(b):
                break
    else:
        t += ns[len(ns) // 2]
print(t)

t = 0
for l in PS[1].splitlines():
    ns = ints(l)
    c = False
    while True:
        for a, b in p0:
            if a in ns and b in ns:
                ai = ns.index(a)
                bi = ns.index(b)
                if ai > bi:
                    ns[bi], ns[ai] = ns[ai], ns[bi]
                    c = True
                    break
        else:
            break
    if c:
        t += ns[len(ns) // 2]

print(t)
