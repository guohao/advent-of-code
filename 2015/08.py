import sys
r1 = 0
r2 = 0
for l in sys.stdin.readlines():
    l = l.strip()
    r1 += len(l) - len(eval(l))
    r2 += l.count('\\')+l.count('"') + 2
print(r1)
print(r2)
