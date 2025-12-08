import sys

r1 = 0
r2 = 0
p = 50
for line in sys.stdin.readlines():
    d = -1 if line[0] == "L" else 1
    s = int(line[1:])
    m = s % 100
    r2 += s // 100
    if p == 0:
        r1 += 1
        r2 += 1
    else:
        r2 += 1 - (0 <= (d * m + p) <= 100)
    p = (d * m + p) % 100
print(r1)
print(r2)
