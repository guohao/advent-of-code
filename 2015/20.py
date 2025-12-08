import math
from functools import cache

d = int(input())
def p1():
    def sof(k):
        s = 0
        for i in range(1, int(math.sqrt(k)) + 1):
            if k % i == 0:
                s += i
                s += k // i
        return s

    for k in range(d):
        if sof(k)* 10>d:
            print(k)
            break
p1()
def p2():
    def sof(k):
        s = 0
        for i in range(1, int(math.sqrt(k)) + 1):
            if k % i == 0:
                if k//i <= 50:
                    s += i
                if i<=50:
                    s += k // i
        return s

    for k in range(d):
        if sof(k)*11>d:
            print(k)
            break
p2()
