# import sys

# input = lambda: sys.stdin.readline().strip()

# n, m = map(int, input().split())
# arr = [[0 for _ in range(m + 2)]] + [[0] + list(map(int, input())) + [0] for _ in range(n)] + [[0 for _ in range(m + 2)]]

# prefix = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
# suffix = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
# mx = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + (arr[i][j] == 0)
#         suffix[i][j] = suffix[i - 1][j] + suffix[i][j - 1] - suffix[i - 1][j - 1] + (arr[i][j] == 1)
        
#         if arr[i][j] == 1:
#             continue
        
#         for x in range(i):
#             for y in range(j):
#                 if suffix[i][j] or suffix[x][y]:
#                     continue
                
#                 mx = max(prefix[i][j] - prefix[x][j] - prefix[i][y] + prefix[x][y], mx)
# print(mx)


import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [[0] + list(map(int, input())) for _ in range(n)]
print(arr)
dp = [[0] * (m + 1) for _ in range(n + 1)]

mx = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            mx = max(mx, dp[i][j])
print(dp)
print(mx * mx)