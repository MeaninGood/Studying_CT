import heapq, sys
input = sys.stdin.readline

n = int(input())

que = []
for i in range(n):
    x = int(input())
    
    if x == 0:
        try:
            a = -heapq.heappop(que)
        except:
            a = 0
        print(a)
    
    else:
        heapq.heappush(que, -x)