import sys
from hashlib import md5
from itertools import count

D = input().strip()
ans = ""

for i in count():
    s = md5((D + str(i)).encode()).hexdigest()[:6]
    if s[:5] == "0" * 5:
        ans += s[-1]
        if len(ans) == 8:
            break
print(ans)

ans = ["x"] * 8
for i in count():
    s = md5((D + str(i)).encode()).hexdigest()[:7]
    if s[:5] == "0" * 5:
        p = int(s[5], 16)
        if p < 8 and ans[p] == "x":
            ans[p] = s[6]
            if "x" not in ans:
                print("".join(ans))
                break
