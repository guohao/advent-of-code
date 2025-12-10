from itertools import count
import sys

I = list(map(int, input().strip().split()))
nums = I.copy()

seen = {}
pc = 0
for step in count(1):
    state = tuple(nums)
    if state in seen:
        print(step - 1)
        pc += 1
        if pc == 2:
            print(step - 1 - seen[state])
            break
        seen.clear()
    seen[state] = step - 1
    most = max(nums)
    t = nums.index(most)
    k = most // len(nums)
    m = most % len(nums)
    nums[t] = 0
    for j in range(len(nums)):
        nums[j] += k
    for j in range(1, m + 1):
        nums[(j + t) % len(nums)] += 1
