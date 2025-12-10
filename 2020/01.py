from itertools import combinations
import math
import sys

L = sys.stdin.readlines()
nums = set(int(line.strip()) for line in L)
for n in nums:
    if 2020 - n in nums:
        print(n * (2020 - n))
        break

for c in combinations(nums, 3):
    if sum(c) == 2020:
        print(math.prod(c))
        break
