import re
import sys

D = sys.stdin.read()
import math


data = D

dt = int(data.splitlines()[0])
ans = dt, -1
for line in data.splitlines()[1].split(","):
    if line == "x":
        continue
    x = int(line)
    r = math.ceil(dt / x) * x - dt
    if r < ans[0]:
        ans = r, x
print(math.prod(ans))


# 实现中国剩余定理（CRT）
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        return None
    return (x % m + m) % m


def crt(mods, rems):
    N = 1
    for m in mods:
        N *= m

    result = 0
    for i in range(len(mods)):
        Ni = N // mods[i]
        Mi = mod_inverse(Ni, mods[i])
        result += rems[i] * Ni * Mi

    return result % N


data = D

mods = []
rems = []

for i, bus in enumerate(data.splitlines()[1].split(",")):
    if bus == "x":
        continue
    id = int(bus)
    mods.append(id)
    rems.append((id - i) % id)
print(crt(mods, rems))
