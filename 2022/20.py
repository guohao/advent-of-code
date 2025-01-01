from util import *


def f(k, p2=None):
    ns = I
    if p2:
        ns = [811589153 * x for x in ns]
    N = len(ns)
    move = deque(range(N))
    for _ in range(k):
        for i, di in enumerate(ns):
            src = move.index(i)
            move.rotate(-src)
            move.popleft()
            move.rotate(-di)
            move.appendleft(i)
    move.rotate(-move.index(ns.index(0)))
    ans = sum([ns[move[i % N]] for i in (1000, 2000, 3000)])
    print(ans)


f(1)
f(10, 1)
