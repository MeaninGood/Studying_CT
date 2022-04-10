# 1916번_최소비용 구하기

## N개의 도시가 있다
## 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다
## A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화
## A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력
## 도시의 번호는 1부터 N까지

'''
# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)
# 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)
# 째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어짐
# 처음에는 그 버스의 출발 도시의 번호
# 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어짐
# 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수
# M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호
# 발점에서 도착점을 갈 수 있는 경우만 입력으로 주어짐
## 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력
## 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력
## 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력

(입력)
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

(출력)
4

'''


# import sys, heapq
# si = sys.stdin.readline

# def get_dist(s, v, pr):
#     pq = []
    
#     dist[s] = 0
#     heapq.heappush(pq, (0, s, pr))
#     while len(pq) > 0:
#         d, cur, pr = heapq.heappop(pq)
        
#         if dist[cur] != d:
#             continue
        
#         for i in range(len(v[cur])):
#             nxt = v[cur][i][0]
#             nd = d + v[cur][i][1]
            
#             if dist[nxt] > nd:
#                 dist[nxt] = nd
#                 prv[nxt] = cur
#                 heapq.heappush(pq, (nd, nxt, cur))


# n = int(si())
# m = int(si())
# v = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b, c = map(int, si().split())
#     v[a].append([b, c])
    
# s, e = map(int, si().split())
    
# dist = [1000000000 for _ in range(n + 1)]
# prv = [0 for _ in range(n + 1)]
# get_dist(s, v, -1)

# print(dist[e])
# print(prv[e])


import sys, heapq
si = sys.stdin.readline


n = int(si())
m = int(si())
v = [[] for _ in range(n + 1)]
dist = [1000000000 for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, si().split())
    
    v[a].append([b, c])
    
s, e = map(int, si().split())
    
    
prv = [-1 for _ in range(n + 1)]    

pq = []

dist[s] = 0
heapq.heappush(pq, (0, s))
while len(pq) > 0:
    # d, cur, pr = heapq.heappop(pq)
    d, cur = heapq.heappop(pq)
    
    if dist[cur] != d:
        continue
    
    # for i in range(len(v[cur])):
    #     nxt = v[cur][i][0]
    #     nd = d + v[cur][i][1]
    #     prv[nxt] = cur
    
    for nxt, nd in v[cur]:
        nd += d

        if dist[nxt] > nd:
            dist[nxt] = nd
            prv[nxt] = cur
            # heapq.heappush(pq, (nd, nxt, cur))
            heapq.heappush(pq, (nd, nxt))
            
print(dist[e])

ans = []
cur = e
while cur != -1:
    ans.append(cur)
    cur = prv[cur]

print(len(ans))
print(*ans[::-1])