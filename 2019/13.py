import intcode

from util import *

data = D 

vm = intcode.IntCodeVM(data)
vm.run()
sq = vm.sq
g = {}
while sq:
    x = sq.popleft()
    y = sq.popleft()
    t = sq.popleft()
    if t == 2:
        g[x, y] = t
print(len(g))

data = D

data = '2' + data[1:]
vm = intcode.IntCodeVM(data)
sq = vm.sq
rq = vm.rq
score = 0
paddle_x = 0
while True:
    vm.run()
    if not sq:
        break
    x = sq.popleft()
    y = sq.popleft()
    t = sq.popleft()
    if (x, y) == (-1, 0):
        score = t
        continue
    if t == 3:
        paddle_x = x
    elif t == 4:
        rq.append(int((x > paddle_x) - (x < paddle_x)))

print(score)
