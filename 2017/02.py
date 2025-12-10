import sys
from itertools import product

NS = [list(map(int, line.split())) for line in sys.stdin.readlines()]

print(sum(max(ns) - min(ns) for ns in NS))

print(
    sum(a // b for ns in NS for a, b in product(ns, repeat=2) if a != b and a % b == 0)
)
