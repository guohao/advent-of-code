from collections import Counter
import sys

L = [line.strip() for line in sys.stdin.readlines()]
a = b = 0
for line in L:
    c = Counter(line)
    if 2 in c.values():
        a += 1
    if 3 in c.values():
        b += 1
print(a * b)

for a in L:
    for b in L:
        if a == b or len(a) != len(b):
            continue
        if sum(a[i] != b[i] for i in range(len(a))) == 1:
            print("".join(a[i] for i in range(len(a)) if a[i] == b[i]))
            break
    else:
        continue
    break
