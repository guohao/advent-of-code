import sys
import functools
r1 = 0
r2 = 0
@functools.cache
def max_joltage(arr,digit_num):
    if digit_num == 1:
        return max(arr)
    mj = 0
    for i,num in enumerate(arr[:-digit_num+1]):
        mj = max(mj,max_joltage(arr[i+1:],digit_num-1)+num*pow(10,digit_num-1))
    return mj


for line in sys.stdin.readlines():
    nums = tuple(map(int,line.strip()))
    r1+= max_joltage(nums,2)
    r2+= max_joltage(nums,12)
print(r1)
print(r2)

