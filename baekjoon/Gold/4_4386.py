# 4386번_별자리 만들기

## 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것
## 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태
## 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 함
## 별들이 2차원 평면 위에 놓여 있을 때, 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다
## 별자리를 만드는 최소 비용을 구하시

'''
# 첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
# 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 최대 소수점 둘째자리까지 주어짐
# 좌표는 1000을 넘지 않는 양의 실수
## 첫째 줄에 정답을 출력
## 절대/상대 오차는 10-2까지 허용

(입력)
3
1.0 1.0
2.0 2.0
2.0 4.0

(출력)
3.41

'''

import sys, heapq
input = sys.stdin.readline

# def get_dist(x, y, d):
#     pq = []
    
#     dist[x][y] = 0
#     heapq.heappush(pq, [0, x, y])
    
#     while pq:
#         d, x, y = heapq.heappop(pq)
        
#         if dist[x][y] != d:
#             continue
        
#         for nx, ny in v:
#             nd = abs(nx - x)**2 + abs(ny - y)**2
#             nd = nd ** 1/2
#             if dist[nx][ny] > nd:
#                 dist[nx][ny] = nd
#                 heapq.heappush(pq, [nd, nx, ny])
                
        
# n = int(input())
# v = [list(map(int, input().split())) for _ in range(n)]
# print(v)

# dist = [[1000000000 for i in range(10)] for j in range(10)]

# get_dist(0, 0, 0)
# print(dist)


import sys
input = sys.stdin.readline

def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])


def union_(a, b):
    a, b = find_(a), find_(b)
    
    if a == b:
        return
    
    if rnk[a] > rnk[b]:
        par[b] = a
        
    elif rnk[a] < rnk[b]:
        par[a] = b
        
    else:
        par[a] = b
        rnk[b] += 1

n = int(input())
v = [list(map(float, input().split())) for _ in range(n)]
arr = []

for i in range(n - 1):
    x1, y1 = v[i]
    for j in range(i + 1, n):
        x2, y2 = v[j]
        
        tmp = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1/2)
        
        arr.append([i, j, tmp])

arr.sort(key = lambda x: x[2])

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]

total = 0
cnt = 0
for a, b, c in arr:
    if find_(a) != find_(b):
        union_(a, b)
        total += c
        cnt += 1
    
    if cnt == n - 1:
        print(total)
        exit()
