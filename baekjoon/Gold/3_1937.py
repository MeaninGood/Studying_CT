import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 1, 0, -1]
dy= [1, 0, -1, 0]

def dfs(x, y):
    global ans
    
    ret = 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not in_range(nx, ny) or arr[nx][ny] <= arr[x][y]:
            continue

        ret = max(ret, dfs(nx, ny) + 1)
        
    dp[x][y] = ret
    return ret



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for i in range(n)] for j in range(n)]

ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
        
print(ans)