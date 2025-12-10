import re
import sys

from intcode import IntCodeVM

data = D

vm = IntCodeVM(data)
vm.rq.append(1)
vm.run()
print(vm.sq.popleft())

vm = IntCodeVM(data)
vm.rq.append(2)
vm.run()
print(vm.sq.popleft())
