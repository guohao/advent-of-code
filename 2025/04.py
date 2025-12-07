import sys
from collections import defaultdict
g = {}
for i,line in enumerate(sys.stdin.readlines()):
    for j,c in enumerate(line.strip()):
        if c == '@':
            g[i,j] = c
ret=[]
while True:
    rm = set()
    for i,j in g.keys():
        adj_cnt = 0
        for c in range(i-1,i+2):
            for r in range(j-1,j+2):
                if c==i and r==j:
                    continue
                if (c,r) in g :
                    adj_cnt +=1
        if adj_cnt < 4:
            rm.add((i,j))
    if len(rm) ==0:
        break
    for i,j in rm:
        del g[i,j]
    ret.append(len(rm))
print(ret[0])
print(sum(ret))


