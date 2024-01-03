from collections import deque

n, m = map(int, input().split())
arr = [input() for i in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y, hand):
    que = deque()
    visited = [[[False for k in range(2)] for i in range(m)] for j in range(n)]
    
    que.append([x, y, hand])
    visited[x][y][hand] = True
    
    d = 1
    while que:
        size = len(que)
        
        for _ in range(size):
            x, y, hand = que.popleft()
            
            if x == n - 1 and y == m - 1:
                return d
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # if not in_range(nx, ny) or visited[nx][ny]:
                #     continue
                
                if not in_range(nx, ny):
                    continue
                
                nhand = hand + int(arr[nx][ny])
                
                if nhand > 1 or visited[nx][ny][nhand]:
                    continue
                
                # 벽인 경우에 continue 조건 -> 딱 하나 ! 내가 벽을 뚫고 왔어 이미
                
                que.append([nx, ny, nhand])
                visited[nx][ny][nhand] = True
                
        d += 1
        
    return -1


print(bfs(0, 0, 0))