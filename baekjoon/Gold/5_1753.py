# 1753번_최단경로

## 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성
## 모든 간선의 가중치는 10 이하의 자연수

'''
# 첫째 줄에 정점의 개수 V와 간선의 개수 E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정
# 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어짐
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어짐
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻
# u와 v는 서로 다르며 w는 10 이하의 자연수
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음
## 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
## 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력

(입력)
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

(출력)
0
2
3
7
INF

'''

import heapq

n, m = map(int, input().split())
s = int(input())
v = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c])
    
dist = [1000000000 for i in range(n + 1)]

pq = []

dist[s] = 0
heapq.heappush(pq, (0, s))

while len(pq) > 0:
    d, cur = heapq.heappop(pq)
    
    if dist[cur] != d:
        continue
    
    for i in range(len(v[cur])):
        nxt = v[cur][i][0]
        nd = dist[cur] + v[cur][i][1]
        
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))


for i in range(1, n + 1):
    if dist[i] == 1000000000:
        print('INF')
    else:
        print(dist[i])