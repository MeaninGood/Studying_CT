# 1238번_파티

## N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
## 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모임
## 이 마을 사이에는 총 M개의 단방향 도로들이 있고
## i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비
## 각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 함
## 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를수도 있음
## N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구인가

'''
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X
# 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 소요시간 Ti
# 두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어짐
# 시작점과 끝점이 같은 도로는 없으며
# 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개
# 모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어짐
## 첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력

(입력)
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

(출력)
10

'''
# import sys
# import heapq
# si = sys.stdin.readline
# n, m, x = map(int, si().split())

# v = [[] for i in range(n + 1)]
# rv = [[] for i in range(n + 1)]
# for i in range(m):
#     a, b, c = map(int, si().split())
#     v[a].append([b, c])
#     rv[b].append([a, c])
    
    
# def get_dist(s, v):
#     pq = []
    
#     dist[s] = 0
#     heapq.heappush(pq, (0, s))
    
#     while len(pq) > 0:
#         d, cur = heapq.heappop(pq)
        
#         if dist[cur] != d:
#             continue
        
#         for i in range(len(v[cur])):
#             nxt = v[cur][i][0]
#             nd = dist[cur] + v[cur][i][1]
            
#             if dist[nxt] > nd:
#                 dist[nxt] = nd
#                 heapq.heappush(pq, (nd, nxt))

# dist = [1000000000 for i in range(n + 1)]
# get_dist(x, v)
# ans = dist.copy()

# dist = [1000000000 for i in range(n + 1)]
# get_dist(x, rv)

# for i in range(1, n + 1):
#     ans[i] += dist[i]
    
# mx = -1000000000
# for i in range(1, n + 1):
#     if ans[i] > mx:
#         mx = ans[i]
        
# print(mx)
    


import sys
import heapq
si = sys.stdin.readline

def get_dist(s, v):
    pq = []
    
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    
    while len(pq) > 0:
        size = len(pq)
        
        for _ in range(size):
            d, cur = heapq.heappop(pq)
            
            if dist[cur] != d:
                continue
            
            for i in range(len(v[cur])):
                nxt = v[cur][i][0]
                nd = d + v[cur][i][1]
                
                if dist[nxt] > nd:
                    dist[nxt] = nd
                    heapq.heappush(pq, (nd, nxt))

n, m, x = map(int, si().split())

v = [[] for i in range(n + 1)]
rv = [[] for i in range(n + 1)] 

for i in range(m):
    a, b, c = map(int, si().split())
    v[a].append([b, c])
    rv[b].append([a, c])
    
dist = [1000000000 for _ in range(n + 1)]
get_dist(x, v)
ans = dist.copy()

dist = [1000000000 for _ in range(n + 1)]
get_dist(x, rv)


for i in range(1, n + 1):
    ans[i] += dist[i]
    
mx = -10000000
for i in range(1, n + 1):
    if mx < ans[i]:
        mx = ans[i]

print(mx)