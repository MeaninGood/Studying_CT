import sys, heapq
from pprint import pprint
input = lambda : sys.stdin.readline().strip()

m, n = map(int, input().split())
arr = [[0 for i in range(m + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]\
    + [[0 for i in range(m + 2)]]

def in_range(x, y):
    return 0 <= x < n+2 and 0 <= y < m+2

# 0: 홀수 , 1: 짝수
dx = [[-1, -1, 0, 0, 1, 1], [-1, -1, 0, 0, 1, 1]]
dy = [[0, 1, -1, 1, 0, 1], [-1, 0, -1, 1, -1, 0]]

def get_dist(x, y, d):
    pq = []
    dist[x][y] = d
    
    heapq.heappush(pq, [d, x, y])
    while pq:
        d, x, y = heapq.heappop(pq)

        if dist[x][y] != d:
            continue

        for i in range(6):
            if x % 2 == 1:
                nx = x + dx[0][i]
                ny = y + dy[0][i]

            else:
                nx = x + dx[1][i]
                ny = y + dy[1][i]

            if not in_range(nx, ny):
                continue

            nd = d + arr[nx][ny]

            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, [nd, nx, ny])


dist = [[1 << 31 for i in range(m + 2)] for j in range(n + 2)]

get_dist(0, 0, 0)

cnt = 0
for i in range(n + 2):
    for j in range(m + 2):
        if dist[i][j] == 1 and arr[i][j] == 1:
            for d in range(6):
                if i % 2 == 1:
                    nx = i + dx[0][d]
                    ny = j + dy[0][d]
                
                else:
                    nx = i + dx[1][d]
                    ny = j + dy[1][d]

                if dist[nx][ny] == 0:
                    cnt += 1

print(cnt)
pprint(dist)