import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n = int(input())
pq = []
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(pq, (-b, a))

d = {}
while pq:
    score, day = heapq.heappop(pq)
    for i in range(1, day + 1)[::-1]:
        if d.get(i):
            continue
        
        d[i] = d.get(i, -score)
        break

print(sum(d.values()))