import sys
import re
lines = [l[:-1] for l in sys.stdin.readlines()]
print(sum(eval(l[-1].join(l[:-1])) for l in zip(*list(re.findall(r'\S+',line)  for line in lines))))
ls =[''.join(l) for l in zip(*lines[:-1])]
ss =re.findall(r'\S',lines[-1])
i = 0
r2 = 0 
for s in ss:
    j = i 
    while i<len(ls) and ls[i].strip():
        i+=1
    r2+=eval(s.join(ls[j:i]))
    i+=1
print(r2)



