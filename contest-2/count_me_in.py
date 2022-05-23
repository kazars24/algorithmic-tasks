nums = list(map(int, input().split()))
min_e, max_e = min(nums), max(nums)
cnt = {x: 0 for x in range(min_e, max_e + 1)}
for i in nums:
    cnt[i] += 1
res = []
for i in range(min_e, max_e + 1):
    res += [i] * cnt[i]
print(' '.join(map(str, res)))
