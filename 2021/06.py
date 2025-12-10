from collections import defaultdict
import sys

import re

seq = list(map(int, D.split(",")))
lfs = defaultdict(int)
for t in seq:
    lfs[t] += 1


def gen_next_day(d):
    nlfs = defaultdict(int)
    for t, c in d.items():
        if t > 0:
            nlfs[t - 1] += c
        else:
            nlfs[6] += c
            nlfs[8] += c
    return nlfs


for _ in range(80):
    lfs = gen_next_day(lfs)
print(sum(lfs.values()))

for _ in range(256 - 80):
    lfs = gen_next_day(lfs)
print(sum(lfs.values()))
