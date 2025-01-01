from util import *

t = 0
for l in L:
    a, b = l.split()
    pa = 'ABC'.index(a)
    pb = 'XYZ'.index(b)
    if pa == pb:
        t += 3
    elif (pb - 1) % 3 == pa:
        t += 6
    t += pb + 1

print(t)

t = 0
for l in L:
    a, b = l.split()
    pa = 'ABC'.index(a)
    pb = 'XYZ'.index(b)
    t += pb * 3 + 1
    if pb == 1:
        t += pa
    elif pb == 2:
        t += (pa + 1) % 3
    else:
        t += (pa - 1) % 3

print(t)
