import re

r = 0
while True:
    s = input()
    if not s:
        break
    if not re.search(r'(\w{2}).*\1', s):
        continue
    if not re.search(r'(\w)\w\1', s):
        continue
    r += 1
print(r)