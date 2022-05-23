import math


def dist_func(x, a, v_p, v_f):
    dist = math.sqrt(x * x + (1 - a) * (1 - a)) / v_p + math.sqrt(a * a + (1 - x) * (1 - x)) / v_f
    return dist


v_p, v_f = list(map(int, input().split()))
a = float(input())

left = 0
right = 1
while right - left >= 0.00000001:
    g = right - (right - left) / 3
    f = left + (right - left) / 3
    if dist_func(f, a, v_p, v_f) < dist_func(g, a, v_p, v_f):
        right = g
    else:
        left = f

print(left)
