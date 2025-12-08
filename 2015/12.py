import json
import sys
import re

d = input()
print(sum(map(int, re.findall(r"-?\d+", d))))


def walk(j):
    if isinstance(j, dict):
        if "red" in j.values():
            return 0
        else:
            return sum(walk(k) + walk(v) for k, v in j.items())
    elif isinstance(j, list):
        return sum(walk(k) for k in j)
    elif isinstance(j, int):
        return j
    elif isinstance(j, str):
        return sum(map(int, re.findall("-?\d+", j)))


print(walk(json.loads(d)))
