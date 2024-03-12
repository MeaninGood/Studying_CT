import sys

input = lambda: sys.stdin.readline().strip()

m, n = map(int, input().split())

def in_range(x, y):
    return 1 <= x < n + 1 and 1 <= y < m + 1

# 방향 저장할 배열
visited = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

dp  = [[[-1 for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]
# 아래, 오른쪽
dx = [1, 0]
dy = [0, 1]
def recur(x, y, dir):
  
    if x == n and y == m:
        return 1
    
    if dir != -1:
        visited[x][y] = dir
        
    if dp[x][y][dir] != -1:
        return dp[x][y][dir]
    
    ret = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if dir == -1:
            visited[x][y] = i
        
        # 범위 넘거나, 왼쪽 위와 같은 방향이면 continue
        if not in_range(nx, ny) or visited[x - 1][y - 1] == i:
            continue
        
        ret += recur(nx, ny, i)
        
    dp[x][y][dir] = ret % 100000
    visited[x][y] = -1
        
    return dp[x][y][dir]

print(recur(1, 1, -1))