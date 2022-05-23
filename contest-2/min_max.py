import io
import os
import sys


def read_all():
    bytes = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines()
    return list(map(lambda x: x.decode(), bytes))


def write_all(v):
    sys.stdout.write('\n'.join(v) + '\n')


all_it = iter(read_all())
n, m, l = map(int, next(all_it).split())
A = [list(map(int, next(all_it).split())) for _ in range(n)]
B = [list(map(int, next(all_it).split())) for _ in range(m)]


def solve(x, y):
    left, right = -1, l
    while right - left > 1:
        mid = (right + left) // 2
        if x[mid] < y[mid]:
            left = mid
        else:
            right = mid
    if right == l or left >= 0 and max(x[left], y[left]) < max(x[right], y[right]):
        return left
    return right


q = int(next(all_it))
out = [''] * q
for idx in range(q):
    i, j = map(int, next(all_it).split())
    a, b = A[i - 1], B[j - 1]
    out[idx] = str(solve(a, b) + 1)
write_all(out)
