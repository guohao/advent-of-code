from util import *


def f(ns):
    p = list(map(math.prod, combinations(ns, 2)))
    return min(p) + sum(p) * 2


f2 = lambda ns: 2 * min(map(sum, combinations(ns, 2))) + math.prod(ns)

print(count_nums(f))
print(count_nums(f2))
