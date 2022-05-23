def cnt(dp, i, j, H, W):
    if not (0 <= i < H and 0 <= j < W):
        return 0
    if dp[i][j] == 0:
        a = cnt(dp, i + 1, j - 2, H, W)
        b = cnt(dp, i - 1, j - 2, H, W)
        c = cnt(dp, i - 2, j - 1, H, W)
        d = cnt(dp, i - 2, j + 1, H, W)
        dp[i][j] = a + b + c + d
    return dp[i][j]


n, m = map(int, input().split())
dp = [[0 for j in range(m)] for i in range(n)]
dp[0][0] = 1
ans = cnt(dp, n - 1, m - 1, n, m)
print(ans)
