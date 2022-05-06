import heapq, sys
input = sys.stdin.readline

n = int(input())
pq = []

for i in range(n):
    a = int(input())
    
    if a != 0:
        heapq.heappush(pq, a)
    
    elif a == 0:
        if len(pq) > 0:
            print(heapq.heappop(pq))
        else:
            print(0)