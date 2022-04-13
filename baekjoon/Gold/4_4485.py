# 4485번_녹색 옷 입은 애가 젤다지?

## 링크는 지금 도둑루피만 가득한 N x N 크기의 동굴의 제일 왼쪽 위에 있다
## 링크는 이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다
## 동굴의 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 됨
## 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 함
## 한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다

'''
# 입력은 여러 개의 테스트 케이스
# 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N(2 ≤ N ≤ 125)
# N = 0인 입력이 주어지면 전체 입력이 종료
# 이어서 N개의 줄에 걸쳐 동굴의 각 칸에 있는 도둑루피의 크기가 공백으로 구분되어 차례대로 주어짐
# 도둑루피의 크기가 k면 이 칸을 지나면 k루피를 잃는다는 뜻
# 여기서 주어지는 모든 정수는 0 이상 9 이하인 한 자리 수
## 각 테스트 케이스마다 한 줄에 걸쳐 정답을 형식에 맞춰서 출력

(입력)
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0

(출력)
Problem 1: 20
Problem 2: 19
Problem 3: 36

'''

import sys
import heapq
si = sys.stdin.readline

cnt = 1
while 1:
    n = int(si())
    
    if n == 0:
        break

    arr = [list(map(int, si().split())) for i in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def get_dist(x, y, arr):
        pq = []
        dist[x][y] = arr[x][y]
        
        heapq.heappush(pq, (arr[x][y], x, y))
        while len(pq) > 0:
            d, x, y = heapq.heappop(pq)
            
            if dist[x][y] != d:
                continue 
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not in_range(nx, ny):
                    continue
                
                nd = d + arr[nx][ny]
                
                if dist[nx][ny] > nd:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))
                    
    dist = [[1000000000 for i in range(n)] for j in range(n)]

    get_dist(0, 0, arr)

    print(f'Problem {cnt}: {dist[n - 1][n - 1]}')
    
    cnt += 1