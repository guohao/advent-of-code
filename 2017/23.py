from collections import defaultdict
import math
import re
import sys

L = sys.stdin.readlines()
R = len(L)

r = defaultdict(int)
i = 0


def vo(n: str):
    if re.fullmatch(r"-?\d+", n):
        return int(n)
    return r[n]


ans = 0
while 0 <= i < R:
    c, *a = L[i].split()
    if "set" == c:
        r[a[0]] = vo(a[1])
    elif "sub" == c:
        r[a[0]] -= vo(a[1])
    elif "mul" == c:
        ans += 1
        r[a[0]] *= vo(a[1])
    elif "jnz" == c:
        if vo(a[0]) != 0:
            i += vo(a[1])
            continue
    i += 1
print(ans)

b = 93 * 100 + 100000
c = b + 17000


def is_prime(n: int) -> bool:
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


ans = 0
for i in range(b, c + 1, 17):
    if not is_prime(i):
        ans += 1
print(ans)
