import sys
import string
from itertools import product

ls = sys.stdin.readlines()
r1 = 0
atz = string.ascii_lowercase
for s in ls:
    if sum(s.count(x) for x in "aeiou") < 3:
        continue
    if not any(x + x in s for x in atz):
        continue
    if any(x in s for x in ["ab", "cd", "pq", "xy"]):
        continue
    r1 += 1
print(r1)

r2 = 0
for s in ls:
    if not any(s.count("".join(x)) > 1 for x in product(atz, repeat=2)):
        continue
    if not any(s.count("".join(x) + x[0]) for x in product(atz, repeat=2)):
        continue
    r2 += 1
print(r2)
