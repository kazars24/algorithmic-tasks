N = int(input())
dp, path = [0] * (N + 1), [0] * (N + 1)
for i in range(2, N + 1):
    dp[i], path[i] = dp[i - 1] + 1, i - 1
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i], path[i] = dp[i // 2] + 1, i // 2
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i], path[i] = dp[i // 3] + 1, i // 3

ans, x = [], N
op_to_diff = {
    '1': lambda x, y: y == x - 1,
    '2': lambda x, y: y == x / 2,
    '3': lambda x, y: y == x / 3
}
while dp[x] != 0:
    new_x = path[x]
    for op, diff in op_to_diff.items():
        if diff(x, new_x):
            ans.append(op)
            break
    x = new_x

print(''.join(ans[::-1]))
