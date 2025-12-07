import sys
import re
r1 = 0
r2 = 0
for pair in sys.stdin.read().strip().replace('\n','').split(','):
    f,t = map(int,pair.split('-'))
    for i in range(f,t+1):
        s = str(i)
        l = len(s)
        if re.fullmatch(r'(\S+?)\1',s):
            r1+=i
        if re.fullmatch(r"(\S+)\1+",s):
            r2+=i
print(r1)
print(r2)
