from itertools import count
import sys

sys.path.insert(0, "..")
from util import *

count_nums = lambda f: sum(map(f, NS))

import re

count_nums = lambda f: sum(map(f, NS))

print(count_nums(lambda dr: dr[0] * dr[1] if not dr[0] % (2 * dr[1] - 2) else 0))

for i in count():
    if all((i + d) % (2 * r - 2) for d, r in NS):
        print(i)
        break
