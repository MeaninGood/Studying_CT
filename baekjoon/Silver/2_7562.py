# 7562번_나이트의 이동

## 체스판 위에 한 나이트가 놓여져 있다
## 나이트가 이동하려고 하는 칸이 주어질 때, 몇 번 움직이면 이 칸으로 이동할 수 있을까?

'''
# 첫째 줄에는 테스트 케이스의 개수, 각 테스트 케이스는 세 줄
# 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)
# 체스판의 크기는 l x l
# 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} x {0, ..., l-1}
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸
## 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력

(입력)
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

(출력) 
5
28
0

'''

import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(n)] for j in range(n)]
    cnt = 0
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x = que[0][0]
            y = que[0][1]
            que.popleft()
            
            if x == ex and y == ey:
                return cnt
            
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
        cnt += 1
                
                
                
T = int(sys.stdin.readline())

for tc in range(T):
    n = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    
    print(bfs(sx, sy))
    
