# m, n = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(m)]

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# cnt = 0
# def recur(x, y):
#     global cnt
#     # visited = [[False for i in range(n)] for j in range(m)]

#     if x == m - 1 and y == n - 1:
#         return 1
    
#     # visited[x][y] == True
    
#     # if arr[x][y] > arr[x+1][y] and not visited[x+1][y]:
#     #     recur(x+1, y)
#     # elif arr[x][y] > arr[x][y+1] and not visited[x][y+1]:
#     #     recur(x, y+1)
#     # elif arr[x][y] > arr[x][y-1] and not visited[x][y-1]:
#     #     recur(x, y-1)
    
#     if (0 <= x+1 < m) and arr[x][y] > arr[x+1][y]:
#         recur(x+1, y)
#     if (0 <= y+1 < n) and arr[x][y] > arr[x][y+1]:
#         recur(x, y+1)
#     if (0 <= y+1 < n) and arr[x][y] > arr[x][y-1]:
#         recur(x, y-1)
    
#     return
    
# recur(0, 0)

# print(cnt)



m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dp = [[-1 for i in range(n)] for j in range(m)]
    
def recur(x, y):
    ret = 0
   
    if x == m - 1 and y == n - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < m and 0 <= ny < n) or arr[nx][ny] >= arr[x][y]:
            continue
        
        ret += recur(nx, ny)
    
    dp[x][y] = ret
    
    return ret
print(recur(0, 0))
