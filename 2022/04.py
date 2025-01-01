from util import *

t = 0
for a, b, c, d in NS:
    t += (c - a) * (d - b) <= 0
print(t)

t = 0
for a, b, c, d in NS:
    t += (d - a) * (c - b) <= 0
print(t)
