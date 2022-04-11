# 1504번_특정한 최단 경로

## 방향성이 없는 그래프가 주어짐
## 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 할 때
## 임의로 주어진 두 정점은 반드시 통과해야 함
## 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다
## 하지만 반드시 최단 경로로 이동해야 한다
## 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램
## 각 (A, B) 쌍에 대해 변호사 A가 변호사 B를 변호할지 말지를 선택하여 모든 변호사가 무죄가 되는 것이 가능한지 판정

'''
# 첫째 줄에 정점의 개수 N과 간선의 개수 E(2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
# 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c
# a번 정점에서 b번 정점까지 양방향 길이 존재, 그 거리가 c라는 뜻(1 ≤ c ≤ 1,000)
# 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어짐(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
# 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재
## 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력
## 그러한 경로가 없을 때에는 -1을 출력

(입력)
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

(출력)
7

'''

import sys, heapq
input = sys.stdin.readline

# def get_dist(s):
#     pq = []
#     dist[s] = 0
    
#     heapq.heappush(pq, [dist[s], s])
    
#     while pq:
#         d, cur = heapq.heappop(pq)
        
#         if dist[cur] != d:
#             continue
        
#         for nxt, nd in v[cur]:
#             nd += d
            
#             if 
            
#             if dist[nxt] > nd:
#                 dist[nxt] = nd
#                 heapq.heappush(pq, (nd, nxt))
        
import sys, heapq
input = sys.stdin.readline

def get_dist(s):
    pq = []
    dist = [1000000000 for _ in range(n + 1)]
    dist[s] = 0

    heapq.heappush(pq, (0, s))

    while pq:
        d, cur = heapq.heappop(pq)
        
        if dist[cur] != d:
            continue
        
        for nxt, nd in v[cur]:
            nd += d
            
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
                
    return dist
                
    
n, m = map(int, input().split())
v = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    v[a].append([b, c])
    v[b].append([a, c])

v1, v2 = map(int, input().split())


ds = get_dist(1)
dv1 = get_dist(v1)
dv2 = get_dist(v2)

ans = min(ds[v1] + dv1[v2] + dv2[n], ds[v2] + dv2[v1] + dv1[n])

if ans >= 1000000000:
    print(-1)
else:
    print(ans)