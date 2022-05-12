n = int(input())
idx = 9
tmp = n - 1

dp = [0 for i in range(n + 1)]
dp[0] = 0
dp[1] = 9
total = 0
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 2)  % 1000000000
    
print(dp[n] % 1000000000)