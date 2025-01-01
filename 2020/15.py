from util import *

data = D 

seq = list(map(int, data.split(',')))
seen = {}
for t in range(2019):
    if t == len(seq) - 1:
        if seq[t] in seen:
            seq.append(t - seen[seq[t]])
        else:
            seq.append(0)
    seen[seq[t]] = t
print(seq[-1])

seq = list(map(int, data.split(',')))
seen = {}
for t in range(30000000 - 1):
    if t == len(seq) - 1:
        if seq[t] in seen:
            seq.append(t - seen[seq[t]])
        else:
            seq.append(0)
    seen[seq[t]] = t
print(seq[-1])
