import sys

RAW = sys.stdin.read()
PS = RAW.strip().split("\n\n")
t = 0
for part in PS:
    t = max(t, sum(map(int, part.splitlines())))
print(t)

ts = [sum(map(int, part.splitlines())) for part in PS]
print(sum(sorted(ts)[-3:]))
