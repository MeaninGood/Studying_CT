import sys, heapq
input = lambda : sys.stdin.readline().strip()

def get_dist(s, arr, prv):
    pq = []
    
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if cur == y:
            return dist[cur]
        
        if dist[cur] != d:
            continue
        
        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = d + v[cur][i][1]
            
            if dist[nxt] > nd:
                dist[nxt] = nd
                prv[nxt] = cur
                heapq.heappush(pq, (nd, nxt))

n, m = map(int, input().split())
v = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    v[a].append([b, c])
    v[b].append([a, c])
    
x, y = map(int, input().split())

prv = [-1 for i in range(n + 1)]
dist = [1 << 30 for i in range(n + 1)]

print(get_dist(x, v, prv))

tmp = y
ans = []
while tmp != x:
    ans.append(tmp)
    tmp = prv[tmp]

ans.append(x)
ans = ans[::-1]
print(*ans)