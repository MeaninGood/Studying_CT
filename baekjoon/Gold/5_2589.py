# 16724번_보물섬

## 이동은 상하좌우로 이웃한 육지로만 가능
## 물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있음
## 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 됨
## 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성

'''
# 첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어짐
# L과 W로 표시된 보물 지도가 아래의 예와 같이 주어짐
# 각 문자 사이에는 빈 칸이 없음
# 보물 지도의 가로, 세로의 크기는 각각 50이하
## 첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력

(입력)
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

(출력)
8

'''

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    
    que.append([x, y])
    visited[x][y] = True
    
    ret = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 'W':
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
        ret += 1
        
    return ret

n, m = map(int, input().split())
arr = [input() for _ in range(n)]

mx = -1000000
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            mx = max(mx, bfs(i, j))

print(mx - 1)