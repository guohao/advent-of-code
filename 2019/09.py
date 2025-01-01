from intcode import IntCodeVM
from util import *

data = D

vm = IntCodeVM(data)
vm.rq.append(1)
vm.run()
print(vm.sq.popleft())

vm = IntCodeVM(data)
vm.rq.append(2)
vm.run()
print(vm.sq.popleft())
