import sys
import re

tt = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
ttm = {}
for l in tt.split("\n"):
    i, c = l.split(":")
    ttm[i] = int(c)

greaters = ["trees", "cats"]
fewers = ["pomeranians", "goldfish"]
for l in sys.stdin.readlines():
    l = l.strip()
    i = re.findall(r"(?<=Sue )\d+(?=:)", l)[0]
    if all(
        int(m[2]) == ttm[m[1]] for m in re.finditer(r"(\w+): (\d+)", l) if m[1] in ttm
    ):
        print("r1", i)
        break
    for m in re.finditer(r"(\w+): (\d+)", l):
        k = m[1]
        v = int(m[2])
        if k in greaters:
            if ttm[k] > v:
                break
        elif k in fewers:
            if ttm[k] < v:
                break
        else:
            if k in ttm and ttm[k] != v:
                break
    else:
        print("r2", i)
