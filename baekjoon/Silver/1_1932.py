import sys
from pprint import pprint
input = sys.stdin.readline

n = int(input())
arr = [[0] + list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n + 1)] for j in range(n)]
dp[-1] = arr[-1]

for i in range(n - 1)[::-1]:
    for j in range(1, i + 2):
        dp[i][j] = max(arr[i][j] + dp[i + 1][j], arr[i][j] + dp[i + 1][j + 1])
        
print(dp[0][1])