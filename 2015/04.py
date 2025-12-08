from hashlib import md5
from itertools import count

sk = input()
r1 = True
for i in count():
    d = md5((sk + str(i)).encode()).hexdigest()
    if d[:5] == "00000":
        if r1:
            print(i)
            r1 = False
        if d[:6] == "000000":
            print(i)
            break
