import sys
import re
from collections import defaultdict
ls = sys.stdin.readlines()
g = defaultdict(int)
for l in ls:
    x0,y0,x1,y1 = map(int,re.findall(r'\d+',l))
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            if 'turn on' in l:
                g[x,y] = 1
            elif 'toggle' in l:
                g[x,y] = 1- g[x,y]
            elif 'turn off' in l:
                g[x,y] = 0
print(sum(g.values()))

g = defaultdict(int)
for l in ls:
    x0,y0,x1,y1 = map(int,re.findall(r'\d+',l))
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            if 'turn on' in l:
                g[x,y] +=1
            elif 'toggle' in l:
                g[x,y] +=2
            elif 'turn off' in l:
                g[x,y] =max(0,g[x,y]-1)
print(sum(g.values()))








