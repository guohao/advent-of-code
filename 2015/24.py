from util import *


def f(n):
    group_weight = sum(I) // n
    for i in range(1, R):
        ans = math.inf
        for c in combinations(I, i):
            if sum(c) == group_weight:
                ans = min(ans, math.prod(c))
        if ans != math.inf:
            print(ans)
            break


f(3)
f(4)
