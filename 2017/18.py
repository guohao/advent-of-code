from collections import defaultdict, deque
from itertools import count
import sys

L = sys.stdin.readlines()
R = len(L)
PC = "PC"


def v_of(n: str, r):
    try:
        return int(n)
    except:
        return r[n]


def run(r, rcv_q, snd_q, p2=None):
    cmds = [line.split() for line in L]
    while 0 <= r[PC] < R:
        op, *opr = cmds[r[PC]]
        if len(opr) == 1:
            a = opr[0]
            b = None
        else:
            a, b = opr
        match op:
            case "snd":
                snd_q.append(v_of(a, r))
                r["snd_cnt"] += 1
            case "set":
                r[a] = v_of(b, r)
            case "mul":
                r[a] *= v_of(b, r)
            case "add":
                r[a] += v_of(b, r)
            case "mod":
                r[a] %= v_of(b, r)
            case "rcv":
                if p2:
                    if not rcv_q:
                        return
                    r[a] = rcv_q.popleft()
                else:
                    if v_of(a, r):
                        print(snd_q[-1])
                        return
            case "jgz":
                if v_of(a, r) > 0:
                    r[PC] += v_of(b, r)
                    continue
        r[PC] += 1


run(defaultdict(int), deque(), deque())
ar = defaultdict(int)
ar["p"] = 0
arq = deque()
br = defaultdict(int)
br["p"] = 1
brq = deque()
for k in count():
    run(ar, arq, brq, 1)
    run(br, brq, arq, 1)
    if not arq and not brq:
        print(br["snd_cnt"])
        break
