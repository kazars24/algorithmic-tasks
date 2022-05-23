n, m = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

a2pos = {}
for i in range(n):
    v = a[i]
    if v not in a2pos:
        a2pos[v] = []
    a2pos[v].append(i + 1)

a2max = {}
for v in a2pos:
    v_pos = a2pos[v]
    max_f = 0
    for i in range(len(v_pos)):
        l_weight = i + 1
        r_weight = n - v_pos[i] - (len(v_pos) - (i + 1))
        max_f = max(max_f, l_weight * r_weight)
    a2max[v] = max_f

ans = [a2max.get(v, 0) for v in x]
print(*ans)
