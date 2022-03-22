from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    que = deque()
    visited = [[False for i in range(n)] for j in range(n)]

    que.append([x, y])
    visited[x][y] = True

    ret = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que[0][0], que[0][1]
            que.popleft()
            
            if arr[x][y] == 3:
                return ret - 1
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 1:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
        ret += 1
    return 0

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    sx, sy = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                sx, sy = i, j
                
    print(f'#{tc} {bfs(sx, sy)}') 
