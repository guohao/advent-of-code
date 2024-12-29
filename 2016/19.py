from util import *

d = I[0]
q = deque(range(1, d + 1))
while len(q) != 1:
    q.rotate(-1)
    q.popleft()
print(q.pop())


q = deque(range(d, 0, -1))

q.rotate(len(q) // 2)
while len(q) != 1:
    q.pop()
    if not len(q) % 2:
        q.rotate(1)
print(q.pop())
