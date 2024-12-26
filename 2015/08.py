from util import *

print(counts(lambda s: len(s) - len(eval(s))))
print(counts(lambda s: s.count('\\') + s.count('"') + 2))
