def recur(x, y):
    if x > n - 1 or y > n - 1:
        return 100000000
 
    if x == n - 1 and y == n - 1:
        return 0
 
    if dp[x][y] != -1:
        return dp[x][y]
 
    dp[x][y] = min(recur(x + 1, y) + arr[x][y], recur(x, y + 1) + arr[x][y])
    return dp[x][y]
 
T = int(input())
 
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1 for i in range(n)] for j in range(n)]
     
    print(f'#{tc} {recur(0, 0) + arr[n - 1][n - 1]}')

