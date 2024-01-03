import sys
import heapq

input = lambda: sys.stdin.readline().strip()


def get_dist(s):
    pq = []
    dist = [1000000000 for _ in range(n + 1)]
    dist[s] = 0
    total = 0

    heapq.heappush(pq, (0, s, total))

    while pq:
        d, cur, total = heapq.heappop(pq)

        for nxt, nd in v[cur]:
            ntotal = total + nd
            nd = max(d, nd)

            if ntotal > money:
                continue

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt, ntotal))

    return dist


n, m, s, e, money = map(int, input().split())
v = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())

    v[a].append([b, c])
    v[b].append([a, c])


dv = get_dist(s)


print(dv[e] if dv[e] != 1000000000 else -1)
