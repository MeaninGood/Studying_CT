import heapq

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    v = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        
        v[a].append([b, c])
        
    dist = [1e9 for _ in range(n + 1)]
    pq = []

    dist[0] = 0
    heapq.heappush(pq, (0, 0))
    while len(pq) > 0:
        d, cur = heapq.heappop(pq)
        
        if dist[cur] != d:
            continue
        
        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = d + v[cur][i][1]
            
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
        
    print(f'#{tc} {dist[n]}')
    
    



INF = int(1e6)
def dijkstra(start):
    visited = [0] * (N + 1)
    distance = [INF] * (N+1)
    distance[start] = 0

    while not visited[N]:
        nxtDistance = INF
        for idx in range(N+1):
            if nxtDistance > distance[idx] and not visited[idx]:
                nxtDistance = distance[idx]
                nxtNode = idx

        visited[nxtNode] = 1
        for i in range(N+1):
            if graph[nxtNode][i] and distance[i] > distance[nxtNode] + graph[nxtNode][i] :
                distance[i] = distance[nxtNode] + graph[nxtNode][i]

    return distance[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int,input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    print(f'#{tc} {dijkstra(0)}')