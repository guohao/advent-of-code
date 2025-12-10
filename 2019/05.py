import re
import sys

D = sys.stdin.read()
from intcode import IntCodeVM

data = D

vm = IntCodeVM(data)
vm.rq.append(1)
vm.run()
print(vm.sq.pop())

data = D

vm = IntCodeVM(data)
vm.rq.append(5)
vm.run()
print(vm.sq.pop())
