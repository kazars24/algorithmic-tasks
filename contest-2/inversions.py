def merge_sort(a, l, r):
    if r - l < 2:
        return 0
    m = (r + l) // 2
    return merge_sort(a, l, m) + merge_sort(a, m, r) + merge(a, l, m, r)


def merge(a, l, m, r):
    l1, r1 = l, m
    l2, r2 = m, r
    res = []
    inv = 0
    while l1 < r1 and l2 < r2:
        if a[l1] < a[l2]:
            res.append(a[l1])
            l1 += 1
            inv += l2 - m
        else:
            res.append(a[l2])
            l2 += 1
    while l1 < r1:
        res.append(a[l1])
        l1 += 1
        inv += l2 - m
    while l2 < r2:
        res.append(a[l2])
        l2 += 1
    for i in range(l, r):
        a[i] = res[i - l]
    return inv


with open('inverse.in', 'r') as f:
    n = int(f.readline())
    x = list(map(int, f.readline().split()))
ans = merge_sort(x, 0, n)
with open('inverse.out', 'w') as f:
    f.write(str(ans))
