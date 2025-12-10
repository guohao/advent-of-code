import sys

import re

from z3 import *

sys.path.insert(0, "..")
from util import *

ss = NS
ans = 0
MIN = 200000000000000
MAX = 400000000000000
for i in range(len(ss)):
    for j in range(i):
        a = ss[i]
        b = ss[j]
        ax, ay, _, adx, ady, _ = a
        bx, by, _, bdx, bdy, _ = b
        if ady * bdx == adx * bdy:
            continue
        tb = (adx * (by - ay) - ady * (bx - ax)) / (ady * bdx - adx * bdy)
        if tb <= 0:
            continue
        ta = (bdx * tb + bx - ax) / adx
        if ta <= 0:
            continue
        xc = tb * bdx + bx
        yc = tb * bdy + by
        if MIN <= xc <= MAX and MIN <= yc <= MAX:
            ans += 1
print(ans)

ls = NS
n = len(ls)
x, y, z, dx, dy, dz = (
    Real("x"),
    Real("y"),
    Real("z"),
    Real("dx"),
    Real("dy"),
    Real("dz"),
)

T = [Real(f"T{i}") for i in range(len(ls))]
s = Solver()
for i in range(len(ls)):
    s.add(x + T[i] * dx - ls[i][0] - T[i] * ls[i][3] == 0)
    s.add(y + T[i] * dy - ls[i][1] - T[i] * ls[i][4] == 0)
    s.add(z + T[i] * dz - ls[i][2] - T[i] * ls[i][5] == 0)
s.check()
print(s.model().eval(x + y + z))
