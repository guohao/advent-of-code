import sys
import re
r1 = 0 
r2 = 0 
for pair in sys.stdin.read().strip().replace('\n','').split(','):
    f,t = map(int,pair.split('-'))
    for i in range(f,t+1):
        s = str(i)
        l = len(s)
        if re.fullmatch("(\\w+)\1+",s):
            r2+=1
        if l%2 ==1:
            continue
        m = len(s)//2
        if s[:m]==s[m:]:
            r1+=i
print(r1)
print(r2)
