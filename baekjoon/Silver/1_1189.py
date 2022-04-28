# from collections import deque

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def bfs(x, y):
#     global ans
    
#     que = deque()
#     visited = [[False for i in range(m)] for j in range(n)]
    
#     que.append([x, y])
#     visited[x][y] = True
#     while que:
#         size = len(que)
        
#         for _ in range(size):
#             x, y = que.popleft()
            
#             if x == n - 1 and y == m - 1:
#                 ans += 1
            
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
                
#                 if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 'T':
#                     continue
                
#                 que.append([nx, ny])
#                 visited[nx][ny] = True


# n, m, k = map(int, input().split())
# arr = [list(map(str, input())) for i in range(n)]

# ans = 0
# bfs(0, 0)
# print(ans)



# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# def dfs(x, y, total):
#     ret = 0
#     if total > k :
#         return
    
#     if x == n - 1 and y == m - 1:
#         return 1
    
#     visited[x][y][total] = True
#     if (x + 1 < n and y < m) and not visited[x + 1][y] and arr[x + 1][y] != 'T':
#         dfs(x + 1, y, total + 1)
#     if (x < n and y + 1 < m) and not visited[x][y + 1] and arr[x][y + 1] != 'T':
#         dfs(x, y + 1, total + 1)
        


# n, m, k = map(int, input().split())
# arr = [list(map(str, input())) for i in range(n)]
# visited = [[[False for i in range(k + 1)] for j in range(m)] for k in range(n)]

# print(dfs(0, 0, 0))



# def in_range(a, b):
#     return 0 <= a < n and 0 <= b < m

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# def dfs(x, y, total):
#     ret = 0
#     visited[x][y] = True
    
#     if x == n - 1 and y == m - 1 and total == k:
#         print(f'##{total}')
#         return 1
    
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         ntotal = total + 1
        
#         if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 'T':
#             continue
        
#         ret += dfs(nx, ny, ntotal)
#         visited[nx][ny] = False
        
#     return ret


# n, m, k = map(int, input().split())
# arr = [list(map(str, input())) for i in range(n)]
# visited = [[False for j in range(m)] for k in range(n)]

# print(dfs(0, 0, 0))


def in_range(a, b):
    return 0 <= a < n and 0 <= b < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, total):
    ret = 0
    
    if total > k:
        return 0
    
    if x == n - 1 and y == m - 1 and total == k:
        return 1
    
    visited[x][y] = True
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 'T':
            continue
        
        ret += dfs(nx, ny, total + 1)
        
    visited[x][y] = False
        
    return ret

n, m, k = map(int, input().split())
tmp = [list(map(str, input())) for i in range(n)]
visited = [[False for j in range(m)] for k in range(n)]
arr = tmp[::-1]
print(dfs(0, 0, 1))



# from pprint import pprint

# def recur(x, y, cnt):
#     global ans
#     if x == n or y == m:
#         return
    
#     if arr[x][y] == 'T':
#         return
    
#     if x == n - 1 and y == m - 1 and cnt == k:
#         ans += 1
#         return

#     recur(x + 1, y, cnt + 1)
#     recur(x, y + 1, cnt + 1)
    

# n, m, k = map(int, input().split())
# tmp = [list(map(str, input())) for i in range(n)]
# print('##원래 입력')
# pprint(tmp)
# arr = tmp[::-1] 
# print('##뒤집은 거')
# pprint(arr)
# ans = 0
# recur(0, 0, 1)
# print(ans)