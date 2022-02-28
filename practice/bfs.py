# from collections import deque

# def bfs(s):
#     que = deque()
#     visited = [False for i in range(n + 1)]
    
#     que.append(s)
#     visited[s] = True
#     while len(que) > 0:
#         cur = que[0]
#         que.popleft()
        
        
#         for nxt in v[cur]:
#             if visited[nxt]:
#                 continue
            
#             que.append(nxt)
#             visited[nxt] = True
            
# n, m, s = map(int, input().split())
# v = [[] for i in range(n + 1)]

# for i in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)
    
    
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    
    d = 1
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x = que[0][0]
            y = que[0][1]
            que.popleft()
        
            if x == n - 1 and y == m - 1:
                print(d)
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] or arr[nx][ny] != '1':
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                print(que)
                
        d += 1
    
n, m = map(int, input().split())
arr =  [input() for i in range(n)]

bfs(0, 0)
