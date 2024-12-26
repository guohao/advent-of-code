from util import *


def run(s: str, n: int):
    for _ in range(n):
        s = re.sub(r'(\d)\1*', lambda m: str(m.end() - m.start()) + m.group(1), s)
    return len(s)


print(run(raw(), 40))
print(run(raw(), 50))
