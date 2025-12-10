from collections import defaultdict, deque
from itertools import count
import sys

import re

sys.path.insert(0, "..")
from util import *

PC = "PC"


def run(r, rcv_q, snd_q, p2=None):
    cmds = [line.split() for line in L]

    def v_of(n: str):
        try:
            return int(n)
        except:
            return r[n]

    while 0 <= r[PC] < R:
        op, *opr = cmds[r[PC]]
        if len(opr) == 1:
            a = opr[0]
            b = None
        else:
            a, b = opr
        match op:
            case "snd":
                snd_q.append(v_of(a))
                r["snd_cnt"] += 1
            case "set":
                r[a] = v_of(b)
            case "mul":
                r[a] *= v_of(b)
            case "add":
                r[a] += v_of(b)
            case "mod":
                r[a] %= v_of(b)
            case "rcv":
                if p2:
                    if not rcv_q:
                        return
                    else:
                        r[a] = rcv_q.popleft()
                else:
                    if v_of(a):
                        print(snd_q.pop())
                        return
            case "jgz":
                if v_of(a) > 0:
                    r[PC] += v_of(b)
                    continue
        r[PC] += 1


run(defaultdict(int), deque(), deque())
ar = defaultdict(int) | {"p": 0}
arq = deque()
br = defaultdict(int) | {"p": 1}
brq = deque()
for k in count():
    run(ar, arq, brq, 1)
    run(br, brq, arq, 1)
    if not arq and not brq:
        print(br["snd_cnt"])
        break
