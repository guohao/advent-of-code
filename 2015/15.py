from util import *


def sum_n(n, total, prefix=None):
    if prefix is None:
        prefix = []
    if n == 1:
        yield prefix + [total]
    else:
        for x in range(total + 1):
            new_prefix = prefix + [x]
            yield from sum_n(n - 1, total - x, new_prefix)


def score_of(c):
    return math.prod(
        max(0, sum(NS[i][j] * c[i] for i in range(R))) for j in range(N - 1)
    )


def c500(c):
    return sum(NS[i][-1] * c[i] for i in range(R)) == 500


print(max(map(score_of, sum_n(R, 100))))
print(max(map(score_of, filter(c500, sum_n(R, 100)))))
