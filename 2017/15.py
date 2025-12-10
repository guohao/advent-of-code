import re
import sys

from functools import cache

sys.path.insert(0, "..")
from util import *

a, b = I
i = 0
ans = 0
N = 40000000
while i < N:
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 0xFFFF == b & 0xFFFF:
        ans += 1
    i += 1
print(ans)


@cache
def gen_next_a(prev: int) -> int:
    v = (prev * 16807) % 2147483647
    while v % 4 != 0:
        v = (v * 16807) % 2147483647
    return v


@cache
def gen_next_b(prev: int) -> int:
    v = (prev * 48271) % 2147483647
    while v % 8 != 0:
        v = (v * 48271) % 2147483647
    return v


ans = 0
a, b = I
N = 5000000
for i in range(N):
    a = gen_next_a(a)
    b = gen_next_b(b)
    if a & 0xFFFF == b & 0xFFFF:
        ans += 1
print(ans)
