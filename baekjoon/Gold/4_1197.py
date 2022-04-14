# import heapq, sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# v = [[] for i in range(n + 1)]

# for i in range(m):
#     a, b, c = map(int, input().split())

#     v[a].append([b, c])

# dist = [1000000000 for i in range(n + 1)]

# pq = []

# dist[1] = 0
# heapq.heappush(pq, (0, 1))
# while len(pq) > 0:
#     # mn = 100000000
#     # cur = 0
#     # for i in range(1, n + 1):
#     #     if not visited[i] and dist[i] < mn:
#     #         mn = dist[i]
#     #         cur = i
#     d, cur = heapq.heappop(pq)

#     # if visited[cur]:
#     #     continue
#     #
#     # visited[cur] = True

#     if dist[cur] != d:
#         continue

#     for i in range(len(v[cur])):
#         nxt = v[cur][i][0]
#         nd = dist[cur] + v[cur][i][1]

#         if dist[nxt] > nd:
#             dist[nxt] = nd
#             heapq.heappush(pq, (nd, nxt))


# print(dist[n])

import heapq, sys
input = sys.stdin.readline



def find_(x):
    if par[x] == x:
        return x
    
    par[x] = find_(par[x])
    return par[x]


def union_(a, b):
    a = find_(a)
    b = find_(b)
    
    if a == b:
        return
    
    if rnk[a] < rnk[b]:
        par[a] = b
        # sz[b] += sz[a]
    
    if rnk[a] > rnk[b]:
        par[b] = a
        # sz[a] += sz[b]
    else:
        par[a] = b
        # sz[b] += sz[a]
        rnk[b] += 1
        
                
n, m = map(int, input().split())
v = [list(map(int, input().split())) for i in range(m)]

par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]
# sz = [1 for _ in range(n + 1)]
    
v.sort(key = lambda x: x[2])

tmp = 0
for i in range(m):
    if find_(v[i][0]) == find_(v[i][1]):
        continue
    
    union_(v[i][0], v[i][1])
    
    tmp += v[i][2]
    
print(tmp)
    


        