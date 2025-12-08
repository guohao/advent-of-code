d = input()
print(d.count("(") - d.count(")"))

f = 0
for i, c in enumerate(d):
    f += 1 if c == "(" else -1
    if f == -1:
        print(i + 1)
        break
