with open('mega.in', 'r') as f:
    n = int(f.readline())
    x = list(map(int, f.readlines()))
INV_S = [0] * (n + 1)
INV_R = [0] * (n + 1)


def merge_sort(a, l, r, reverse=False):
    if r - l < 2:
        return 0
    m = (r + l) // 2
    merge_sort(a, l, m, reverse)
    merge_sort(a, m, r , reverse)
    merge(a, l, m, r, reverse)


def merge(a, l, m, r, reverse=False):
    l1, r1 = l, m
    l2, r2 = m, r
    res = []
    while l1 < r1 and l2 < r2:
        if a[l1] < a[l2]:
            if not reverse:
                res.append(a[l1])
                l1 += 1
                INV_S[a[l1 - 1]] += l2 - m
            else:
                res.append(a[l2])
                l2 += 1
                INV_R[a[l2 - 1]] += l1 - l
        else:
            if not reverse:
                res.append(a[l2])
                l2 += 1
            else:
                res.append(a[l1])
                l1 += 1
    while l1 < r1:
        res.append(a[l1])
        l1 += 1
        if not reverse:
            INV_S[a[l1 - 1]] += l2 - m
    while l2 < r2:
        res.append(a[l2])
        l2 += 1
        if reverse:
            INV_R[a[l2 - 1]] += l1 - l
    for i in range(l, r):
        a[i] = res[i - l]


merge_sort(x.copy(), 0, n)
merge_sort(x.copy(), 0, n, True)
ans = sum([INV_S[i] * INV_R[i] for i in range(1, n + 1)])
with open('mega.out', 'w') as f:
    f.write(str(ans))
