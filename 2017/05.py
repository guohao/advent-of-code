from util import *

t = 0
i = 0
nums = I.copy()
while 0 <= i < R:
    n = nums[i]
    nums[i] += 1
    i += n
    t += 1
print(t)

nums = I.copy()
t = 0
i = 0
while 0 <= i < R:
    n = nums[i]
    if n >= 3:
        nums[i] -= 1
    else:
        nums[i] += 1
    i += n
    t += 1

print(t)
