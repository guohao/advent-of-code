import sys
import re
I, J = list(map(int,re.findall(r'-?\d+',sys.stdin.read())))
c = 20151125
i = j = 1
while True:
    while i != 0:
        j += 1
        i -= 1
        c = c * 252533 % 33554393
        if i == I and j == J:
            print(c)
            exit()
    i = j
    j = 1
