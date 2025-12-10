from collections import deque
import sys

import re

sys.path.insert(0, "..")
from util import *

q = deque(range(256))
skip_size = 0
cur_pos = 0
for lens in I:
    q1 = deque()
    for _ in range(lens):
        q1.append(q.popleft())
    while q1:
        q.append(q1.pop())
    q.rotate(-skip_size)
    cur_pos += lens + skip_size
    skip_size += 1

q.rotate(cur_pos)
print(q[0] * q[1])

nums = list(map(ord, D)) + [17, 31, 73, 47, 23]
q = deque(range(256))
skip_size = 0
cur_pos = 0
for _ in range(64):
    for lens in nums:
        q1 = deque()
        for _ in range(lens):
            q1.append(q.popleft())
        while q1:
            q.append(q1.pop())
        q.rotate(-skip_size)
        cur_pos += lens + skip_size
        skip_size += 1
q.rotate(cur_pos)

ans = ""
while q:
    x = 0
    for _ in range(16):
        x ^= q.popleft()
    ans += f"{x:02x}"

print(ans)
