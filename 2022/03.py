import sys
from functools import reduce

# 读取输入，过滤空行
L = [line.strip() for line in sys.stdin.readlines() if line.strip()]


def priority(c):
    """计算字符的优先级：a-z = 1-26, A-Z = 27-52"""
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27


# Part 1: 找到每个背包两个隔间中都出现的物品类型
t = 0
for line in L:
    n = len(line) // 2
    a = line[:n]
    b = line[n:]
    common = set(a) & set(b)
    if common:
        c = list(common)[0]
        t += priority(c)
print(t)

# Part 2: 找到每三个背包组中都出现的物品类型（徽章）
t = 0
for i in range(0, len(L), 3):
    tg = L[i : i + 3]
    if len(tg) < 3:
        continue
    common = reduce(lambda x, y: x & y, map(set, tg))
    if common:
        c = list(common)[0]
        t += priority(c)
print(t)
