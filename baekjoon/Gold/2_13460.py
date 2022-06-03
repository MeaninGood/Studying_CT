import sys
from collections import deque
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    
    que.append([x, y])
    visited[x][y] = True
    
    while que:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                while 1:
                    if not in_range(nx, ny) or arr[nx][ny] == '#' or visited[nx][ny]:
                        continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
    
n, m = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(n)]

rx, ry, bx, by, ex, ey = 0, 0, 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        
        elif arr[i][j] == 'B':
            bx, by = i, j
        
        elif arr[i][j] == 'O':
            ex, ey = i, j