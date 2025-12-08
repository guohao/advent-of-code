import json
import sys
import re

d = sys.stdin.read()
print(sum(re.findall(r"-?\d+", d)))
