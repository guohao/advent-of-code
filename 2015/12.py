import json

from util import *

print(sum(ints(raw())))
print(sum(ints(str(json.loads(raw(), object_hook=lambda o: {} if "red" in o.values() else o)))))
