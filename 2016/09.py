from util import *

d = D
i = 0
ans = 0
while i < len(d):
    if d[i] == '(':
        j = i + 1
        while d[j] != ')':
            j += 1
        a, b = map(int, d[i + 1:j].split('x'))
        ans += a * b
        i = j + a
    else:
        ans += 1
    i += 1
print(ans)


def x(s: str) -> int:
    m = re.search(r'\((\d+)x(\d+)\)', s)
    if not m:
        return len(s)
    a, b = map(int, m.groups())
    return m.start() + x(s[m.end():m.end() + a]) * b + x(s[m.end() + a:])


print(x(d))
