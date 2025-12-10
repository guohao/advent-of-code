import sys
import re
from itertools import combinations, product, permutations
from collections import deque, defaultdict
import heapq
import math
from z3 import *

def p1(l):
    cells = l.split()
    lts,btns = cells[0][1:-1],cells[1:-1]
    btns = [list(map(int,x[1:-1].split(','))) for x in btns]
    o = Optimize()
    x =IntVector('x',len(btns))
    for xi in x:
        o.add(xi>=0)
    for i in range(len(lts)):
        s = 1 if lts[i] =='#' else 0
        v_btns = []
        for j,btn in enumerate(btns):
            if i in btn:
                v_btns.append(j)
        o.add(Sum(x[j] for j in v_btns)%2==s)
    o.minimize(Sum(x))
    if o.check() == sat:
        return o.model().eval(Sum(x)).as_long()

def p2(l):
    cells = l.split()
    lts,btns,jls = cells[0][1:-1],cells[1:-1],cells[-1][1:-1]
    btns = [list(map(int,x[1:-1].split(','))) for x in btns]
    jls = [int(x) for x in jls.split(',')]
    o = Optimize()
    x = IntVector('x',len(btns))
    for xi in x:
        o.add(xi>=0)
    for i in range(len(jls)):
        s = jls[i]
        v_btns = []
        for j,btn in enumerate(btns):
            if i in btn:
                v_btns.append(j)
        o.add(Sum(x[j] for j in v_btns)==s)
    o.minimize(Sum(x))
    if o.check() == sat:
        return o.model().eval(Sum(x)).as_long()

ls = sys.stdin.readlines()
print(sum(map(p1,ls)))
print(sum(map(p2,ls)))
