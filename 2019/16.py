from util import *


def p1():
    def fft(s: str):
        s = '0' + s
        out = ''
        cums = [0]
        for x in s:
            cums.append(cums[-1] + int(x))
        for i in range(len(s)):
            total = 0
            step = i + 1
            for j in range(0, len(s), 4 * step):
                total += cums[min(j + 2 * step, len(s))] - cums[min(j + step, len(s))]
                total -= cums[min(j + 4 * step, len(s))] - cums[min(j + 3 * step, len(s))]
            out += str(total)[-1]
        return out

    data = D
    for _ in range(100):
        data = fft(data)
    print(data[:8])


def p2():
    data = (D * 10000)[int(D[:7]):]

    def fft2(s: str):
        out = ''
        cum = 0
        for i in s[::-1]:
            cum += int(i)
            out = str(cum)[-1] + out
        return out

    for t in range(100):
        data = fft2(data)
    print(data[:8])


p1()
p2()
