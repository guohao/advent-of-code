from util import *

t0 = 0
t1 = 0
for line in L:
    a, b, c, d = ints(line, False)
    t0 += (c - a) * (d - b) <= 0
    t1 += (d - a) * (c - b) <= 0
print(t0)
print(t1)
