n = int(input())
arr = [[0 for i in range(3)]] + [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(3)] for j in range(n + 1)]

for i in range(1, n + 1):
    mn = 1000000
    midx = 0
    for j in range(3):
        if mn > dp[i - 1][j]:
            mn = dp[i - 1][j]
            midx = j

    for j in range(3):
        if j == midx:
            continue

        dp[i][j] = mn + arr[i][j]

    mn = 1000000
    for j in range(3):
        if j == midx:
            continue

        mn = min(mn, dp[i - 1][j])

    dp[i][midx] = mn + arr[i][midx]

print(min(dp[n]))