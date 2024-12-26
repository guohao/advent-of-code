from util import *

print(join(Counter(s).most_common(1)[0][0] for s in zip(*L)))
print(join(Counter(s).most_common()[-1][0] for s in zip(*L)))
