from util import *

print(first(lambda i: md5(f'{D}{i}').startswith('0' * 5)))
print(first(lambda i: md5(f'{D}{i}').startswith('0' * 6)))
