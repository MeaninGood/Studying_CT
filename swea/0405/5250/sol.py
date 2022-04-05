from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    que = deque()
    visited = [[False for i in range(n)] for j in range(n)]
    li = set()
    
    que.append([x, y])
    visited[x][y] = True
    li.add(arr[x][y])
    
    ret = 0
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            if x == n - 1 and y == n - 1:
                return ret
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny]:
                    continue         
                    
                que.append([nx, ny])
                visited[nx][ny] = True
                
                if arr[nx][ny] > arr[x][y] and arr[nx][ny] not in li:
                    ret += arr[nx][ny] - arr[x][y]
            
                li.add(arr[nx][ny])
                
                    
        # if arr[x][y] != arr[nx][ny] and arr[nx][ny] > arr[x][y]:
        #     ret += arr[nx][ny] - arr[x][y]
            
        ret += 1
    
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for i in range(n)] for j in range(n)]

print(bfs(0, 0))


# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# def dfs(x, y):
#     ret = [0, arr[x][y]]
#     visited[x][y] = True
    
#     if x == n - 1 and y == n - 1:
#         return
    
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]

#         if not in_range(nx, ny) or visited[nx][ny]:
#             continue
        
#         li = dfs(nx, ny)
        
#         ret[0] += li[0]
#         if li[1] > ret[1]:
#             ret[1] += li[1]
    
    

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False for i in range(n)] for j in range(n)]