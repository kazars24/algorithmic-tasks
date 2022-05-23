import sys
from functools import cmp_to_key


def cmp(x, y):
    return 1 if x + y > y + x else -1


v = list()
for line in sys.stdin:
    v.append(line[:-1])
v.sort(key=cmp_to_key(cmp), reverse=True)
print(''.join(v))
