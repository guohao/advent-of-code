import sys
parts = sys.stdin.read().split('\n\n')

ft = set()
for line in parts[0].split('\n'):
    f,t= map(int,line.split('-'))
    ft.add((f,t))

while True:
    nft = ft.copy()
    for f0,t0 in ft:
        for f1,t1 in ft - {(f0,t0)}:
            if (f0-t1)*(t0-f1)<=0:
                nft.add((min(f0,f1),max(t0,t1)))
    if ft == nft:
        break
    ft = nft
while True:
    nft = ft.copy()
    for f0,t0 in nft.copy():
        for f1,t1 in nft- {(f0,t0)}:
            if f0<=f1 and t0>=t1:
                if (f1,t1) in nft:
                    nft.remove((f1,t1))
    if ft == nft:
        break
    ft = nft





r1 = 0
for line in parts[1].split('\n'):
    if not line.strip():
        continue
    i = int(line.strip())
    for f,t in ft:
        if f<=i<=t:
            r1+=1
            break

print(r1)
print(sum(t-f+1 for f,t in ft))
