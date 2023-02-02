import sys
from collections import deque
from pprint import pprint
input = lambda : sys.stdin.readline().strip()




# 층 범위
def in_stack(x):
    return 0 <= x < z

# x, y 좌표 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 층 추가하기
def bfs():
    global visited
    que = deque()
    
    for a, b, c in v:
        visited[a][b][c] = True
        que.append([a, b, c])

    ret = 0
    while que:
        size = len(que)
        
        for _ in range(size):
            h, x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
    
                nu = h - 1 # 위층
                nd = h + 1 # 아래층
                
                # 위층 갈 수 있는 경우
                if in_stack(nu) and not visited[nu][x][y] and arr[nu][x][y] != -1 and arr[nu][x][y] != 1:
                    visited[nu][x][y] = True
                    que.append([nu, x, y])
                    
                # 아래층 갈 수 있는 경우
                if in_stack(nd) and not visited[nd][x][y] and arr[nd][x][y] != -1 and arr[nd][x][y] != 1:
                    visited[nd][x][y] = True
                    que.append([nd, x, y])
                    
                # 범위 초과하지 않고 사방으로 갈 수 있는 경우
                if in_range(nx, ny) and not visited[h][nx][ny] and arr[h][nx][ny] != -1 and arr[h][nx][ny] != 1:
                    visited[h][nx][ny] = True
                    que.append([h, nx, ny])
        
        if que:
            ret += 1

    return ret





m, n, z = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(z)]
visited = [[[False for i in range(m)] for j in range(n)] for k in range(z)]

# 익은 토마토 배열 [h, x, y]
v = []
for k in range(z):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                v.append([k, i, j])
                
tmp = bfs()

# bfs 돈 후 모든 토마토가 익었는지 체크
for k in range(z):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0 and not visited[k][i][j]:
                print(-1)
                exit()
                
else:
    print(tmp)
    
