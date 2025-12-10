import re
import sys

L = sys.stdin.readlines()
from collections import deque

from functools import reduce

import math


def f(p2=None):
    pc = [0, 0]
    dest = {}
    types = {}
    states = {}
    for line in L:
        f, t = line.strip().split(" -> ")
        name = f if f[0] not in "%&" else f[1:]
        dest[name] = [x.strip() for x in t.split(",")]

        if f[0] == "%":
            types[name] = "%"
            states[name] = 0
        elif f[0] == "&":
            types[name] = "&"
            states[name] = {}
        else:
            types[name] = name
    for m, tos in dest.items():
        for t in tos:
            if t in types and types[t] == "&":
                states[t][m] = 0
    q = deque()

    def send(name, pulse):
        pc[pulse] += len(dest[name])  # 计数发送的脉冲
        for to in dest[name]:
            q.append((name, to, pulse))

    needs = {"sg", "dh", "db", "lm"}
    cycles = {x: 0 for x in needs}
    source = "jm"
    max_iter = 1000 if not p2 else 10000
    for i in range(max_iter):
        pc[0] += 1  # 按钮发送的低脉冲
        q.append(("button", "broadcaster", 0))
        while q:
            prev, curr, p = q.popleft()
            if p2:
                if p and prev in cycles.keys() and curr == source and not cycles[prev]:
                    cycles[prev] = i + 1
                    if all(cycles.values()):
                        print(reduce(math.lcm, cycles.values()))
                        return
            if curr not in types:
                continue
            match types[curr]:
                case "broadcaster":
                    send(curr, p)
                case "%":
                    if p == 0:
                        states[curr] = 1 - states[curr]
                        send(curr, states[curr])
                case "&":
                    states[curr][prev] = p
                    send(curr, not all(states[curr].values()))
    # 处理完所有按钮后打印结果
    if not p2:
        print(math.prod(pc))


f()
f(1)
