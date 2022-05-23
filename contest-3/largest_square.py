def solve(dp, n, m):
    if n == 1 and m == 1:
        return 1, 1, 1
    max_i, max_j, max_size = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if dp[i][j] > 0:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            if dp[i][j] > max_size:
                max_size = dp[i][j]
                max_i, max_j = i - max_size + 1, j - max_size + 1
    return max_size, max_i + 1, max_j + 1


n, m = map(int, input().split())
a = [None] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
x, y, z = solve(a, n, m)
print(x)
print(y, z)
