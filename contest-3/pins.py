n = int(input())
a = list(map(int, input().split()))
a.sort()
dp = [[0 for i in range(2)] for j in range(n)]
dp[1][0] = a[1] - a[0]
dp[1][1] = a[1] - a[0]
for i in range(2, n):
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + (a[i] - a[i - 1])
    dp[i][0] = dp[i - 1][1]
print(dp[n - 1][1])
