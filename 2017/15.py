import re
import sys
from functools import cache

I = [int(re.search(r"\d+", line).group()) for line in sys.stdin.readlines()]
a, b = I

ans = 0
for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 0xFFFF == b & 0xFFFF:
        ans += 1
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
for _ in range(5000000):
    a = gen_next_a(a)
    b = gen_next_b(b)
    if a & 0xFFFF == b & 0xFFFF:
        ans += 1
print(ans)
