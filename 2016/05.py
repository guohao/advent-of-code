from util import *

ans = ''
for d in md5_seq(D):
    if d[:5] == '0' * 5:
        ans += d[5]
        if len(ans) == 8:
            print(ans)
            break

ans = ['x'] * 8
for d in md5_seq(D):
    if d[:5] == '0' * 5:
        p = int(d[5], 16)
        if p < 8 and ans[p] == 'x':
            ans[p] = d[6]
            if 'x' not in ans:
                print(join(ans))
                break
