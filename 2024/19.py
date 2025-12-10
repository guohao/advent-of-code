import sys

L = sys.stdin.readlines()
ps = set(L[0].strip().split(", "))
max_len = max(len(pat) for pat in ps)

t = 0
for line in L[2:]:
    line = line.strip()
    n = len(line)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for l in range(1, min(max_len, i) + 1):
            if dp[i - l] and line[i - l : i] in ps:
                dp[i] = True
                break

    if dp[n]:
        t += 1

print(t)

t = 0
for line in L[2:]:
    line = line.strip()
    n = len(line)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n + 1):
        for p in ps:
            l = len(p)
            if i >= l and line[i - l : i] == p:
                dp[i] += dp[i - l]
    t += dp[n]

print(t)
