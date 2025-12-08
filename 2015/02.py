import sys
import re

ls = sys.stdin.readlines()
r1 = 0
r2 = 0
for l in ls:
    a, b, c = list(map(int, re.findall(r"\d+", l)))
    areas = [a * b, b * c, a * c]
    r2 += ((a + b + c) - max(a, b, c)) * 2 + a * b * c
    r1 += sum(areas) * 2 + min(areas)
print(r1)
print(r2)
