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
    
    d = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que[0][0], que[0][1]
            que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dx[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or (v[x][y] + 1 != v[nx][ny]):
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True

        d += 1
    
    return d

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]

    ans = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            ans.append(bfs(i, j))
            
    print(ans)