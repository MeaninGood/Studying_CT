# m, n = map(int, input().split())

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# visited = [[False for i in range(m)] for j in range(n)]

# def dfs(x, y):
#     visited[x][y] = True
    
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
        
#         if not (0 <= nx <= n - 1 and 0 <= ny < m - 1) or visited[nx][ny]:
#             continue
        
#         dfs(nx, ny)
        
#     return x, y
        

# dfs(0, 0)

from pprint import pprint

m, n = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x = 0
y = 0
for i in range(1, n * m + 1):
    arr[x][y] = i

    nx = x + dx[d]
    ny = y + dy[d]
    
    if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
        d = (d + 1) % 4
    
    x += dx[d]
    y += dy[d]
        
for i in range(n):
    for j in range(m):
        if arr[i][j] == (n * m):
            print(j, i)
            exit()
        
