from util import *

ans = ['' for _ in range(40)]
ans[0] = D
for i in range(1, 40):
    for j in range(len(D)):
        l = '.' if j - 1 < 0 else ans[i - 1][j - 1]
        m = ans[i - 1][j]
        r = '.' if j + 1 == len(D) else ans[i - 1][j + 1]
        if l == '^' == m and r == '.':
            ans[i] += '^'
        elif m == r == '^' and l == '.':
            ans[i] += '^'
        elif m == '.' == r and l == '^':
            ans[i] += '^'
        elif m == '.' == l and r == '^':
            ans[i] += '^'
        else:
            ans[i] += '.'
print(sum(s.count('.') for s in ans))

ans = D.count('.')


def subf(m: re.Match) -> str:
    l = '.' if m.start() - 1 < 0 else D[m.start() - 1]
    r = '.' if m.start() + 1 == len(D) else D[m.start() + 1]
    return '^' if l != r else '.'


for i in range(400000 - 1):
    D = re.sub(r'[.\\^]', subf, D)
    ans += D.count('.')
print(ans)
