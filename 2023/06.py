from util import *

ans = 1
for t, d in zip(*NS):
    ans *= sum(x * (t - x) > d for x in range(t))

print(ans)

lines = [list(map(int, re.findall(r'-?\d+', line.strip().replace(' ', '')))) for line in L]
ans = 1
for t, d in zip(*lines):
    ans *= sum(x * (t - x) > d for x in range(t))

print(ans)
