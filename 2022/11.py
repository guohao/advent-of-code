from util import *

sys.set_int_max_str_digits(10 ** 6)


def f(n, p2=None):
    mks = []
    inspected = Counter()
    m = 1
    for part in PS:
        lines = part.splitlines()
        items = ints(lines[1])
        operation = lines[2]
        test = ints(lines[3])[0]
        if p2:
            m *= test
        true_to = ints(lines[4])[0]
        false_to = ints(lines[5])[0]
        mks.append((deque(items), operation, test, true_to, false_to))
    for _ in range(n):
        for i in range(len(mks)):
            mk = mks[i]
            while mk[0]:
                inspected[i] += 1
                item = mk[0].popleft()
                item = eval(mk[1].replace('old', str(item)).split('=')[1])
                if p2:
                    item = item % m
                else:
                    item //= 3
                if item % mk[2] == 0:
                    mks[mk[3]][0].append(item)
                else:
                    mks[mk[4]][0].append(item)
    print(math.prod(c for _, c in inspected.most_common(2)))


f(20)
f(10000, 1)
