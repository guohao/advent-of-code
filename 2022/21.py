from util import *
from z3 import *

nums = {}
ops = {}

for line in L:
    name, op = line.split(':')
    if op.strip().isnumeric():
        nums[name] = int(op)
    else:
        a, op, b = op.split()
        ops[name] = (a, op, b)

while 'root' in ops:
    for name, op in ops.copy().items():
        a, op, b = op
        if a in nums and b in nums:
            if op == '+':
                nums[name] = nums[a] + nums[b]
            elif op == '-':
                nums[name] = nums[a] - nums[b]
            elif op == '*':
                nums[name] = nums[a] * nums[b]
            elif op == '/':
                nums[name] = nums[a] // nums[b]
            del ops[name]
print(nums['root'])

nums = {}
ops = {}

for line in L:
    name, op = line.split(':')
    if name == 'humn':
        nums[name] = 'x'
        continue

    if op.strip().isnumeric():
        nums[name] = op
    else:
        a, op, b = op.split()
        if name == 'root':
            ops[name] = (a, '==', b)
        else:
            ops[name] = (a, op, b)

while 'root' in ops:
    for name, op in ops.copy().items():
        a, op, b = op
        if a in nums and b in nums:
            if a.isnumeric() and b.isnumeric():
                if op == '+':
                    nums[name] = nums[a] + nums[b]
                elif op == '-':
                    nums[name] = nums[a] - nums[b]
                elif op == '*':
                    nums[name] = nums[a] * nums[b]
                elif op == '/':
                    nums[name] = nums[a] // nums[b]
            else:
                nums[name] = f'(({nums[a]})' + op + f'({nums[b]}))'
            del ops[name]

x = Int('x')
s = Solver()
s.add(eval(nums['root']))
s.check()
print(s.model()[x])
