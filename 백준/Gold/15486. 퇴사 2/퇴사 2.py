import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n + 1)]

for i in range(n):
    if arr[i][0] <= n - i:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])
        
    dp[i + 1] = max(dp[i + 1], dp[i])
        
print(dp[n])