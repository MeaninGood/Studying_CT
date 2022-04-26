import sys
input = sys.stdin.readline

n = int(input())
dp = [-1 for i in range(1000010)]
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 3
dp[6] = 2

ans = [n]
if n > 6:
    for i in range(6, n + 1):
        if i % 6 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1)
            
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
            
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)

        else:
            dp[i] = dp[i - 1] + 1
    print(dp[n])
else:
    print(dp[n])
