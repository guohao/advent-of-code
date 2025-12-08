import sys
import re
import math

ls = sys.stdin.readlines()
ins = [list(map(int, re.findall(r"-?\d+", l))) for l in ls]


def dfs(prev, i, remain, c500=False):
    if i == len(ins) - 1:
        curr = prev + (remain,)
        if not c500 or 500 >= sum(ins[j][4] * curr[j] for j in range(len(ins))):
            return score(curr)
        return 0
    return max(dfs(prev + (j,), i + 1, remain - j, c500) for j in range(remain + 1))


def score(cnt):
    return math.prod(
        max(0, sum(ins[i][j] * cnt[i] for i in range(len(ins)))) for j in range(4)
    )


print(dfs(tuple(), 0, 100))
print(dfs(tuple(), 0, 100, True))
