# 2636번_치즈

## 정사각형 칸들로 이루어진 사각형 모양의 판
## 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다
## 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다
## 이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어짐
## 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 됨
## 입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때,
## 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과
## 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성

'''
# 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어짐
# 세로와 가로의 길이는 최대 100
# 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어짐
# 치즈가 없는 칸은 0, 치즈가 있는 칸은 1, 각 숫자 사이에는 빈칸이 하나씩 있음
## 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력
## 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력

(입력)
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

(출력)
3
5

'''

import sys
import heapq
si = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_dist(x, y, arr):
    pq = []
    dist[x][y] = arr[x][y]
    
    heapq.heappush(pq, (arr[x][y], x, y))
    # ret = 1
    while len(pq) > 0:
        d, x, y = heapq.heappop(pq)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not in_range(nx, ny):
                continue 
            
            nd = dist[x][y] + arr[nx][ny]
            
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, (nd, nx, ny))
        
    #     ret += 1
    # return ret
            
    

n, m = map(int, si().split())
arr = [list(map(int, si().split())) for _ in range(n)]
dist = [[1000000000 for _ in range(m + 1)] for j in range(n + 1)]

get_dist(0, 0, arr)



mx = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] > mx:
            mx = dist[i][j]
else:  
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dist[i][j] == mx and arr[i][j] == 1:
                cnt += 1
                
    print(mx)
    print(cnt)