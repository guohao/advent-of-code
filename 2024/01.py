import sys

NS = list(map(int, sys.stdin.read().split()))
a = sorted(NS[0::2])
b = sorted(NS[1::2])
print(sum(abs(a - b) for a, b in zip(a, b)))
print(sum(x * b.count(x) for x in a))
