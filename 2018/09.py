from collections import deque
import re
import sys

D = input().strip()


def f(p2=None):
    pc, last_points = list(map(int, re.findall(r"-?\d+", D)))
    ps = [0] * pc

    q = deque()
    if p2:
        mm = last_points * 100 + 1
    else:
        mm = last_points + 1
    for i in range(mm):
        if i == 0 or i % 23:
            q.rotate(-1)
            q.append(i)
        else:
            q.rotate(7)
            ps[i % pc] += q.pop() + i
            q.rotate(-1)
    print(max(ps))


f()
f(1)
