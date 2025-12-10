import re
import sys
import string

D = input().strip()


def dance(s: str) -> str:
    s = list(s)
    for cmd in D.split(","):
        if cmd[0] == "s":
            x = int(cmd[1:])
            s = s[-x:] + s[:-x]
        elif cmd[0] == "x":
            a, b = map(int, cmd[1:].split("/"))
            s[a], s[b] = s[b], s[a]
        elif cmd[0] == "p":
            a, b = cmd[1:].split("/")
            ia, ib = s.index(a), s.index(b)
            s[ia], s[ib] = s[ib], s[ia]
    return "".join(s)


ans = string.ascii_lowercase[:16]
print(dance(ans))
seen = {}
N = 1000000000
for i in range(N):
    if ans in seen:
        cycle = i - seen[ans]
        remaining = N - i
        i += (remaining // cycle) * cycle
        for _ in range(remaining % cycle):
            ans = dance(ans)
        break
    seen[ans] = i
    ans = dance(ans)
print(ans)
