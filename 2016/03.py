from util import *


def f(ns):
    ns = sorted(ns)
    return sum(ns[:2]) > ns[2]


print(count_nums(f))

t = 0
columns = list(chain.from_iterable(zip(*NS)))
for i in range(0, len(columns), 3):
    nums = sorted(columns[i:i + 3])
    t += sum(nums[:2]) > nums[2]
print(t)
