from itertools import combinations
import math
import sys

import re

nums = set([int(line.strip()) for line in L])
t = 0
for n in nums:
    if 2020 - n in nums:
        print(n * (2020 - n))
        break
t = 0
for c in combinations(nums, 3):
    if sum(c) == 2020:
        print(math.prod(c))
        break
