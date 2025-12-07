import sys
import re
from itertools import groupby
lines = [l[:-1] for l in sys.stdin.readlines()]
print(sum(eval(l[-1].join(l[:-1])) for l in zip(*list(re.findall(r'\S+',line)  for line in lines))))
parts = [list(g) for k, g in groupby(list(''.join(l) for l in zip(*lines[:-1])), key=lambda s: bool(s.strip())) if k]
print(sum(eval(s.join(p)) for s,p in zip(re.findall(r'\S',lines[-1]),parts)))



