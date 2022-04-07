'''
그래프 이론
1. 다익스트라
2. disjoint set(union find) => 부록(분할 상환 기법)
3. MST(minimum spanning tree) => 크루스칼 알고리즘
'''





'''
다익스트라

가중치가 없는 그래프에서 최단거리를 구한다 => BFS
음이 아닌 가중치가 있는 그래프에서 최단거리를 구한다 => 다익스트라

가중치가 있는 그래프에서 최단거리를 구한다 => 벨만포드 => X
모든 노드에서 다른 모든 노드까지의 거리(N * N쌍)를 모두 구한다 => 플로이드 워셔 => X



5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

import heapq

q = []

heapq.heappush(q, (0, start))
dist, now = heapq.heappop(q)
'''
import heapq

n, m = map(int, input().split())
s = int(input())
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())

    v[a].append([b, c])

dist = [1000000000 for i in range(n + 1)]

pq = []

dist[s] = 0
heapq.heappush(pq, (0, s))
while len(pq) > 0:
    # mn = 100000000
    # cur = 0
    # for i in range(1, n + 1):
    #     if not visited[i] and dist[i] < mn:
    #         mn = dist[i]
    #         cur = i
    d, cur = heapq.heappop(pq)

    # if visited[cur]:
    #     continue
    #
    # visited[cur] = True

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

