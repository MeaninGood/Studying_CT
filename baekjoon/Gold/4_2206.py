# 2206번_벽 부수고 이동하기

## N×M의 행렬로 표현되는 맵
## 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽
## 당신은 (1, 1)에서 (N, M)의 위치까지 최단경로로 이동하려 함
## 시작하는 칸과 끝나는 칸도 포함해서 센다
## 벽을 한 개 까지 부수고 이동하여도 됨
## 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸
## 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성


'''
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
# 다음 N개의 줄에 M개의 숫자로 맵이 주어짐
# (1, 1)과 (N, M)은 항상 0이라고 가정
## 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력

(입력)
6 4
0100
1110
1000
0000
0111
0000

(출력)
15

'''
from pprint import pprint
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y, hand):
    que = deque()
    visited = [[[False for i in range(2)] for j in range(m)] for k in range(n)]
    
    que.append([x, y, hand])
    visited[x][y][hand] = True
    
    ret = 1
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y, hand = que.popleft()
            
            if x == n - 1 and y == m - 1:
                return ret

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny):
                    continue
                
                nhand = hand + arr[nx][ny]
                
                if nhand > 1 or visited[nx][ny][nhand]:
                    continue
                
                que.append([nx, ny, nhand])
                visited[nx][ny][nhand] = True
        ret += 1
    return -1
                

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0, 0))