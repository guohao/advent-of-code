from collections import deque
from itertools import count
import hashlib
import re
import sys

D = input().strip()


def md5(s: str):
    return hashlib.md5(s.encode()).hexdigest()


def p1():
    c = 0
    for i in count():
        m = re.search(r"(\w)\1\1", md5(D + str(i)))
        if not m:
            continue
        for j in range(i + 1, i + 1001):
            if m.group(1) * 5 in md5(D + str(j)):
                c += 1
                if c == 64:
                    print(i)
                    return
                break


def p2():
    def digest_2017(k):
        s = md5(f"{D}{k}")
        for _ in range(2016):
            s = md5(s)
        return s

    c = 0
    q = deque(digest_2017(i) for i in range(1000))

    for i in count():
        q.append(digest_2017(i + 1000))
        m = re.search(r"(\w)\1\1", q.popleft())
        if not m:
            continue
        if any(m.group(1) * 5 in x for x in q):
            c += 1
            if c == 64:
                print(i)
                return


p1()
p2()
