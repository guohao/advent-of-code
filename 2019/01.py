from util import *

nums = [int(line.strip()) for line in L]
t = 0
for n in nums:
    t += n // 3 - 2
print(t)
from util import *

nums = [int(line.strip()) for line in L]
t = 0
for n in nums:
    while n // 3 - 2 > 0:
        n = n // 3 - 2
        t += n
print(t)
