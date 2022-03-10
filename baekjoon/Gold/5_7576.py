import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(n, m):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    cnt = 0
    
    temp = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                que.append([i, j])
                visited[i][j] = True
                temp += 1
            elif arr[i][j] == -1:
                visited[i][j] = True

    if temp == 0:
        return -1
    
    while len(que) > 0:        
        size = len(que)
        
        for _ in range(size):
            x = que[0][0]
            y = que[0][1]
            que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0 or visited[nx][ny]:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
        
        if len(que) > 0:
            cnt += 1
        
        else:
            for i in range(n):
                if False in visited[i]:
                    return -1
                else:
                    return cnt
    
print(bfs(n, m))
