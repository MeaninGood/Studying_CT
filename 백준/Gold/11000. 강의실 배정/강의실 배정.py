import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

pq = []
heapq.heapify(arr)

mx = 0
while arr:
    s, e = heapq.heappop(arr)
    
    if pq:
        while pq and s >= pq[0]:
            heapq.heappop(pq)

    heapq.heappush(pq, e)
    mx = max(mx, len(pq))

          
print(mx)