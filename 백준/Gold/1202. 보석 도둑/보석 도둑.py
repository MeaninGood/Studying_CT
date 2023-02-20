import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
heapq.heapify(arr)
heapq.heapify(bags)


pq = []
total = 0
while bags:
    
    tmp = heapq.heappop(bags)
    while arr and arr[0][0] <= tmp:
        w, v = heapq.heappop(arr)
        heapq.heappush(pq, -v)
    
    if pq:
        total += -heapq.heappop(pq)

print(total)