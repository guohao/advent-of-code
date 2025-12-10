from collections import deque
import sys

import re

sys.path.insert(0, "..")
from util import *

skip = I[0]
q = deque()
for i in range(2018):
    q.rotate(-skip)
    q.append(i)
print(q.popleft())

q = deque()
for i in range(50000000):
    q.rotate(-skip)
    q.append(i)
q.rotate(-q.index(0) - 1)
print(q.popleft())
