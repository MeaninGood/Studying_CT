from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(1001)] for j in range(1001)]
    
    que.append([x, y])
    visited[x][y] = True
    ret = 0
    while que:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            if x == ex and y == ey:
                return ret
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not (0 <= nx < 1001 and 0 <= ny < 1001) or visited[nx][ny] or arr[nx][ny] != -1:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
        ret += 1
    

r, c, n = map(int, input().split())

ex = 500 + r
ey = 500 + c 
arr = [[-1 for i in range(1001)] for j in range(1001)]

for i in range(n):
    a, b = map(int, input().split())
    
    arr[500 + a][500 + b] = 1


print(bfs(500, 500))
