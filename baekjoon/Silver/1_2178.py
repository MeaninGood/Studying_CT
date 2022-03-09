# 2178번_미로 탐색

## N×M크기의 배열로 표현되는 미로
## 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸
## (1, 1)에서 출발, (N, M)로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램

'''
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)
# 다음 N개의 줄에는 M개의 정수로 미로가 주어짐
# 각각의 수들은 붙어서 입력으로 주어짐
## 첫째 줄에 지나야 하는 최소의 칸 수를 출력
## 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진

(입력)
4 6
101111
101010
101011
111011

(출력) 
15

'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
    
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    cnt = 0
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        cnt += 1
        
        for _ in range(size):
            x = que[0][0]
            y = que[0][1]
            que.popleft()
            
            if (x == n - 1) and (y == m - 1):
                return cnt
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 1 or visited[nx][ny]:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True               
    
print(bfs(0, 0))