from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

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
