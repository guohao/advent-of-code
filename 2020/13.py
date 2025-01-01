import math
from util import *

data = D 

dt = int(data.splitlines()[0])
ans = dt, -1
for line in data.splitlines()[1].split(','):
    if line == 'x':
        continue
    x = int(line)
    r = math.ceil(dt / x) * x - dt
    if r < ans[0]:
        ans = r, x
print(math.prod(ans))

from sympy.ntheory.modular import crt

data = D 

mods = []
rems = []

for i, bus in enumerate(data.splitlines()[1].split(',')):
    if bus == 'x':
        continue
    id = int(bus)
    mods.append(id)
    rems.append((id - i) % id)
print(crt(mods, rems)[0])
