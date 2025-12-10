from collections import deque
import sys

skip = int(sys.stdin.read())
q = deque([0])
for i in range(1, 2018):
    q.rotate(-skip)
    q.append(i)
print(q.popleft())
q.rotate(-skip)

pos = 0
ans = 0
for i in range(1, 50000001):
    pos = (pos + skip) % i + 1
    if pos == 1:
        ans = i
print(ans)
