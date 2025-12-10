import sys

L = sys.stdin.readlines()
import re


nums = {}
ops = {}

for line in L:
    name, op = line.split(":")
    if op.strip().isnumeric():
        nums[name] = int(op)
    else:
        a, op, b = op.split()
        ops[name] = (a, op, b)

while "root" in ops:
    for name, op in ops.copy().items():
        a, op, b = op
        if a in nums and b in nums:
            if op == "+":
                nums[name] = nums[a] + nums[b]
            elif op == "-":
                nums[name] = nums[a] - nums[b]
            elif op == "*":
                nums[name] = nums[a] * nums[b]
            elif op == "/":
                nums[name] = nums[a] // nums[b]
            del ops[name]
print(nums["root"])

nums = {}
ops = {}

for line in L:
    name, op = line.split(":")
    name = name.strip()
    op = op.strip()
    if name == "humn":
        continue
    if op.isnumeric():
        nums[name] = int(op)
    else:
        a, op, b = op.split()
        if name == "root":
            ops[name] = (a, "==", b)
        else:
            ops[name] = (a, op, b)

# 先计算所有可以计算的
while True:
    changed = False
    for name, op in ops.copy().items():
        if name == "root":
            continue
        a, op, b = op
        if a in nums and b in nums:
            if op == "+":
                nums[name] = nums[a] + nums[b]
            elif op == "-":
                nums[name] = nums[a] - nums[b]
            elif op == "*":
                nums[name] = nums[a] * nums[b]
            elif op == "/":
                nums[name] = nums[a] // nums[b]
            del ops[name]
            changed = True
    if not changed:
        break


# 反向求解humn
def solve(name, target):
    if name == "humn":
        return target
    if name in nums:
        return nums[name]
    # name在ops中
    a, op, b = ops[name]
    a_val = nums.get(a)
    b_val = nums.get(b)

    if a_val is not None:
        # a已知，b包含humn
        if op == "+":
            return solve(b, target - a_val)
        elif op == "-":
            return solve(b, a_val - target)
        elif op == "*":
            return solve(b, target // a_val)
        elif op == "/":
            return solve(b, a_val // target)
    elif b_val is not None:
        # b已知，a包含humn
        if op == "+":
            return solve(a, target - b_val)
        elif op == "-":
            return solve(a, target + b_val)
        elif op == "*":
            return solve(a, target // b_val)
        elif op == "/":
            return solve(a, target * b_val)


# root: a == b
root_a, root_op, root_b = ops["root"]
if root_a in nums:
    print(solve(root_b, nums[root_a]))
else:
    print(solve(root_a, nums[root_b]))
