from itertools import permutations
import re
import sys

L = sys.stdin.readlines()


def join(l):
    return "".join(map(str, l))


def f(d: str):
    for line in L:
        line = line.strip()
        nums = list(map(int, re.findall(r"-?\d+", line)))
        if "swap position" in line:
            x, y = sorted(nums)
            d = d[:x] + d[y] + d[x + 1 : y] + d[x] + d[y + 1 :]
        elif "swap letter" in line:
            x = line.split()[2]
            y = line.split()[-1]
            d = re.sub(f"{x}|{y}", lambda m: x if m.group() == y else y, d)
        elif "step" in line:
            x = nums[0] * (-1 if "left" in line else 1)
            d = d[-x:] + d[:-x]
        elif "based on" in line:
            idx = d.index(line[-1])
            rc = (1 + idx + (idx >= 4)) % len(d)
            d = d[-rc:] + d[:-rc]
        elif "reverse" in line:
            x, y = nums
            d = d[:x] + d[x : y + 1][::-1] + d[y + 1 :]
        elif "move" in line:
            x, y = nums
            if x < y:
                d = d[:x] + d[x + 1 : y + 1] + d[x] + d[y + 1 :]
            else:
                d = d[:y] + d[x] + d[y:x] + d[x + 1 :]
        else:
            raise Exception(line)
    return d


print(f("abcdefgh"))
for s in permutations("fbgdceah"):
    s = join(s)
    if f(s) == "fbgdceah":
        print(s)
        break
