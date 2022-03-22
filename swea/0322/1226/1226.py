from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < 16 and 0 <= y < 16

def bfs(x, y):
    que = deque()
    visited = [[False for i in range(16)] for j in range(16)]
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que[0][0], que[0][1]
            que.popleft()
            
            if v[x][y] == 3:
                return 1
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or v[nx][ny] == 1:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
    return 0

for tc in range(10):
    n = int(input())
    v = [list(map(int, input())) for _ in range(16)]
    
    sx, sy = 0, 0
    for i in range(16):
        for j in range(16):
            if v[i][j] == 2:
                sx, sy = i, j
                break
                 
    print(f'#{n} {bfs(sx, sy)}')
    
    

