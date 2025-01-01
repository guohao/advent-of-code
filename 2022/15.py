from util import *

def d(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


BS = {}
for x1, y1, x2, y2  in NS:
    BS[(x1, y1)] = (x2, y2)

def check(p) -> bool:
    for s, b in BS.items():
        if d(p, s) <= d(s, b):
            return True
    return False


ret = set()
for a, b in BS.items():
    diff = d(a, b) - abs(a[1] - 2000000)
    for i in range(a[0] - diff, a[0] + diff + 1):
        ret.add(i)

for b in BS.values():
    if b[1] == 2000000 and b[0] in ret:
        ret.remove(b[0])
print(len(ret))

def check(p) -> bool:
    for s, b in BS.items():
        if d(p, s) <= d(s, b):
            return True
    return False


x_r = range(0, 4000000)
y_r = range(0, 4000000)
for y in y_r:
    nv = []
    for a, b in BS.items():
        diff = d(a, b) - abs(a[1] - y)
        nv.append(range(max(0, a[0] - diff), min(4000000, a[0] + diff + 1)))
    x = 0
    while x in x_r:
        found = False
        for v in nv:
            if x in v:
                found = True
                x = v.stop
        if not found:
            break
    if x in x_r:
        print(x * 4000000 + y)
        break
