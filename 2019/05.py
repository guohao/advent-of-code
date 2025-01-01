from intcode import IntCodeVM

from util import *

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
