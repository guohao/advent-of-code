from util import *

d = int(D)
n = [3, 7]
p = [0, 1]
while len(n) < d + 10:
    n += map(int, str(n[p[0]] + n[p[1]]))
    p = [(1 + p[i] + n[p[i]]) % len(n) for i in range(2)]
print("".join((map(str, n[d : d + 10]))))

d = D
n = [3, 7]
p = [0, 1]
while True:
    n += map(int, str(n[p[0]] + n[p[1]]))
    p = [(1 + p[i] + n[p[i]]) % len(n) for i in range(2)]
    if d in "".join(map(str, n[-len(d) - 1 :])):
        print("".join(map(str, n)).index(d))
        break
