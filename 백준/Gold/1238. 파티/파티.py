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