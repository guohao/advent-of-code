import sys
import re

ps = sys.stdin.read().split("\n\n")
gift = {}
for para in ps[:-1]:
    parts = para.split(":")
    gift[int(parts[0])] = parts[1].count("#")
r = 0
for region in ps[-1].splitlines():
    ns = list(map(int, re.findall(r"\d+", region)))
    R, C = ns[:2]
    need = sum(gift[i] * cnt for i, cnt in enumerate(ns[2:]))
    if need * 1.2 < R * C:
        r += 1
print(r)
