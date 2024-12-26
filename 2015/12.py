import json

from util import *

print(sum(ints(D)))
print(sum(ints(str(json.loads(D, object_hook=lambda o: {} if "red" in o.values() else o)))))
