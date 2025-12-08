import sys
def epoch(g):
    ng = {}
    for x,y in g:
        on = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==dy==0:
                    continue
                nb = x+dx,y+dy
                if nb in g and g[nb]=='#':
                    on+=1
        if g[x,y]=='#' and on in {2,3}:
            ng[x,y] = '#'
        elif g[x,y] =='.' and on == 3:
            ng[x,y] ='#'
        else:
            ng[x,y] = '.'
    return ng
d = {(i,j):c for i,l in enumerate(sys.stdin.readlines()) for j,c in enumerate(l.strip())}
g1 = d
g2 = d
def stuck_on(g):
    xm,ym = max(g2)
    g2[xm,ym] = '#'
    g2[xm,0] = '#'
    g2[0,0] = '#'
    g2[0,ym] = '#'


for i in range(100):
    g1 = epoch(g1)
    stuck_on(g2)
    g2 = epoch(g2)

print(sum(v =='#' for v in g1.values()))
stuck_on(g2)
print(sum(v =='#' for v in g2.values()))

