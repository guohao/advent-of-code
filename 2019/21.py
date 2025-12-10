import re
import sys

from intcode import IntCodeVM

sys.path.insert(0, "..")
from util import *

data = D

vm = IntCodeVM(data)
commands = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
"""
for cmd in commands:
    vm.rq.append(ord(cmd))
vm.run()
print(vm.sq.pop())

data = D

vm = IntCodeVM(data)
commands = """NOT B J 
NOT C T
OR T J
AND D J
AND H J
NOT A T
OR T J 
RUN
"""
for cmd in commands:
    vm.rq.append(ord(cmd))
vm.run()
print(vm.sq.pop())
