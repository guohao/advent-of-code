import re
import sys

D = sys.stdin.read()
from collections import deque
from itertools import count

from intcode import IntCodeVM


def p1():
    data = D

    n = 50
    vms = []

    for i in range(n):
        vm = IntCodeVM(data, deque(), deque())
        vm.rq.append(i)
        vms.append(vm)
    for _ in count():
        for i in range(n):
            vm = vms[i]
            if not vm.rq:
                vm.rq.append(-1)
            vm.run()
            while vm.sq:
                a = vm.sq.popleft()
                x = vm.sq.popleft()
                y = vm.sq.popleft()
                if a == 255:
                    print(y)
                    return
                else:
                    vms[a].rq.append(x)
                    vms[a].rq.append(y)


def p2():
    data = D

    n = 50
    vms = []

    for i in range(n):
        vm = IntCodeVM(data, deque(), deque())
        vm.rq.append(i)
        vms.append(vm)
    nat = None
    seen = set()
    for _ in count():
        has_sq = False
        for i in range(n):
            vm = vms[i]
            if not vm.rq:
                vm.rq.append(-1)
            vm.run()
            while vm.sq:
                has_sq = True
                a = vm.sq.popleft()
                x = vm.sq.popleft()
                y = vm.sq.popleft()
                if a == 255:
                    nat = x, y
                else:
                    vms[a].rq.append(x)
                    vms[a].rq.append(y)
        if not has_sq and nat:
            vms[0].rq.append(nat[0])
            if nat[1] in seen:
                print(nat[1])
                return
            seen.add(nat[1])
            vms[0].rq.append(nat[1])


p1()
p2()
