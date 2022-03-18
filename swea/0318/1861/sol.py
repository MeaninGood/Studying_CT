# from collections import deque

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n


# def bfs(x, y):
#     que = deque()
#     visited = [[False for i in range(n)] for j in range(n)]
    
#     d = 0
#     que.append([x, y])
#     visited[x][y] = True
    
#     while len(que) > 0:
#         size = len(que)
        
#         for _ in range(size):
#             x, y = que[0][0], que[0][1]
#             que.popleft()

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#                 if not in_range(nx, ny) or visited[nx][ny] or (v[nx][ny] != v[x][y] + 1):
#                     continue
                
#                 que.append([nx, ny])
#                 visited[nx][ny] = True

#         d += 1
    
#     return d

# T = int(input())

# for tc in range(1, T + 1):
#     n = int(input())
#     v = [list(map(int, input().split())) for _ in range(n)]

#     ans = []
#     for i in range(n):
#         for j in range(n):
#             ans.append(bfs(i, j))
            
#     print(ans)
    
    
    
    
# n = int(input())
# v = [list(map(int, input().split())) for _ in range(n)]

# ans = []
# for i in range(n):
#     for j in range(n):
#         ans.append(bfs(i, j))
        
# print(ans)



# def dfs(x, y):
#     ret = 1
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] != '1':
#             continue
#
#         ret += dfs(nx, ny)
#
#     return ret


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    ret = 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not in_range(nx, ny) or (v[nx][ny] != v[x][y] + 1):
            continue
        
        ret = max(ret, dfs(nx, ny) + 1)
    
    dp[x][y] = ret
    
    return ret

T = int(input())


### 처음 코드
# for tc in range(1, T + 1):
#     n = int(input())
#     v = [list(map(int, input().split())) for _ in range(n)]

#     dp = [[-1 for i in range(n)] for j in range(n)]
    
#     ans = 0
#     idx = 10000000
#     for i in range(n):
#         for j in range(n):
#             ans = max(ans, dfs(i, j))

#     idx = 10000000000
#     for i in range(n):
#         for j in range(n):
#             if dp[i][j] == ans:
#                 idx = min(idx, v[i][j])

#     print(f'#{tc} {idx} {ans}')
    

### 수정한 코드
for tc in range(1, T + 1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]

    dp = [[-1 for i in range(n)] for j in range(n)]
    
    ans = 0
    idx = 0
    for i in range(n):
        for j in range(n):
            x = dfs(i, j)
            if ans < x :
                ans = x
                idx = v[i][j]
            
            elif ans == x and idx > v[i][j]:
                idx = v[i][j]

    print(f'#{tc} {idx} {ans}')






