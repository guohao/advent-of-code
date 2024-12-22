import re
import sys

ls = [l.strip() for l in sys.stdin.readlines()]


def f(s: int, n=2000):
    for _ in range(n):
        s = (s * 64) ^ s
        s %= 16777216
        s = (s // 32) ^ s
        s %= 16777216
        s = (s * 2048) ^ s
        s %= 16777216
    return s


t = 0
for line in ls:
    t += f(next(map(int, re.findall(r'-?\d+', line))))
print(t)
