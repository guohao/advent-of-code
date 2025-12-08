from util import *

lines = L
h, d = 0, 0
for line in lines:
    a, b = line.split()
    b = int(b)
    if "fo" in a:
        h += b
    elif "down" in a:
        d += b
    else:
        d -= b
print(h * d)

a, h, d = 0, 0, 0
for line in lines:
    l, r = line.split()
    r = int(r)
    if "fo" in l:
        h += r
        d += a * r
    elif "down" in l:
        a += r
    else:
        a -= r
print(h * d)
